import time
import json
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login, logout
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from json import dumps
from .models import ChallanModels, ParticularsModels, PriceModels, Customer, TeamsModels, Product

# import models
# Create your views here.


def dashboard(request):
    if request.user.is_authenticated:
        print(request.user)
        member = TeamsModels.objects.get(username=request.user)
        if member.Designation == "MD":
            return render(request, 'dashboard.html')
        else:
            return redirect('product')
    else:
        return HttpResponse("404- Not found")


def challan(request):
    if request.user.is_authenticated:
        print(request.user)
        member = TeamsModels.objects.get(username=request.user)
        if member.Designation == "MD":
            Challans = ChallanModels.objects.all().order_by('Challan_no').values()
            Particulars = ParticularsModels.objects.all()
            Prices = PriceModels.objects.all()
            result = ChallanModels.objects.values()
            Challans1 = [
                entry for entry in result]
            for i in range(0, len(Challans1)):
                del Challans1[i]['StartDate']
            context = {
                'Challans': Challans,
                'Particulars': Particulars,
                'Prices': Prices,
                'jsonchallan': list(Challans1),
                'table': 'challan'
            }
            return render(request, 'challan.html', context)
        else:
            return HttpResponse("404- Not found")
    else:
        return HttpResponse("404- Not found")


def jobsheet(request):
    if request.user.is_authenticated:
        print(request.user)
        member = TeamsModels.objects.get(username=request.user)
        if member.Designation == "MD":
            Challans = ChallanModels.objects.all().order_by('Challan_no').values()
            Particulars = ParticularsModels.objects.all()
            Prices = PriceModels.objects.all()
            result = ChallanModels.objects.values()
            Challans1 = [
                entry for entry in result]
            for i in range(0, len(Challans1)):
                del Challans1[i]['StartDate']
            context = {
                'Challans': Challans,
                'Particulars': Particulars,
                'Prices': Prices,
                'jsonchallan': list(Challans1)
            }
            return render(request, 'jobsheet.html', context)
        else:
            return HttpResponse("404- Not found")
    else:
        return HttpResponse("404- Not found")


@csrf_exempt
def addnewchallan(request):
    if request.method == "POST":
        data = request.POST
        if data:
            challan = ChallanModels(
                Company_Name=data['nc-companyname'], Contact_Person=data['nc-contactperson'], Mobile_no=data['nc-mobno'], Status=data['nc-status'],
                # Remark=data['nc-remark']
            )
            challan.save()
            print("challan saved")
            for i in range(0, len(data.get('nc-size-desc').split())):
                particular = ParticularsModels(Challan_no_part=ChallanModels.objects.latest(
                    'Challan_no'), Particular_Name=data['nc-particulars-desc'].split()[i], Size=data['nc-size-desc'].split()[i], Amount=data['nc-amount-desc'].split()[i])
                particular.save()
                print("particular ", i, " saved")
            price = PriceModels(Challan_no_part=ChallanModels.objects.latest(
                'Challan_no'), Total_Price=data['nc-totalprice'], Advance_Price=data['nc-advanceprice'], Net_Price=data['nc-netprice'], Paid_by=data['nc-paidby'])
            price.save()
            print("price saved")
            return JsonResponse({"response": "added", "challan": str(ChallanModels.objects.latest(
                'Challan_no'))}, status=200)
    print("post")


@csrf_exempt
def updatechallan(request, pk):
    challan = ChallanModels.objects.get(Challan_no=pk)
    particular = ParticularsModels.objects.filter(Challan_no_part=pk)
    price = PriceModels.objects.get(Challan_no_part=pk)

    if request.method == "POST":
        data = request.POST
        if data:
            challan.Company_Name = data['uc-companyname']
            challan.Contact_Person = data['uc-contactperson']
            challan.Mobile_no = data['uc-mobno']
            challan.Status = data['uc-status']
            challan.Remark = data['uc-remark']
            challan.save()
            print("challan saved")
            if (len(list(particular)) == len(data.get('uc-size-desc').split())):
                for i in range(0, len(data.get('uc-size-desc').split())):
                    particular[i].Particular_Name = data['uc-particulars-desc'].split()[i]
                    particular[i].Size = data['uc-size-desc'].split()[i]
                    particular[i].Amount = data['uc-amount-desc'].split()[i]
                    particular[i].Rate = data['uc-rate-desc'].split()[i]
                    particular[i].Quantity = data['uc-qty-desc'].split()[i]
                    particular[i].save()
                    print("particular ", i, " saved")
            else:
                for i in range(0, len(list(particular))):
                    particular[i].Particular_Name = data['uc-particulars-desc'].split()[i]
                    particular[i].Size = data['uc-size-desc'].split()[i]
                    particular[i].Amount = data['uc-amount-desc'].split()[i]
                    particular[i].Rate = data['uc-rate-desc'].split()[i]
                    particular[i].Quantity = data['uc-qty-desc'].split()[i]
                    particular[i].save()
                    print("particular ", i, " saved")
                for i in range(len(list(particular)), len(data.get('uc-size-desc').split())):
                    parts = ParticularsModels(Challan_no_part=ChallanModels.objects.get(
                        Challan_no=pk), Particular_Name=data['uc-particulars-desc'].split()[
                        i], Size=data['uc-size-desc'].split()[i], Amount=data['uc-amount-desc'].split()[i], Rate=data['uc-rate-desc'].split()[i], Quantity=data['uc-qty-desc'].split()[i])
                    parts.save()
                    print("particular ", i, " saved")
            price.Total_Price = data['uc-totalprice']
            price.Advance_Price = data['uc-advanceprice']
            price.Net_Price = data['uc-netprice']
            price.Paid_by = data['uc-paidby']
            price.save()
            print("price saved")
            return JsonResponse({"response": "updated", "challan": str(pk)}, status=200)
    print("post")


@csrf_exempt
def deletechallan(request, pk):
    challan = ChallanModels.objects.get(Challan_no=pk)
    challan.delete()
    return JsonResponse({"response": "deleted", "challan": str(pk)}, status=200)


@csrf_exempt
def product(request):
    if request.method == "POST":
        data = request.POST
        if data:
            product = Product(
                Customer_mob_product=Customer.objects.get(Mobile_no=data['np-custcode']), job_name=data['np-custjobname'], size_name=data['np-custsize'], Quantity=data['np-custqty'], print_type=data['np-custpside'], print_color=data['np-custprcolor'], paper_name=data['np-custpname'], binding='NA', lamination=data['np-custlamination'], folding=data['np-custfolding'], perforated=data['np-custperforated'], rate=data['np-custrate'], amount=data['np-custamount'], design_status=data['np-custdesigner'])
            product.save()
            print("product saved")
            return JsonResponse({"response": "added"}, status=200)
    product = Product.objects.all()
    context = {
        'Product': product,
        'table': 'product'
    }
    return render(request, 'product.html', context)


@csrf_exempt
def customer(request):
    if request.user.is_authenticated:
        print(request.user)
        member = TeamsModels.objects.get(username=request.user)
        if member.Designation == "MD":
            if request.method == "POST":
                data = request.POST
                if len(data) == 1:
                    try:
                        customer = Customer.objects.get(
                            Mobile_no=data['custcode'])
                        cust_name = customer.Contact_Person
                        return JsonResponse({"cust_name": cust_name}, status=200)
                    except Exception as e:
                        print(e, "inexcept")
                        return JsonResponse({"cust_name": "not-exist"}, status=200)
                elif len(data) > 1:
                    customer = Customer(
                        Company_Name=data['nc-companyname'], Contact_Person=data['nc-contactperson'], Mobile_no=data['nc-mobcust'], Email_id=data[
                            'nc-email'], Area=data['nc-area'], City=data['nc-city'], State=data['nc-state'], Pincode=data['nc-pincode'], Gstin=data['nc-gstin'], Reference=data['nc-refx'], Description=data['nc-description'])
                    customer.save()
                    print("challan saved")
                    return JsonResponse({"response": "added", 'customername': data['nc-contactperson'], "customercode": data['nc-mobcust']}, status=200)
            Customers = Customer.objects.all()
            context = {
                'Customers': Customers,
                'table': 'customer'
            }
            return render(request, 'customer.html', context)
        else:
            return HttpResponse("404- Not found")
    else:
        return HttpResponse("404- Not found")


@csrf_exempt
def savecustomer(request):
    if request.user.is_authenticated:
        print(request.user)
        member = TeamsModels.objects.get(username=request.user)
        if member.Designation == "MD":
            if request.method == "POST":
                data = request.POST
                code = data['code']
                product = Product(
                    Customer_mob_product=Customer.objects.get(Mobile_no=data['np-custcode'+code]), job_name=data['ft-custjobname'+code], size_name=data['ft-custsize'+code], Quantity=data['ft-custqty'+code], print_type=data['ft-custpside'+code], print_color=data['ft-custprcolor'+code], paper_name=data['ft-custpname'+code], binding='NA', lamination=data['ft-custlamination'+code], folding=data['ft-custfolding'+code], perforated=data['ft-custperforated'+code], rate=data['ft-custrate'+code], amount=data['ft-custamount'+code], design_status=data['ft-custdesigner'+code])
                product.save()
                print("product saved")
                return JsonResponse({"response": "added"}, status=200)


@csrf_exempt
def teams(request):
    if request.user.is_authenticated:
        print(request.user)
        member = TeamsModels.objects.get(username=request.user)
        if member.Designation == "MD":
            if request.method == "POST":
                data = request.POST
                if data:
                    member = TeamsModels(Member_name=data['nm-membername'], Designation=data['nm-designation'], Mobile_no=data['nm-mobno'], Email_id=data['nm-email'], Area=data['nm-area'],
                                         City=data['nm-city'], State=data['nm-state'], Pincode=data['nm-pincode'], Department=data['nm-department'], username=data['nm-username'], passcode=data['nm-passcode'])
                    email = data['nm-email']
                    username = data['nm-username']
                    passcode = data['nm-passcode']
                    member.save()
                    myuser = User.objects.create_user(
                        username, email, passcode)
                    myuser.first_name = data['nm-membername'].split()[0]
                    myuser.last_name = data['nm-membername'].split()[1]
                    myuser.save()
                    print("Member added")
                return JsonResponse({"response": "added"}, status=200)
            Teams = TeamsModels.objects.all()
            context = {
                'Teams': Teams,
                'table': 'member'
            }
            return render(request, 'teams.html', context)
        else:
            return redirect('product')
    else:
        return HttpResponse("404- Not found")


def jobstatus(request):
    Jobs4status = Product.objects.all()
    context = {
        'Jobs4status': Jobs4status,
        'table': 'jobstatus'
    }
    return render(request, 'jobstatus.html', context)


# @csrf_exempt
# def mylogin(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        print("login")
        try:
            member = TeamsModels.objects.get(username=data['loginusername'])
            memlogin = loginstatus.objects.get(
                member_login=data['loginusername'])
            if member.passcode == data['loginpassword']:
                memlogin.member_des = member.Designation
                memlogin.loginstatus = 'yes'
                memlogin.save()
                memberlogin = {
                    "member_id": member.member_id,
                    "member_des": member.Designation,
                    "memb_login": memlogin.loginstatus
                }
                return render(request, 'dashboard.html')
            else:
                return JsonResponse({"member": 'not_exist'}, status=200)
        except Exception as e:
            print(e, "inexcept")
            return JsonResponse({"member": "not-exist"}, status=200)

    return render(request, 'login.html')


# @csrf_exempt
def logout(request):
    # if request.method == "POST":
    # data = request.POST
    # memlogin = loginstatus.objects.get(member_login=data['username'])
    # memlogin.loginstatus = 'no'
    # memlogin.save()
    return render(request, 'login.html')


def handleSignUp(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input
        if len(username) < 10:
            messages.error(
                request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(
                request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1 != pass2):
            messages.error(request, " Passwords do not match")
            return redirect('home')

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")


@csrf_exempt
def handeLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            # return redirect("mylogin")
            return HttpResponse("404- Not found")

    # return HttpResponse("404- Not found")

    return render(request, 'login.html')


def handelLogout(request):
    print(request.user)
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('login')
