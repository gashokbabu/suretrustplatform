from django.contrib import admin
from .models import Student
# Register your models here.
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['name','registration_no','gender','phone']
#     list_filter = ('user__date_joined','gender',)
#     list_per_page = 25
#     search_fields = ('name','registration_no')

admin.site.register(Student)