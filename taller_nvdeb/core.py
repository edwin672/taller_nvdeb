# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['foo', 'saludo', 'saludo_a', 'concatena']

# %% ../nbs/00_core.ipynb 3
def foo(var_bool):
    "Esta funcion muestra un mensaje dependiendo del valor de la variable de entrada"
    if var_bool:
        return "verdadero"
    else:
        return "falso"
    return
    

# %% ../nbs/00_core.ipynb 7
def saludo():
    "Esta funcion muestra un saludo"
    print("Hola!")
    return

# %% ../nbs/00_core.ipynb 8
def saludo_a(to):
    """Imprime hola a un nombre"""
    print("Hola",to)
    print("¿Cómo estás?")
    return

# %% ../nbs/00_core.ipynb 12
def concatena(nombre = None):
    saludo()
    saludo_a(nombre)
    return
