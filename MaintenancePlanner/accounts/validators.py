from django.core.exceptions import ValidationError


def user_name_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Only letters are allowed')