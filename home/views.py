import re
import datetime
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from category.models import *
from django.http import HttpResponse, Http404
from userimg.models import *
from raw_material.models import *
import uuid
import qrcode
from io import *
from django.template.loader import get_template
from xhtml2pdf import pisa
from Customer_receipt.models import *
import operator
import pandas as pd
import matplotlib.pyplot as plt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random
from twilio.rest import Client
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Create your views here.
des_time = ''
customer_name = 0
Code_auth = []
def red() :
    return redirect("/")
def home(request):
    return render(request, 'index.html')
def home1(request):
    return redirect('/')
def chori(request):
    a = 0
    dest = Product_View.objects.filter(product_type_id=1)
    for i in dest:
        a = a + 1
        i.id = a
    for i in dest:
        a = a + 1
        if ( i.id%4 == 0) :
            i.p_dis = "in"
    return render(request, 'chori.html', {'dests': dest, 'a1': a})
def gate(request):
    a = 0
    dest = Product_View.objects.filter(product_type_id=2)
    for i in dest:
        a = a+1
        i.id = a
    for i in dest:
        a=a+1
        if(i.id%4 == 0):
            i.p_dis = "in"
    return render(request, 'gate.html', {'dests': dest,'a1': a})
def tablechair(request):
    a = 0
    dest = Product_View.objects.filter(product_type_id=3)
    for i in dest:
        a = a+1
        i.id = a
    for i in dest:
        a = a+1
        if( i.id%4 == 0):
            i.p_dis = "in"
    return render(request, 'tablechair.html', {'dests': dest, 'a1': a})
def paat(request):
    a = 0
    dest = Product_View.objects.filter(product_type_id=4)
    for i in dest:
        a = a+1
        i.id = a

    for i in dest:
        a = a+1
        if(i.id % 4 == 0):
            i.p_dis = "in"
    return render(request, 'paat.html', {'dests': dest,'a1': a})
def others(request):
    a = 0
    dest = Product_View.objects.filter(product_type_id=5)
    for i in dest:
        a = a+1
        i.id = a

    for i in dest:
        a = a+1
        if(i.id % 4 == 0):
            i.p_dis = "in"
    return render(request, 'other.html', {'dests': dest,'a1': a})
uemail = []
ucompanyperno = []
userdata = []
def userregister(request):
    a = 0
    b = 0
    cdi = customer_detail.objects.all()
    if request.method == 'POST':
        customername = request.POST['Customer_Name']
        CustomerAddress = request.POST['Customer_Address']
        companypername = request.POST['company_per_name']
        companyperno = request.POST['company_per_no']
        passwordreg = request.POST['passwordregister']
        passwordconfirmation = request.POST['password_confirmation']
        email = request.POST['email']
        uemail.append(email)
        ucompanyperno.append(companyperno)
        userdata.append(customername), userdata.append(CustomerAddress),userdata.append(companypername),
        userdata.append(companyperno)
        userdata.append(passwordreg), userdata.append(email)
        if len(customername) <= 6 or len(customername) >= 20:
            raise HttpResponse('customer name should be grater then 6 charchter and less then 20  ')
        if len(CustomerAddress) <= 20 or len(CustomerAddress) >= 100:
            raise HttpResponse('customer addresh should be grater then 20 charchter and less then 100')
        if len(str(companyperno)) != 10:
            raise HttpResponse('mobile number should be 10 digit')
        if len(str(passwordreg)) <= 6 or len(str(passwordreg)) >= 20:
            raise HttpResponse('password should be grater then 6 and less then 20 charchter')
        if not re.findall('\d', passwordreg):
            raise HttpResponse("The password must contain at least 1 digit, 0-9.")

        if not re.findall('[a-z]', passwordreg) and re.findall('[A-Z]', passwordreg):
            v1 = 1
            raise HttpResponse(
                ("The password must contain at least 1  letter, A-Z or a-z."),
                code='password_no_upper',
            )
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', passwordreg):
            raise HttpResponse(
                ("The password must contain at least 1 symbol: " +
                  "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
                code='password_no_symbol',
            )
        if passwordreg == passwordconfirmation:
            for cd in cdi:
                 if cd.e_mail == email:
                     a+=1
            for cd in cdi:
                 if cd.com_per_no == companyperno:
                     b+=1
            if (a == 1 and b ==1):
                b = 'Email alredy exist \nor Mobile number is already takken'
                return render(request, 'addcart.html', {'b': b, 'a3': 12})
            if(a==1 and b== 0):
                b = 'Email alredy exist \n Enter new E-mail'
                return render(request, 'addcart.html', {'b': b, 'a3': 12})
            if(b==1 and a==0):
                b = 'Mobile number is alredy takken'
                return render(request, 'addcart.html', {'b': b, 'a3': 12})
        else:
            a += 1
            return HttpResponse("<h1>password is not match try again!!</h1>")
        if(a == 0):
            No = random.randrange(100000, 900000, 7)
            try:
                Code_auth.insert(0, No)
            except:
                return Http404()
            email_code(No, email)
            mobile_code(No, companyperno)
            return render(request, 'VerifyCustomer.html', {'email': email, 'mobile': companyperno})
    else:
        return Http404()
def mobile_code(no, mobile):
    try:
        account_sid = 'AC1a3c9b79884e0757c4fb3119839ffd4c'
        auth_token = 'c1a0335dd78659a5af4e6ac96ad142c3'
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body='Your Verification code is=' + str(no),
            from_='+18634171921',
            to='+91'+str(mobile)
        )
    except:
        pass
def CreateAccount(request):
    if request.method == 'POST':
        Code = request.POST['code']
        try:
             if(int(Code) == int(Code_auth[0])):
                user = customer_detail(c_name = userdata[0], password = userdata[4], e_mail = userdata[5]
                                       , c_add = userdata[1], com_name = userdata[2], com_per_no = userdata[3])
                user.save()
                cimg = customer_img(img_id=user, c_img='static/dummyprofile.jpeg')
                cimg.save()
                b = 'User Is Created Successfully '
                return render(request, 'addcart.html', {'b': b, 'a4': 12})
             else:
                error = 'Wrong Code Try Again!!!'
                return render(request, 'VerifyCustomer.html',
                                   {'email': uemail[0], 'mobile': ucompanyperno[0], 'error': error})
        except:
            error = 'Wrong Code Try Again!!!'
            return render(request, 'VerifyCustomer.html',
                          {'email': uemail[0], 'mobile': ucompanyperno[0], 'error': error})

    else:
        return Http404()
def email_code(no,send_email):
   try:
        msg = MIMEMultipart()
        message = "Your Account verification Code ="+str(no)
        password = "manthan@330"
        msg['From'] = "manthangelot@gmail.com"
        msg['To'] = str(send_email)
        msg['Subject'] = "Yogi Industries Auth Code"
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
   except:
       pass
   finally:
        server.quit()
def timecheck():
    now = datetime.datetime.now()
    current_time = str(int(now.strftime("%H")))
    current_timeM = str(int(now.strftime("%M")))
    return current_time+':'+current_timeM
def userlogin(request):
    t = timecheck()
    cdi = customer_detail.objects.all()
    if request.method == 'POST':
        try:
            first=int(request.POST['email1'])
            if len(str(first)) != 10:
                raise ValidationError('enter a 10 digit mobile no')
            else:
                for cd in cdi:
                    if cd.com_per_no == str(first):
                        em = customer_detail.objects.get(com_per_no=str(first))
                        second = request.POST['email12']
                        if(em.password == second):
                            dests = customer_detail.objects.get(com_per_no=str(first))
                            customer_name = dests.c_id
                            request.session['customer_name'] = customer_name
                            return render(request, 'index.html', {'dest':dests, 't2': t})
                else:
                    b = 'check Mobile_no or password and try again'
                    return render(request, 'addcart.html', {'b': b, 'a3': 12})
        except ValueError:
            first = request.POST['email1']
            if len(first) >= 7:
                for cd in cdi:
                    if cd.e_mail == first:
                        if type(first) == str:
                            em = customer_detail.objects.get(e_mail=first)
                            second = request.POST['email12']
                            if (em.password == second):
                                dests = customer_detail.objects.get(e_mail=first)
                                customer_name = dests.c_id
                                request.session['customer_name'] = customer_name
                                return render(request, 'index.html', {'dest': dests,'t2': t})
                else:
                    b = 'check Email or password and try again'
                    return render(request, 'addcart.html', {'b': b, 'a3': 12})
            else:
                b = 'enter a proper Email'
                return render(request, 'addcart.html', {'b': b, 'a3': 12})

    else:
        t = timecheck()
        dests = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
        return render(request, 'index.html', {'dest': dests, 't2': t})
def userhome(request,user):
    dests = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
    t = timecheck()
    return render(request, 'index.html', {'dest': dests, 't2': t})
def logout(request,ul=1):
    if(ul == 1):
        temp_cart.objects.filter(c_id=str(request.session.get('customer_name'))).all().delete()
        try:
            del request.session['customer_name']
        except KeyError:
            pass
        b = "You're logged out."
        return render(request, 'addcart.html', {'b': b, 'a4': 12})
    else:
        try:
            del request.session['customer_name']
        except KeyError:
            pass
        b = "You're logged out."
        return render(request, 'addcart.html', {'b': b, 'a4': 12})
def profile(request):
    a1 = int(request.session.get('customer_name'))
    cdi = customer_img.objects.all()
    cdi1=customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
    for i in cdi:
        if(i.img_id.c_id == a1):
            dest=customer_img.objects.get(img_id=i.img_id)
            return render(request, 'profile.html',{'dests':dest,'destss':cdi1})
    else:
        return render(request, 'profile.html', {'destss': cdi1})
def disp_chori(request,product_type,p_code):
        try:
            cdi1 = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
            dest = Product_View.objects.get(p_code=p_code)
            a1 = request.session.get('customer_name')
            colors = color.objects.all()
            p_color = PColor.objects.all()
            return render(request, 'display.html', {'dests': dest, 'user' : a1, 'color': colors, 'p_color': p_color})
        except:
            dest = Product_View.objects.get(p_code=p_code)
            return render(request, 'display.html', {'dests': dest, 'user': 0})
def disp_choriI(request,product_type,p_code):
        try:
            cdi1 = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
            dest = Custom_Product.objects.get(p_code=p_code)
            a1 = request.session.get('customer_name')
            colors = color.objects.all()
            p_color = PColor.objects.all()
            return render(request, 'displayI.html', {'dests': dest, 'user': a1, 'color': colors, 'p_color': p_color})
        except:
            dest = Product_View.objects.get(p_code=p_code)
            return render(request, 'display.html', {'dests': dest, 'user': 0})
def finalorder(request,product_type,p_code):
    a = p_code
    dest = Product_View.objects.get(p_code=a)
    colors = color.objects.all()
    return render(request, 'order.html', {'code': p_code,'dest': dest,'color': colors})
def changesName(request):
    if request.method == 'POST':
        chname = request.POST['chname']
        chpass = request.POST['chpass']
        user=customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
        if (user.password == chpass):
            if(len(chname) > 6 and len(chname) < 20):
                user.c_name = chname
                user.save()
                b = 'Change Name Successfully'
                return render(request, 'addcart.html', {'a2': 'a', 'b': b})
            else:
                cons = 'Name'
                error = "name is should be 6 to 20 charchter"
                return render(request, 'changes.html', {'coms': cons, 'er': error})
        error = 'Password Not Match'
        cons = 'Name'
        return render(request, 'changes.html', {'coms': cons, 'er': error})
    else:
        cons='Name'
        return render(request, 'changes.html', {'coms': cons})
def ChangeMobileNumber(request):
    if request.method == 'POST':
        chname = request.POST['chMame']
        chpass = request.POST['chpass']
        user = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
        if (user.password == chpass):
            if(len(chname) == 10):
                try:
                    cn = customer_detail.objects.get(com_per_no=str(chname))
                    b = 'Mobile Number is Alredy Present Try Another Mobile Number'
                    return render(request, 'addcart.html', {'a3': 'a', 'b': b})
                except:
                    user.com_per_no=chname
                    user.save()
                    b = 'Change Mobile Number Successfully'
                    return render(request, 'addcart.html', {'a2': 'a', 'b': b})
            else:
                cons = 'Mobile'
                error = "Mobile Number is should be 10 Digit"
                return render(request, 'changes.html', {'coms': cons,'er':error})
        error = 'Password Not Match'
        cons = 'Mobile'
        return render(request, 'changes.html', {'coms': cons, 'er': error})
    else:
        cons='Mobile'
        return render(request, 'changes.html', {'coms': cons})
email=[]
def ChangeEmail(request):
    if request.method == 'POST':
        chemail = request.POST['chemail']
        chpass = request.POST['chpass']
        user=customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
        if (user.password == chpass):
            if ( len(chemail) > 7 ):
                try:
                    cn = customer_detail.objects.get(e_mail=str(chemail))
                    b = 'E-mail is Alredy Present Try Another E-mail Id'
                    return render(request, 'addcart.html', {'a3': 'a', 'b': b})
                except:
                    No = random.randrange(100000, 900000, 7)
                    try:
                        Code_auth.insert(0,No)
                        email.insert(0,chemail)
                    except:
                        return Http404()
                    email_code(No, chemail)
                    return render(request,'VerifyCustomer.html',{'email': chemail})

            else:
                cons = 'Email'
                error = "Email is to small"
                return render(request, 'changes.html', {'coms': cons, 'er': error})
        error = 'Password Not Match'
        cons = 'Email'
        return render(request, 'changes.html', {'coms': cons, 'er': error})
    else:
        cons = 'Email'
        return render(request, 'changes.html', {'coms': cons})
def ChangedEmail(request):
        Code = request.POST['code']
        user = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
        try:
            if int(Code_auth[0]) == int(Code):
                print(int(Code_auth[0]) == int(Code))
                user.e_mail = email[0]
                user.save()
                b1 = 'Change E-mail Successfully'
                return render(request, 'addcart.html', {'a2': 'a', 'b': b1})
            else:
                error = 'Wrong Code Try Again!!!'
                return render(request, 'VerifyCustomer.html',
                                   {'email': email[0], 'error': error})
        except:
            error = 'Wrong Code Try Again!!!'
            return render(request, 'VerifyCustomer.html',
                          {'email': email[0], 'error': error})
def changesAddress(request):
    if request.method == 'POST':
        chAddress = request.POST['chAddress']
        chpass = request.POST['chpass']
        user=customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
        if (user.password == chpass):
            if (len(chAddress) > 20 and len(chAddress) < 100):
                user.c_add = chAddress
                user.save()
                b = 'Change Address Successfully'
                return render(request, 'addcart.html', {'a2': 'a', 'b': b})
            else:
                cons = 'Address'
                error = "Address is should be 20 to 100 charchter"
                return render(request, 'changes.html', {'coms': cons, 'er': error})
        error = 'Password Not Match'
        cons = 'Address'
        return render(request, 'changes.html', {'coms': cons, 'er': error})
    else:
        cons = 'Address'
        return render(request, 'changes.html', {'coms': cons})
def changesPassword(request):
    v1 = 0
    if request.method == 'POST':
        chnpass = request.POST['chnpass']
        chpass = request.POST['chopass']
        chrpass = request.POST['chrpass']
        user=customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
        if (user.password == chpass):
            if(chnpass == chrpass):
                    if not re.findall('\d', chnpass):
                        v1 = 1
                        raise ValidationError(
                        ("The password must contain at least 1 digit, 0-9."),
                        code='password_no_number',
                    )
                    if not re.findall('[a-z]', chnpass) or re.findall('[A-Z]', chnpass):
                        v1 = 1
                        raise ValidationError(
                            ("The password must contain at least 1  letter, A-Z or a-z."),
                            code='password_no_upper',
                        )
                    if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', chnpass):
                        v1 = 1
                        raise ValidationError(
                            ("The password must contain at least 1 symbol: " +
                             "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
                            code='password_no_symbol',
                        )
                    if(v1 == 0):
                        user.password=chnpass
                        user.save()
                        b = 'Change PassWord Successfully'
                        return render(request, 'addcart.html', {'a2': 'a', 'b': b})
                    else:
                        cons = 'Password'
                        error = "Password Not Match"
                        return render(request, 'changes.html', {'coms': cons, 'er': error})
            else:
                cons = 'Password'
                error = "name is should be 6 to 20 charchter"
                return render(request, 'changes.html', {'coms': cons, 'er': error})
        error = 'Password Not Match'
        cons = 'Password'
        return render(request, 'changes.html', {'coms': cons, 'er': error})
    else:
        cons = 'Password'
        return render(request, 'changes.html', {'coms': cons})

def changesImage(request):
    a1 = int(request.session.get('customer_name'))
    cdi = customer_img.objects.all()
    cdi1 = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
    for i in cdi:
        if (i.img_id.c_id == a1):
            pimage = customer_img.objects.get(img_id=i.img_id)

    if request.method == 'POST':
        chfile = request.FILES['chfile']
        chpass = request.POST['chpass']
        user = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
        if (user.password == chpass):
                pimage.c_img = chfile
                pimage.save()
                b = 'Change Profile Image Successfully'
                return render(request, 'addcart.html', {'a2': 'a', 'b': b})
        else:
            error = 'Password Not Match'
            cons = 'Image'
            return render(request, 'changes.html', {'coms': cons, 'er': error, 'pimage': pimage})
    else:
        cons = 'Image'
        return render(request, 'changes.html', {'coms': cons,'pimage': pimage})
def usercart(request,uname,p_id='2',p_color='hhhh'):
    a = 1
    if p_id == '2' and p_color== 'hhhh':
            user = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
            tmp = temp_cart.objects.filter(c_id=user.c_id)
            sub_totel = 0
            for i in tmp:
                sub_totel += int(i.Totel)
            return  render(request,'cart.html',{'user': user, 'tmp': tmp, 'sub_totel': sub_totel})
    else:
        user = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
        tmp = temp_cart.objects.filter(c_id=user.c_id)
        for i in tmp:
            if (i.modifiction == p_color and i.p_id == p_id):
                delete=temp_cart.objects.get(id=i.id).delete()
        tmp = temp_cart.objects.filter(c_id=user.c_id)
        sub_totel = 0
        for i in tmp:
            sub_totel += int(i.Totel)
        return render(request, 'cart.html', {'user': user, 'tmp': tmp, 'sub_totel': sub_totel})


def Myoreder(request,o_id1=9):
    user = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
    dest = reversed(customer_order.objects.filter(c_id=user.c_id))
    eorder = delivery.objects.all()
    dests = customer_order.objects.filter(c_id=user.c_id)
    einfo = employee_master.objects.all()
    da = {}
    for i in eorder:
        da[int(re.sub('\D', '', str(i.o_id)))]=i.d_add

    de = {}
    for i in eorder:
        de[int(re.sub('\D', '', str(i.o_id)))] = i.e_id

    return render(request, 'myorder.html', {'user' : user, 'dest': dest
        , 'dests': dests, 'edel': eorder, 'einfo': einfo, 'da': da, 'de': de})
def Myorederdetail(request,o_id1=9):
    user = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
    dest = customer_order.objects.filter(c_id=user.c_id)
    eorder = delivery.objects.all()
    einfo = employee_master.objects.all()
    orderdetail = order_detail.objects.filter(o_id=o_id1)
    for i in orderdetail:
        if(i.qty>0):
            return render(request, 'myorder.html', {'user': user, 'dest': dest, 'edel': eorder,
                                                    'einfo': einfo, 'orderdetail': orderdetail,'oidno': o_id1})
            break;
    else:
            orderalert = 'NULL ORDER'
            return render(request,'myorder.html',{'user' : user,'dest' : dest,'edel' : eorder,'einfo' : einfo,
                                                  'orderdetail' : orderdetail,'oidno' : o_id1,'orderalert' : orderalert})
def tempcart(request,product_type,p_color,p_code,p_price,no):
    user = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
    t = temp_cart.objects.filter(c_id=user.c_id)
    a = ''
    for i in t:
        if(i.p_id == p_color):
                if(i.modifiction == p_code):
                        i.qty = str(int(i.qty)+int(no))
                        t = 0
                        for i1 in range(int(i.qty)):
                            t = t + int(p_price)
                        i.Totel = str(t)
                        i.save()
                        a = 'Added in Cart'
                        b = 'Alredy Present so we added in quantity'
                        return render(request, 'addcart.html', {'b' : b})
    pric = int(p_price)
    qty1 = int(no)
    t = 0
    for i in range(qty1):
       t = t + int(p_price)
    totel = t
    tmp = temp_cart(c_id=user.c_id,p_name=product_type,modifiction=p_code,p_id=p_color,qty=no,price=p_price,Totel=totel)
    tmp.save()
    a = 'Add in Cart'
    return render(request, 'addcart.html', {'b': a})
def tempcartI(request,product_type,p_color,p_code,p_price,no,iqu_id):
    user = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
    t = temp_cart.objects.filter(c_id=user.c_id)
    a = ''
    for i in t:
        if (i.p_id == p_color):
            if (i.modifiction == p_code):
                i.qty = str(int(i.qty) + int(no))
                t = 0
                for i1 in range(int(i.qty)):
                    t = t + int(p_price)
                i.Totel = str(t)
                i.save()
                a = 'Added in Cart'
                b = 'Alredy Present so we added in quantity'
                return render(request, 'addcart.html', {'b': b})
    pric = int(p_price)
    qty1 = int(no)
    t = 0
    for i in range(qty1):
       t = t+int(p_price)
    totel = t
    tmp = temp_cart(c_id=user.c_id, p_name=product_type,
                    modifiction=p_code, p_id=p_color, qty=no, price=p_price, Totel=totel)
    tmp.save()
    ip = Inquery_order.objects.get(id=int(iqu_id))
    user = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
    c_p = Custom_Product(c_id=user, p_img=ip.i_img, p_code=ip.c_no, p_description=ip.c_Description,
                         p_type_id=ip.i_type,p_color=ip.i_color,p_price=p_price)
    c_p.save()
    ip.delete()
    a = 'Add in Cart'
    return render(request, 'addcart.html', {'b': a})
def deleteproduct(request, pcode):
    if request.method == 'POST':
        dest = Custom_Product.objects.get(p_code=pcode).delete()
        b = 'Delete Product Successfully'
        return render(request, 'addcart.html', {'a2': 'a', 'b': b})
def order_email(e_mail, id, dstatus):
    orderdetail = order_detail.objects.filter(o_id=int(id))
    totel_amt = 0
    message = '\n' + '------------------------------------------------------------------------------------------'
    message = '            Your order no is ' + str(id) + ' ' + dstatus
    message = message + '\n|' + ' Product Type ' + ' | ' + '     Date     ' + ' | ' + ' Color ' + ' | ' + ' Quntity ' + '|' + '     Price     ' + '|' + '     Totle_Rate     ' \
                                                                                                                                                     '' + '|'
    for i in orderdetail:
        totel_amt = totel_amt + float(i.rate)
        message = message + '\n| ' + str(i.p_id) + '  | ' + str(i.order_date) + ' | ' + str(i.p_color) + '  |     ' \
                  + str(i.qty) + '     |     ' + str(i.price) + '     |     ' + str(i.rate) + '     |     '
    message = message + '\n' + "totel Amt : " + str(totel_amt)
    try:
        msg = MIMEMultipart()
        Message = message
        password = "manthan@330"
        msg['From'] = "manthangelot@gmail.com"
        msg['To'] = str(e_mail)
        msg['Subject'] = "Yogi Industries Order Details"
        msg.attach(MIMEText(Message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
    except:
        pass
    finally:
        server.quit()
def filedorder(request,sub_totel):
    user = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
    tm = datetime.datetime.now()
    d = tm.strftime("%Y-%m-%d")
    cd = customer_order(c_id=user, d_status='no', order_date=d, totel_amt=sub_totel)
    cd.save()
    order=customer_order.objects.get(o_id=cd.o_id)
    tmp=temp_cart.objects.filter(c_id=str(user.c_id))
    for i in tmp:
        tm = datetime.datetime.now()
        d = tm.strftime("%Y-%m-%d")
        odetail = order_detail(o_id=order, p_id=i.p_id+" "+i.p_name, order_date=d, p_color=i.modifiction, qty=i.qty, price=i.price, rate=i.Totel)
        odetail.save()
    tmp.delete()
    mess = 'The product is added in My Order your order id number is='
    order_email(user.e_mail, str(order.o_id), 'without delivery')
    return  render(request, 'cart.html', {'user': user, 'mess': mess, 'o_id': str(order.o_id)})
def filedorderwithdeli(request,sub_totel):
    user = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
    tm = datetime.datetime.now()
    d = tm.strftime("%Y-%m-%d")
    cd = customer_order(c_id=user, d_status='yes', order_date=d, totel_amt=sub_totel)
    cd.save()

    order = customer_order.objects.get(o_id=cd.o_id)
    user = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
    DL = delivery(o_id=order, d_add=user.c_add,)
    DL.save()
    tmp = temp_cart.objects.filter(c_id=str(request.session.get('customer_name')))
    for i in tmp:
        tm = datetime.datetime.now()
        d = tm.strftime("%Y-%m-%d")
        odetail = order_detail(o_id=order, p_id=i.p_id+" "+i.p_name, order_date=d, p_color=i.modifiction, qty=i.qty, price=i.price, rate=i.Totel)
        odetail.save()
    tmp.delete()
    mess = 'The product is added in My Order your order id number is='
    order_email(user.e_mail, str(order.o_id), 'with delivery')
    return render(request, 'cart.html', {'user': user, 'mess': mess, 'o_id': str(order.o_id)})

def inquery_order(request):
        return render(request , 'inquery_order.html')
def new_inquery_order(request):
    if request.method == 'POST':
        user = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
        p_img1 = request.FILES['p_img']
        qty1 = request.POST['qty']
        subject = request.POST['subject']
        product_type = request.POST['product_type']
        color = request.POST['color']

        if (p_img1 == '' ):
            qa = 'You have not select any image'
            return render(request, 'new_inquery_order.html', {'eri': qa})
        if (str(color) == '' or str(color) == '0'):
            qa = 'Color is field is empty'
            return render(request, 'new_inquery_order.html', {'er': qa})
        if str(qty1) == '' or str(qty1) == '0':
            qa='Qunatity is null you have to buy 1 item'
            return render(request, 'new_inquery_order.html',{'er':qa})
        if(str(product_type) == ''):
            qa = 'Product Type is not selected'
            return render(request, 'new_inquery_order.html', {'er': qa})
        if (str(subject) == ''):
            qa = 'Description is Null'
            return render(request, 'new_inquery_order.html', {'er': qa})
        user = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
        iq = Inquery_order(c_id=user, i_type=product_type, i_color=color, i_img=p_img1,
                           c_Description=subject, a_Description='', qty=qty1, a_status='', price='')
        iq.save()
        return render(request, 'new_inquery_order.html', {'sub': 'okay'})
    return render(request, 'new_inquery_order.html')
def inqdata(request):
    user = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
    iqd = Inquery_order.objects.filter(c_id=user)
    return render(request, 'inq_data.html', {'dest': iqd})
def inqueryhistory(request):
    user = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
    dest = Custom_Product.objects.filter(c_id=user)
    a = 0
    for i in dest:
        a = a + 1
        i.id = a
    for i in dest:
        a = a + 1
        if (i.id % 4 == 0):
            i.p_dis = "in"
    return render(request, 'inqueryhistory.html', {'dests': dest, 'a1': a})

def render_to_pdf(template_src, context_dict={}):
        template = get_template(template_src)
        html = template.render(context_dict)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        if not pdf.err:
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return None
def GenBill(request,o_id):
    if(o_id == ''):
        return Http404()
    else:
        data = {
            "company": "Yogi Industries",
            "address": "3,jalaram Estate,Opp Torrent AEC Station,Nr. Shahwadi Bus Stop,Narol-Lambha Road,",
            "city": "Ahmedabad",
            "state": "India",
            "zipcode": "98663",
            "phone": "079-25732942",
            "email": "yogishaileshpanchal@yahoo.co.in",
            "website": "YogiIndustries.com",
        }
        orderdetail = order_detail.objects.filter(o_id=o_id)
        order = customer_order.objects.get(o_id=o_id)
        cri = customer_receipt.objects.filter(o_id=o_id).exists()
        if cri == False :
            qr = qrcode.QRCode(
                version=1,
                box_size=4,
                border=5
            )
            data2 = data
            n=uuid.uuid4()
            user = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
            qr.add_data('RECIEPT id Number='+str(n)+'\n'+'order id Number='+str(o_id)+'\n'+'Customer Name='+user.c_name+' '+str(user.c_id)+'\n'+'Email='+str(user.e_mail)+'\n'+'Customer Mobile.no.='+str(user.com_per_no)
                        +'\n'+'totel Amount='+str(order.totel_amt)
                   )
            qr.make(fit=True)
            user = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
            try:
                delvr = delivery.objects.get(o_id=o_id)
                cr = customer_receipt(r_id=n, o_id=order, c_id=user, d_id=delvr, c_email=user.e_mail,
                                      c_mobile=user.com_per_no,c_amt=order.totel_amt)
            except:
                cr = customer_receipt(r_id=n, o_id=order, c_id=user, c_email=user.e_mail, c_mobile=user.com_per_no,
                                  c_amt=order.totel_amt)
            cr.save()
            img = qr.make_image(fill="black", back_color="white")
            img.save('static/qrcode/' + str(o_id) + '.png')
            dpath = 'static/qrcode/' + str(o_id) + '.png'
            path = os.path.join(BASE_DIR, dpath)
            cr = customer_receipt.objects.get(o_id=o_id)
            user = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
            res = customer_receipt.objects.get(o_id=o_id)
            try:
                delv=delivery.objects.get(o_id=o_id)
                deladdress=delv.d_add
            except:
                deladdress="No delivey"
            pdf = render_to_pdf('app/pdf_template.html', {'data': data, 'ord': orderdetail, 'orc': order, 'com':user,
                'res': res,'add':deladdress,'Path': path,'cr': cr})
            return HttpResponse(pdf, content_type='application/pdf')
        else:
            cr = customer_receipt.objects.get(o_id=o_id)
            dpath = 'static/qrcode/' + str(o_id) + '.png'
            path = os.path.join(BASE_DIR, dpath)
            user = customer_detail.objects.get(c_id=int(request.session.get('customer_name')))
            res = customer_receipt.objects.get(o_id=o_id)
            try:
                delv=delivery.objects.get(o_id=o_id)
                deladdress=delv.d_add
            except:
                deladdress="no delivery"
            pdf = render_to_pdf('app/pdf_template.html',
                                {'data': data,'res': res, 'ord': orderdetail, 'orc': order, 'com': user, 'Path': path,'add':deladdress,'cr': cr})
            return HttpResponse(pdf, content_type='application/pdf')
def DeleteAccount(request):
    customer_detail.objects.filter(c_id=str(request.session.get('customer_name'))).all().delete()
    return redirect("/")
def report(request):
    if request.method == 'POST':
        rep = request.POST['report_type']
        if(rep == 'hsell'):
            od = order_detail.objects.all()
            dis = {}
            for i in od:
                i1 = i.p_id
                if i1 in dis.keys():
                    dis[i1] = dis[i1]+i.qty
                else:
                    dis[i1] = i.qty
            dis = dict(sorted(dis.items(), key=operator.itemgetter(1), reverse=True))
            f = []
            dis1 = {}
            for i, j in dis.items():
                f.append(0)
                if(int(len(f)) <= 10):
                    dis1[i] = j
            lis = list(dis1.values())
            lis2 = list(dis1.keys())
            lis1 = []
            for i in lis2:
                i2 = i.split(" ")
                lis1.append(i2[0]+"\n"+i2[1].capitalize())
            s = pd.Series(lis, lis1)
            fig, ax = plt.subplots()
            s.plot()
            plt.plot(linewidth=2.0)
            plt.ylabel('Qunatity')
            plt.title('Highest Sell \n Product names')
            fig.savefig('d:/d/yogi/static/hsell.png')
            return render(request, 'report_detail.html',{'a': 'Highest Sell Product names', 'dest': dis1})
        if (rep == 'tsell'):
            tm = datetime.datetime.now()
            d = tm.strftime("%Y-%m-%d")
            rte = 0.0
            od=order_detail.objects.filter(order_date=d)
            for i in od:
                rte += float(i.rate)
            return render(request, 'report_detail.html', {'b': 'Total Sell Product names', 'dest': od, 'rate':  rte})
        if (rep == 'mhsell'):
            tm = datetime.datetime.now()
            d = tm.strftime("%Y-%m-%d").split("-")
            d1 = int(d[1])-1
            d3 = int(d[0])
            d4 = int(d[2])
            d2 = datetime.datetime(d3, d1, d4)
            start = datetime.datetime(d3, d1, d4)
            end = datetime.datetime.now()
            date_array = \
                (start + datetime.timedelta(days=x) for x in range(0, (end - start).days+1))
            od = order_detail.objects.all()
            disA = {}
            for date_object in date_array:
                dis = {}
                for i in od:
                    if(str(i.order_date) == str(date_object.strftime("%Y-%m-%d"))):
                        i1 = (i.p_id).split(" ")
                        if i1[0] in dis.keys():
                            dis[i1[0]] = dis[i1[0]] + i.qty
                        else:
                            dis[i1[0]] = i.qty
                        dis = dict(sorted(dis.items(), key=operator.itemgetter(1), reverse=True))
                        fl = []
                        l1 = list(dis)
                        l2 = str(dis[l1[0]])
                        fl.append(l1[0])
                        fl.append(i1[1])
                        fl.append(l2)
                        disA[str(date_object.strftime("%Y-%m-%d"))] = fl
            if(len(disA) <= 8):
                lis = [0]
                lis1 = [0]
                f = []
                dis1 = {}
                for i, j in disA.items():
                    f.append(0)
                    if ( int( len(f) ) <= 10 ):
                        dis1[i] = j
                for i, j in dis1.items():
                    lis.append(int(j[2]))
                    lis1.append(j[0]+"\n "+i)
                lis.append(0)
                lis1.append(0)
            else:
                lis = []
                lis1 = []
                f = []
                dis1 = {}
                for i, j in disA.items():
                    f.append(0)
                    if (int(len(f)) <= 10):
                        dis1[i] = j
                for i, j in dis1.items():
                    lis.append(int(j[2]))
                    lis1.append(j[0] + "\n " + i)
            s = pd.Series(lis, lis1)
            fig, ax = plt.subplots()
            ax.XTickLabelRotation = 45
            s.plot()
            plt.xlabel('Product Name')
            plt.ylabel('Qunatity')
            plt.title('Highest sell Product Of Month')
            fig.savefig('d:/d/yogi/static/mhsell.png')
            return render(request, 'report_detail.html', {'c': 'Highest sell Product Of Month ', 'dest': disA})
        if (rep == 'hmsell'):
            tm = datetime.datetime.now()
            d = tm.strftime("%Y-%m-%d").split("-")
            d1 = int(d[1]) - 1
            d3 = int(d[0])
            d4 = int(d[2])
            d2 = datetime.datetime(d3, d1, d4)
            start = datetime.datetime(d3, d1, d4)
            end = datetime.datetime.now()
            date_array = \
                (start + datetime.timedelta(days=x) for x in range(0, (end - start).days + 1))
            od = order_detail.objects.all()
            disA = {}
            for date_object in date_array:
                dis = {}
                for i in od:
                    if ( str( i.order_date ) == str( date_object.strftime( "%Y-%m-%d" ) ) ):
                            i1 = ( i.p_id ).split(" ")
                            lis = []
                            lis = [i1[1], i.p_color, i.qty, i.rate]
                            if i1[0] in dis:
                                distmp = dis[i1[0]][2]
                                lis = int(lis[2])
                                lis1 = distmp+lis
                                dis[i1[0]] = [i1[1], i.p_color, lis1, i.rate]
                            else:
                                dis[i1[0]] = lis
                            #dis[i1[0]]=lis
                            disA[str(date_object.strftime("%Y-%m-%d"))] = dis
            total = 0.0
            for i, j in disA.items():
                j4 = 0.0
                for j1, j2 in j.items():
                    j4 += float(j2[3])
                total += j4
                j2.append(j4)
            return render(request, 'report_detail.html', {'d': 'Month Sell Total Amount', 'dest': disA, 'total': total})
    return Http404()
def reporta(request):
    if request.method == "POST":
        return render(request, 'report.html')
def get(request):
    tm = datetime.datetime.now()
    d = tm.strftime("%Y-%m-%d")
    dis = {}
    rte = 0.0
    od = order_detail.objects.filter(order_date=d)
    for i in od:
        rte += float(i.rate)
    pdf = render_to_pdf('report_detail.html', {'b': 'Total Sell Product names', 'dest': od,'rate':rte})
    response = HttpResponse(pdf, content_type='application/pdf')
    filename = "Invoice_%s.pdf" % ( "12341231" )
    content = "attachment; filename='%s'" % ( filename )
    response['Content-Disposition'] = content
    return response