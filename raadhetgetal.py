import random

def raadhetgetal():
    max_getal = 30
    aantal_pogingen = 5
    geheim_getal = random.randint(1, max_getal)

    print("Welkom bij het raad het getal!")
    print(f"Raad het getal tussen 1 en {max_getal}.")
    print(f"Je hebt {aantal_pogingen} pogingen.")

    for poging in range(1, aantal_pogingen + 1):
        gok = int(input(f"Poging {poging}: Zeg het maar! "))

        if gok == geheim_getal:
            print(f"SIIII! Je hebt het getal ({geheim_getal}) geraden in {poging} pogingen.")
            break
        elif gok < geheim_getal:
            print("Te laag, probeer een hoger getal.")
        else:
            print("Te hoog, probeer een lager getal.")

        if poging == aantal_pogingen:
            print(f"Jammer, je hebt het juiste getal ({geheim_getal}) niet geraden.")

if __name__ == "__main__":
    raadhetgetal()
