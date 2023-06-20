from django.contrib import admin

from app.models import JobPost, Location, Author, Skills

class JobAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'date', 'salary', 'description')
    list_filter = ('date', 'salary', 'description', 'expiry')
    search_fields =['date', 'salary', 'title', 'description', 'expiry']
    search_help_text = "Write in a query and hit enter"
    # fields = (('title', 'description'),'expiry')
    # exclude = ('title',)  #### this is to exclude certain fields
    fieldsets = (
        ('Basic information', { 
         'fields' :('title', 'description')
        }),
        ('More information', { 
         'classes' :('collapse', 'wide'),
         'fields' :(('expiry', 'salary'), 'slug')
        }),
    )
    
# Register your models here.
admin.site.register(JobPost)
# admin.site.register(JobAdmin)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)