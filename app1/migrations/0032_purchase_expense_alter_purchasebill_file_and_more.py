# Generated by Django 4.0.4 on 2022-10-04 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0031_remove_invoice_taxamount'),
    ]

    operations = [
        migrations.CreateModel(
            name='purchase_expense',
            fields=[
                ('expenseid', models.AutoField(primary_key=True, serialize=False, verbose_name='eid')),
                ('expense_no', models.IntegerField(default=1000)),
                ('date', models.DateField()),
                ('expenseaccount', models.CharField(max_length=100, null=True)),
                ('expensetype', models.CharField(max_length=100, null=True)),
                ('hsn_sac', models.CharField(max_length=100, null=True)),
                ('amount', models.IntegerField(null=True)),
                ('paidthrough', models.CharField(max_length=100, null=True)),
                ('vendor', models.CharField(max_length=100, null=True)),
                ('gsttype', models.CharField(max_length=100, null=True)),
                ('sourceofsupply', models.CharField(max_length=100, null=True)),
                ('destinofsupply', models.CharField(max_length=100, null=True)),
                ('customer', models.CharField(max_length=100, null=True)),
                ('tax', models.CharField(max_length=100, null=True)),
                ('reference', models.CharField(max_length=100, null=True)),
                ('note', models.CharField(max_length=255, null=True)),
                ('file', models.FileField(default=None, upload_to='purchase/expense')),
            ],
        ),
        migrations.AlterField(
            model_name='purchasebill',
            name='file',
            field=models.FileField(default=None, upload_to='purchase/bill'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='file',
            field=models.FileField(default=None, upload_to='purchase/purchaseorder'),
        ),
    ]
