import graphene
from graphql import GraphQLError
from .types import *
from .queries import *

from .models import *

#Enquiry...........Add................................

class AddEnquiry(graphene.Mutation):
    class Arguments:  
        customerName = graphene.String(required = True)
        contactNo = graphene.Int(required = True)
        email = graphene.String(required = True)
        address = graphene.String(required = True)
        Pincode = graphene.Int(required = True)
        deviceType = graphene.String(required = True)
        Serial_no = graphene.String(required = True)
        brand = graphene.String(required = True)
        deviceModel = graphene.String(required = True)
        problemCategory = graphene.String(required = True)
        problem = graphene.String(required = True)
        deviceCondition = graphene.String(required = True)
        minimum_charge = graphene.Int(required = True)
        status = graphene.String(required = True)
    enquiry = graphene.Field(EnquiryType)
    def mutate(root,info,customerName,contactNo,email,address,Pincode,deviceType,Serial_no,brand,deviceModel,problemCategory,problem,deviceCondition,minimum_charge,status):
        user = info.context.user

        if input is None:
            return AddEnquiry(enquiry = None)
        if user.is_anonymous:
            raise GraphQLError("user must logged in")
        enquiry = Enquiry.objects.create(customerName=customerName,contactNo = contactNo,email = email,address = address,Pincode=Pincode,deviceType=deviceType,Serial_no=Serial_no,brand=brand,deviceModel=deviceModel,problemCategory=problemCategory,problem=problem,deviceCondition=deviceCondition,minimum_charge=minimum_charge,status=status)
        return AddEnquiry(enquiry = enquiry)

#TestDetail.....................Add...................
class AddTestDetail(graphene.Mutation):
    class Arguments:
        Enquiry_Id = graphene.Int()
        actualProblem = graphene.String(required = True)
        actualProblemDescription = graphene.String(required = True)   
        estimatedCost = graphene.Int(required = True)
        advance = graphene.Int(required = True)
    testdetail = graphene.Field(TestDetailType)
    def mutate(root,info,Enquiry_Id,actualProblem,actualProblemDescription,estimatedCost,advance):
        user = info.context.user
        if input is None:
            return AddTestDetail(testdetail = None)
        if user.is_anonymous:
            raise GraphQLError("user must logged in")
        enquiry = Enquiry.objects.get(receiptID = Enquiry_Id)
        testdetail = TestDetail.objects.create(actualProblem = actualProblem,Enquiry=enquiry,actualProblemDescription = actualProblemDescription,estimatedCost = estimatedCost,advance = advance)
        return AddTestDetail(testdetail = testdetail)


#Labour Add..................///////////////////////////////................................

class AddLabour(graphene.Mutation):
    class Arguments:
        # input = LabourInput(required = True)
        Enquiry_Id = graphene.Int()
        Description = graphene.String(required = True)
        Hours = graphene.Int(required = True)   
        Unit = graphene.Float(required = True)
        Labour_Charge = graphene.Float(required = True)
    labour = graphene.Field(LabourType)
    def mutate(root,info,Enquiry_Id,Description,Hours,Unit,Labour_Charge):
        user = info.context.user
        if input is None:
            return AddLabour(labour = None)
        if user.is_anonymous:
            raise GraphQLError("user must logged in")
        enquiry = Enquiry.objects.get(receiptID = Enquiry_Id)
        labour = Labour.objects.create(Description = Description,Enquiry_Id = enquiry,Unit = Unit,Labour_Charge = Labour_Charge,Hours = Hours)
        return AddLabour(labour = labour)

#TaskAssignment Add..............///////////////////////////......Add.......................................

class AddTaskAssignment(graphene.Mutation):
    class Arguments:
        # input = TaskAssignmentInput(required = True)
        Enquiry_Id = graphene.Int(required = True)
        EmployeeName = graphene.Int(required = True)
        TaskTiltle = graphene.String(required = True)   
        TaskDescription = graphene.String(required = True)
        Date = graphene.Date()
    taskassignment = graphene.Field(TaskAssignmentType)

    def mutate(root,info,Enquiry_Id,EmployeeName,TaskTiltle,TaskDescription):
        user = info.context.user
        if input is None:
            return AddTaskAssignment(taskassignment = None)
        if user.is_anonymous:
            raise GraphQLError("user must logged in")
        enquiry = Enquiry.objects.get(receiptID = Enquiry_Id)
        Employee_id = CustomUser.objects.get(id = EmployeeName)
        taskassignment = TaskAssignment.objects.create(TaskTiltle = TaskTiltle,Enquiry = enquiry,TaskCreatedBy = info.context.user,EmployeeName = Employee_id,TaskDescription = TaskDescription )
        return AddTaskAssignment(taskassignment = taskassignment)

# Add Products..........//////////////////////////////////////...........................................

class AddProducts(graphene.Mutation):
    class Arguments:
        Enquiry_Id = graphene.Int(required = True)
        Component_name = graphene.String(required = True)
        Component_quantity = graphene.Int(required = True)  
        Component_amount = graphene.Int(required = True)
        accessories_quantity = graphene.Int(required = True)
        accessories_price = graphene.Int(required = True)
  
    product = graphene.Field(ProductType)

    def mutate(root,info,Enquiry_Id,Component_name,Component_quantity,Component_amount,accessories_quantity,accessories_price):
        user = info.context.user
        if input is None:
            return AddProducts(product = None)
        if user.is_anonymous:
            raise GraphQLError("user must logged in")
        enquiry = Enquiry.objects.get(receiptID = Enquiry_Id)
        product = Product.objects.create(Component_name = Component_name,Enquiry_Id = enquiry,Component_quantity = Component_quantity,Component_amount = Component_amount,accessories_quantity = accessories_quantity,accessories_price = accessories_price )
        return AddProducts(product = product)

#......//////////////..............UpdateSection......................///////////////////////............

# Update....Enquiry..................../////////////////..............
 
class UpdateEnquiryMutation(graphene.Mutation):
    class Arguments:
        receiptID = graphene.Int(required = True)
        customerName = graphene.String()
        contactNo = graphene.Int()
        email = graphene.String()
        address = graphene.String()
        Pincode = graphene.Int()
        deviceType = graphene.String()
        Serial_no = graphene.String()
        brand = graphene.String()
        deviceModel = graphene.String()
        problemCategory = graphene.String()
        problem = graphene.String()
        deviceCondition = graphene.String()
        minimum_charge = graphene.Int()
        status = graphene.String()
    enquiry = graphene.Field(EnquiryType)

    def mutate(root,info,receiptID,customerName = None,contactNo = None,email = None,address = None,Pincode = None,deviceType = None,Serial_no = None,brand = None,deviceModel = None,problemCategory = None,problem = None,deviceCondition = None,minimum_charge = None,status = None):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("user must logged in")
        enquiry = Enquiry.objects.get(receiptID = receiptID)
        enquiry.customerName = customerName if customerName != None and customerName != "" else enquiry.customerName
        enquiry.contactNo = contactNo if contactNo != None and contactNo != "" else enquiry.contactNo
        enquiry.email = email if email != None and email != "" else enquiry.email
        enquiry.address = address if address != None and address != "" else enquiry.address
        enquiry.Pincode = Pincode if Pincode != None and Pincode != "" else enquiry.Pincode
        enquiry.deviceType = deviceType if deviceType != None and deviceType != "" else enquiry.deviceType
        enquiry.Serial_no = Serial_no if Serial_no != None and Serial_no != "" else enquiry.Serial_no
        enquiry.brand = brand if brand != None and brand != "" else enquiry.brand
        enquiry.deviceModel = deviceModel if deviceModel != None and deviceModel != "" else enquiry.deviceModel
        enquiry.problemCategory = problemCategory if problemCategory != None and problemCategory != "" else enquiry.problemCategory
        enquiry.problem = problem if problem != None and problem != "" else enquiry.problem
        enquiry.deviceCondition = deviceCondition if deviceCondition != None and deviceCondition != "" else enquiry.deviceCondition
        enquiry.minimum_charge = minimum_charge if minimum_charge != None and minimum_charge != "" else enquiry.minimum_charge
        enquiry.status = status if status != None and status != "" else enquiry.status
        enquiry.save()
        return UpdateEnquiryMutation(enquiry = enquiry)

# Update..//////......TestDetail..................../////////////////....................................

class UpdateTestDetailMutation(graphene.Mutation):
    class Arguments:
        Enquiry_Id = graphene.Int(required = True)
        actualProblem = graphene.String()
        actualProblemDescription = graphene.String()   
        estimatedCost = graphene.Int()
        advance = graphene.Int()    
    testdetail = graphene.Field(TestDetailType)    
    
    def mutate(self, info, Enquiry_Id, actualProblem=None, actualProblemDescription=None, estimatedCost=None, advance=None):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("user must logged in")
        testdetail = TestDetail.objects.get(Enquiry = Enquiry_Id)
        testdetail.actualProblem = actualProblem if actualProblem != None and actualProblem != "" else testdetail.actualProblem
        testdetail.actualProblemDescription = actualProblemDescription if actualProblemDescription != None and actualProblemDescription != "" else testdetail.actualProblemDescription
        testdetail.estimatedCost = estimatedCost if estimatedCost != None and estimatedCost != "" else testdetail.estimatedCost
        testdetail.advance = advance if advance != None and advance != "" else testdetail.advance
        testdetail.save()
        return UpdateTestDetailMutation(testdetail = testdetail)

# Update..//////......Task Assignment..................../////////////////...............................


class UpdateTaskAssignmentMutation(graphene.Mutation):
    class Arguments:
        Enquiry_Id = graphene.Int(required = True)
        EmployeeName = graphene.Int()
        TaskTiltle = graphene.String()   
        TaskDescription = graphene.String()
        TaskCreatedBy  = graphene.Int()

    taskassignment = graphene.Field(TaskAssignmentType)    
    def mutate(self, info, Enquiry_Id, EmployeeName=None, TaskTiltle=None, TaskDescription=None,TaskCreatedBy = None):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("user must logged in")
        taskassignment = TaskAssignment.objects.get(Enquiry = Enquiry_Id)
        taskassignment.EmployeeName = EmployeeName if EmployeeName != None and EmployeeName != "" else taskassignment.EmployeeName
        taskassignment.TaskTiltle = TaskTiltle if TaskTiltle != None and TaskTiltle != "" else taskassignment.TaskTiltle
        taskassignment.TaskDescription = TaskDescription if TaskDescription != None and TaskDescription != "" else taskassignment.TaskDescription
        taskassignment.TaskCreatedBy = TaskCreatedBy if TaskCreatedBy != None and TaskCreatedBy != "" else taskassignment.TaskCreatedBy
        taskassignment.save()
        return UpdateTaskAssignmentMutation(taskassignment = taskassignment)


# Update..//////......Product..................../////////////////...............................


class UpdateProductsMutation(graphene.Mutation):
    class Arguments:
        Enquiry_Id = graphene.Int(required = True)
        Component_name = graphene.String()
        Component_quantity = graphene.Int()  
        Component_amount = graphene.Int()
        accessories_quantity = graphene.Int()
        accessories_price = graphene.Int()
  
    product = graphene.Field(ProductType)

    product = graphene.Field(ProductType)    
    def mutate(self, info, Enquiry_Id, Component_name=None, Component_quantity=None, Component_amount=None,accessories_quantity = None,accessories_price = None):
        user = info.context.user
        product = Product.objects.get(Enquiry_Id = Enquiry_Id)
        if user.is_anonymous:
            raise GraphQLError("user must logged in")
        product.Component_name = Component_name if Component_name != None and Component_name != "" else product.Component_name
        product.Component_quantity = Component_quantity if Component_quantity != None and Component_quantity != "" else product.Component_quantity
        product.Component_amount = Component_amount if Component_amount != None and Component_amount != "" else product.Component_amount
        product.accessories_quantity = accessories_quantity if accessories_quantity != None and accessories_quantity != "" else product.accessories_quantity
        product.accessories_price = accessories_price if accessories_price != None and accessories_price != "" else product.accessories_price
        product.save()
        return UpdateTaskAssignmentMutation(product = product)

# Update..//////.........Labour..................../////////////////...............................

class UpdateLabourMutation(graphene.Mutation):
    class Arguments:
        Enquiry_Id = graphene.Int()
        Description = graphene.String(required = True)
        Hours = graphene.Int(required = True)   
        Unit = graphene.Float(required = True)
        Labour_Charge = graphene.Float(required = True)
    labour = graphene.Field(LabourType)

    def mutate(self, info, Enquiry_Id, Description=None, Hours=None, Unit=None,Labour_Charge = None):
        user = info.context.user
        labour = Labour.objects.get(Enquiry_Id = Enquiry_Id)
        if user.is_anonymous:
            raise GraphQLError("user must logged in")
        labour.Description = Description if Description != None and Description != "" else labour.Description
        labour.Hours = Hours if Hours != None and Hours != "" else labour.Hours
        labour.Unit = Unit if Unit != None and Unit != "" else labour.Unit
        labour.Labour_Charge = Labour_Charge if Labour_Charge != None and Labour_Charge != "" else labour.Labour_Charge
        labour.save()
        return UpdateLabourMutation(labour = labour)



#.........//////////////..............Delete Section...............//////////////////////////


# Delete..Enquiry...........//////////////...............................////////////////////

class DeleteEnquiryMutation(graphene.Mutation):
    class Arguments:
        Enquiry_Id = graphene.ID()
    enquiry = graphene.Field(EnquiryType)

    @classmethod
    def mutate(cls,root,info,Enquiry_Id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("user must logged in")
        enquiry = Enquiry.objects.get(receiptID=Enquiry_Id)
        enquiry.delete()
        return None

# Delete....TestDetail...........//////////////...............................////////////////////

class DeleteTestDetail(graphene.Mutation):
    class Arguments:
        Enquiry_Id = graphene.ID()
    testdetail = graphene.Field(LabourType)

    @classmethod
    def mutate(cls,root,info,Enquiry_Id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("user must logged in")
        testdetail = TestDetail.objects.get(Enquiry=Enquiry_Id)
        testdetail.delete()
        return None

# Delete....TaskAssignment...........//////////////...............................////////////////////

class DeleteTaskAssignment(graphene.Mutation):
    class Arguments:
        Enquiry_Id = graphene.ID()
    taskassignment = graphene.Field(TaskAssignmentType)

    @classmethod
    def mutate(cls,root,info,Enquiry_Id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("user must logged in")
        taskassignment = TaskAssignment.objects.get(Enquiry=Enquiry_Id)
        taskassignment.delete()
        return None


# Delete....Product...........//////////////...............................////////////////////

class DeleteProduct(graphene.Mutation):
    class Arguments:
        Enquiry_Id = graphene.ID()
    Product = graphene.Field(ProductType)

    @classmethod
    def mutate(cls,root,info,Enquiry_Id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("user must logged in")
        product = Product.objects.get(Enquiry_Id=Enquiry_Id)
        product.delete()
        return None

# Delete....Labour...........//////////////...............................////////////////////

class DeleteLabour(graphene.Mutation):
    class Arguments:
        Enquiry_Id = graphene.ID()
    labour = graphene.Field(LabourType)

    @classmethod
    def mutate(cls,root,info,Enquiry_Id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("user must logged in")
        labour = Labour.objects.get(Enquiry_Id=Enquiry_Id)
        labour.delete()
        return None


#.......////////...........Register Mutations Here........................////////////////////////........
class Mutation(graphene.ObjectType):
    #..........Enquiry Mutation.......................
    add_enquiry = AddEnquiry.Field()
    update_enquiry = UpdateEnquiryMutation.Field()
    delete_enquiry = DeleteEnquiryMutation.Field()
    #.........TestDetail Mutation.....................
    add_testdetail = AddTestDetail.Field()
    update_testdetail = UpdateTestDetailMutation.Field()
    delete_testdetail = DeleteTestDetail.Field()
    #...........TaskAssignment  Mutation...................
    add_taskassignment = AddTaskAssignment.Field()
    update_taskassignment = UpdateTaskAssignmentMutation.Field()
    delete_taskassignment = DeleteTaskAssignment.Field()
    #..........Product Mutation......................
    add_product = AddProducts.Field()
    update_product = UpdateProductsMutation.Field()
    delete_product = DeleteProduct.Field()
    #...........Labour Mutation......................
    add_labour = AddLabour.Field()
    update_labour = UpdateLabourMutation.Field()
    delete_labour = DeleteLabour.Field()

