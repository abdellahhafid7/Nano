import random

def galgje():
    woorden = ['Abdellah', 'Ayoub', 'Cesur', 'Rayaan', 'Aymane',]
    woord = random.choice(woorden).lower()  # Het woord wordt in kleine letters gezet voor consistentie
    spelwoord = ['_'] * len(woord)
    pogingen = 7
    geradenletters = []

    print("Welkom bij Galgje!")
    begin = input("Denk je dat je het aankan? ").strip().capitalize()

    if begin == "Ja":
        while pogingen > 0 and "_" in spelwoord:
            print("\nWoord: " + " ".join(spelwoord))
            print(f"Huidige pogingen: {pogingen}")
            print(f"Geraden letters: {', '.join(geradenletters)}")

            gok = input("Raad een letter: ").lower()

            if gok in geradenletters:
                print("Dit zei je net al....")
            elif gok in woord:
                print(f"Goed! '{gok}' zit in het woord.")
                geradenletters.append(gok)
                for i, letter in enumerate(woord):
                    if letter == gok:
                        spelwoord[i] = gok
            else:
                print(f"Helaas, '{gok}' zit niet in het woord :(")
                geradenletters.append(gok)
                pogingen -= 1

            if "_" not in spelwoord:
                print("\nSterkkk! Je hebt het woord geraden:", woord)
                break
        else:
            print("\nHahahahahaah! Je hebt geen pogingen meer. Het woord was:", woord)
    else:
        print("Saffi dan niet.")

if __name__ == "__main__":
    galgje()
