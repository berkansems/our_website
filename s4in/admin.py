from django.contrib import admin
from .models import *
# Register your models here.


class PostImageAdmin(admin.StackedInline):
    model = Pictures

@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','type','sector','link','showInMainPage')
    list_filter = ('sector','type')
    search_fields = ('name','sector')
    ordering = ('name',)
    inlines = [PostImageAdmin]


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name','description')




admin.site.register(Sectors)
admin.site.register(MainPage)
admin.site.register(AboutUs)
admin.site.register(Services,ServicesAdmin)
admin.site.register(WhyUs)
admin.site.register(Advantages)
admin.site.register(Address)
