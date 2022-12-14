# Generated by Django 4.0.6 on 2022-09-29 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_alter_estimate_cgst_alter_estimate_igst_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='salesorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salename', models.CharField(max_length=100)),
                ('saleemail', models.EmailField(max_length=254)),
                ('saleaddress', models.CharField(max_length=150)),
                ('saledate', models.CharField(max_length=10)),
                ('saleno', models.CharField(max_length=20)),
                ('placeofsupply', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=100)),
                ('hsn', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('qty', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
                ('tax', models.CharField(default='0', max_length=100)),
                ('product1', models.CharField(default='', max_length=100)),
                ('hsn1', models.CharField(default='', max_length=100)),
                ('description1', models.CharField(default='', max_length=100)),
                ('qty1', models.CharField(default='', max_length=100)),
                ('rate1', models.CharField(default='', max_length=100)),
                ('total1', models.CharField(default='', max_length=100)),
                ('tax1', models.CharField(default='0', max_length=100)),
                ('product2', models.CharField(default='', max_length=100)),
                ('hsn2', models.CharField(default='', max_length=100)),
                ('description2', models.CharField(default='', max_length=100)),
                ('qty2', models.CharField(default='', max_length=100)),
                ('rate2', models.CharField(default='', max_length=100)),
                ('total2', models.CharField(default='', max_length=100)),
                ('tax2', models.CharField(default='0', max_length=100)),
                ('product3', models.CharField(default='', max_length=100)),
                ('hsn3', models.CharField(default='', max_length=100)),
                ('description3', models.CharField(default='', max_length=100)),
                ('qty3', models.CharField(default='', max_length=100)),
                ('rate3', models.CharField(default='', max_length=100)),
                ('total3', models.CharField(default='', max_length=100)),
                ('tax3', models.CharField(default='0', max_length=100)),
                ('taxamount', models.CharField(default='', max_length=100)),
                ('reference_number', models.CharField(default='', max_length=100)),
                ('note', models.TextField()),
                ('subtotal', models.CharField(max_length=100)),
                ('IGST', models.CharField(max_length=100)),
                ('CGST', models.CharField(max_length=100)),
                ('SGST', models.CharField(max_length=100)),
                ('TCS', models.CharField(max_length=100)),
                ('estimatetotal', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='estimate')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
    ]
