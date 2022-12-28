class Tankas:
    def __init__(self, x_koordinate=0, y_koordinate=0, kryptis="Šiaurė", suviai=0,
                 siaures_suviai=0, pietu_suviai=0, vakaru_suviai=0, rytu_suviai=0):
        self.x_koordinate = x_koordinate
        self.y_koordinate = y_koordinate
        self.kryptis = kryptis
        self.suviai = suviai
        self.siaures_suviai = siaures_suviai
        self.pietu_suviai = pietu_suviai
        self.vakaru_suviai = vakaru_suviai
        self.rytu_suviai = rytu_suviai

    def info(self):
        print(f"Tanko kryptis: {self.kryptis}, "
              f"tanko pozicija: (x = {self.x_koordinate}, y = {self.y_koordinate}), "
              f"iššauta šūvių: {self.suviai}. "
              f"Iš jų: {self.siaures_suviai} į šiaurę, {self.pietu_suviai} į pietus, "
              f"{self.vakaru_suviai} į vakarus, {self.rytu_suviai} į rytus")

    def pirmyn(self):
        self.kryptis = "Šiaurė"
        self.y_koordinate += 1
        return self.y_koordinate, self.kryptis

    def atgal(self):
        self.kryptis = "Pietūs"
        self.y_koordinate -= 1
        return self.y_koordinate, self.kryptis

    def kairen(self):
        self.kryptis = "Vakarai"
        self.x_koordinate -= 1
        return self.x_koordinate, self.kryptis

    def desinen(self):
        self.kryptis = "Rytai"
        self.x_koordinate += 1
        return self.x_koordinate, self.kryptis

    def sauti(self):
        self.suviai += 1
        if self.kryptis == "Šiaurė":
            self.siaures_suviai += 1
        elif self.kryptis == "Pietūs":
            self.pietu_suviai += 1
        elif self.kryptis == "Vakarai":
            self.vakaru_suviai += 1
        else:
            self.rytu_suviai += 1
        return self.suviai, self.siaures_suviai, self.pietu_suviai, self.vakaru_suviai, self.rytu_suviai


tankas = Tankas()

while True:
    veiksmas = input("""Pasirinkite veiksmą:
w - Važiuoti pirmyn
s - Važiuoti atgal
a - Važiuoti į kairę
d - Važiuoti į dešinę
e - Šauti
i - Parodyti statistiką
q - Išeiti iš žaidimo
""")
    if veiksmas == str("w"):
        tankas.pirmyn()
    elif veiksmas == str("s"):
        tankas.atgal()
    elif veiksmas == str("a"):
        tankas.kairen()
    elif veiksmas == str("d"):
        tankas.desinen()
    elif veiksmas == str("e"):
        tankas.sauti()
    elif veiksmas == str("i"):
        tankas.info()
    elif veiksmas == str("q"):
        print("Žaidimas baigtas")
        break
    else:
        print("Nekorektiškas pasirinkimas")
