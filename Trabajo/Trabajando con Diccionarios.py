
# Ejemplo de diccionario:
informacion_personal = {"nombre": "Natalia", "edad": 24, "ciudad": "Putumayo", "profesion": "Estudiante"}
print (informacion_personal)

# Acceder y Modificar valores:
print(informacion_personal["ciudad"])
print(informacion_personal["edad"])

# Modificar ciudad:
print(informacion_personal["ciudad"]=="San Miguel")

# Agregar profesion:
print(informacion_personal["profesion"]=="Estudiante")

# Verificar existencia de "telefono" y agregarlo si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0992119153"
    print(informacion_personal)

# Eliminar una Clave:
del informacion_personal["edad"]
print(informacion_personal)