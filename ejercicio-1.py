#Entrada
monto=int(input("ingrese el valor de la compra"))
if monto<50:
    print("descuento aplicado:$",monto*0)
    print("total a pagar:$",monto)

elif monto>49 and monto<101:
    print("descuento aplicado:$",monto*0.05)
    print("total a pagar:$",monto-(monto*0.05))

elif monto>100:
    print("descuento aplicado:$",monto*0.1)
    print("total a pagar:$",monto-(monto*0.1))