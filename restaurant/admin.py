from django.contrib import admin
from .models import company,user,employee,menu,material,bill,company_bill,table,finance_unit,dispatching_unit,kitchen,order,purchase_unit

class employeeAdmin(admin.ModelAdmin):
    list_display = ['short_employee_id','short_employee_name','short_employee_title','short_employee_salary','short_employee_password','short_employee_tel']
    list_filter = ['employee_title']
    fieldsets = [

         ]

class userAdmin(admin.ModelAdmin):
    list_display = ['short_id','short_name','short_password','short_balance','short_real_name','short_link']


class menuAdmin(admin.ModelAdmin):
    list_display = ['short_id','short_name','short_type','short_price']

class checkAdmin(admin.ModelAdmin):
    list_display = ['short_food','short_material','short_number']

class materialAdmin(admin.ModelAdmin):
    list_display = ['short_id','short_name','short_price','short_number']

class billAdmin(admin.ModelAdmin):
    list_display = ['short_bill_id','short_order_id','short_cashier_id','short_finance_id','short_dispatching_id','short_dispatching_time','short_dispatching_evaluate','short_bill_price']

class orderAdmin(admin.ModelAdmin):
    list_display = ['short_user_id','short_food_id','short_table_id','short_order_count','short_order_time','short_cook_id']

class kitchenAdmin(admin.ModelAdmin):
    list_display = ['short_cook_id','short_cook_name']
class purchase_unitAdmin(admin.ModelAdmin):
    list_display = ['short_purchase_id','short_purchase_name']
class finance_unitAdmin(admin.ModelAdmin):
    list_display = ['short_finance_id','short_finance_id','short_finance_name']
class dispatching_unitAdmin(admin.ModelAdmin):
    list_display = ['short_dispatching_id','short_dispatching_name','short_dispatching_evaluate']
class tableAdmin(admin.ModelAdmin):
    list_display = ['short_table_id','colored_name']
admin.site.site_header = '格朗庭餐馆管理系统'
admin.site.site_title='餐馆管理后台'
# Register your models here.
admin.site.register(company)
admin.site.register(employee,employeeAdmin)
admin.site.register(user,userAdmin)
admin.site.register(menu,menuAdmin)
#admin.site.register(check,checkAdmin)
admin.site.register(material,materialAdmin)
admin.site.register(bill,billAdmin)
admin.site.register(company_bill)
admin.site.register(table,tableAdmin)
admin.site.register(purchase_unit,purchase_unitAdmin)
admin.site.register(dispatching_unit,dispatching_unitAdmin)
admin.site.register(kitchen,kitchenAdmin)
admin.site.register(order,orderAdmin)
admin.site.register(finance_unit,finance_unitAdmin)

