#Escritura de Archivo de Texto
# Escritura de Archivo de Texto
# Abrimos (o creamos) el archivo en modo escritura ('w')
with open("my_notes.txt", "w") as file:
    # Escribimos tres líneas de notas personales
    file.write("Hoy aprendí a trabajar con archivos de texto en Python.\n")
    file.write("El método write() me permite escribir en el archivo.\n")
    file.write("También aprendí a leer línea por línea con readline().\n")
# El archivo se cierra automáticamente al salir del bloque 'with'

# Lectura de Archivo de Texto
# Abrimos el archivo en modo lectura ('r')
file = open("my_notes.txt", "r")

# Leemos línea por línea utilizando readline()
print("Contenido del archivo:")
line = file.readline()
while line:
    print(line.strip())  # Mostramos la línea sin el salto de línea extra
    line = file.readline()

# Cierre del archivo manualmente
file.close()
