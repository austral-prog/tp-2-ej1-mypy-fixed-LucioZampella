def is_leap_year() -> bool:
    """Pide al usuario ingresar un año y determina si es bisiesto o no."""
    year = int(input("Ingrese un año: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        es_bisiesto = True
        mensaje = f"El año {year} es bisiesto"
    else:
        es_bisiesto = False
        mensaje = f"El año {year} no es bisiesto"
    print(mensaje)
    return es_bisiesto
