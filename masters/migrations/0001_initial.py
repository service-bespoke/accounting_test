# Generated by Django 4.2.6 on 2023-10-20 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_code', models.IntegerField(unique=True)),
                ('supplier_name', models.CharField(max_length=200)),
                ('supplier_address1', models.CharField(max_length=200)),
                ('supplier_address2', models.CharField(max_length=200)),
                ('supplier_address3', models.CharField(max_length=200)),
                ('supplier_phone1', models.CharField(max_length=200)),
                ('supplier_phone2', models.CharField(max_length=200)),
                ('supplier_trn', models.CharField(max_length=20)),
                ('supplier_slno', models.IntegerField(unique=True)),
                ('supplier_ob_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('supplier_ob_date', models.DateTimeField(auto_now_add=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_code', models.IntegerField(unique=True)),
                ('customer_name', models.CharField(max_length=200)),
                ('customer_address1', models.CharField(max_length=200)),
                ('customer_address2', models.CharField(max_length=200)),
                ('customer_address3', models.CharField(max_length=200)),
                ('customer_phone1', models.CharField(max_length=200)),
                ('customer_phone2', models.CharField(max_length=200)),
                ('customer_trn', models.CharField(max_length=20)),
                ('customer_slno', models.IntegerField(unique=True)),
                ('customer_ob_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('customer_ob_date', models.DateTimeField(auto_now_add=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_code', models.IntegerField(unique=True)),
                ('bank_name', models.CharField(max_length=200)),
                ('bank_branch', models.CharField(max_length=200)),
                ('bank_accountno', models.CharField(max_length=20)),
                ('bank_iban', models.CharField(max_length=30)),
                ('bank_slno', models.IntegerField(unique=True)),
                ('bank_ob_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('bank_ob_date', models.DateTimeField(auto_now_add=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
