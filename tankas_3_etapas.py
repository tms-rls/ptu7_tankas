import random


class Tankas:
    def __init__(self, taskai=10, x_koordinate=0, y_koordinate=0, kryptis="Šiaurė",
                 siaures_suviai=0, pietu_suviai=0, vakaru_suviai=0, rytu_suviai=0):
        self.taskai = taskai
        self.x_koordinate = x_koordinate
        self.y_koordinate = y_koordinate
        self.kryptis = kryptis
        self.siaures_suviai = siaures_suviai
        self.pietu_suviai = pietu_suviai
        self.vakaru_suviai = vakaru_suviai
        self.rytu_suviai = rytu_suviai
        self.visi_suviai = 0
        self.numusti_taikiniai = 0

    def pirmyn(self):
        self.taskai -= 1
        self.kryptis = "Šiaurė"
        self.y_koordinate += 1
        if self.taskai == 0:
            print(f"Baigėsi taškai - žaidimo pabaiga")
            quit()
        return self.y_koordinate, self.kryptis, self.taskai

    def atgal(self):
        self.kryptis = "Pietūs"
        self.y_koordinate -= 1
        self.taskai -= 1
        if self.taskai == 0:
            print(f"Baigėsi taškai - žaidimo pabaiga")
            quit()
        return self.y_koordinate, self.kryptis, self.taskai

    def kairen(self):
        self.kryptis = "Vakarai"
        self.x_koordinate -= 1
        self.taskai -= 1
        if self.taskai == 0:
            print(f"Baigėsi taškai - žaidimo pabaiga")
            quit()
        return self.x_koordinate, self.kryptis, self.taskai

    def desinen(self):
        self.kryptis = "Rytai"
        self.x_koordinate += 1
        self.taskai -= 1
        if self.taskai == 0:
            print(f"Baigėsi taškai - žaidimo pabaiga")
            quit()
        return self.x_koordinate, self.kryptis, self.taskai

    def sauti(self):
        if self.kryptis == "Šiaurė":
            self.siaures_suviai += 1
        elif self.kryptis == "Pietūs":
            self.pietu_suviai += 1
        elif self.kryptis == "Vakarai":
            self.vakaru_suviai += 1
        else:
            self.rytu_suviai += 1
        self.visi_suviai = self.siaures_suviai + self.pietu_suviai + self.vakaru_suviai + self.rytu_suviai
        self.taskai -= 1
        if self.taskai == 0:
            print(f"Baigėsi taškai - žaidimo pabaiga. Numušėte {self.numusti_taikiniai} taikinius")
            quit()
        return self.taskai, self.siaures_suviai, self.pietu_suviai, self.vakaru_suviai, self.rytu_suviai, self.visi_suviai


class Taikinys:
    def __init__(self, x_koordinate=random.randint(-5, 5), y_koordinate=random.randint(-5, 5)):
        self.x_koordinate = x_koordinate
        self.y_koordinate = y_koordinate

    def naujas(self):
        self.x_koordinate = random.randint(-5, 5)
        self.y_koordinate = random.randint(-5, 5)
        return f"Naujo taikinio pozicija: {self.x_koordinate, self.y_koordinate}"


class Musis:
    def pataikymas(self):
        if tankas.x_koordinate == taikinys.x_koordinate and tankas.y_koordinate == taikinys.y_koordinate:
            tankas.numusti_taikiniai += 1
            print(f"Sprogote kartu su taikiniu. Žaidimo pabaiga. Numušti taikiniai: {tankas.numusti_taikiniai}")
            quit()
        else:
            if tankas.x_koordinate == taikinys.x_koordinate:
                if tankas.y_koordinate > taikinys.y_koordinate and tankas.kryptis == "Pietūs":
                    tankas.numusti_taikiniai += 1
                    tankas.taskai += 5
                    print("Pataikei!")
                    print(taikinys.naujas())
                    print(f"Gavote 5 taškus, dabar turite: {tankas.taskai}")
                    return tankas.numusti_taikiniai, tankas.taskai
                elif tankas.y_koordinate < taikinys.y_koordinate and tankas.kryptis == "Šiaurė":
                    tankas.numusti_taikiniai += 1
                    tankas.taskai += 5
                    print("Pataikei!")
                    print(taikinys.naujas())
                    print(f"Gavote 5 taškus, dabar turite: {tankas.taskai}")
                    return tankas.numusti_taikiniai, tankas.taskai
                else:
                    print("Nepataikei!")
                    return tankas.numusti_taikiniai, tankas.taskai
            elif tankas.y_koordinate == taikinys.y_koordinate:
                if tankas.x_koordinate > taikinys.x_koordinate and tankas.kryptis == "Vakarai":
                    tankas.numusti_taikiniai += 1
                    tankas.taskai += 5
                    print("Pataikei!")
                    print(taikinys.naujas())
                    print(f"Gavote 5 taškus, dabar turite: {tankas.taskai}")
                    return tankas.numusti_taikiniai, tankas.taskai
                elif tankas.x_koordinate < taikinys.x_koordinate and tankas.kryptis == "Rytai":
                    tankas.numusti_taikiniai += 1
                    tankas.taskai += 5
                    print("Pataikei!")
                    print(taikinys.naujas())
                    print(f"Gavote 5 taškus, dabar turite: {tankas.taskai}")
                    return tankas.numusti_taikiniai, tankas.taskai
                else:
                    print("Nepataikei!")
                    return tankas.numusti_taikiniai, tankas.taskai
            else:
                print("Nepataikei!")
                return tankas.numusti_taikiniai, tankas.taskai

    def info(self):
        print(f"Taškai: {tankas.taskai}, Tanko kryptis: {tankas.kryptis}, "
              f"tanko pozicija: (x = {tankas.x_koordinate}, y = {tankas.y_koordinate}), "
              f"iššauta šūvių: {tankas.visi_suviai}. "
              f"Iš jų: {tankas.siaures_suviai} į šiaurę, {tankas.pietu_suviai} į pietus, "
              f"{tankas.vakaru_suviai} į vakarus, {tankas.rytu_suviai} į rytus, "
              f"numušta {tankas.numusti_taikiniai} taikinių\n"
              f"Taikinio pozicija:(x = {taikinys.x_koordinate}, y = {taikinys.y_koordinate})")


tankas = Tankas()
taikinys = Taikinys()
musis = Musis()

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
        musis.pataikymas()
    elif veiksmas == str("i"):
        musis.info()
    elif veiksmas == str("q"):
        print("Žaidimas baigtas")
        break
    else:
        print("Nekorektiškas pasirinkimas")
