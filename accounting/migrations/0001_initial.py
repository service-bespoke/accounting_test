# Generated by Django 4.2.6 on 2023-10-09 10:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0001_initial'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupLedger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gl_no', models.IntegerField(unique=True)),
                ('gl_description', models.CharField(max_length=200)),
                ('if_balance_sheet', models.BooleanField(default=False)),
                ('if_profit_loss', models.BooleanField(default=False)),
                ('if_trade_ac_flag', models.BooleanField(default=False)),
                ('if_not_balance_sheet', models.BooleanField(default=False)),
                ('if_current_finyear', models.BooleanField(default=False)),
                ('if_individual', models.BooleanField(default=False)),
                ('if_consolidate_in_tb', models.BooleanField(default=False)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubLedger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl_no', models.IntegerField(unique=True)),
                ('sl_description', models.CharField(max_length=200)),
                ('remark', models.CharField(max_length=200)),
                ('ob_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ob_date', models.DateTimeField(auto_now_add=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('group_ledger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.groupledger')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Daybook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('js_number', models.IntegerField(unique=True)),
                ('js_date', models.DateTimeField(auto_now_add=True)),
                ('js_description', models.CharField(max_length=200)),
                ('manual_voucher_no', models.CharField(max_length=200)),
                ('if_manual_entry', models.BooleanField(default=False)),
                ('js_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('if_multiple_journal', models.BooleanField(default=False)),
                ('ref_number', models.IntegerField(blank=True, null=True)),
                ('multiple_journal_no', models.IntegerField(blank=True, null=True)),
                ('bank_book_no', models.IntegerField(blank=True, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('credit_sl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credit', to='accounting.subledger')),
                ('debit_sl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debit', to='accounting.subledger')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BankBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_book_code', models.IntegerField(unique=True)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('if_cash', models.BooleanField(default=False)),
                ('cheque_no', models.CharField(blank=True, max_length=200, null=True)),
                ('cheque_date', models.DateField(default=datetime.date.today)),
                ('transaction_type', models.CharField(choices=[('RECEIPT', 'RECEIPT'), ('PAYMENT', 'PAYMENT')], default='RECEIPT', max_length=20)),
                ('cheque_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('PASSED', 'PASSED'), ('BOUNCED', 'BOUNCED'), ('CANCELLED', 'CANCELLED')], default='PENDING', max_length=20)),
                ('status_date', models.DateField(default=datetime.date.today)),
                ('if_rtgs', models.BooleanField(default=False)),
                ('cheque_name', models.CharField(max_length=200)),
                ('bank_charge', models.DecimalField(decimal_places=2, max_digits=15)),
                ('bounce_charge', models.DecimalField(decimal_places=2, max_digits=15)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('bank_sl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banksl', to='accounting.subledger')),
                ('bankbook_sl_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bankbook', to='accounting.subledger')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('js_no1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='js1', to='accounting.daybook')),
                ('js_no2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='js2', to='accounting.daybook')),
                ('js_no3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='js3', to='accounting.daybook')),
                ('js_no4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='js4', to='accounting.daybook')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]