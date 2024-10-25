import random

# Lista de palabras para adivinar
Palabras =["casa", "perro", "gato", "raton", "elefante", "leon", "tigre", "jirafa", "mono", "pajaro", "pez", "ballena", "delfin", "tiburon", "serpiente", "cocodrilo", "rinoceronte", "hipopotamo", "oso", "lobo", "zorro", "ciervo", "caballo", "vaca", "cerdo", "oveja", "conejo", "ardilla", "oso hormiguero", "oso panda", "oso polar", "alquimista", "arquitecto", "astronauta", "biologo", "botanico", "cantante", "carpintero", "cocinero", "compositor", "danzarín", "dibujante", "director", "escritor", "fotografo", "ingeniero", "jardinero", "maestro", "medico", "militar", "musico", "pintor", "poeta", "profesor","software"]

def seleccionar_palabra():
    return random.choice(Palabras)# Seleccionar una palabra al azar