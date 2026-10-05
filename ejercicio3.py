logs = [
    "INFO: Conexión establecida con la base de datos.",
    "ERROR: Llave primaria duplicada en tabla Clientes.",
    "WARNING: Tiempo de respuesta lento en query de ventas.",
    "ERROR: Conexión perdida con el servidor.",
    "INFO: Respaldo automático completado con éxito.",
    "ERROR: Intento de inyección SQL detectado."
]

resultado={
    "ERROR" : 0,
    "WARNING" : 0,
    "INFO" : 0}

for log in logs:
    if log.startswith('INFO'):
        resultado['INFO'] += 1
    elif log.startswith('ERROR'):
        resultado['ERROR'] += 1
    elif log.startswith('WARNING'):
        resultado['WARNING'] +=1

print(resultado)