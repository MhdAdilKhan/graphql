from django.contrib import admin


from expertlaptop.models import Billing, Enquiry, Labour, Product, TaskAssignment, TaskAssignment, TestDetail

# Register your models here.
from .models import *

admin.site.register(Enquiry)

admin.site.register(TestDetail)

admin.site.register(Product)

admin.site.register(Labour)

admin.site.register(Billing)

admin.site.register(TaskAssignment)