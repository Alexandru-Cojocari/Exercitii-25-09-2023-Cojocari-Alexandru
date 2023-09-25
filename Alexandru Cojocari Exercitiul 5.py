# Ion alege un numar
numar_ales_de_ion=int(input("Ion alege un numar: "))

# Gasim cele 5 numere consecutive cu numarul ales de Ion in mijloc
numere_gasite = (numar_ales_de_ion-2, numar_ales_de_ion-1, numar_ales_de_ion,
 numar_ales_de_ion+1, numar_ales_de_ion+2)

# Afisam numerele gasite de Vasile
print(f"Vasile a gasit urmatoarele numere: {numere_gasite}")
