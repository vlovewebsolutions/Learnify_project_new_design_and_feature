from django import template

register = template.Library()


@register.simple_tag()
def multiply(session_fee, gst, *args, **kwargs):
    # you would need to do any localization of the result here
    return int(float(session_fee) * gst)



