# Generated by Django 4.2.6 on 2023-10-30 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0003_alter_employee_company'),
        ('company', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logincompany',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.company'),
        ),
        migrations.AlterField(
            model_name='logincompany',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.company'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userpermission',
            name='staff',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='employee.employee'),
        ),
        migrations.AlterField(
            model_name='userpermission',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
