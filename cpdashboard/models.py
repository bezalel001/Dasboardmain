from django.db import models
from django.utils.functional import cached_property
from django.core.urlresolvers import reverse
from django.utils import timezone
import datetime
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
STATUS = -100

#class Industry(models.Model):
#    name = models.CharField(max_length=30)

#    def __str__(self):
#        return '{0}'.format(self.name)

#class Company(models.Model):
#    name = models.CharField(max_length=30)
#    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
#    added_on = models.DateTimeField(auto_now_add=True)

#    def get_absolute_url(self):
#        return reverse('cpdashboard:company-detail', kwargs={'pk': self.pk})

#    def __str__(self):
#        return '{0}'.format(self.name)

class Perspective(models.Model):
    description = models.CharField(max_length=30)
    #company = models.ForeignKey(Company, on_delete=models.CASCADE)
    slug = models.CharField(max_length=10, unique=True, default='perspective')

    def __str__(self):
        return self.description

class Objective(models.Model):
    description = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)
    result = models.CharField(max_length=100)
    objective_commentary = models.TextField(default="Explanation")
    perspective = models.ForeignKey(Perspective, related_name='objectives', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    #slug = models.CharField(max_length=10, unique=True, default="objective")

    @cached_property
    def inits(self):
       return Initiative.objects.filter(objective__pk=self.pk)

    
    def status(self, color_code):
       color  = 0
       
       for item in self.inits:
           if item.time_status == color_code:
               color += 1
       return color

    @cached_property
    def green(self):
       return self.status(0)

    @cached_property
    def amber(self):
       return self.status(1)

    @cached_property
    def red(self):
       return self.status(2)


    def get_absolute_url(self):
        return reverse('cpdashboard:objective-detail', kwargs={'pk':self.pk})

    def get_initiatives_url(self):
        return reverse('cpdashboard:inobjective', args=(self.pk,))

    def __str__(self):
        return self.description


class Initiative(models.Model):
    description = models.CharField(max_length=255)
    objective = models.ForeignKey(Objective, related_name='initiatives', on_delete=models.CASCADE)
    code_suffix = models.CharField(max_length=10)
    performance_measure = models.CharField(max_length=100)
    target = models.CharField(max_length=100)
    debit_code = models.CharField(max_length=20, default='')
    weight = models.IntegerField(default=0)
    scheduled_start_date = models.DateField()
    scheduled_end_date = models.DateField()
    actual_start_date = models.DateField(null=True, blank=True)
    projected_end_date = models.DateField(null=True, blank=True)
    actual_end_date = models.DateField(null=True, blank=True)
    budgeted_cost = models.DecimalField(max_digits=10, decimal_places=2)
    projected_end_cost = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    actual_cost = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    budgeted_manhours = models.DecimalField(max_digits=5, decimal_places=2)
    projected_manhours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    actual_manhours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='file/', null=True, blank=True)
    image = models.ImageField(upload_to='file/', null=True, blank=True)
    is_under_pressure = models.BooleanField(default=False)
    responsibility = models.CharField(max_length=30, default='')
    #manager = models.ForeignKey('Manager', related_name='initiatives', on_delete=models.CASCADE)
    
    

    #notes = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('cpdashboard:initiative-detail', kwargs={'pk': self.pk})

    @cached_property
    def code(self):
        counter = 0
        for i in self.objective.initiatives.all():
            counter = counter + 1
            if i.id == self.id:
                if counter < 10: counter = '0' + str(counter)
                return '{0}.{1}'.format(self.objective.code, counter)

    @cached_property
    def time_status(self):
        STATUS = 10
        if self.projected_end_date is None:
            STATUS = None
        elif self.is_under_pressure:
            STATUS = 1 # amber
        elif (self.projected_end_date - self.scheduled_end_date).days <= 0:
            if (self.scheduled_end_date - datetime.date.today()).days >= 0:
                STATUS = 0 # green
            elif ( self.actual_end_date is not None) and ((self.actual_end_date - datetime.date.today()).days < 0):
                STATUS = -1 # not active
        elif  (self.projected_end_date - self.scheduled_end_date).days > 0 :
            STATUS = 2 # red   
            
                
        return STATUS

    @cached_property
    def progress_color(self):
        color = ''
        if self.time_status == 0:
            color = 'green'
        elif self.time_status == -1:
            color = 'darkorange'
        else: color ='red'

        return color


    

    @cached_property
    def cost_status(self):
        if self.projected_end_cost is None:
            return 0
        return '{:.2f}'.format((self.projected_end_cost - self.budgeted_cost)*self.weight )

    def __str__(self):
        return '{0}'.format(self.description)

#class Participant(models.Model):
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=30)
#    email = models.EmailField()
#    designation = models.OneToOneField("Designation", on_delete=models.CASCADE, verbose_name='Job Title')
#    department = models.ForeignKey("Department", on_delete=models.CASCADE)
#    initiatives = models.ManyToManyField(Initiative, related_name='participants')
#    is_initiative_manager = models.BooleanField(default=False)
#    image = models.ImageField(upload_to='profile/', blank=True,null=True)


#    @cached_property
#    def full_name(self):
#        return "{0} {1}".format(self.first_name, self.last_name)

#    def __str__(self):
#        return '{0}'.format(self.full_name)

#class Designation(models.Model):
#    title = models.CharField(max_length=30)

#    def __str__(self):
#        return '{0}'.format(self.title)

#class Department(models.Model):
#    name = models.CharField(max_length=30)
#    def __str__(self):
#        return '{0}'.format(self.name)

class Comment(models.Model):
    initiative = models.ForeignKey(Initiative, on_delete=models.CASCADE, related_name='comments', default='', null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return '{0} -{1}'.format(self.content, self.author)


#class File(models.Model):
#    file = models.FileField(upload_to='file/', null=True, blank=True)
#    image = models.ImageField(upload_to='file/', null=True, blank=True)


class Manager(models.Model): # initiative manager(responsibility)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    job_title = models.CharField(max_length=100)    
    image = models.ImageField(upload_to='profile/', blank=True,null=True)
    slug = models.CharField(max_length=10, unique=True, default="manager")

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


