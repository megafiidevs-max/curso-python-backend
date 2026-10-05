inventario = [
    {"nombre": "Teclado Mecánico", "precio": 85.0, "stock": 4},
    {"nombre": "Mouse Óptico", "precio": 25.0, "stock": 15},
    {"nombre": "Monitor 4K", "precio": 450.0, "stock": 2},
    {"nombre": "Cable HDMI", "precio": 12.0, "stock": 8},
    {"nombre": "Audífonos Pro", "precio": 120.0, "stock": 20}
]



resultado = [producto for producto in inventario if producto["precio"]>50 and producto["stock"]<10]
print(resultado)