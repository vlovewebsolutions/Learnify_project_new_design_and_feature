import LearnifyApp
from .models import AddStudent, FeesStructure


def update_fee_detail_of_those_students_who_are_going_to_be_promoted(student, year_session):
    #session_id = FeesStructure.objects.only('id').get(year_session=student_object.student_registered_in_session).id
    student_object = AddStudent.objects.get(id=int(student))
    print(type(student_object))
    fees = FeesStructure.objects.filter(year_session=year_session)
    gst = 0.18
    for fee in fees:
        # first_session_fee = fee.FirstSessionFee
        second_session_fee = fee.second_session_fee
        third_session_fee = fee.third_session_fee
        fourth_session_fee = fee.fourth_session_fee
    if student_object.current_year_of_student == '1' and student_object.course_type_of_student == 'Four Year Program':
        due_fee = float(second_session_fee) + (float(second_session_fee) * gst)
    elif student_object.current_year_of_student == '2' and student_object.course_type_of_student == 'Four Year Program':
        due_fee = float(third_session_fee) + (float(third_session_fee) * gst)
    elif student_object.current_year_of_student == '3' and student_object.course_type_of_student == 'Four Year Program':
        due_fee = float(fourth_session_fee) + (float(fourth_session_fee) * gst)
    elif student_object.current_year_of_student == '1' and student_object.course_type_of_student == 'Three Year Program':
        due_fee = float(third_session_fee) + (float(third_session_fee) * gst)
    elif student_object.current_year_of_student == '2' and student_object.course_type_of_student == 'Three Year Program':
        due_fee = float(fourth_session_fee) + (float(fourth_session_fee) * gst)
    elif student_object.current_year_of_student == '1' and student_object.course_type_of_student == 'Two Year Program':
        due_fee = float(fourth_session_fee) + (float(fourth_session_fee) * gst)
    return str(int(due_fee))


def promote_students_func(id):
    for k in id:
        k = int(k)
        student = AddStudent.objects.get(id=k)
        if student.course_type_of_student == "Four Year Program" and student.current_year_of_student == '1' or student.current_year_of_student == '2' or student.current_year_of_student == '3':
            value_of_current_year_is = int(student.current_year_of_student) + 1
        elif student.course_type_of_student == "Three Year Program" and student.current_year_of_student == '1' or student.current_year_of_student == '2':
            value_of_current_year_is = int(student.current_year_of_student) + 1
        elif student.course_type_of_student == "Two Year Program" and student.current_year_of_student == '1':
            value_of_current_year_is = int(student.current_year_of_student) + 1

        session_of_students = student.current_session_of_students
        value_of_current_session_first_is = session_of_students[0:4]
        value_of_current_session_second_is = session_of_students[-2:]
        value_of_current_session_first_is = int(value_of_current_session_first_is) + 1
        value_of_current_session_second_is = int(value_of_current_session_second_is) + 1
        value_of_current_session_is = str(value_of_current_session_first_is) + '-' + str(
            value_of_current_session_second_is)
        if FeesStructure.objects.filter(year_session=value_of_current_session_is).exists():
            due_fee_of_student = update_fee_detail_of_those_students_who_are_going_to_be_promoted(k,
                                                                                                  value_of_current_session_is)
            value_of_registration_of_student = student.registration_number
            if not '_promoted_in_' in value_of_registration_of_student:
                value_of_registration_of_student = str(value_of_registration_of_student) + '_promoted_in_' + str(
                    value_of_current_year_is) + '_year'
            else:
                number = value_of_registration_of_student[-6:]
                increased_number = int(number) + 1
                value_of_registration_of_student = value_of_registration_of_student[-5:] + str(
                    increased_number) + value_of_registration_of_student[-6:]
            AddStudent.objects.create(student_registered_in_session=student.student_registered_in_session,
                                      current_year_of_student=str(value_of_current_year_is),
                                      current_session_of_students=str(value_of_current_session_is),
                                      registration_number=value_of_registration_of_student,
                                      registration_date=student.registration_date,
                                      student_name=student.student_name, student_image=student.student_image,
                                      student_date_of_birth=student.student_date_of_birth, student_gender=student.student_gender,
                                      student_present_class=student.student_present_class,
                                      course_type_of_student=student.course_type_of_student,
                                      student_present_school_name=student.student_present_school_name,
                                      student_school_board_affiliation=student.student_school_board_affiliation,
                                      fathers_name=student.fathers_name,
                                      fathers_qualification=student.fathers_qualification,
                                      occupation_of_father=student.occupation_of_father,
                                      mothers_name=student.mothers_name,
                                      present_address_of_student=student.present_address_of_student,
                                      correspondence_address_of_student=student.correspondence_address_of_student,
                                      email_of_student=student.email_of_student, mobile_number_of_student=student.mobile_number_of_student,
                                      mobile_number_of_father=student.mobile_number_of_father,
                                      discount_on_session_fee=str(0), remarks_of_discount="Discount is not given yet!",
                                      fee_paid_by_student=str(0),
                                      due_fee_of_student=due_fee_of_student, fee_status_student='Pending',
                                      student_status=student.student_status
                                      )

            print("Yes have called promote_students function of promote module:-" + str(id))
            return 'success'
        else:
            return 'fail'
