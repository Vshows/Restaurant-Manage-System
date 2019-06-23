from django.contrib.auth.models import Group
from django.http import request

import xadmin
from xadmin import views
from django.contrib import admin
from .models import user,employee,menu,material,bill,company_bill,table,finance_unit,dispatching_unit,kitchen,order,purchase_unit,cash_unit,check

class GlobalSetting(object):
    site_title = "格朗庭餐馆后台管理系统"
    menu_style = 'accordion'
xadmin.site.register(views.CommAdminView, GlobalSetting)


class employeeAdmin(object):
    list_display = ['short_employee_id','short_employee_name','short_employee_title','short_employee_salary','short_employee_password','short_employee_tel']
    list_filter = ['employee_title']
    fieldsets = [

         ]

class userAdmin(object):
    list_display = ['short_id','short_name','short_password','short_balance','short_real_name','short_link']


class menuAdmin(object):
    list_display = ['short_id','short_name','short_type','short_price']

class checkAdmin(object):
    list_display = ['food','material','number']

class materialAdmin(object):
    list_display = ['short_id','short_name','short_price','short_number']
    def get_readonly_fields(self):
        print(self.request.user.username)
        if self.request.user.is_superuser:
            self.readonly_fields = []
        elif employee.objects.get(employee_id=self.request.user.username).employee_title=='采购员':
            self.readonly_fields=('material_id','material_name','material_price')

        return self.readonly_fields

class billAdmin(object):
    readonly_fields = ('bill_id', 'order_id', 'bill_price')
    list_display = ['short_bill_id','short_user_id','short_order_id','short_cashier_id','short_finance_id','short_dispatching_id','short_dispatching_time','short_dispatching_evaluate','short_bill_price']
    def get_readonly_fields(self):
        print(self.request.user.username)
        if self.request.user.is_superuser:
            self.readonly_fields = []
        elif employee.objects.get(employee_id=self.request.user.username).employee_title=='财务员':
            self.readonly_fields=('bill_id','order_id','bill_price','user_id','cashier_id','dispatching_id','dispatching_time','dispatching_evaluate')

        return self.readonly_fields

class company_billAdmin(object):

    list_display = ['short_bill_id','short_affair','short_profit','short_finance']
    data_charts = {
        'prifit':{'title':'公司利润表','x-field':'bill_id','y-field':'profit'},
    }




class orderAdmin(object):
    list_display = ['short_user_id','short_food_id','short_table_id','short_order_count','short_order_time','short_cook_id']
    def save_model(self,obj):
        food = self.model.objects.get(pk = obj.pk).food_id
        order_count = self.model.objects.get(pk = obj.pk).order_count
        print(food.food_name)
        materials = check.objects.filter(food=food)
        for material in materials:
            count = check.objects.get(food=food, material=material.material).number
            material.material.material_number = material.material.material_number - count * order_count
            material.material.save()


class kitchenAdmin(object):
    list_display = ['short_cook_id','short_cook_name']

class purchase_unitAdmin(object):
    list_display = ['short_purchase_id','short_purchase_name']
class finance_unitAdmin(object):
    list_display = ['short_finance_id','short_finance_id','short_finance_name']
class dispatching_unitAdmin(object):
    list_display = ['short_dispatching_id','short_dispatching_name','short_dispatching_evaluate']
class tableAdmin(object):
    list_display = ['short_table_id','colored_name']
xadmin.site.site_header = '格朗庭餐馆管理系统'
xadmin.site.site_title='餐馆管理后台'
# Register your models here.
#xadmin.site.register(company)
xadmin.site.register(employee,employeeAdmin)
xadmin.site.register(user,userAdmin)
xadmin.site.register(menu,menuAdmin)
xadmin.site.register(check,checkAdmin)
xadmin.site.register(material,materialAdmin)
xadmin.site.register(bill,billAdmin)
xadmin.site.register(company_bill,company_billAdmin)
xadmin.site.register(table,tableAdmin)
xadmin.site.register(purchase_unit,purchase_unitAdmin)
xadmin.site.register(dispatching_unit,dispatching_unitAdmin)
xadmin.site.register(kitchen,kitchenAdmin)
xadmin.site.register(order,orderAdmin)
xadmin.site.register(finance_unit,finance_unitAdmin)
xadmin.site.register(cash_unit)
