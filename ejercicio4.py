billetes = {
    "500" : 0,
    "200" : 0,
    "100" : 0}

def retirar_dinero(cantidad):
    if (cantidad % 100)>0:
        return 'error'
    result = billetes.copy()
    resto = cantidad
    for billete in billetes:
        cuantos=resto // int(billete)
        if (cuantos) > 0 :
            result[billete]=cuantos
            resto -= (cuantos * int(billete))        
    return result

print(retirar_dinero(1300))
print(retirar_dinero(500))
print(retirar_dinero(300))
print(retirar_dinero(700))
print(retirar_dinero(2300))
print(retirar_dinero(4500))