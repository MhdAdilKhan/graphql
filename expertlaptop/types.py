from graphene_django import DjangoObjectType

from .models import * 


class EnquiryType(DjangoObjectType):
    class Meta:
        model = Enquiry
        fields = "__all__"

class usersType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = "__all__"


class TestDetailType(DjangoObjectType):
    class Meta:
        model = TestDetail
        fields = "__all__"

class TaskAssignmentType(DjangoObjectType):
    class Meta:
        model = TaskAssignment
        fields = "__all__"
 

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__" 

class LabourType(DjangoObjectType):
    class Meta:
        model = Labour
        fields = "__all__"

class BillingType(DjangoObjectType):
    class Meta:
        model = Billing
        fields = "__all__"       