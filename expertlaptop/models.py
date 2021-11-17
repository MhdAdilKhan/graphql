from django.db import models

# Create your models here.


from django.db import models

# Create your models here.

from django.db.models.fields import DateField

from custom_user.models import CustomUser


#.................../////////////////////...............ENQUIRY MODEL........///////////


class Enquiry(models.Model):

    receiptID = models.AutoField(primary_key=True)
    enquiryDate = models.DateField(auto_now_add=True)
    customerName = models.CharField(max_length=200)
    contactNo = models.IntegerField()
    email = models.CharField(max_length=2000, blank=True)
    address = models.TextField(null=True, blank=True)
    Pincode = models.IntegerField(null=True)
    deviceType = models.CharField(max_length=200)
    Serial_no = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, null=True, blank=True)
    deviceModel = models.CharField(max_length=200)
    problemCategory = models.CharField(
        max_length=100)
    problem = models.CharField(max_length=200, null=True, blank=True)
    deviceCondition = models.TextField(null=True, blank=True)
    minimum_charge = models.IntegerField(default=0, null=True, blank=True)
    status = models.CharField(
        max_length=100)


    def __str__(self):
        return str(self.receiptID) + " : "  + str(self.status) + " : "  + str(self.customerName) + " : " + str(self.brand) + " : " + str(self.deviceModel) + " :" + str(self.enquiryDate)

#.................../////////////////////...............TEST DETAIL........///////////


class TestDetail(models.Model):
    Enquiry = models.ForeignKey(Enquiry, on_delete=models.CASCADE)
    actualProblem = models.CharField(max_length = 50)
    actualProblemDescription = models.TextField()
    estimatedCost = models.IntegerField()
    advance = models.IntegerField()
    
    def __str__(self):
        return str(self.Enquiry.receiptID) + " : " + str(self.Enquiry.status) + " : " + self.Enquiry.customerName + " : " + self.actualProblem


#.................../////////////////////...............TASK ASSIGNMENT MODEL........///////////


class TaskAssignment(models.Model):
    Enquiry = models.ForeignKey(
        Enquiry, on_delete=models.CASCADE, related_name='enquiry')
    EmployeeName = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='employee_name')
    TaskTiltle = models.CharField(max_length=122)
    TaskCreatedBy = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='admin_name')
    TaskDescription = models.TextField(max_length=122)
    Date = models.DateField(auto_now_add=True)

    
    def __str__(self):
        return str(self.Enquiry.receiptID) + " : " + str(self.Enquiry.status) + " : " + str(self.Enquiry.customerName) + " : " + str(self.TaskCreatedBy)

#.................../////////////////////...............PRODUCT MODEL........///////////

class Product(models.Model):
    Enquiry_Id = models.ForeignKey(Enquiry,on_delete=models.CASCADE)
    Component_name = models.CharField(max_length=200)
    Component_quantity = models.IntegerField(null = True)
    Component_amount = models.FloatField(null = True)
    accessories_quantity = models.IntegerField(null = True)
    accessories_price =models.IntegerField(null = True)

    def __str__(self):
        return str(self.Enquiry_Id)



#.................../////////////////////...............LABOUR MODEL........///////////


class Labour(models.Model):
    Enquiry_Id = models.ForeignKey(Enquiry,on_delete=models.CASCADE)
    Description = models.TextField(max_length=500)
    Hours = models.IntegerField(null = True)
    Unit = models.IntegerField(null = True)
    Labour_Charge = models.FloatField(null=True)


    def __str__(self):
        return str(self.Enquiry_Id)

#.................../////////////////////...............BILLING MODEL........///////////

class Billing(models.Model):
    CustomerName = models.ForeignKey(
        Enquiry, on_delete=models.CASCADE)
        
    total_amount = models.IntegerField(null=True)

    def __str__(self):
        return str(self.CustomerName)
