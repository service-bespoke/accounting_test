# Generated by Django 4.2.7 on 2023-11-14 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0005_alter_bankbook_js_no1_alter_bankbook_js_no2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subledger',
            name='ob_date',
            field=models.DateTimeField(),
        ),
    ]