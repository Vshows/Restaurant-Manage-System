# Generated by Django 2.1.1 on 2018-09-20 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0011_company_bill_company_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company_bill',
            name='company_balance',
        ),
    ]
