import datetime
import random

from django import forms
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django_redis import get_redis_connection
from django.core.cache import cache
from .models import menu, bill, table, user,order,kitchen,dispatching_unit,purchase_unit,cash_unit,employee,check,material,company_bill


# Create your views here.

class UserInfo(forms.Form):
    user_id = forms.IntegerField()
    password = forms.CharField()

def index(request):

    try:
        user_name = request.session.get('user_name')
        user_balance = user.objects.get(user_id=request.session['user_id']).user_balance
        menu_list = menu.objects.all()
        m = []
        for i in menu_list:
            m.append(i.food_type)
        new = []
        for n in m:
            if n not in new:
                new.append(n)
        context = {
            'menu_list': new,
            'user_name':request.session['user_name'],
            'user_balance':user_balance,
            'user_id':request.session['user_id']
        }
        return render(request, 'index.html', context)
    except:

        return HttpResponseRedirect("login/")

def menu_list(request,name):
    menu_list = menu.objects.filter(food_type=name)
    user_name = request.session['user_name']
    user_balance = user.objects.get(user_id=request.session['user_id']).user_balance
    context = {
        'user_name':user_name,
        'user_balance':user_balance,
        'menu':menu_list,
        'name':name,
    }
    return render(request,'menu_list.html',context)

def login(request):
    return render(request,'login.html')
def detail(request,name):
    menu_list = menu.objects.all()
    user_name  = request.session['user_name']
    user_balance = user.objects.get(user_id=request.session['user_id']).user_balance
    for i in menu_list:
        if i.food_name == name:
            list = i
    context = {
        'user_name':user_name,
        'user_balance':user_balance,
        'food_list': list
    }
    return render(request,'food_detail.html',context)

def logout(request):
    del request.session["user_name"]
    del request.session["user_id"]
    del request.session['user_balance']
    return HttpResponseRedirect('../login')

def user_check(request):
    if request.method=="POST":
        try:
            User_id = request.POST['Username']
            Password = request.POST['Password']
            User = user.objects.filter(user_id=User_id)[0]
            if User.user_password==Password:
                request.session['user_id'] = User_id
                request.session['user_name'] = User.user_name
                request.session['user_balance'] = User.user_balance
                return HttpResponseRedirect('..')
            else:
                return render(request,'login.html',{'msg':'用户名或者密码错误！'})
        except:
            return render(request, 'login.html', {'msg': '用户名或者密码错误！'})
def user_add(request):
    if request.method=='POST':
        user_name = request.POST['Username']
        password = request.POST['Password']
        user_link = request.POST['Phone']
        try:
            if user.objects.get(user_link=user_link):
                message = "邮箱已存在"
                return render(request, 'login.html', {'m':message})
        except:
            user.user_link = user_link
        real_name = request.POST['Real_name']
        if user.objects.last()!=None:
            user_id = user.objects.last().user_id+1
        else:
            user_id = 10000
        user.objects.create(user_id=user_id,user_name=user_name,user_link=user_link,user_balance=0,user_real_name=real_name,user_password=password)
        return render(request,'login.html',{"success":'恭喜！注册成功！您的用户ID为：'+str(user_id)})

def cart_add(request):
    food_name = request.POST.get('food_name')
    count = request.POST.get('count')
    count = int(count)
    conn = get_redis_connection('default')
    cart_key = 'cart_'+str(request.session['user_id'])
    cart_count = conn.hget(cart_key,food_name)
    if cart_count:
        count = int(cart_count)+count
    conn.hset(cart_key,food_name,count)
    cart_count = conn.hlen(cart_key)
    return JsonResponse({'cart_count':cart_count, 'message':'添加成功','food_name':food_name,})

def evaluate(request):
    evaluate_value = request.POST.get('evaluate')
    bill_id = request.session['bill_id']
    bill.objects.filter(bill_id=bill_id)[0].dispatching_evaluate = evaluate_value
    return JsonResponse({'msg':1})

def cancel(request):

    conn = get_redis_connection('default')
    user_id = request.session['user_id']
    conn.delete('cart_'+user_id)

    return HttpResponseRedirect('../cart')

def edit(request):
    return render(request,'edit.html')
def edit_solve(request):
    try:
        user_name = request.POST.get('Username')
        password = request.POST.get('Password')
        user_id = request.session['user_id']
        User = user.objects.get(user_id=user_id)
        User.user_name = user_name
        User.user_password = password
        User.save()

    except:
        return HttpResponseRedirect('../login')
    return HttpResponseRedirect('../login')
def cart(request):
    conn = get_redis_connection('default')
    try:
        user_id = request.session['user_id']



        user_balance = user.objects.get(user_id=user_id).user_balance
        cart_key = 'cart_'+str(user_id)
    except:
        return HttpResponseRedirect('../login')
    dict = conn.hgetall(cart_key)
    foods=[]
    total_count = 0
    total_price = 0
    for food_name,count in dict.items():

        food_name = str(food_name,'utf-8')
        if food_name!=None:

            food = menu.objects.get(food_name=food_name)
            amount = food.food_price*int(count)
            food.amount = amount
            food.count =int(count)
            foods.append(food)
            total_count+=int(count)
            total_price+=amount

    context = {
            'user_name':request.session['user_name'],
            'user_balance':user_balance,
            'foods':foods,
            'total_count':total_count,
            'total_price':total_price,
        }

    return render(request,'cart.html',context)

def bill_create(request):
    conn = get_redis_connection('default')
    key ='cart_'+str(request.session['user_id'])
    cart = conn.hgetall(key)
    for food_name,count in cart.items():
        food_name = str(food_name,'utf-8')
        print(food_name)
        try:
            food = menu.objects.get(food_name=food_name)
        except:
            continue
        food_count  = int(count)
        materials = check.objects.filter(food=food)
        for material in materials:
            count = check.objects.get(food=food,material=material.material).number
            material.material.material_number =   material.material.material_number - count*food_count
            material.material.save()




    food_price = request.POST.get('food_price')
    user_id = request.session['user_id']
    User = user.objects.filter(user_id=user_id)[0]
    User.user_balance = User.user_balance - int(food_price)
    User.save()
    if bill.objects.last() != None:
        bill_id = int(bill.objects.last().bill_id) + 1
    else:
        bill_id = 10000

    request.session['bill_id'] = bill_id
    i=random.randint(0,1)

    if i==1:
        bill.objects.create(bill_id=bill_id, user_id=User, bill_price=food_price,dispatching_time=random.randint(20,60),dispatching_id=dispatching_unit.objects.filter(dispatching_name='李玲')[0],dispatching_evaluate=random.randint(60,100))
    else:
        bill.objects.create(bill_id=bill_id, user_id=User, bill_price=food_price,dispatching_time=random.randint(20,60),dispatching_id=dispatching_unit.objects.filter(dispatching_name='李凌')[0],dispatching_evaluate=random.randint(60,100))

    conn.delete('cart_'+user_id)
    company_bill.objects.create(bill_id=bill_id,affair='餐厅业务收入',profit=food_price)
    return JsonResponse()
