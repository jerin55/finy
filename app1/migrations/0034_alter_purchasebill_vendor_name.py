# Generated by Django 4.0.5 on 2022-10-06 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0033_alter_purchase_expense_file_alter_purchasebill_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasebill',
            name='vendor_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
