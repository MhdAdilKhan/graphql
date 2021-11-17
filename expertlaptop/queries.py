import graphene
from graphene.types import schema
from .types import *
from graphql import GraphQLError


class Query(graphene.ObjectType):
    all_enquiries = graphene.Field(EnquiryType,receiptID=graphene.Int())
    
    all_testdetail = graphene.Field(TestDetailType,Enquiry=graphene.Int())

    all_product = graphene.Field(ProductType,Enquiry=graphene.Int())

    all_labour = graphene.Field(LabourType,Enquiry_Id=graphene.Int())

    all_taskassignment = graphene.Field(TaskAssignmentType,Enquiry=graphene.Int())

    all_billing = graphene.Field(BillingType,CustomerName=graphene.Int())

    def resolve_all_enquiries(root,info,receiptID):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("user must logged in")
        return Enquiry.objects.get(receiptID= receiptID)
    
    def resolve_all_testdetail(root,info,Enquiry):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("user must logged in")
        return TestDetail.objects.get(Enquiry = Enquiry)
    
    def resove_all_product(root,info,Enquiry):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("user must logged in")
        return Product.objects.get(Enquiry = Enquiry)
    
    def resolve_all_labour(root,info,Enquiry_Id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("user must logged in")
        return Labour.objects.get(Enquiry_Id = Enquiry_Id)
    
    def resolve_all_taskassignment(root,info,Enquiry):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("user must logged in")
        return TaskAssignment.objects.get(Enquiry = Enquiry)
    
    def resolve_all_billing(root,info,CustomerName):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("user must logged in")
        return Billing.objects.get(CustomerName=CustomerName)




    






