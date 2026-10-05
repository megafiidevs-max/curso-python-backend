class CuentaBancaria():
    def __init__(self,titular,saldo_inicial):
        self.titular=titular
        self._saldo=saldo_inicial

    def depositar(self,monto):
        self._saldo += monto
        return self._saldo

    def retirar(self,monto):
        if monto <= self._saldo :
            self._saldo -= monto
            return self._saldo
        else:
            print("Fondos insuficientes")

class CuentaAhorros(CuentaBancaria):
    def __init__(self,titular,saldo_inicial,tasa_interes):
        super().__init__(titular, saldo_inicial)
        self.tasa_interes = tasa_interes
    def aplicar_interes(self):
        interes = self._saldo * self.tasa_interes
        super().depositar(interes)

# --- ZONA DE PRUEBAS ---
if __name__ == "__main__":
    print("--- Creando Cuenta de Ahorros de Ana ---")
    # Creamos una cuenta de ahorros para Ana con $1000 iniciales y 5% de interés
    cuenta_ana = CuentaAhorros("Ana Gómez", 1000.0, 0.05)
    
    # 1. Probamos depósito
    cuenta_ana.depositar(500.0) 
    
    # 2. Probamos aplicar intereses (5% de $1500 = $75)
    cuenta_ana.aplicar_interes()
    
    # 3. Probamos retiro exitoso
    cuenta_ana.retirar(200.0)
    
    # 4. Probamos el retiro fallido (Fondos insuficientes)
    cuenta_ana.retirar(2000.0)
    
    
    # 5. Intentamos ver el saldo final (Crea un método o lee _saldo)
    print(f"Saldo final de {cuenta_ana.titular}: ${cuenta_ana._saldo}")
