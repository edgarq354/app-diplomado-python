from django.core.exceptions import ValidationError


def validar_monto(value):
    if value <= 0:
        raise ValidationError('%(value)s no es un monto válido. Debe ser mayor a 0.',
                              params={"value": value})
                              
def validar_nombre(value):
    if not value.isalpha():
        raise ValidationError('El nombre solo debe contener letras.')
