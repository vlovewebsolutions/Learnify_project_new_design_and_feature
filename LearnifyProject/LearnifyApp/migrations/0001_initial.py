# Generated by Django 3.1.7 on 2021-05-30 04:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_registered_in_session', models.CharField(max_length=7, verbose_name='Select session for which student going to be registered')),
                ('current_year_of_student', models.CharField(max_length=1, verbose_name='Current year of student')),
                ('current_session_of_students', models.CharField(max_length=7, verbose_name='Current session of student')),
                ('registration_number', models.CharField(max_length=256, unique=True, verbose_name='Reg. No.')),
                ('registration_date', models.DateField(verbose_name='Date')),
                ('student_name', models.CharField(max_length=256, verbose_name='Student Name')),
                ('student_image', models.ImageField(blank=True, null=True, upload_to='StudentPics/', verbose_name='Student Picture')),
                ('student_date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('student_gender', models.CharField(max_length=7, verbose_name='Gender')),
                ('student_present_class', models.CharField(max_length=17)),
                ('course_type_of_student', models.CharField(max_length=20, verbose_name='Course Type')),
                ('student_present_school_name', models.CharField(blank=True, max_length=1000, verbose_name='Present School Name')),
                ('student_school_board_affiliation', models.CharField(blank=True, max_length=10, verbose_name='School is affiliated to')),
                ('fathers_name', models.CharField(max_length=256, verbose_name="Father's Name")),
                ('fathers_qualification', models.CharField(blank=True, max_length=256, verbose_name="Father's Qualification")),
                ('occupation_of_father', models.CharField(blank=True, max_length=256, verbose_name="Father's Occupation")),
                ('mothers_name', models.CharField(blank=True, max_length=1000, verbose_name="Mother's Name")),
                ('present_address_of_student', models.CharField(max_length=10000, verbose_name='Present Address')),
                ('correspondence_address_of_student', models.CharField(max_length=10000, verbose_name='Correspondence Address')),
                ('email_of_student', models.EmailField(blank=True, max_length=254, verbose_name="Student's Email")),
                ('mobile_number_of_student', models.CharField(blank=True, max_length=10, verbose_name="Student's Phone Number")),
                ('mobile_number_of_father', models.CharField(blank=True, max_length=10, verbose_name="Father's Phone")),
                ('discount_on_session_fee', models.CharField(blank=True, default=0, max_length=256, null=True, verbose_name='Discount')),
                ('remarks_of_discount', models.TextField(blank=True, max_length=20000, null=True, verbose_name='Please enter remark, if you are applying some discount on fee of this student')),
                ('fee_paid_by_student', models.PositiveIntegerField(blank=True, default='0', verbose_name='Fee Paid')),
                ('due_fee_of_student', models.PositiveIntegerField(blank=True, default='0', verbose_name='Fee Due')),
                ('fee_status_student', models.CharField(blank=True, default='Pending', max_length=100000, verbose_name='Fee Status')),
                ('student_status', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='FeeReceipts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReceiptNumber', models.CharField(max_length=100000, verbose_name='Receipt Number')),
                ('RegNO', models.CharField(max_length=100, verbose_name='Registration Number')),
                ('Date', models.DateField()),
                ('DateTimeForReminder', models.DateField(blank=True, null=True)),
                ('RegDATE', models.CharField(max_length=26, verbose_name='Registration Date')),
                ('StudentNAME', models.CharField(max_length=1000)),
                ('StudentsFathersName', models.CharField(max_length=2000, verbose_name='Father Name')),
                ('StudentsFathersMobile', models.CharField(blank=True, max_length=13, verbose_name="Father's Mobile Number")),
                ('Course', models.CharField(max_length=20, verbose_name='Course Type')),
                ('AmountReceived', models.CharField(max_length=20000, verbose_name='Amount Receiving')),
                ('FeesForSession', models.CharField(max_length=8, verbose_name='Session')),
                ('ChequeNumber', models.CharField(blank=True, max_length=30, verbose_name='Cheque Number')),
                ('BankName', models.CharField(blank=True, max_length=10000, verbose_name='Bank Name')),
            ],
        ),
        migrations.CreateModel(
            name='FeesStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('YearSession', models.CharField(max_length=7, validators=[django.core.validators.RegexValidator(regex='\\d{4}-\\d{2}')], verbose_name='Session should be like 2020-21')),
                ('FirstSessionFee', models.CharField(max_length=100000, verbose_name='First Session Fee')),
                ('SecondSessionFee', models.CharField(max_length=100000, verbose_name='Second Session Fee')),
                ('ThirdSessionFee', models.CharField(max_length=100000, verbose_name='Second Session Fee')),
                ('FourthSessionFee', models.CharField(max_length=100000, verbose_name='Second Session Fee')),
            ],
        ),
        migrations.CreateModel(
            name='ResultClassIX',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StuSession', models.CharField(max_length=7, verbose_name='Session')),
                ('StuRegNo', models.CharField(max_length=256, unique=True, verbose_name='Reg. No.')),
                ('StuRegDate', models.CharField(max_length=40, verbose_name='Date')),
                ('StuName', models.CharField(max_length=40)),
                ('StuMobile', models.CharField(max_length=10)),
                ('CourseType', models.CharField(max_length=20, verbose_name='Course Type')),
                ('Physics_MARKS', models.CharField(max_length=6)),
                ('Chemistry_MARKS', models.CharField(max_length=6)),
                ('Maths_MARKS', models.CharField(max_length=6)),
                ('BIO_MARKS', models.CharField(max_length=6)),
                ('MAT_MARKS', models.CharField(max_length=6)),
                ('SST_MARKS', models.CharField(max_length=6)),
                ('TOTAL_MARKS', models.CharField(max_length=6)),
                ('Overall_RANK', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='ResultClassX',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StuSession', models.CharField(max_length=7, verbose_name='Session')),
                ('StuRegNo', models.CharField(max_length=256, unique=True, verbose_name='Reg. No.')),
                ('StuRegDate', models.CharField(max_length=40, verbose_name='Date')),
                ('StuName', models.CharField(max_length=40)),
                ('StuMobile', models.CharField(max_length=10)),
                ('CourseType', models.CharField(max_length=20, verbose_name='Course Type')),
                ('Physics_MARKS', models.CharField(max_length=6)),
                ('Chemistry_MARKS', models.CharField(max_length=6)),
                ('Maths_MARKS', models.CharField(max_length=6)),
                ('BIO_MARKS', models.CharField(max_length=6)),
                ('MAT_MARKS', models.CharField(max_length=6)),
                ('SST_MARKS', models.CharField(max_length=6)),
                ('TOTAL_MARKS', models.CharField(max_length=6)),
                ('Overall_RANK', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='ResultClassXI_JEE_ADVANCE_P1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StuSession', models.CharField(max_length=7, verbose_name='Session')),
                ('StuRegNo', models.CharField(max_length=256, unique=True, verbose_name='Reg. No.')),
                ('StuRegDate', models.CharField(max_length=40, verbose_name='Date')),
                ('StuName', models.CharField(max_length=40)),
                ('StuMobile', models.CharField(max_length=10)),
                ('CourseType', models.CharField(max_length=20, verbose_name='Course Type')),
                ('Physics_MARKS', models.CharField(max_length=6)),
                ('Physics_RANK', models.CharField(max_length=6)),
                ('Chemistry_MARKS', models.CharField(max_length=6)),
                ('Chemistry_RANK', models.CharField(max_length=6)),
                ('Maths_MARKS', models.CharField(max_length=6)),
                ('Maths_RANK', models.CharField(max_length=6)),
                ('TOTAL_MARKS', models.CharField(max_length=6)),
                ('Overall_RANK', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='ResultClassXI_JEE_ADVANCE_P2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StuSession', models.CharField(max_length=7, verbose_name='Session')),
                ('StuRegNo', models.CharField(max_length=256, unique=True, verbose_name='Reg. No.')),
                ('StuRegDate', models.CharField(max_length=40, verbose_name='Date')),
                ('StuName', models.CharField(max_length=40)),
                ('StuMobile', models.CharField(max_length=10)),
                ('CourseType', models.CharField(max_length=20, verbose_name='Course Type')),
                ('Physics_MARKS', models.CharField(max_length=6)),
                ('Physics_RANK', models.CharField(max_length=6)),
                ('Chemistry_MARKS', models.CharField(max_length=6)),
                ('Chemistry_RANK', models.CharField(max_length=6)),
                ('Maths_MARKS', models.CharField(max_length=6)),
                ('Maths_RANK', models.CharField(max_length=6)),
                ('TOTAL_MARKS', models.CharField(max_length=6)),
                ('Overall_RANK', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='ResultClassXI_JEE_MAIN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StuSession', models.CharField(max_length=7, verbose_name='Session')),
                ('StuRegNo', models.CharField(max_length=256, unique=True, verbose_name='Reg. No.')),
                ('StuRegDate', models.CharField(max_length=40, verbose_name='Date')),
                ('StuName', models.CharField(max_length=40)),
                ('StuMobile', models.CharField(max_length=10)),
                ('CourseType', models.CharField(max_length=20, verbose_name='Course Type')),
                ('Physics_MARKS', models.CharField(max_length=6)),
                ('Physics_RANK', models.CharField(max_length=6)),
                ('Chemistry_MARKS', models.CharField(max_length=6)),
                ('Chemistry_RANK', models.CharField(max_length=6)),
                ('Maths_MARKS', models.CharField(max_length=6)),
                ('Maths_RANK', models.CharField(max_length=6)),
                ('TOTAL_MARKS', models.CharField(max_length=6)),
                ('Overall_RANK', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='ResultClassXII_JEE_ADVANCE_P1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StuSession', models.CharField(max_length=7, verbose_name='Session')),
                ('StuRegNo', models.CharField(max_length=256, unique=True, verbose_name='Reg. No.')),
                ('StuRegDate', models.CharField(max_length=40, verbose_name='Date')),
                ('StuName', models.CharField(max_length=40)),
                ('StuMobile', models.CharField(max_length=10)),
                ('CourseType', models.CharField(max_length=20, verbose_name='Course Type')),
                ('Physics_MARKS', models.CharField(max_length=6)),
                ('Physics_RANK', models.CharField(max_length=6)),
                ('Chemistry_MARKS', models.CharField(max_length=6)),
                ('Chemistry_RANK', models.CharField(max_length=6)),
                ('Maths_MARKS', models.CharField(max_length=6)),
                ('Maths_RANK', models.CharField(max_length=6)),
                ('TOTAL_MARKS', models.CharField(max_length=6)),
                ('Overall_RANK', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='ResultClassXII_JEE_ADVANCE_P2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StuSession', models.CharField(max_length=7, verbose_name='Session')),
                ('StuRegNo', models.CharField(max_length=256, unique=True, verbose_name='Reg. No.')),
                ('StuRegDate', models.CharField(max_length=40, verbose_name='Date')),
                ('StuName', models.CharField(max_length=40)),
                ('StuMobile', models.CharField(max_length=10)),
                ('CourseType', models.CharField(max_length=20, verbose_name='Course Type')),
                ('Physics_MARKS', models.CharField(max_length=6)),
                ('Physics_RANK', models.CharField(max_length=6)),
                ('Chemistry_MARKS', models.CharField(max_length=6)),
                ('Chemistry_RANK', models.CharField(max_length=6)),
                ('Maths_MARKS', models.CharField(max_length=6)),
                ('Maths_RANK', models.CharField(max_length=6)),
                ('TOTAL_MARKS', models.CharField(max_length=6)),
                ('Overall_RANK', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='ResultClassXII_JEE_MAIN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StuSession', models.CharField(max_length=7, verbose_name='Session')),
                ('StuRegNo', models.CharField(max_length=256, unique=True, verbose_name='Reg. No.')),
                ('StuRegDate', models.CharField(max_length=40, verbose_name='Date')),
                ('StuName', models.CharField(max_length=40)),
                ('StuMobile', models.CharField(max_length=10)),
                ('CourseType', models.CharField(max_length=20, verbose_name='Course Type')),
                ('Physics_MARKS', models.CharField(max_length=6)),
                ('Physics_RANK', models.CharField(max_length=6)),
                ('Chemistry_MARKS', models.CharField(max_length=6)),
                ('Chemistry_RANK', models.CharField(max_length=6)),
                ('Maths_MARKS', models.CharField(max_length=6)),
                ('Maths_RANK', models.CharField(max_length=6)),
                ('TOTAL_MARKS', models.CharField(max_length=6)),
                ('Overall_RANK', models.CharField(max_length=6)),
            ],
        ),
    ]
