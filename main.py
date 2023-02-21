from osoba import Osoba
from pes import Pes

karel = Osoba("Karel Novák")
lenka = Osoba("Lenka Nováková")
azor = Pes("Azor")
karel.pes = azor
lenka.pes = azor
print(azor)

# Zestárnutí psa
karel.pes.zestarni()
lenka.pes.zestarni()

# Kontrolní výpis dat
print(azor)