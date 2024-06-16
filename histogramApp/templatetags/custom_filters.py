from django import template
import base64


register=template.Library()

#This creates a custom b64encode filter that uses the base64.b64encode() function to encode the input value

@register.filter
def b64encode(value):
    import base64
    return base64.b64encode(value.encode('utf-8')).decode('utf-8')




