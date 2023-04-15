from django.template import Library
from datetime import datetime
from django.utils.timesince import timesince

register = Library()

@register.filter
def parse_date(value):
    return datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ').strftime('%d %B %Y')


@register.filter
def hours_since(value):
    time_diff = timesince(value).split(', ')
    return time_diff[0]
    # if len(time_diff) > 1:
    #     # print('jsf' , time_diff[0],time_diff[0].split()[0])
    #     # hours = int(time_diff[0].split()[0])
    #     return f'{int(time_diff[0])}'
    # else:
    #     return time_diff[0]


@register.filter
def split(value, arg):
    return value.split(arg)
