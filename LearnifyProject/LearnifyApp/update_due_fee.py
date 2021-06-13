import pdb
from .models import FeesStructure


def update_due_fee_initially(course, discount, registration_session):
    if not discount:
        discount = 0
    try:
        try:
            Obj = FeesStructure.objects.filter(year_session=registration_session)
            gst = 0.18
            if course == 'Four Year Program':
                for i in Obj:
                    TotalFee = int(i.first_session_fee)
                    gstOnFee = TotalFee * gst
                    stu_due_fee = int(TotalFee) + int(gstOnFee) - int(discount)
            elif course == 'Three Year Program':
                for i in Obj:
                    TotalFee = int(i.second_session_fee)
                    gstOnFee = TotalFee * gst
                    stu_due_fee = int(TotalFee) + int(gstOnFee) - int(discount)
            elif course == 'Two Year Program':
                for i in Obj:
                    TotalFee = int(i.third_session_fee)
                    gstOnFee = TotalFee * gst
                    stu_due_fee = int(TotalFee) + int(gstOnFee) - int(discount)
            elif course == 'One Year Program':
                for i in Obj:
                    TotalFee = int(i.fourth_session_fee)
                    gstOnFee = TotalFee * gst
                    stu_due_fee = int(TotalFee) + int(gstOnFee) - int(discount)
            print(stu_due_fee)
            return stu_due_fee
        except Exception as FeeFetchError:
            print("Error in fetching fee from database:- " + str(FeeFetchError))
    except Exception as NoFeeStructureForThisSession:
        return str(NoFeeStructureForThisSession)
