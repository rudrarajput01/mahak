from contextlib import nullcontext
from email.policy import default
from random import triangular
from telnetlib import STATUS
from unicodedata import decimal
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
Status_choices = (
    ('Assigned', 'Assigned'),
    ('Pending', 'Pending'),
    ('Waiting', 'Waiting'),
    ('Ready', 'Ready'),
    ('Delivered', 'Delivered'),
)
paidvia_choices = (
    ('Paytm', 'Paytm'),
    ('Cash', 'Cash'),
    ('Phonepe', 'Phonepe'),
    ('Other', 'Other')
)

Job_choice = (
    ('Leaflet', 'Leaflet'),
    ('Visiting Card', 'Visiting Card'),
    ('Invitation Card', 'Invitation Card'),
    ('Brochure', 'Brochure'),
    ('Pamphlet', 'Pamphlet'),
    ('Other', 'Other')
)


class ChallanModels(models.Model):
    Challan_no = models.AutoField(primary_key=True)
    Company_Name = models.CharField(max_length=200)
    Contact_Person = models.CharField(max_length=200)
    Mobile_no = models.CharField(max_length=10)
    StartDate = models.DateField(auto_now_add=True)
    Status = models.CharField(
        max_length=10, choices=Status_choices, default='pending')
    Remark = models.CharField(max_length=200)

    def __str__(self):
        return f"MG{self.Challan_no}"


class ParticularsModels(models.Model):
    Challan_no_part = models.ForeignKey(
        ChallanModels, on_delete=models.CASCADE)
    Particular_Name = models.CharField(max_length=200)
    Size = models.CharField(max_length=20)
    Rate = models.DecimalField(
        default=0.00, max_digits=10, decimal_places=2, blank=True)
    Quantity = models.IntegerField(default=22, blank=True)
    Amount = models.DecimalField(
        default=0.00, max_digits=10, decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.Challan_no_part}"


class PriceModels(models.Model):
    Challan_no_part = models.OneToOneField(
        ChallanModels, on_delete=models.CASCADE, primary_key=True)
    Total_Price = models.DecimalField(
        default=0.00, max_digits=10, decimal_places=2, blank=True)
    Advance_Price = models.DecimalField(
        default=0.00, max_digits=10, decimal_places=2, blank=True)
    Net_Price = models.DecimalField(
        default=0.00, max_digits=10, decimal_places=2, blank=True)
    Paid_by = models.CharField(
        max_length=10, choices=paidvia_choices, default='Cash')

    def __str__(self):
        return f"{self.Challan_no_part}"


class TeamsModels(models.Model):
    Member_name = models.CharField(max_length=20)
    Designation = models.CharField(max_length=20)
    Department = models.CharField(max_length=20)
    Mobile_no = models.CharField(max_length=20)
    Email_id = models.CharField(max_length=20)
    Area = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    City = models.CharField(max_length=20)
    Pincode = models.CharField(max_length=20)
    username = models.CharField(max_length=20, primary_key=True)
    passcode = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.Member_name}"


class JobsheetModels(models.Model):
    Jobsheet_no = models.AutoField(primary_key=True)
    Job_Name = models.CharField(max_length=200)
    Contact_Person = models.CharField(max_length=200)
    Mobile_no = models.CharField(max_length=10)
    StartDate = models.DateField(auto_now_add=True)
    Status = models.CharField(
        max_length=10, choices=Status_choices, default='pending')
    Remark = models.CharField(max_length=200)

    def __str__(self):
        return f"MG{self.Jobsheet_no}"


class Customer(models.Model):
    Company_Name = models.CharField(max_length=200)
    Contact_Person = models.CharField(max_length=200)
    Mobile_no = models.CharField(max_length=20, primary_key="true")
    Email_id = models.CharField(max_length=20)
    Area = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    City = models.CharField(max_length=20)
    Pincode = models.CharField(max_length=20)
    Gstin = models.CharField(max_length=20)
    Reference = models.CharField(max_length=20)
    Description = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.Contact_Person}"


class Product(models.Model):
    Customer_mob_product = models.ForeignKey(
        Customer, on_delete=models.CASCADE)
    job_name = models.CharField(max_length=20)
    size_name = models.CharField(max_length=20)
    Quantity = models.IntegerField()
    print_type = models.CharField(max_length=20)
    print_color = models.CharField(max_length=20)
    paper_name = models.CharField(max_length=20)
    binding = models.CharField(max_length=20)
    lamination = models.CharField(max_length=20)
    folding = models.CharField(max_length=20)
    perforated = models.CharField(max_length=20)
    rate = models.CharField(max_length=20)
    amount = models.CharField(max_length=20)
    design_status = models.CharField(max_length=20, default="pending")

    def __str__(self):
        return f"{self.job_name}"


class DesignerAllotion(models.Model):
    Customer_product = models.ForeignKey(
        Customer, on_delete=models.CASCADE)
    Job_product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    Designer_name = models.CharField(max_length=20)


# class loginstatus(models.Model):
#     member_login = models.OneToOneField(
#         TeamsModels, on_delete=models.CASCADE)
#     member_des = models.CharField(max_length=10)
#     loginstatus = models.CharField(max_length=10)
