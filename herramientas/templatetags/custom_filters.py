from django import template
from datetime import time

register = template.Library()

@register.filter
def filter_hora(clases, hora):
    clases_filtradas = [clase for clase in clases if clase.hora_inicio <= hora and clase.hora_fin >= hora]
    return clases_filtradas