# Generated by Django 4.2.6 on 2023-10-27 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0002_customer_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_address1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_address2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_address3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_ob_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_ob_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_phone1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_phone2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_trn',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
