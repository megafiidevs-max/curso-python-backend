# Un diccionario en Python es como un registro dinámico indexado
datos_usuario = {
    "nombre": "Ingeniero",
    "año_egreso": 2004,
    "lenguaje_anterior": "Delphi"
}

# Un bucle 'for' que itera directamente sobre una estructura de datos
print("--- Iniciando actualización tecnológica ---")
for clave, valor in datos_usuario.items():
    print(f"Propiedad: {clave.upper()} -> Valor: {valor}")
