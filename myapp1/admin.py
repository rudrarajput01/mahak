from django.contrib import admin

from .models import ChallanModels, ParticularsModels, PriceModels, Customer, Product, TeamsModels


# Register your models here.


class ChallanAdmin(admin.ModelAdmin):
    list_display = ('Challan_no', 'Company_Name', 'Contact_Person',
                    'Mobile_no', 'Status', 'Remark', 'StartDate')


class ParticularsAdmin(admin.ModelAdmin):
    list_display = ('Challan_no_part', 'Particular_Name', 'Size',
                    'Amount')


class PricesAdmin(admin.ModelAdmin):
    list_display = ('Challan_no_part', 'Total_Price', 'Advance_Price',
                    'Net_Price', 'Paid_by')


class DesignerAdmin(admin.ModelAdmin):
    list_display = ('Designer_name', 'Designation')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('Company_Name', 'Contact_Person', 'Mobile_no',
                    'Email_id', 'Gstin', 'Reference', 'Description')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('job_name', 'size_name', 'Quantity',
                    'print_type', 'print_color', 'paper_name', 'binding',
                    'lamination', 'folding', 'perforated', 'rate', 'amount')


class TeamsAdmin(admin.ModelAdmin):
    list_display = ('Member_name', 'Department', 'Designation', 'username')


# class LoginAdmin(admin.ModelAdmin):
#     list_display = ('member_login', 'member_des', 'loginstatus')


admin.site.register(ChallanModels, ChallanAdmin)
admin.site.register(ParticularsModels, ParticularsAdmin)
admin.site.register(PriceModels, PricesAdmin)
# admin.site.register(DesignerModels, DesignerAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(TeamsModels, TeamsAdmin)
# admin.site.register(loginstatus, LoginAdmin)
