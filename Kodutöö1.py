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
inimesi = int(input("Sisesta inimeste arv: "))
kohad = int(input("Sisesta ühe bussi kohtade arv: "))

busside_arv = inimesi // kohad
ulejaanud = inimesi % kohad

if ulejaanud > 0:
    busside_arv += 1
    viimases_bussis = ulejaanud
else:
    viimases_bussis = kohad

print("Inimeste arv:", inimesi)
print("Kohtade arv:", kohad)
print("Busse vaja:", busside_arv)
print("Viimases bussis inimesi:", viimases_bussis)

istekohti = 40
reisijad = 40


taisbuss = reisijad // istekohti
jaak = reisijad % istekohti

if jaak > 0:
    lisabuss = 1
else:
    lisabuss = 0

print("Busside arv:", taisbuss + lisabuss)

