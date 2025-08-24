# app/templatetags/custom_filters.py
from django import template
import re

register = template.Library()

@register.filter(name='bullets')
def bullets(value):
    if not value:
        return ""

    # Normalizar saltos de línea a <br>
    text = value.replace("\r\n", "\n").replace("\r", "\n")

    # Dividir por líneas
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    # Si ya vienen con <li> no hacemos nada
    if any("<li>" in l for l in lines):
        return value
    
    # Convertir a lista con ✔
    html = "<ul class='custom-bullets' style='list-style: none;'>"
    for line in lines:
        clean = re.sub(r'<[^>]+>', '', line)  # eliminar tags extra si hubiera
        html += f"<li>{clean}</li>"
    html += "</ul>"

    return html
