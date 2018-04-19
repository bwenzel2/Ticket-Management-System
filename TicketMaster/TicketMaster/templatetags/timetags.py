from django import template
import datetime
import time

register = template.Library()

def print_timestamp(timestamp):
    ts = "{:%B %d, %Y, %I:%M %p}".format(timestamp)
    return ts

register.filter(print_timestamp)
