from django.template import Library
from datetime import datetime

register = Library()

@register.filter
def parse_date(value):
    return datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ').strftime('%d %B %Y')


