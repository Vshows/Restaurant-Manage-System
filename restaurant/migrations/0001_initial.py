# Generated by Django 2.1.1 on 2018-09-19 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bill',
            fields=[
                ('bill_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('dispatching_time', models.IntegerField(blank=True, null=True)),
                ('dispatching_evaluate', models.IntegerField(blank=True, default=None, null=True)),
                ('bill_price', models.IntegerField(default=1000)),
                ('bill_check_time', models.DateTimeField(default=None)),
            ],
            options={
                'verbose_name': '账单管理',
                'verbose_name_plural': '账单管理',
            },
        ),
        migrations.CreateModel(
            name='cash_unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash_name', models.CharField(max_length=10, verbose_name='员工编号')),
            ],
            options={
                'verbose_name': '收银部门',
                'verbose_name_plural': '收银部门',
            },
        ),
        migrations.CreateModel(
            name='check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.FloatField(default=0, verbose_name='所需数量')),
            ],
            options={
                'verbose_name': '菜品食材对照表',
                'verbose_name_plural': '菜品食材对照表',
            },
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=20)),
                ('company_finance', models.IntegerField(default=100000)),
                ('company_address', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='company_bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.CharField(max_length=20)),
                ('affair', models.CharField(max_length=20)),
                ('profit', models.IntegerField(default=1000)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('employee_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=10)),
                ('employee_title', models.CharField(max_length=10)),
                ('employee_salary', models.IntegerField(default=1000)),
                ('employee_password', models.CharField(max_length=30)),
                ('employee_tel', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '员工信息管理',
                'verbose_name_plural': '员工信息管理',
            },
        ),
        migrations.CreateModel(
            name='material',
            fields=[
                ('material_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('material_name', models.CharField(max_length=10)),
                ('material_price', models.IntegerField(default=1000)),
                ('material_number', models.IntegerField(default=1000)),
            ],
            options={
                'verbose_name': '食材信息管理',
                'verbose_name_plural': '食材信息管理',
            },
        ),
        migrations.CreateModel(
            name='menu',
            fields=[
                ('food_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('food_name', models.CharField(max_length=20)),
                ('food_type', models.CharField(max_length=6)),
                ('food_price', models.IntegerField(default=1000)),
                ('food_image', models.CharField(max_length=100)),
                ('food_description', models.CharField(default='', max_length=1000)),
            ],
            options={
                'verbose_name': '菜品信息管理',
                'verbose_name_plural': '菜品信息管理',
            },
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('order_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('order_count', models.IntegerField(default=0)),
                ('order_time', models.DateTimeField(auto_now=True)),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.menu')),
            ],
            options={
                'verbose_name': '点菜单管理',
                'verbose_name_plural': '点菜单管理',
            },
        ),
        migrations.CreateModel(
            name='table',
            fields=[
                ('table_id', models.CharField(default='', max_length=3, primary_key=True, serialize=False)),
                ('table_status', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': '餐桌管理',
                'verbose_name_plural': '餐桌管理',
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.IntegerField(default=10000, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=20)),
                ('user_password', models.CharField(max_length=30)),
                ('user_link', models.CharField(max_length=30)),
                ('user_balance', models.IntegerField(default=1000)),
                ('user_real_name', models.CharField(default='', max_length=20)),
            ],
            options={
                'verbose_name': '用户信息管理',
                'verbose_name_plural': '用户信息管理',
            },
        ),
        migrations.CreateModel(
            name='dispatching_unit',
            fields=[
                ('dispatching_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='dispatching_id', serialize=False, to='restaurant.employee', unique=True)),
                ('dispatching_name', models.CharField(max_length=10)),
                ('dispatching_evaluate', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '配送部门',
                'verbose_name_plural': '配送部门',
            },
        ),
        migrations.CreateModel(
            name='finance_unit',
            fields=[
                ('finance_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='finance_id', serialize=False, to='restaurant.employee', unique=True)),
                ('finance_name', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': '财务部门',
                'verbose_name_plural': '财务部门',
            },
        ),
        migrations.CreateModel(
            name='kitchen',
            fields=[
                ('cook_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='cook_id', serialize=False, to='restaurant.employee', unique=True)),
                ('cook_name', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': '厨房',
                'verbose_name_plural': '厨房',
            },
        ),
        migrations.CreateModel(
            name='purchase_unit',
            fields=[
                ('purchase_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='purchase_id', serialize=False, to='restaurant.employee', unique=True)),
                ('purchase_name', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': '采购部门',
                'verbose_name_plural': '采购部门',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='table_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.table'),
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.user'),
        ),
        migrations.AddField(
            model_name='check',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food', to='restaurant.menu', verbose_name='菜品'),
        ),
        migrations.AddField(
            model_name='check',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material', to='restaurant.material', verbose_name='食材'),
        ),
        migrations.AddField(
            model_name='cash_unit',
            name='cash_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.employee', unique=True, verbose_name='员工编号'),
        ),
        migrations.AddField(
            model_name='bill',
            name='cashier_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.employee'),
        ),
        migrations.AddField(
            model_name='bill',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.order'),
        ),
        migrations.AddField(
            model_name='bill',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.user'),
        ),
        migrations.AddField(
            model_name='order',
            name='cook_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.kitchen'),
        ),
        migrations.AddField(
            model_name='bill',
            name='dispatching_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.dispatching_unit'),
        ),
        migrations.AddField(
            model_name='bill',
            name='finance_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.finance_unit'),
        ),
    ]