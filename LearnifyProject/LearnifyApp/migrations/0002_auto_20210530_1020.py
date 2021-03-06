# Generated by Django 3.1.7 on 2021-05-30 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LearnifyApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feereceipts',
            old_name='AmountReceived',
            new_name='amount_received',
        ),
        migrations.RenameField(
            model_name='feereceipts',
            old_name='BankName',
            new_name='bank_name',
        ),
        migrations.RenameField(
            model_name='feereceipts',
            old_name='ChequeNumber',
            new_name='cheque_number',
        ),
        migrations.RenameField(
            model_name='feereceipts',
            old_name='Course',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='feereceipts',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='feereceipts',
            old_name='DateTimeForReminder',
            new_name='date_for_reminder',
        ),
        migrations.RenameField(
            model_name='feereceipts',
            old_name='StudentsFathersMobile',
            new_name='fathers_mobile_number',
        ),
        migrations.RenameField(
            model_name='feereceipts',
            old_name='StudentsFathersName',
            new_name='fathers_name',
        ),
        migrations.RenameField(
            model_name='feereceipts',
            old_name='FeesForSession',
            new_name='fee_against_which_session',
        ),
        migrations.RenameField(
            model_name='feereceipts',
            old_name='ReceiptNumber',
            new_name='receipt_number',
        ),
        migrations.RenameField(
            model_name='feereceipts',
            old_name='RegDATE',
            new_name='reg_date',
        ),
        migrations.RenameField(
            model_name='feereceipts',
            old_name='RegNO',
            new_name='reg_number',
        ),
        migrations.RenameField(
            model_name='feereceipts',
            old_name='StudentNAME',
            new_name='student_name',
        ),
        migrations.RenameField(
            model_name='feesstructure',
            old_name='FirstSessionFee',
            new_name='first_session_fee',
        ),
        migrations.RenameField(
            model_name='feesstructure',
            old_name='FourthSessionFee',
            new_name='fourth_session_fee',
        ),
        migrations.RenameField(
            model_name='feesstructure',
            old_name='SecondSessionFee',
            new_name='second_session_fee',
        ),
        migrations.RenameField(
            model_name='feesstructure',
            old_name='ThirdSessionFee',
            new_name='third_session_fee',
        ),
        migrations.RenameField(
            model_name='feesstructure',
            old_name='YearSession',
            new_name='year_session',
        ),
    ]
