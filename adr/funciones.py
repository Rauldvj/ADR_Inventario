import re
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#AQUÍ CREAREMOS DIFERENTES FUNCIONES QUE NOS VALIDEN CIERTOS ATRIBUTOS DE LOS MODELOS

#VALIDAR LONGITUD DEL RUT Y EL DÍGITO VERIFICADOR


def validar_rut(rut):
    rut = rut.replace(".", "").replace("-", "").lower()
    rut = rut[:-1] + "-" + rut[-1]

    rut = rut.split("-")
    cuerpo_rut = rut[0]
    digito_verificador = rut[1]

    suma = 0
    multiplo = 2
    for i in reversed(cuerpo_rut):
        suma += int(i) * multiplo
        multiplo += 1
        if multiplo == 8:
            multiplo = 2

    digito_calculado = 11 - (suma % 11)
    if digito_calculado == 11:
        digito_calculado = 0
    elif digito_calculado == 10:
        digito_calculado = "k"

    return str(digito_calculado) == digito_verificador


# Ejemplo de uso:
if __name__ == "__main__":
    rut = "11111111-1"  # Aquí coloca el RUT que quieres validar
    if validar_rut(rut):
        print("El RUT es válido.")
    else:
        print("El RUT no es válido.")





#FUNCIÓN PARA PASAR DE PLURAL A SINGULAR LOS GRUPOS
def plural_singular(plural):
    plural_singular = {
        'Usuario': 'Usuario',
        'ADR': 'ADR',
        'Operadores ADR': 'Operador ADR',
        'Auxiliares Operadores ADR': 'Auxiliar Operador ADR',
        'Alumnos en Práctica': 'Alumno en Práctica',
    }
    return plural_singular.get(plural, "error")


#FUNCION DE FILTRADO Y PAGINADO
from django.core.paginator import Paginator

def filtrar_y_paginar(request, queryset, paginate_by):
    filter_ubicacion = request.GET.get('filter_ubicacion', '')

    if filter_ubicacion:
        queryset = queryset.filter(ubicacion_all_in_one=filter_ubicacion)

    paginator = Paginator(queryset, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Obtener la lista de ubicaciones únicas para el filtro
    ubicaciones = queryset.values_list('ubicacion_all_in_one', flat=True).distinct()

    return page_obj, filter_ubicacion, ubicaciones
