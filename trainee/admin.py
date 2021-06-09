from django.contrib import admin
from .models import Student,ContactUs
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','registration_no','gender','phone']
    list_filter = ('user__date_joined','gender',)
    list_per_page = 25
    search_fields = ('name','registration_no')
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['student','subject','resolved']
    list_filter = ['date','resolved']
    list_per_page = 25

admin.site.register(Student,StudentAdmin)
admin.site.register(ContactUs,ContactUsAdmin)