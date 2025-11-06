#Harjutus 1.1
print ("Tere, maailm!")

#Harjutus 1.2
aasta = 2020
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa = ". aasta liblikas on "
lause = str(aasta) + lause_keskosa + liblikas
print(lause)

#Harjutus 1.3
korgus = float(input("Sisesta pilvede aluse kõrgus (km): "))

if korgus > 6:
    print("Need on ülemised pilved.")
elif 2 <= korgus <= 6:
    print("Need on keskmised pilved.")
else:
    print("Need on alumised pilved.")
    
#Harjutus 1.4
    
Reisijaid = int(input("Sisesta reisijate arv: "))
Istekohti = int(input("Sisesta ühe bussi istekohtade arv:"))

busside_arv = Reisijaid / Istekohti
jaak = Reisijaid - Istekohti
    
    

istekohti = 40
Reisijad = 40

busside_arv = Reisijad // istekohti

lisabuss = Reisijad % istekohti



if jaak > 0:
    lisabuss = 1
else:
    lisabuss = 0

print("Busside arv:", busside_arv + lisabuss)


