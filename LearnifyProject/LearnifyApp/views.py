import csv, io
from datetime import datetime
from LearnifyApp.promote_students import promote_students_func
from . import update_due_fee

import pdb
from .update_due_fee import update_due_fee_initially
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View

import LearnifyApp
from .models import AddStudent, ResultClassIX, ResultClassX, ResultClassXII_JEE_ADVANCE_P1, \
    ResultClassXI_JEE_ADVANCE_P2, ResultClassXI_JEE_ADVANCE_P1, ResultClassXII_JEE_MAIN, \
    ResultClassXI_JEE_MAIN, ResultClassXII_JEE_ADVANCE_P2, FeesStructure, FeeReceipt
from .forms import AddStudent_form, CollectFeeForm

# Create your views here.
from .utils import render_to_pdf


def filter_objects_on_session_basis(request):
    if request.method == 'GET':
        print("yes i am here in get block!")
        SESSION = request.GET.get('Session', None)
        ResultName = request.GET.get('Result_Name', None)
        print("yes i am here in filter objects function!")
        MODEL_NAME = getattr(LearnifyApp.models, ResultName)
        # RESULT_DATA = MODEL_NAME.objects.filter(current_session_of_students=SESSION)
        RESULT_DATA = MODEL_NAME.objects.values().filter(current_session_of_students=SESSION)
        # serialized_qs = serializers.serialize('json', RESULT_DATA)
        # data = {"queryset": serialized_qs}
        student_data = list(RESULT_DATA)
        return JsonResponse({'student_data': student_data})


def filter_objects_on_result_name_basis(request):
    if request.method == 'GET':
        print("yes i am here in get block of FILTER ON RESULT BASIS!")
        SESSION = request.GET.get('Session', None)
        ResultName = request.GET.get('Result_Name', None)
        print("yes i am here in filter objects on Basis of result!")
        print("-----------------------------------------------------")
        print(ResultName)
        print("-----------------------------------------------------")
        print(SESSION)
        print("-----------------------------------------------------")
        MODEL_NAME = getattr(LearnifyApp.models, str(ResultName))
        # RESULT_DATA = MODEL_NAME.objects.filter(current_session_of_students=SESSION)
        try:
            RESULT_DATA = MODEL_NAME.objects.values().filter(StuSession=SESSION)
            student_data = list(RESULT_DATA)
            return JsonResponse({'student_data': student_data})
        except Exception as Error:
            return JsonResponse({'error': Error})


@csrf_exempt
@login_required(login_url='/login/')
def index(request):
    requested_session = request.session['SessionRequested']
    if request.method == 'POST':
        requested_session = request.POST.get('Session')
        request.session['SessionRequested'] = requested_session
        print('Yes i got the session changed value:- ' + requested_session)
        sessions = FeesStructure.objects.all()
        students = AddStudent.objects.filter(current_session_of_students=requested_session)
        return render(request, 'index.html', context={'requested_session': requested_session, 'session': sessions,
                                                      'students': students, 'AckAddStudent': 'FromIndexChangedSession'})
    else:
        sessions = FeesStructure.objects.all()
        students = AddStudent.objects.filter(current_session_of_students=requested_session)
        return render(request, 'index.html', context={'requested_session': requested_session, 'session': sessions,
                                                      'students': students, 'AckAddStudent': 'FromIndex'})


def login_func(request):
    sessions_with_fees = FeesStructure.objects.all()
    if request.method == "POST":
        try:
            print('yes i am here try block! of Log In Page')
            username = request.POST.get('username')
            password = request.POST.get('password')
            session_selected = request.POST.get('Session')
            request.session['SessionRequested'] = session_selected
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                # return render(request, 'index.html')
                return redirect(index)
            else:
                messages.error(request, "Invalid Credentials!!!!")
                return render(request, 'login.html', context={'sessions_with_fees': sessions_with_fees})
        except Exception as error:
            messages.error(request, "'I got this exception error:- '" + str(error))
            print('I got this exception error:- ' + str(error))
            return redirect(login_func)
    else:
        return render(request, 'login.html', context={'sessions_with_fees': sessions_with_fees})


@login_required(login_url='/login/')
def LogOut(request):
    auth.logout(request)
    return redirect(login_func)


def check_reg_no_availability(request):
    reg_no = request.GET.get('Reg_No')
    STUDENTS_CHECK_REG_NO = AddStudent.objects.filter(registration_number=reg_no)
    all_reg_no = []
    for REG_NO in STUDENTS_CHECK_REG_NO:
        all_reg_no.append(REG_NO.registration_number)
    if reg_no in all_reg_no:
        STATUS = True
        RegCheck = {
            'is_taken': STATUS
        }
    else:
        status = False
        RegCheck = {
            'is_taken': status
        }
    return JsonResponse(RegCheck)


@login_required(login_url='/login/')
def add_student(request):
    requested_session = request.session['SessionRequested']
    Sessions = FeesStructure.objects.all()
    students = AddStudent.objects.filter(current_session_of_students=requested_session)
    if request.method == 'POST' or request.FILES:
        form = AddStudent_form(request.POST, request.FILES)
        if form.is_valid():
            update_form = form.save(commit=False)
            update_form.due_fee_of_student = update_due_fee.update_due_fee_initially(update_form.course_type_of_student,
                                                                                     update_form.discount_on_session_fee,
                                                                                     update_form.student_registered_in_session)
            update_form.save()
            messages.success(request, "You have registered student successfully!")
        else:
            messages.error(request, "May be you are using duplicate registration number!")
        requested_session = request.POST.get('current_session_of_students')
        request.session['SessionRequested'] = requested_session
        students = AddStudent.objects.filter(current_session_of_students=requested_session)

    data = {'AckAddStudent': 'AddStudent', 'students': students, 'session': Sessions,
            'requested_session': requested_session}
    return render(request, 'index.html', data)


@login_required(login_url='/login/')
def edit_detail(request, id):
    students = AddStudent.objects.all()
    Sessions = FeesStructure.objects.all()
    student = AddStudent.objects.get(id=id)
    form = AddStudent_form()
    context = {
        'student': student,
        'form': form,
        'students': students,
        'session': Sessions,
        'requested_session': student.current_session_of_students,
        'AckAddStudent': 'FromEditFunction'
    }
    return render(request, 'index.html', context)


@login_required(login_url='/login/')
def UpdateDetail(request, id):
    Sessions = FeesStructure.objects.all()
    students = AddStudent.objects.all()
    StudentForm = AddStudent.objects.get(id=id)
    form = AddStudent_form(request.POST or None or request.FILES or None, instance=StudentForm)
    if request.method == 'POST':
        RequestedSession = request.POST.get('current_session_of_students')
        if form.is_valid():
            NewForm = form.save(commit=False)
            NewForm.discount_on_session_fee = str(int(StudentForm.discount_on_session_fee) + int(NewForm.discount_on_session_fee))
            NewForm.due_fee_of_student = str(int(NewForm.due_fee_of_student) - int(NewForm.discount_on_session_fee))
            update_student_fee(NewForm.discount_on_session_fee, id)
            if 'student_image' in request.FILES:
                NewForm.student_image = request.FILES['student_image']
            NewForm.save()
            context = {'AckAddStudent': 'UpdateDetailFunc', 'students': students, 'session': Sessions,
                       'requested_session': RequestedSession}
            messages.success(request, 'Student details have been updated successfully')
            return redirect(add_student)
        else:
            error = form.errors.as_data()
            print(error)
            context = {
                'form': StudentForm,
                'AckAddStudent': 'UpdateDetailFunc',
                'students': students,
                'session': Sessions,
                'requested_session': RequestedSession,
            }
            messages.error(request, 'Invalid data. Something went wrong!')
            return render(add_student)
    else:
        context = {'AckAddStudent': 'UpdateDetailFunc', 'students': students, 'session': Sessions}
        return render(request, 'index.html', context)


@login_required(login_url='/login/')
def DeleteDetail(request, id):
    Sessions = FeesStructure.objects.all()
    RequestedSession = request.session['SessionRequested']
    students = AddStudent.objects.filter(current_session_of_students=RequestedSession)
    student = AddStudent.objects.get(id=id)
    try:
        student.delete()
        context = {
            'AckAddStudent': 'DeleteStudentFunc',
            'students': students,
            'session': Sessions,
            'requested_session': RequestedSession,
        }
        messages.success(request, 'You have removed student detail successfully!')
        return render(request, 'index.html', context)
    except Exception as error:
        context = {
            'AckAddStudent': 'DeleteStudentFunc',
            'students': students,
            'session': Sessions,
            'requested_session': RequestedSession,
        }
        messages.error(request, error)
        return render(request, 'index.html', context)


@login_required(login_url='/login/')
def accounts(request):
    gst = 0.18
    if request.method == 'POST' and request.POST.get('Session') is not None:
        RequestedSession = request.POST.get('Session')
        request.session['SessionRequested'] = RequestedSession
        print('Yes i got the session changed value at accounts function:- ' + str(RequestedSession))
        Sessions = FeesStructure.objects.all()
        # session_id = FeesStructure.objects.only('id').get(year_session=RequestedSession).id
        students = AddStudent.objects.filter(current_session_of_students=RequestedSession)
        fees = FeesStructure.objects.filter(year_session=RequestedSession)
        fee_receipts = FeeReceipt.objects.filter(fee_against_which_session=RequestedSession)
        print(fees)
        if not fees:
            first_session_fee = 0
            second_session_fee = 0
            third_session_fee = 0
            fourth_session_fee = 0
            context = {'session': Sessions,
                       'requested_session': RequestedSession,
                       'students': students,
                       'SessionFeeOfFirst': first_session_fee,
                       'SessionFeeOfSecond': second_session_fee,
                       'SessionFeeOfThird': third_session_fee,
                       'SessionFeeOfFourth': fourth_session_fee,
                       'Receipts': fee_receipts,
                       'gst': gst,
                       }
            return render(request, 'accounts.html', context)
        else:
            for fee in fees:
                first_session_fee = fee.first_session_fee
                second_session_fee = fee.second_session_fee
                third_session_fee = fee.third_session_fee
                fourth_session_fee = fee.fourth_session_fee
            context = {'session': Sessions,
                       'requested_session': RequestedSession,
                       'students': students,
                       'SessionFeeOfFirst': first_session_fee,
                       'SessionFeeOfSecond': second_session_fee,
                       'SessionFeeOfThird': third_session_fee,
                       'SessionFeeOfFourth': fourth_session_fee,
                       'Receipts': fee_receipts,
                       'gst': gst,
                       }
            return render(request, 'accounts.html', context)
    else:
        RequestedSession = request.session['SessionRequested']
        Sessions = FeesStructure.objects.all()
        # session_id = FeesStructure.objects.only('id').get(year_session=RequestedSession).id
        students = AddStudent.objects.filter(current_session_of_students=RequestedSession)
        fees = FeesStructure.objects.filter(year_session=RequestedSession)
        fee_receipts = FeeReceipt.objects.filter(fee_against_which_session=RequestedSession)
        if not fees:
            first_session_fee = 0
            second_session_fee = 0
            third_session_fee = 0
            fourth_session_fee = 0
            context = {'session': Sessions,
                       'requested_session': RequestedSession,
                       'students': students,
                       'SessionFeeOfFirst': first_session_fee,
                       'SessionFeeOfSecond': second_session_fee,
                       'SessionFeeOfThird': third_session_fee,
                       'SessionFeeOfFourth': fourth_session_fee,
                       'Receipts': fee_receipts,
                       'gst': gst,
                       }
            return render(request, 'accounts.html', context)
        else:
            for fee in fees:
                first_session_fee = fee.first_session_fee
                second_session_fee = fee.second_session_fee
                third_session_fee = fee.third_session_fee
                fourth_session_fee = fee.fourth_session_fee
            context = {'session': Sessions,
                       'requested_session': RequestedSession,
                       'students': students,
                       'SessionFeeOfFirst': first_session_fee,
                       'SessionFeeOfSecond': second_session_fee,
                       'SessionFeeOfThird': third_session_fee,
                       'SessionFeeOfFourth': fourth_session_fee,
                       'Receipts': fee_receipts,
                       'gst': gst,
                       }
            return render(request, 'accounts.html', context)


def UploadResultJee(request, EXAM, CSV):
    try:
        data_set = CSV.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        # The below step is very important where i am converting the EXAM string value into model name
        model_name = getattr(LearnifyApp.models, EXAM)
        # --------------------------------------------------------------------------------------------
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            _, created = model_name.objects.update_or_create(StuSession=column[0], StuRegNo=column[1],
                                                             StuRegDate=column[2], StuName=column[3],
                                                             StuMobile=column[4], CourseType=column[5],
                                                             Physics_MARKS=column[6], Chemistry_MARKS=column[7],
                                                             Maths_MARKS=column[8], BIO_MARKS=column[9],
                                                             MAT_MARKS=column[10], SST_MARKS=column[11],
                                                             TOTAL_MARKS=column[12], Overall_RANK=column[13])

        messages.success(request, 'You have uploaded the result successfully!')
        return redirect(result)
    except Exception as error:
        messages.error(request, 'Please check your file type or file data! -' + str(error))
        print(error)
        return redirect(result)


def UploadResult(request, EXAM, CSV):
    try:
        data_set = CSV.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        # The below step is very important where i am converting the EXAM string value into model name
        model_name = getattr(LearnifyApp.models, EXAM)
        # --------------------------------------------------------------------------------------------
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            _, created = model_name.objects.update_or_create(StuSession=column[0], StuRegNo=column[1],
                                                             StuRegDate=column[2], StuName=column[3],
                                                             StuMobile=column[4], CourseType=column[5],
                                                             Physics_MARKS=column[6], Physics_RANK=column[7],
                                                             Chemistry_MARKS=column[8], Chemistry_RANK=column[9],
                                                             Maths_MARKS=column[10], Maths_RANK=column[11],
                                                             TOTAL_MARKS=column[12], Overall_RANK=column[13])

        messages.success(request, 'You have uploaded the result successfully!')
        return redirect(result)
    except Exception as error:
        messages.error(request, 'Please check your file type or file data! -' + str(error))
        print(error)
        return redirect(result)


@login_required(login_url='/login/')
def result(request):
    RequestedSession = request.session['SessionRequested']
    Sessions = FeesStructure.objects.all()
    ResultObjects = ResultClassIX.objects.all()
    print(ResultObjects)
    if request.method == 'POST' and request.FILES:
        exam = request.POST.get('EXAM')
        print(exam)
        csv_file = request.FILES['CsvFile']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'This is not csv file!!!!')
            return redirect(result)
        if exam == 'ResultClassIX' or exam == 'ResultClassX':
            UploadResultJee(request, exam, csv_file)
        else:
            UploadResult(request, exam, csv_file)
    context = {'session': Sessions,
               'requested_session': RequestedSession, 'result': ResultObjects}
    return render(request, 'result.html', context)


@login_required(login_url='/login/')
def send_result(request):
    if request.method == 'POST':
        RESULT = request.POST.getlist('RESULT[]')
        print(RESULT)
        if RESULT:
            messages.success(request, 'You have sent result successfully!')
        else:
            messages.error(request, 'You have not selected any result yet!')
    return redirect(result)


def update_student_fee(amount_receiving, id):
    amount = amount_receiving
    student = AddStudent.objects.get(id=id)
    student.fee_paid_by_student = int(amount) + int(student.fee_paid_by_student)
    student.due_fee_of_student = int(student.due_fee_of_student) - int(amount)
    student.save()


@login_required(login_url='/login/')
def check_receipt_no_availability(request):
    FEE_RECEIPTS = FeeReceipt.objects.all()
    fee_receipts_numbers_list = []
    for receipts in FEE_RECEIPTS:
        fee_receipts_numbers_list.append(receipts.receipt_number)
    if request.method == "GET":
        receipt_no = request.GET.get("RECEIPT_NO")
        if receipt_no in fee_receipts_numbers_list:
            Status = True
            CheckReceiptNo = {
                'is_taken': Status
            }
        else:
            Status = False
            CheckReceiptNo = {
                'is_taken': Status
            }
        return JsonResponse(CheckReceiptNo)


@login_required(login_url='/login/')
def collect_student_fee(request, id):
    fees = FeesStructure.objects.all()
    fee_receipts = FeeReceipt.objects.all()
    if request.method == 'POST':
        form = CollectFeeForm(request.POST)
        if form.is_valid():
            NewForm = form.save(commit=False)
            update_student_fee(NewForm.amount_received, id)
            NewForm.save()
            messages.success(request, "You have received fee successfully")
            return redirect(accounts)
        else:
            messages.error(request, "Fee form is not valid! may be you are using duplicate receipt no.")
    for fee in fees:
        first_session_fee = fee.first_session_fee
        second_session_fee = fee.second_session_fee
        third_session_fee = fee.third_session_fee
        fourth_session_fee = fee.fourth_session_fee
    studentFeeDetail = AddStudent.objects.get(id=id)
    RequestedSession = request.session['SessionRequested']
    Sessions = FeesStructure.objects.all()
    context = {
        'StuFeeDetail': studentFeeDetail,
        'Receipts': fee_receipts,
        'requested_session': RequestedSession,
        'session': Sessions,
        'RequestFor': 'CollectFeePage',
        'SessionFeeOfFirst': first_session_fee,
        'SessionFeeOfSecond': second_session_fee,
        'SessionFeeOfThird': third_session_fee,
        'SessionFeeOfFourth': fourth_session_fee,
        'gst': 0.18,
    }
    return render(request, 'accounts.html', context)


# NUMBER TO WORDS IN PYTHON (INDIAN SYSTEM)
def Words(n):
    units = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
             "Nineteen"]
    tens = ["Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    if n <= 9:
        return units[n]
    elif n >= 10 and n <= 19:
        return teens[n - 10]
    elif n >= 20 and n <= 99:
        return tens[(n // 10) - 2] + " " + (units[n % 10] if n % 10 != 0 else "")
    elif n >= 100 and n <= 999:
        return Words(n // 100) + " Hundred " + (Words(n % 100) if n % 100 != 0 else "")
    elif n >= 1000 and n <= 99999:
        return Words(n // 1000) + " Thousand " + (Words(n % 1000) if n % 1000 != 0 else "")
    elif n >= 100000 and n <= 9999999:
        return Words(n // 100000) + " Lakh " + (Words(n % 100000) if n % 100000 != 0 else "")
    elif n >= 10000000:
        return Words(n // 10000000) + " Crore " + (Words(n % 10000000) if n % 10000000 != 0 else "")


class GeneratePdf(View):
    def get(self, request, id, *args, **kwargs):
        template = get_template('invoice.html')
        now = datetime.now()
        Object = FeeReceipt.objects.get(id=id)
        Obj2 = AddStudent.objects.get(registration_number=Object.reg_number)
        session_total_fee = int(Obj2.due_fee_of_student) + int(Obj2.fee_paid_by_student)
        context = {
            'Date': now,
            'student': Object,
            'Obj2': Obj2,
            'total_fee_of_session': session_total_fee,
            'AmtInWords': Words(int(Object.amount_received)),
            'FirstSessionFee': (Obj2.due_fee_of_student + Obj2.fee_paid_by_student) / 4,
            'TwoSessionsFee': (Obj2.due_fee_of_student + Obj2.fee_paid_by_student) / 3,
            'ThreeSessionsFee': (Obj2.due_fee_of_student + Obj2.fee_paid_by_student) / 2,
            'FourSessionsFee': (Obj2.due_fee_of_student + Obj2.fee_paid_by_student) / 1,

        }
        pdf = render_to_pdf('invoice.html', context)
        return HttpResponse(pdf, content_type='application/pdf')


class DownloadPdf(View):
    def get(self, request, id, *args, **kwargs):
        template = get_template('invoice.html')
        now = datetime.now()
        Object = FeeReceipt.objects.get(id=id)
        Obj2 = AddStudent.objects.get(registration_number=Object.reg_number)
        session_total_fee = int(Obj2.due_fee_of_student) + int(Obj2.fee_paid_by_student)
        context = {
            'Date': now,
            'student': Object,
            'Obj2': Obj2,
            'total_fee_of_session': session_total_fee,
            'AmtInWords': Words(int(Object.amount_received)),
            'FirstSessionFee': (Obj2.due_fee_of_student + Obj2.fee_paid_by_student) / 4,
            'TwoSessionsFee': (Obj2.due_fee_of_student + Obj2.fee_paid_by_student) / 3,
            'ThreeSessionsFee': (Obj2.due_fee_of_student + Obj2.fee_paid_by_student) / 2,
            'FourSessionsFee': (Obj2.due_fee_of_student + Obj2.fee_paid_by_student) / 1,

        }
        pdf = render_to_pdf('invoice.html', context)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" % Object.student_name
        content = 'attachment; filename="%s"' % filename
        response['Content-Disposition'] = content
        return response


@login_required(login_url='/login_func/')
def delete_pay_slip(request, id):
    PaySlip = FeeReceipt.objects.get(id=id)
    try:
        PaySlip.delete()
        messages.success(request, "You have successfully deleted the pay slip!")
        return redirect(accounts)
    except Exception as PAYSLIP_DELETE_ERR:
        messages.error(request, str(PAYSLIP_DELETE_ERR))
        return redirect(accounts)


@login_required(login_url='/login/')
def promote_students_for_next_session(request):
    if request.method == 'POST':
        id_of_students = request.POST.getlist('promote_students[]')
        if not id_of_students:
            messages.error(request, 'You have not selected any student to promote!')
            return redirect(add_student)
        else:
            status = promote_students_func(id_of_students)
            if status == 'success':
                messages.success(request, 'You have promoted the all students which you have selected!')
                return redirect(add_student)
            else:
                messages.error(request,
                               'May be you have not added new session for which you are trying to promote students!')
                return redirect(add_student)
    else:
        return redirect(index)

