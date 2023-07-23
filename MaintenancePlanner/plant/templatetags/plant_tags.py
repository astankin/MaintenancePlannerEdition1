from django import template

register = template.Library()


@register.filter
def get_departments(departments, plant_id):
    return departments.get(plant_id, [])
