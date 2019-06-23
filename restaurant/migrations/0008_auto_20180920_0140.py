# Generated by Django 2.1.1 on 2018-09-19 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_remove_company_bill_bill_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company_bill',
            name='id',
        ),
        migrations.AddField(
            model_name='company_bill',
            name='bill_id',
            field=models.CharField(default=10000, max_length=20, primary_key=True, serialize=False, verbose_name='流水号'),
        ),
    ]
