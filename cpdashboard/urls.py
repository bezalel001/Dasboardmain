"""CPDApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from cpdashboard import views
# from django.contrib.auth import views as auth_views 
from .models import Initiative, Objective
from cpdashboard.views import InitiativeIndexView, ObjectiveIndexView, InitiativeEditView, InitiativeCommentView, CustomerInitiativeIndexView, \
InitiativeDetailView, FinancialInitiativeIndexView, CapacityInitiativeIndexView, ProcessInitiativeIndexView

from rest_framework.urlpatterns import format_suffix_patterns
#from cpdashboard


urlpatterns = [
    url(r'^$', views.index, name='home' ),
    url(r'^initiatives$', InitiativeIndexView.as_view(), name='all-initiatives'),
    url(r'^initiatives/financial$', FinancialInitiativeIndexView.as_view(), name='financial-initiatives'),
    url(r'^initiatives/customer$', CustomerInitiativeIndexView.as_view(), name='customer-initiatives'),
    url(r'^initiatives/processes$', ProcessInitiativeIndexView.as_view(), name='process-initiatives'),
    url(r'^initiatives/capacity$', CapacityInitiativeIndexView.as_view(), name='capacity-initiatives'),

    url(r'^objectives$', ObjectiveIndexView.as_view(), name='objectives'),
    url(r'^objectives/financial$', views.FinancialObjectiveIndexView.as_view(), name='financial-objectives'),
    url(r'^objectives/customer$', views.CustomerObjectiveIndexView.as_view(), name='customer-objectives'),
    url(r'^objectives/processes$', views.ProcessObjectiveIndexView.as_view(), name='process-objectives'),
    url(r'^objectives/capacity$', views.CapacityObjectiveIndexView.as_view(), name='capacity-objectives'),
    url(r'^objectives/edit/(?P<pk>\d+)/$', views.ObjectiveEditView.as_view(model=Objective), name='edit-objective'),
    url(r'^objectives/detail/(?P<pk>\d+)/$', views.ObjectiveDetailView.as_view(), name='objective-detail'),

    url(r'^initiatives/edit/(?P<pk>\d+)/$', InitiativeEditView.as_view(model=Initiative), name='edit-initiative'),
    url(r'^initiatives/detail/(?P<pk>\d+)/comment/$', views.add_comment, name='add-initiative-comment'),
    url(r'^initiatives/detail/(?P<pk>\d+)/$', InitiativeDetailView.as_view(), name='initiative-detail'),
    url(r'^initiatives/dashboard/(?P<pk>\d+)/$', views.InitiativeDashboard.as_view(), name='dashboard'),

    #-----------------API-Django rest framework----------------=
    url(r'^inits/$', views.initiative_list),
    url(r'^inits/(?P<pk>[0-9]+)/$', views.initiative_detail, name='init-detail'),
    url(r'^goals/$', views.ObjectiveGrid.as_view()),
    url(r'^goal/(?P<pk>[0-9]+)/$', views.RetrieveObjective.as_view(), name='obdetails'),
    url(r'^pers/$', views.PerspectiveList.as_view()),
    #------------------------------------------------------------
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^import/$', views.import_data, name="import"),

    url(r'^partials/graph/$', views.d3_graph),
    url(r'^test/$', views.test_page),
    url(r'^some/$', views.some_view, name='pdf'),
    #url(r'^gen/$', views.generate_pdf_view, name='pdf'),
  
    #url(r"^report$", views.HelloPDFView.as_view()),
    url(r'^objectives/initiatives/(?P<objective_id>[0-9]+)$', views.initiatives_for_objective, name='inobjective'),
    url(r'^perspectives/$', views.AllPerspective.as_view(), name='perspectives'), 
    url(r'^objectives/all$', views.StrategicObjectives.as_view(), name='strategicobj'), 
    #url(r'^objectives/edit/(?P<pk>[0-9]+)/$', views.ObjectiveEditView.as_view(), name='edit-objective'),    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)


