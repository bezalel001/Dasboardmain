from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.core.urlresolvers import reverse
from django.conf import settings
from django.forms import ModelForm
from .forms import InitiativeEditForm, CommentForm, UploadFileForm, ObjectiveEditForm
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

#from _compat import JsonResponse
import django_excel as excel



from django.views.generic import UpdateView, ListView, DetailView, CreateView

from cpdashboard.models import  Perspective, Objective, \
Initiative, Manager, Comment
import cpdashboard

from reportlab.pdfgen import canvas
#class ObjectiveEditView(UpdateView):
#    model = Objective
#    fields = ['description', 'objective_commentary', 'result', 'perspective']
#    template_name = 'cpdashboard/objectives/edit.html'


class StrategicObjectives(ListView):
    template_name = 'cpdashboard/objectives/description.html'
    context_object_name = 'objective_list'
    queryset = Objective.objects.all()

class AllPerspective(ListView):
    template_name = 'cpdashboard/perspectives/index.html'
    context_object_name = 'perspectives_list'
    queryset = Perspective.objects.all()

def initiatives_for_objective(request, objective_id):
    objective = Objective.objects.get(pk=objective_id)
    initiatives = Initiative.objects.filter(objective__id=objective_id)

    green = 0
    red = 0
    amber = 0
    total = 0
    for item in initiatives:
        if item.time_status == 0:
            green += 1 
        elif item.time_status == 1:
            amber += 1
        elif item.time_status == 2:
            red += 1
    
    total = green + amber + red
    if total == 0: total = 1
    percent_green = 100*green/ float(total)
    percent_amber = 100*amber/ float(total)
    percent_red = 100*red/ float(total)
    
    context = {'initiative_list': initiatives, 'objective':objective, 'green':percent_green, 'amber':percent_amber, 'red': percent_red}

    return render(request, 'cpdashboard/objectives/initiatives.html', context)

def some_view(request):
    #Create the HttpResponse object with appropriate PDF headers
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file"
    p = canvas.Canvas(response)

    #Draw things on the PDF. Here's where the PDF generation happens.
    p.drawString(100, 100, "Strategic initiatives")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response


class InitiativeIndexView(LoginRequiredMixin, ListView):
    template_name = 'cpdashboard/initiatives/index.html'
    context_object_name = 'initiatives_list' 


    def get_queryset(self):
        """Return all the initiatives."""
        return Initiative.objects.order_by('objective')

    #def get_context_data(self, **kwargs):
    #    context = super(InitiativeIndexView, self).get_context_data(**kwargs)
    #    context['fields'] = self.object._meta_get_fields()
    #    return context


class FinancialInitiativeIndexView(LoginRequiredMixin, ListView):
    template_name = 'cpdashboard/initiatives/index.html'
    context_object_name = 'initiatives_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Initiative.objects.filter(objective__perspective__description='Financial').order_by('objective')

class CustomerInitiativeIndexView(LoginRequiredMixin, ListView):
    template_name = 'cpdashboard/initiatives/index.html'
    context_object_name = 'initiatives_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Initiative.objects.filter(objective__perspective__description='Customer').order_by('objective')

class ProcessInitiativeIndexView(LoginRequiredMixin, ListView):
    template_name = 'cpdashboard/initiatives/index.html'
    context_object_name = 'initiatives_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Initiative.objects.filter(objective__perspective__description='Processes').order_by('objective')

class CapacityInitiativeIndexView(LoginRequiredMixin, ListView):
    template_name = 'cpdashboard/initiatives/index.html'
    context_object_name = 'initiatives_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Initiative.objects.filter(objective__perspective__description='Capacity').order_by('objective')



class ObjectiveIndexView(LoginRequiredMixin, ListView):
    template_name = 'cpdashboard/objectives/index.html'
    context_object_name = 'objectives_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Objective.objects.order_by('perspective')

    def get_context_data(self, **kwargs):
        context = super(ObjectiveIndexView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context







class InitiativeEditView(LoginRequiredMixin, UpdateView):   
	form_class = InitiativeEditForm
	#fields = ['actual_start_date', 'projected_end_date', \
 #       'projected_end_cost','projected_manhours', \
 #       'actual_cost', 'actual_manhours', 'initiative__comment.content' ]
	template_name = 'cpdashboard/initiatives/edit.html'
	success_url = 'cpdashboard:inobjective'


	#slug_field = 'user__username'
	#slug_url_kwarg = 'username'


	def get_success_url(self):
		return reverse(self.success_url , args=(self.object.objective.pk,))


class InitiativeCommentView(LoginRequiredMixin, CreateView):   
	form_class = CommentForm

	template_name = 'cpdashboard/initiatives/comment.html'
	success_url = 'cpdashboard:all-initiatives'


	def get_success_url(self):
		return reverse(self.success_url)



class InitiativeDetailView(LoginRequiredMixin, DetailView):
    model = Initiative
    template_name ='cpdashboard/initiatives/detail.html'

    def get_context_data(self, **kwargs):
        context = super(InitiativeDetailView, self).get_context_data(**kwargs)
        #context['manager'] = Participant.objects.filter(initiatives__pk=self.object.id).filter(is_initiative_manager=False)
        return context



class InitiativeDashboard(LoginRequiredMixin, DetailView):
    model = Initiative
    template_name ='cpdashboard/initiatives/dashboard.html'

    # def get_context_data(self, **kwargs):
    #     context = super(InitiativeDetailView, self).get_context_data(**kwargs)
    #     context['manager'] = Participant.objects.filter(initiatives__pk=self.object.id).filter(is_initiative_manager=False)
    #     return context


#@login_required
def index(request): 
    # if not request.user.is_authenticated():
    #     return redirect('%snext=%s?' % (settings.LOGIN_URL, request.path))
    return render(request, 'cpdashboard/landing/index.html')


class FinancialObjectiveIndexView(LoginRequiredMixin, ListView):
    template_name = 'cpdashboard/objectives/index.html'
    context_object_name = 'objectives_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Objective.objects.filter(perspective__description='Financial').order_by('code')



class CustomerObjectiveIndexView(LoginRequiredMixin, ListView):
    template_name = 'cpdashboard/objectives/index.html'
    context_object_name = 'objectives_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Objective.objects.filter(perspective__description='Customer').order_by('code')


class ProcessObjectiveIndexView(LoginRequiredMixin, ListView):
    template_name = 'cpdashboard/objectives/index.html'
    context_object_name = 'objectives_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Objective.objects.filter(perspective__description='Processes').order_by('code')


class CapacityObjectiveIndexView(LoginRequiredMixin, ListView):
    template_name = 'cpdashboard/objectives/index.html'
    context_object_name = 'objectives_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Objective.objects.filter(perspective__description='Learning and Capacity').order_by('code')


class ObjectiveEditView(LoginRequiredMixin, UpdateView):   
	form_class = ObjectiveEditForm
	#fields = ['actual_start_date', 'projected_end_date', \
 #       'projected_end_cost','projected_manhours', \
 #       'actual_cost', 'actual_manhours' ]
	template_name = 'cpdashboard/objectives/edit.html'
	success_url = 'cpdashboard:objective-detail'


	#slug_field = 'user__username'
	#slug_url_kwarg = 'username'


	def get_success_url(self):
		return reverse(self.success_url, args=(self.object.id,) )



class ObjectiveDetailView(LoginRequiredMixin, DetailView):
    model = Objective
    template_name ='cpdashboard/objectives/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ObjectiveDetailView, self).get_context_data(**kwargs)
        initiatives= Initiative.objects.filter(objective__pk=self.object.id)
        green = 0
        amber = 0
        red = 0
        none = 0
        for init in initiatives:
            if init.time_status == 0:
                green += 1
            elif init.time_status == 1:
                amber += 1
            elif init.time_status ==2:
                red += 1
            else: none += 1
        context['green'] = green
        context['amber'] = amber;
        context['red'] = red;
        context['none'] = none
        return context



###########################################################################################
from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cpdashboard.serializers import InitiativeSerializer
from cpdashboard.serializers import ObjectiveSerializer, PerspectiveSerializer
from rest_framework import generics

@api_view(['GET', 'POST'])
def initiative_list(request, format=None):
    """List all initiatives, or create a new initative"""
    if request.method == 'GET':
        initiatives = Initiative.objects.all()
        serializer = InitiativeSerializer(initiatives, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InitiativeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def initiative_detail(request, pk, format=None):
    """
    Retrieve, update or delete an initiatve instance
    """
    try: 
        initiative = Initiative.objects.get(pk=pk)
    except Initiative.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InitiativeSerializer(initiative)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InitiativeSerializer(initiative, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        initiative.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class ObjectiveGrid(generics.ListCreateAPIView):
    queryset = Objective.objects.all()
    serializer_class = ObjectiveSerializer

class RetrieveObjective(generics.RetrieveAPIView):
    queryset = Objective.objects.all()
    serializer_class = ObjectiveSerializer


class PerspectiveList(generics.ListCreateAPIView):
    queryset = Perspective.objects.all()
    serializer_class = PerspectiveSerializer
#from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
#from cpdashboard.serializers import InitiativeSerializer

#class JSONResponse(HttpResponse):
#    """
#    An HttpResponse that renders its content into JSON
#    """
#    def __init__(self, data, **kwargs):
#        content = JSONRenderer().render(data)
#        kwargs['content_type'] = 'application/json'
#        super(JSONResponse, self).__init__(content, **kwargs)


#@csrf_exempt
#def initiative_list(request):
#    """List all initiative or create a new initiative
#    """
#    if request.method == "GET":
#        initiatives = Initiative.objects.all()
#        serializer = InitiativeSerializer(initiatives, many=True)
#        return JSONResponse(serializer.data)
#    elif request.method == 'POST':
#        data = JSONParser().parse(request)
#        serializer = InitiativeSerializer(data=data)
#        if serializer.is_valid():
#            serializer.save()
#            return JSONResponse(serializer.data, status=201)
#        return JSONResponse(serializer.errors, status=400)


#@csrf_exempt
#def initiative_detail(request, pk):
#    """Retrieve, update or delete an initiative
#    """
#    try:
#        initiative = Initiative.objects.get(pk=pk)
#    except Initiative.DoesNotExist:
#        return HttpResponse(status=404)
#    if request.method == "GET":
#        serializer = InitiativeSerializer(initiative)
#        return JSONResponse(serializer.data)
#    elif request.method =='PUT':
#        data = JSONParser().parse(request)
#        serializer = InitiativeSerializer(initiative, data=data)
#        if serializer.is_valid():
#            serializer.save()
#            return JSONResponse(serializer.data)
#        return JSONResponse(serializer.errors, status=400)
#    elif request.method == "DELETE":
#        initiative.delete()
#        return HttpResponse(status=204)




# User registration

def register(request):
    if request.method == "GET":
        return render(request, "cpdashboard/accounts/register.html")
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        if password != confirm_password:
            return render(request, "cpdashboard/accounts/register.html", {'warning':'Passwords do not match!'})


    # Create user
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name).save()
        a_user = authenticate(username=username, password=password)
        login(request, a_user)
        return redirect("/")

    


# Login
def dashboard_login(request):
    if request.method == "GET":
        return render(request, "cpdashboard/accounts/login.html")
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                
                next = ""
                if "next" in request.GET:
                    next = request.GET["next"]
                if next == None or next == "":
                    next = "/"
                return redirect(next)
            else:
                warning = "Your account is disabled"
                return render(request, "cpdashboard/accounts/login.html", {"warning":warning})
        else:
            warning = "Invalid username or password"
            return render(request, "cpdashboard/accounts/login.html", {"warning":warning})


def dashboard_logout(request):
    logout(request)
    return redirect("/")



def d3_graph(request):
    return render(request, 'cpdashboard/partials/graphs.html')


def test_page(request):
    return render(request, 'cpdashboard/testpage.html')


def add_comment(request, pk):
    initiative = get_object_or_404(Initiative, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.initiative = initiative
            comment.author = request.user.first_name + ' ' +  request.user.last_name
            comment.save()
            return redirect('/initiatives/detail/{0}/'.format(initiative.pk))
    else:
        form = CommentForm()
    return render(request, 'cpdashboard/initiatives/comment.html', {'form': form, 'initiative':initiative})





#from easy_pdf.views import PDFTemplateView

#class HelloPDFView(PDFTemplateView):
#    template_name = "cpdashboard/initiatives/dashboard.html"

#    def get_context_data(self, **kwargs):
#        return super(HelloPDFView, self).get_context_data(
#            pagesize="A4",
#            title="Hi there!",
#            **kwargs
#        )


#import pdfcrowd
#from django.http import HttpResponse

#def generate_pdf_view(request):
#    try:
#        # create an API client instance
#        client = pdfcrowd.Client("username", "apikey")

#        # convert a web page and store the generated PDF to a variable
#        pdf = client.convertURI("/gen")

#         # set HTTP response headers
#        response = HttpResponse(mimetype="application/pdf")
#        response["Cache-Control"] = "max-age=0"
#        response["Accept-Ranges"] = "none"
#        response["Content-Disposition"] = "attachment; filename=google_com.pdf"

#        # send the generated PDF
#        response.write(pdf)
#    except pdfcrowd.Error,why:
#        response = HttpResponse(mimetype="text/plain")
#        response.write(why)
#    return response

# ********************************************************************
def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "csv", file_name="excel file")
    else:
        form = UploadFileForm()
        return render(
            request, 
            'cpdashboard/excel/upload_form.html',
            {
                'form': form,
                'title': 'Excel file upload and download example',
                'header': ('Please choose any excel file ' +
                       'from your cloned repository:')
            })


def import_data(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        def objective_func(row):
            
            p = Perspective.objects.filter(slug=row[4])[0]
            print(p)
            row[4] = p 
            return row
        def initiative_func(row):
            o = Objective.objects.filter(code=row[1])[0]
            print(o)
            row[1] = o
            return row
        if form.is_valid():
            request.FILES['file'].save_book_to_database(
                models = [Perspective, Objective, Initiative],
                initializers=[None, objective_func, initiative_func],
                mapdicts = [
                     ['description', 'slug'],
                     ['description', 'code', 'result', 'objective_commentary', 'perspective'],
                     ['description', 'objective', 'code_suffix',
                      'performance_measure', 'target', 'debit_code',
                      'weight','scheduled_start_date', 'scheduled_end_date',
                      'actual_start_date', 'projected_end_date','actual_end_date',
                      'budgeted_cost', 'projected_end_cost', 'actual_cost', 
                      'budgeted_manhours', 'projected_manhours', 
                      'actual_manhours', 'created_on', 'file', 'image', 'responsibility']
                    ]
                )
            return HttpResponse("OK", status=200)
        else: 
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'cpdashboard/excel/upload_form.html',
        {
            'form': form,
            'title': 'Import excel data into database example',
            'header': 'Please upload dashboard data:'
        })
