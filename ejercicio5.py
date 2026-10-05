correos_sucios = [
    "carlos@Empresa.com", "ANA@mail.com", "carlos@empresa.com", 
    "luis@proyectos.org", "Ana@mail.com", "LUIS@proyectos.org"
]

limpios=set()

for correo in correos_sucios:
    limpios.add(correo.lower())

resultado = list(limpios)
resultado.sort()

print(resultado)