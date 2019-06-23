

from django.db import models

# Create your models here.
from django.utils import timezone
from django.utils.html import format_html


class company(models.Model):
    def __str__(self):
        return self.company_name+'公司资料'
    company_name = models.CharField(max_length=20)
    company_finance = models.IntegerField(default=100000)
    company_address = models.CharField(max_length=30)

class employee(models.Model):
    def __str__(self):
        return self.employee_id+' '+self.employee_title+' '+self.employee_name
    employee_id = models.CharField(max_length=20,primary_key=True)
    employee_name = models.CharField(max_length=10)
    employee_title = models.CharField(max_length=10)
    employee_salary = models.IntegerField(default=1000)
    employee_password = models.CharField(max_length=30)
    employee_tel = models.CharField(max_length=20)
    def short_employee_name(self):
        return self.employee_name
    def short_employee_id(self):
        return self.employee_id
    def short_employee_title(self):
        return self.employee_title
    def short_employee_salary(self):
        return self.employee_salary
    def short_employee_password(self):
        return self.employee_password
    def short_employee_tel(self):
        return self.employee_tel
    short_employee_name.short_description = '员工姓名'
    short_employee_id.short_description = '员工编号'
    short_employee_title.short_description = '员工职称'
    short_employee_salary.short_description = '员工薪水'
    short_employee_password.short_description = '员工密码'
    short_employee_tel.short_description = '员工电话'

    class Meta:
        verbose_name = '员工信息管理'
        verbose_name_plural = verbose_name

class cash_unit(models.Model):
    def __str__(self):
        return '收款员：'+self.cash_name
    cash_id = models.ForeignKey(employee,on_delete=models.CASCADE,unique=True,verbose_name='员工编号')
    cash_name = models.CharField(max_length=10,verbose_name='员工姓名')
    class Meta:
        verbose_name = '收银部门'
        verbose_name_plural = verbose_name
class purchase_unit(models.Model):
    def __str__(self):
        return '采购员:'+self.purchase_id.employee_id+' '+self.purchase_name
    purchase_id = models.ForeignKey(employee,on_delete=models.CASCADE,primary_key=True,unique=True,related_name='purchase_id',default='')
    purchase_name = models.CharField(max_length=10)
    def short_purchase_id(self):
        return self.purchase_id
    def short_purchase_name(self):
        return self.purchase_name
    short_purchase_id.short_description = '员工编号'
    short_purchase_name.short_description = '员工姓名'

    class Meta:
        verbose_name = '采购部门'
        verbose_name_plural = verbose_name
class kitchen(models.Model):
    def __str__(self):
        return '厨师:' + self.cook_id.employee_id+' '+self.cook_name
    cook_id = models.ForeignKey(employee,on_delete=models.CASCADE,primary_key=True,unique=True,related_name='cook_id',default='')
    cook_name = models.CharField(max_length=10)
    def short_cook_id(self):
        return self.cook_id
    def short_cook_name(self):
        return self.cook_name
    short_cook_id.short_description = '员工编号'
    short_cook_name.short_description = '员工姓名'

    class Meta:
        verbose_name = '厨房'
        verbose_name_plural = verbose_name

class finance_unit(models.Model):
    def __str__(self):
        return '财务员:' + self.finance_id.employee_id+' '+self.finance_name
    finance_id = models.ForeignKey(employee,on_delete=models.CASCADE,primary_key=True,unique=True,related_name='finance_id',default=
                                   '')
    finance_name = models.CharField(max_length=10)

    def short_finance_id(self):
        return self.finance_id

    def short_finance_name(self):
        return self.finance_name

    short_finance_id.short_description = '员工编号'
    short_finance_name.short_description = '员工姓名'

    class Meta:
        verbose_name = '财务部门'
        verbose_name_plural = verbose_name

class dispatching_unit(models.Model):
    def __str__(self):
        return '配送员:' + self.dispatching_id.employee_id+' '+self.dispatching_name
    dispatching_id = models.ForeignKey(employee,on_delete=models.CASCADE,primary_key=True,unique=True,related_name='dispatching_id',default='')
    dispatching_name = models.CharField(max_length=10)
    dispatching_evaluate = models.IntegerField(default=0)

    def short_dispatching_id(self):
        return self.dispatching_id

    def short_dispatching_name(self):
        return self.dispatching_name
    def short_dispatching_evaluate(self):
        return self.dispatching_evaluate

    short_dispatching_id.short_description = '员工编号'
    short_dispatching_name.short_description = '员工姓名'
    short_dispatching_evaluate.short_description = '员工评价'

    class Meta:
        verbose_name = '配送部门'
        verbose_name_plural = verbose_name


class user(models.Model):
    def __str__(self):
        return str(self.user_id)+' '+self.user_name
    user_id = models.IntegerField(default=10000,primary_key=True)
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=30)
    user_link = models.CharField(max_length=30)
    user_balance = models.IntegerField(default=100)
    user_real_name = models.CharField(max_length=20,default='')
    def short_name(self):
        return self.user_name
    def short_id(self):
        return self.user_id
    def short_password(self):
        return self.user_password
    def short_link(self):
        return self.user_link
    def short_balance(self):
        return self.user_balance
    def short_real_name(self):
        return self.user_real_name
    short_name.short_description = '用户姓名'
    short_id.short_description = '用户编号'
    short_password.short_description = '用户密码'
    short_link.short_description = '用户电话'
    short_balance.short_description = '用户余额'
    short_real_name.short_description = '用户真实姓名'

    class Meta:
        verbose_name = '用户信息管理'
        verbose_name_plural = verbose_name

class menu(models.Model):
    def __str__(self):
        return self.food_name
    food_id = models.CharField(max_length=10,primary_key=True)
    food_name = models.CharField(max_length=20)
    food_type = models.CharField(max_length=6)
    food_price = models.IntegerField(default=1000)
    food_image = models.CharField(max_length=100)
    food_description = models.CharField(max_length=1000,default='')

    class Meta:
        verbose_name = '菜品信息管理'
        verbose_name_plural = verbose_name

    def short_id(self):
        return self.food_id
    def short_name(self):
        return self.food_name
    def short_type(self):
        return self.food_type
    def short_price(self):
        return self.food_price
    short_name.short_description = '菜品名称'
    short_id.short_description = '菜品编号'
    short_type.short_description = '菜品类型'
    short_price.short_description = '菜品单价'

class material(models.Model):
    def __str__(self):
        return self.material_name
    material_id = models.CharField(max_length=10,primary_key=True)
    material_name = models.CharField(max_length=10)
    material_price = models.IntegerField(default=1000)
    material_number = models.IntegerField(default=1000)

    class Meta:
        verbose_name = '食材信息管理'
        verbose_name_plural = verbose_name

    def short_id(self):
        return self.material_id
    def short_name(self):
        return self.material_name
    def short_number(self):
        return self.material_number
    def short_price(self):
        return self.material_price

    short_name.short_description = '食材名称'
    short_id.short_description = '食材编号'
    short_number.short_description = '剩余量(kg)'
    short_price.short_description = '食材单价'

class check(models.Model):
    def __str__(self):
        return self.food.food_name+' '+self.material.material_name
    food = models.ForeignKey(menu,on_delete=models.CASCADE,related_name='food',verbose_name='菜品')
    material = models.ForeignKey(material,on_delete=models.CASCADE,related_name='material',verbose_name='食材')
    number = models.FloatField(default=0,verbose_name='所需数量')
    class Meta:
       verbose_name = '菜品食材对照表'
       verbose_name_plural = verbose_name


class bill(models.Model):
    def __str__(self):
        return self.bill_id+'号账单'
    bill_id = models.CharField(max_length=50,primary_key=True)
    order_id = models.ForeignKey('order',on_delete=models.CASCADE,null=True,blank=True)
    user_id = models.ForeignKey('user',on_delete=models.CASCADE)
    cashier_id = models.ForeignKey(cash_unit,on_delete=models.CASCADE,null=True,blank=True)
    finance_id = models.ForeignKey(finance_unit,on_delete=models.CASCADE,null=True,blank=True)
    dispatching_id = models.ForeignKey(dispatching_unit,on_delete=models.CASCADE,null=True,blank=True)
    dispatching_time = models.IntegerField(null=True,blank=True)
    dispatching_evaluate = models.IntegerField(default=None,null=True,blank=True)
    bill_price = models.IntegerField(default=1000)
    bill_check_time = models.DateTimeField(default=None,null=True,blank=True)


    def short_bill_id(self):
        return self.bill_id
    def short_order_id(self):
        return self.order_id
    def short_user_id(self):
        return self.user_id
    def short_cashier_id(self):
        return self.cashier_id
    def short_finance_id(self):
        return self.finance_id
    def short_dispatching_id(self):
        return self.dispatching_id
    def short_dispatching_time(self):
        return self.dispatching_time
    def short_dispatching_evaluate(self):
        return self.dispatching_evaluate
    def short_bill_price(self):
        return self.bill_price
    def short_check_time(self):
        return self.bill_check_time

    class Meta:
        verbose_name = '账单管理'
        verbose_name_plural = verbose_name

    short_bill_id.short_description = '账单编号'
    short_order_id.short_description = '点菜单编号'
    short_user_id.short_description = '用户编号'
    short_cashier_id.short_description = '收银员编号'
    short_finance_id.short_description = '财务员编号'
    short_dispatching_id.short_description = '配送员编号'
    short_dispatching_time.short_description = '配送时间'
    short_dispatching_evaluate.short_description = '本次配送评价'
    short_bill_price.short_description = '账单总价'
    short_check_time.short_description = '审计时间'


class table(models.Model):
    def __str__(self):
        return str(self.table_id)+'号桌'
    table_id = models.CharField(max_length=3,default='',primary_key=True)
    table_status  = models.IntegerField(default=1)

    def short_table_id(self):
        return self.table_id

    def short_table_status(self):
        return self.table_status

    def colored_name(self):
        if self.table_status == 1:
            color_code = '04e100'
            text = '空闲中'
        else:
            color_code = 'f00'
            text = '被占用'

        return format_html(
            '<span style="color: #{};">{}</span>',
            color_code,
            text,
        )

    short_table_id.short_description = '餐桌编号'
    colored_name.short_description = '餐桌状态'

    class Meta:
        verbose_name = '餐桌管理'
        verbose_name_plural = verbose_name


class order(models.Model):
    def __str__(self):
        return '点菜单：'+self.order_id
    order_id = models.CharField(max_length=10,primary_key=True)
    user_id = models.ForeignKey(user,on_delete=models.CASCADE)
    food_id = models.ForeignKey(menu,on_delete=models.CASCADE)
    table_id = models.ForeignKey(table,on_delete=models.CASCADE,null=True,blank=True)
    order_count = models.IntegerField(default=0)
    order_time = models.DateTimeField(auto_now=True)
    cook_id = models.ForeignKey(kitchen,on_delete=models.CASCADE)
    def short_table_id(self):
        return self.table_id
    def short_order_id(self):
        return self.order_id
    def short_user_id(self):
        return self.user_id
    def short_food_id(self):
        return self.food_id.food_name
    def short_cook_id(self):
        return self.cook_id.cook_id
    def short_order_count(self):
        return self.order_count
    def short_order_time(self):
        return self.order_time

    class Meta:
        verbose_name = '点菜单管理'
        verbose_name_plural = verbose_name

    short_food_id.short_description = '菜品名称'
    short_order_id.short_description = '点菜单编号'
    short_user_id.short_description = '用户编号'
    short_cook_id.short_description = '厨师编号'
    short_table_id.short_description = '餐桌编号'
    short_order_count.short_description = '点菜数量'
    short_order_time.short_description = '点菜时间'
class company_bill(models.Model):
    def __str__(self):
        return self.bill_id+'号财务流水'

    bill_id = models.CharField(max_length=20,verbose_name='流水号',primary_key=True,default=10000)
    affair = models.CharField(max_length=20,verbose_name='事件')
    profit = models.IntegerField(default=1000,verbose_name='收入')
    finance = models.ForeignKey(finance_unit,on_delete=models.CASCADE,null=True,blank=True,verbose_name='处理人')


    def short_bill_id(self):
        return self.bill_id

    def short_affair(self):
        return self.affair

    def short_profit(self):
        return self.profit

    def short_finance(self):
        return self.finance


    short_bill_id.short_description = '流水编号'
    short_affair.short_description = '业务类型'
    short_profit.short_description = '收入支出'
    short_finance.short_description = '处理人'

    class Meta:
        verbose_name = '公司资金流水'
        verbose_name_plural = verbose_name


