#Programa para dar cambio exacto

dinero = int(input("Cantidad:"))

uno = dinero / 500
restouno = dinero % 500
dos = restouno / 200
restodos = restouno % 200
tres = restodos / 100
restotres = restodos % 100
cuatro = restotres / 50
restocuatro = restotres % 50
cinco = restocuatro / 20
restocinco = restocuatro % 20
seis = restocinco / 10
restoseis = restocinco % 10
if uno !=0:
    if uno == 1:
        print(uno)
        print("Billete de 500 pesos")
    if uno > 1:
        print (uno)
        print("Billete de 500 pesos")
if dos != 0:
        if dos == 1:
            print (dos)
            print("Billete de 200 pesos")
        if dos > 1:
            print (dos)
            print("Billete de 200 pesos")
if tres != 0:
    if tres == 1:
        print (tres)
        print("Billete de 100 pesos")
    if tres > 1:
        print(tres)
        print("Billete de 100 pesos")
if cuatro != 0:
    if cuatro == 1:
        print (cuatro)
        print("Billete de 50 pesos")
    if cuatro > 1:
        print (cuatro)
        print("Billete de 50 pesos")
if cinco != 0:
    if cinco == 1:
        print (cinco)
        print("Billete de 20 pesos")
    if cinco > 1:
        print (cinco)
        print("Billete de 20 pesos")
if seis != 0:
    if seis == 1:
        print (seis)
        print("Moneda de 10 pesos")
    if seis > 1:
        print (seis)
        print("Moneda de 10 pesos")
