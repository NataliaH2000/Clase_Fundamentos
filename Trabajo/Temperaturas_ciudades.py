
#Trabajos
# Definir las ciudades
ciudades = ["QUITO", "GUARANDA", "LAGO AGRIO"]

# Datos de temperaturas
temperaturas = [
    [   # QUITO
        [   # Semana 1
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 25}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 21}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 27}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 29}
        ]
    ],
    [   # GUARANDA
        [   # Semana 1
            {"day": "Lunes", "temp": 44},
            {"day": "Martes", "temp": 45},
            {"day": "Miércoles", "temp": 48},
            {"day": "Jueves", "temp": 43},
            {"day": "Viernes", "temp": 38},
            {"day": "Sábado", "temp": 40},
            {"day": "Domingo", "temp": 42}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 42},
            {"day": "Martes", "temp": 39},
            {"day": "Miércoles", "temp": 38},
            {"day": "Jueves", "temp": 43},
            {"day": "Viernes", "temp": 41},
            {"day": "Sábado", "temp": 39},
            {"day": "Domingo", "temp": 38}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 37},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 36},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 38},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 39},
            {"day": "Martes", "temp": 37},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 36}
        ]
    ],
    [   # LAGO AGRIO
        [   # Semana 1
            {"day": "Lunes", "temp": 62},
            {"day": "Martes", "temp": 66},
            {"day": "Miércoles", "temp": 58},
            {"day": "Jueves", "temp": 60},
            {"day": "Viernes", "temp": 64},
            {"day": "Sábado", "temp": 66},
            {"day": "Domingo", "temp": 69}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 50},
            {"day": "Martes", "temp": 56},
            {"day": "Miércoles", "temp": 59},
            {"day": "Jueves", "temp": 62},
            {"day": "Viernes", "temp": 60},
            {"day": "Sábado", "temp": 64},
            {"day": "Domingo", "temp": 61}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 48},
            {"day": "Martes", "temp": 50},
            {"day": "Miércoles", "temp": 52},
            {"day": "Jueves", "temp": 54},
            {"day": "Viernes", "temp": 47},
            {"day": "Sábado", "temp": 53},
            {"day": "Domingo", "temp": 55}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 83},
            {"day": "Martes", "temp": 91},
            {"day": "Miércoles", "temp": 72},
            {"day": "Jueves", "temp": 88},
            {"day": "Viernes", "temp": 78},
            {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 79}
        ]
    ]
]

# Función para calcular el promedio de temperatura

def calcular_promedio(ciudad_idx=None, semana_idx=None):
    for c_idx, ciudad in enumerate(temperaturas):
        if ciudad_idx is not None and c_idx != ciudad_idx:
            continue
        for s_idx, semana in enumerate(ciudad):
            if semana_idx is not None and s_idx != semana_idx:
                continue
            suma_temperaturas = sum(dia["temp"] for dia in semana)
            promedio = suma_temperaturas / len(semana)
            print(f"Promedio de {ciudades[c_idx]}, Semana {s_idx + 1}: {promedio:.4f}")

# Solicitar filtros al usuario
ciudad_filtro = input("Ingrese el nombre de la ciudad (o presione Enter para todas): ").strip().upper()
semana_filtro = input("Ingrese el número de la semana (1-4) o presione Enter para todas: ").strip()

# Validar si la ciudad ingresada es correcta
if ciudad_filtro and ciudad_filtro not in ciudades:
    print("Error: Ciudad no encontrada. Intente de nuevo.")
    exit()

# Obtener el índice de la ciudad
ciudad_idx = ciudades.index(ciudad_filtro) if ciudad_filtro in ciudades else None

# Validar si la semana ingresada es correcta
if semana_filtro and (not semana_filtro.isdigit() or not (1 <= int(semana_filtro) <= 4)):
    print("Error: Semana inválida. Debe estar entre 1 y 4.")
    exit()

# Obtener el índice de la semana
semana_idx = int(semana_filtro) - 1 if semana_filtro.isdigit() else None

# Calcular promedios según filtros
calcular_promedio(ciudad_idx, semana_idx)