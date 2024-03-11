disponible = {
    100: 3,
    50: 6,
    20: 10,
    10: 50,
    1:  50
}

def total_disponible(): 
    total = 0
    for k,v in disponible.items():
        total += k*v
        return total

def retirar(monto):
    pass

monto = 1350
retirar(monto)

#PENDIENTE