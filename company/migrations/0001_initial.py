# Generated by Django 4.2.6 on 2023-10-09 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('address', models.CharField(max_length=70)),
                ('phone', models.CharField(max_length=70)),
                ('trn_number', models.CharField(max_length=70)),
                ('letter_header', models.ImageField(blank=True, null=True, upload_to='')),
                ('letter_footer', models.ImageField(blank=True, null=True, upload_to='')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
