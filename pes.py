class Pes:
    # Třída reprezentuje psa

    jmeno = None
    vek = 1

    # Konstruktor
    def __init__(self, jmeno):
        self.jmeno = jmeno

    # Nechá psa zestárnout o rok
    def zestarni(self):
        self.vek += 1

    # Vrátí textovou reprezentaci psa
    def __str__(self):
        return "{0} {1}".format(self.jmeno, self.vek)
