"""LearnifyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_func, name='Login'),
    path('logout/', views.LogOut, name='Logout'),
    path('AddStudent/', views.add_student, name='AddStudent'),
    path('Accounts/', views.accounts, name='Accounts'),
    path('Result/', views.result, name='Result'),
    path('Send_Result/', views.send_result, name='Send_Result'),
    path('promote_students/', views.promote_students_for_next_session, name='promote_students'),
    path('GeneratePdf/<int:id>', views.GeneratePdf.as_view(), name='GeneratePdf'),
    path('DownloadPdf/<int:id>', views.DownloadPdf.as_view(), name='DownloadPdf'),
    path('DeletePaySlip/<int:id>', views.delete_pay_slip, name='DeletePaySlip'),
    path('check_reg_no_availability/', views.check_reg_no_availability, name='check_reg_no_availability'),
    path('check_receipt_no_availability/', views.check_receipt_no_availability, name='check_receipt_no_availability'),
    path('Filter_objects_on_session_basis/', views.filter_objects_on_session_basis,
         name='Filter_objects_on_session_basis'),
    path('Filter_objects_on_result_name_basis/', views.filter_objects_on_result_name_basis,
         name='Filter_objects_on_result_name_basis'),
    path('EditDetail/<int:id>', views.edit_detail, name='EditDetail'),
    path('UpdateDetail/<int:id>', views.UpdateDetail, name='UpdateDetail'),
    path('DeleteDetail/<int:id>', views.DeleteDetail, name='DeleteDetail'),
    path('CollectStudentFee/<int:id>', views.collect_student_fee, name='CollectStudentFee'),
]
