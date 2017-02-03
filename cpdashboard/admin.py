from django.contrib import admin
from cpdashboard.models import Perspective, Objective, \
Initiative, Comment, Manager

# Register your models here.
class InitiativeInline(admin.StackedInline):
    model = Initiative
    extra = 0
    

class ObjectiveInline(admin.StackedInline):
    model = Objective
    extra = 0

#class PerspectiveInline(admin.StackedInline):
#    model = Perspective
#    extra = 0
#    max_num = 4

#class CompanyInline(admin.TabularInline):
#    model  = Company
#    extra = 0

#class ParticipantAdmin(admin.ModelAdmin):
#    list_display = ('full_name', 'get_initiatives',  'email', 'is_initiative_manager')
#    search_fields= ('last_name',)

#    def get_initiatives(self, obj):
#        return "\n".join([i.description for i in obj.initiatives.all()])

class InitiativeAdmin(admin.ModelAdmin):
    list_display = (
        "code","description", "scheduled_start_date",
        "scheduled_end_date", "budgeted_cost",
        "performance_measure", "objective", 
        'cost_status', 'time_status', 'is_under_pressure')
    search_fields = ('code', 'objective', 'description')

    #fieldsets = (
    #    (None, {
    #        'fields': ('code_suffix','description', 'objective', 'performance_measure', 'target', 'weight'),
    #    }),
    #    ('More options', {
    #        'classes': ('collapse',),
    #        'fields': (('scheduled_start_date', 'scheduled_end_date'), \
    #            ('actual_start_date', 'projected_end_date'),\
    #            ('budgeted_cost','projected_end_cost'), \
    #            ('budgeted_manhours', 'projected_manhours'),\
    #            ('file', 'image'))
    #    }),
    #)
class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ('code', "description", 'result', 'perspective')
    search_fields = ('code', 'perspective', 'description')
    inlines = [InitiativeInline]

class PerspectiveAdmin(admin.ModelAdmin):
    list_display = ( "description", 'slug',)
    inlines = [ObjectiveInline]

class ManagerAdmin(admin.ModelAdmin):
    list_display = ( "first_name", 'last_name', 'job_title', 'email')
    #inlines = [InitiativeInline]

#class CompanyAdmin(admin.ModelAdmin):
#    fields = ['name']
#    inlines =[PerspectiveInline]

#class IndustryAdmin(admin.ModelAdmin):
#    inlines = [CompanyInline]


    

#admin.site.register(Industry, IndustryAdmin)
#admin.site.register(Company, CompanyAdmin)
admin.site.register(Perspective, PerspectiveAdmin)
admin.site.register(Objective, ObjectiveAdmin)
admin.site.register(Initiative, InitiativeAdmin)
admin.site.register(Manager, ManagerAdmin)
#admin.site.register(Department)
#admin.site.register(Designation)
admin.site.register(Comment)

