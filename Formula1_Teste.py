def formula1():
    pista = int(input("Compirmento da pista em metros: "))
    voltas = int(input("Número de voltas: "))
    rea = int(input("Número de reabestecimento: "))
    combus = int(input("Consumo de Combustível do carro em Km/L: "))
    voltasRe = voltas/rea
    km = pista/voltasRe
    litros = km*combus
    print("Litros necessários para percorrer até o primeiro reabastecimento: ",litros)
