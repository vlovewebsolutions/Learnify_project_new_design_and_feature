from django import template

register = template.Library()


@register.simple_tag()
def add(session_fee, *args, **kwargs):
    # you would need to do any localization of the result here
    gst_on_fee = float(session_fee) * 0.18
    TotalFee = int(session_fee) + int(gst_on_fee)
    return TotalFee
