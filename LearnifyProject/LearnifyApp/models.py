from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User

from django.db import models


# Create your models here.
class AddStudent(models.Model):
    student_registered_in_session = models.CharField(max_length=7, verbose_name="Select session for which student going to be registered")
    current_year_of_student = models.CharField(max_length=1, verbose_name="Current year of student")
    current_session_of_students = models.CharField(max_length=7, verbose_name="Current session of student")
    registration_number = models.CharField(max_length=256, verbose_name='Reg. No.', unique=True)
    registration_date = models.DateField(auto_now=False, verbose_name='Date')
    student_name = models.CharField(max_length=256, verbose_name='Student Name')
    student_image = models.ImageField(upload_to='StudentPics/', blank=True, null=True, verbose_name='Student Picture')
    student_date_of_birth = models.DateField(auto_now=False, verbose_name='Date of Birth')
    student_gender = models.CharField(max_length=7, verbose_name='Gender')
    student_present_class = models.CharField(max_length=17)
    course_type_of_student = models.CharField(max_length=20, verbose_name='Course Type')
    student_present_school_name = models.CharField(max_length=1000, blank=True, verbose_name='Present School Name')
    student_school_board_affiliation = models.CharField(max_length=10, blank=True,
                                                        verbose_name='School is affiliated to')
    fathers_name = models.CharField(max_length=256, verbose_name="Father's Name")
    fathers_qualification = models.CharField(max_length=256, blank=True, verbose_name="Father's Qualification")
    occupation_of_father = models.CharField(max_length=256, blank=True, verbose_name="Father's Occupation")
    mothers_name = models.CharField(max_length=1000, blank=True, verbose_name="Mother's Name")
    present_address_of_student = models.CharField(max_length=10000, verbose_name="Present Address")
    correspondence_address_of_student = models.CharField(max_length=10000, verbose_name="Correspondence Address")
    email_of_student = models.EmailField(blank=True, verbose_name="Student's Email")
    mobile_number_of_student = models.CharField(max_length=10, blank=True, verbose_name="Student's Phone Number")
    mobile_number_of_father = models.CharField(max_length=10, blank=True, verbose_name="Father's Phone")
    discount_on_session_fee = models.CharField(max_length=256, blank=True, null=True, default=0,
                                               verbose_name="Discount")
    remarks_of_discount = models.TextField(max_length=20000, blank=True, null=True,
                                           verbose_name='Please enter remark, if you are applying some discount on fee of this '
                                                        'student')
    fee_paid_by_student = models.PositiveIntegerField(blank=True, default='0', verbose_name="Fee Paid")
    due_fee_of_student = models.PositiveIntegerField(blank=True, default='0', verbose_name="Fee Due")
    fee_status_student = models.CharField(max_length=100000, blank=True, default='Pending', verbose_name='Fee Status')
    student_status = models.CharField(max_length=8)


class ResultClassIX(models.Model):
    StuSession = models.CharField(max_length=7, verbose_name="Session")
    StuRegNo = models.CharField(max_length=256, verbose_name='Reg. No.', unique=True)
    StuRegDate = models.CharField(max_length=40, verbose_name='Date')
    StuName = models.CharField(max_length=40)
    StuMobile = models.CharField(max_length=10)
    CourseType = models.CharField(max_length=20, verbose_name='Course Type')
    Physics_MARKS = models.CharField(max_length=6)
    Chemistry_MARKS = models.CharField(max_length=6)
    Maths_MARKS = models.CharField(max_length=6)
    BIO_MARKS = models.CharField(max_length=6)
    MAT_MARKS = models.CharField(max_length=6)
    SST_MARKS = models.CharField(max_length=6)
    TOTAL_MARKS = models.CharField(max_length=6)
    Overall_RANK = models.CharField(max_length=6)


class ResultClassX(models.Model):
    StuSession = models.CharField(max_length=7, verbose_name="Session")
    StuRegNo = models.CharField(max_length=256, verbose_name='Reg. No.', unique=True)
    StuRegDate = models.CharField(max_length=40, verbose_name='Date')
    StuName = models.CharField(max_length=40)
    StuMobile = models.CharField(max_length=10)
    CourseType = models.CharField(max_length=20, verbose_name='Course Type')
    Physics_MARKS = models.CharField(max_length=6)
    Chemistry_MARKS = models.CharField(max_length=6)
    Maths_MARKS = models.CharField(max_length=6)
    BIO_MARKS = models.CharField(max_length=6)
    MAT_MARKS = models.CharField(max_length=6)
    SST_MARKS = models.CharField(max_length=6)
    TOTAL_MARKS = models.CharField(max_length=6)
    Overall_RANK = models.CharField(max_length=6)


class ResultClassXI_JEE_MAIN(models.Model):
    StuSession = models.CharField(max_length=7, verbose_name="Session")
    StuRegNo = models.CharField(max_length=256, verbose_name='Reg. No.', unique=True)
    StuRegDate = models.CharField(max_length=40, verbose_name='Date')
    StuName = models.CharField(max_length=40)
    StuMobile = models.CharField(max_length=10)
    CourseType = models.CharField(max_length=20, verbose_name='Course Type')
    Physics_MARKS = models.CharField(max_length=6)
    Physics_RANK = models.CharField(max_length=6)
    Chemistry_MARKS = models.CharField(max_length=6)
    Chemistry_RANK = models.CharField(max_length=6)
    Maths_MARKS = models.CharField(max_length=6)
    Maths_RANK = models.CharField(max_length=6)
    TOTAL_MARKS = models.CharField(max_length=6)
    Overall_RANK = models.CharField(max_length=6)


class ResultClassXII_JEE_MAIN(models.Model):
    StuSession = models.CharField(max_length=7, verbose_name="Session")
    StuRegNo = models.CharField(max_length=256, verbose_name='Reg. No.', unique=True)
    StuRegDate = models.CharField(max_length=40, verbose_name='Date')
    StuName = models.CharField(max_length=40)
    StuMobile = models.CharField(max_length=10)
    CourseType = models.CharField(max_length=20, verbose_name='Course Type')
    Physics_MARKS = models.CharField(max_length=6)
    Physics_RANK = models.CharField(max_length=6)
    Chemistry_MARKS = models.CharField(max_length=6)
    Chemistry_RANK = models.CharField(max_length=6)
    Maths_MARKS = models.CharField(max_length=6)
    Maths_RANK = models.CharField(max_length=6)
    TOTAL_MARKS = models.CharField(max_length=6)
    Overall_RANK = models.CharField(max_length=6)


class ResultClassXI_JEE_ADVANCE_P1(models.Model):
    StuSession = models.CharField(max_length=7, verbose_name="Session")
    StuRegNo = models.CharField(max_length=256, verbose_name='Reg. No.', unique=True)
    StuRegDate = models.CharField(max_length=40, verbose_name='Date')
    StuName = models.CharField(max_length=40)
    StuMobile = models.CharField(max_length=10)
    CourseType = models.CharField(max_length=20, verbose_name='Course Type')
    Physics_MARKS = models.CharField(max_length=6)
    Physics_RANK = models.CharField(max_length=6)
    Chemistry_MARKS = models.CharField(max_length=6)
    Chemistry_RANK = models.CharField(max_length=6)
    Maths_MARKS = models.CharField(max_length=6)
    Maths_RANK = models.CharField(max_length=6)
    TOTAL_MARKS = models.CharField(max_length=6)
    Overall_RANK = models.CharField(max_length=6)


class ResultClassXI_JEE_ADVANCE_P2(models.Model):
    StuSession = models.CharField(max_length=7, verbose_name="Session")
    StuRegNo = models.CharField(max_length=256, verbose_name='Reg. No.', unique=True)
    StuRegDate = models.CharField(max_length=40, verbose_name='Date')
    StuName = models.CharField(max_length=40)
    StuMobile = models.CharField(max_length=10)
    CourseType = models.CharField(max_length=20, verbose_name='Course Type')
    Physics_MARKS = models.CharField(max_length=6)
    Physics_RANK = models.CharField(max_length=6)
    Chemistry_MARKS = models.CharField(max_length=6)
    Chemistry_RANK = models.CharField(max_length=6)
    Maths_MARKS = models.CharField(max_length=6)
    Maths_RANK = models.CharField(max_length=6)
    TOTAL_MARKS = models.CharField(max_length=6)
    Overall_RANK = models.CharField(max_length=6)


class ResultClassXII_JEE_ADVANCE_P1(models.Model):
    StuSession = models.CharField(max_length=7, verbose_name="Session")
    StuRegNo = models.CharField(max_length=256, verbose_name='Reg. No.', unique=True)
    StuRegDate = models.CharField(max_length=40, verbose_name='Date')
    StuName = models.CharField(max_length=40)
    StuMobile = models.CharField(max_length=10)
    CourseType = models.CharField(max_length=20, verbose_name='Course Type')
    Physics_MARKS = models.CharField(max_length=6)
    Physics_RANK = models.CharField(max_length=6)
    Chemistry_MARKS = models.CharField(max_length=6)
    Chemistry_RANK = models.CharField(max_length=6)
    Maths_MARKS = models.CharField(max_length=6)
    Maths_RANK = models.CharField(max_length=6)
    TOTAL_MARKS = models.CharField(max_length=6)
    Overall_RANK = models.CharField(max_length=6)


class ResultClassXII_JEE_ADVANCE_P2(models.Model):
    StuSession = models.CharField(max_length=7, verbose_name="Session")
    StuRegNo = models.CharField(max_length=256, verbose_name='Reg. No.', unique=True)
    StuRegDate = models.CharField(max_length=40, verbose_name='Date')
    StuName = models.CharField(max_length=40)
    StuMobile = models.CharField(max_length=10)
    CourseType = models.CharField(max_length=20, verbose_name='Course Type')
    Physics_MARKS = models.CharField(max_length=6)
    Physics_RANK = models.CharField(max_length=6)
    Chemistry_MARKS = models.CharField(max_length=6)
    Chemistry_RANK = models.CharField(max_length=6)
    Maths_MARKS = models.CharField(max_length=6)
    Maths_RANK = models.CharField(max_length=6)
    TOTAL_MARKS = models.CharField(max_length=6)
    Overall_RANK = models.CharField(max_length=6)


class FeesStructure(models.Model):
    year_session = models.CharField(max_length=7, unique=True, validators=[RegexValidator(regex='\d{4}-\d{2}')],
                                   verbose_name="session (eg:-2019-20)")
    first_session_fee = models.CharField(max_length=100000, verbose_name="First Session Fee")
    second_session_fee = models.CharField(max_length=100000, verbose_name="Second Session Fee")
    third_session_fee = models.CharField(max_length=100000, verbose_name="Second Session Fee")
    fourth_session_fee = models.CharField(max_length=100000, verbose_name="Second Session Fee")

    def __str__(self):
        return self.year_session


class FeeReceipt(models.Model):
    receipt_number = models.CharField(max_length=100000, unique=True, verbose_name='Receipt Number')
    reg_number = models.CharField(max_length=100, verbose_name='Registration Number')
    date = models.DateField(auto_now=False)
    date_for_reminder = models.DateField(auto_now=False, blank=True, null=True)
    reg_date = models.CharField(max_length=26, verbose_name="Registration Date")
    student_name = models.CharField(max_length=1000)
    fathers_name = models.CharField(max_length=2000, verbose_name="Father Name")
    fathers_mobile_number = models.CharField(max_length=13, blank=True, verbose_name="Father's Mobile Number")
    course = models.CharField(max_length=20, verbose_name='Course Type')
    amount_received = models.CharField(max_length=20000, verbose_name="Amount Receiving")
    fee_against_which_session = models.CharField(max_length=8, verbose_name="Session")
    cheque_number = models.CharField(max_length=30, blank=True, verbose_name="Cheque Number")
    bank_name = models.CharField(max_length=10000, blank=True, verbose_name='Bank Name')
