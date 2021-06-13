from django import template
from .models import AddStudent

register = template.Library()


@register.simple_tag()
def fees(id):
    fee = AddStudent.objects.filter(id=id)
    for i in fee:
        fees = i.current_year_of_student
    return fees

