import pickle
import django

class Irasas:
    def __init__(self, suma):
        self.suma = suma


class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, info):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.info = info

    def __str__(self):
        return f"Pajamos: {self.suma} (siuntėjas - {self.siuntejas}, info - {self.info})"


class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta, info):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta = isigyta
        self.info = info

    def __str__(self):
        return f"Išlaidos: {self.suma} (atsiskaitymo būdas - {self.atsiskaitymo_budas}, įsigyta - {self.isigyta}, info - {self.info})"


class Biudzetas:
    def __init__(self):
        self.zurnalas = self.nuskaityti_pkl()

    def nuskaityti_pkl(self):
        try:
            with open("zurnalas.pkl", 'rb') as file:
                zurnalas = pickle.load(file)
        except:
            zurnalas = []
        return zurnalas

    def irasyti_pkl(self):
        with open("zurnalas.pkl", 'wb') as file:
            pickle.dump(self.zurnalas, file)

    def prideti_pajamu_irasa(self):
        suma = abs(float(input("Suma: ")))
        siuntejas = input("Siuntėjas: ")
        info = input("Papildoma informacija: ")
        irasas = PajamuIrasas(suma, siuntejas, info)
        self.zurnalas.append(irasas)
        self.irasyti_pkl()

    def prideti_islaidu_irasa(self):
        suma = abs(float(input("Suma: ")))
        atsiskaitymo_budas = input("Atsiskaitymo būdas: ")
        isigyta = input("Įsigyta prekė/paslauga: ")
        info = input("Papildoma informacija: ")
        irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta, info)
        self.zurnalas.append(irasas)
        self.irasyti_pkl()

    def ataskaita(self):
        for irasas in self.zurnalas:
            print(irasas)

    def balansas(self):
        suma = 0
        for irasas in self.zurnalas:
            if type(irasas) is PajamuIrasas:
                suma += irasas.suma
            else:
                suma -= irasas.suma
        print(suma)
        return suma


biudzetas = Biudzetas()

while True:
    pasirinkimas = int(input("1 - įvesti pajamas\n2 - įvesti išlaidas\n3 - peržiūrėti\n4 - balansas\n0 - išeiti\n"))
    match pasirinkimas:
        case 1:
            biudzetas.prideti_pajamu_irasa()
        case 2:
            biudzetas.prideti_islaidu_irasa()
        case 3:
            biudzetas.ataskaita()
        case 4:
            biudzetas.balansas()
        case 0:
            break
