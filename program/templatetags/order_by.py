# -*- coding: utf-8 -*-
from django import template
register = template.Library()


@register.filter
def order_by(queryset, order):
    return queryset.order_by(order)
