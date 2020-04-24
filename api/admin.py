from django.contrib import admin

# Register your models here.
from api.models import Vacancy, Company

admin.site.register(Vacancy),
admin.site.register(Company)