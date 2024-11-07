# menu.py
from hangman import galgje
from raadhetgetal import raadhetgetal

def hoofdmenu():
    while True:
        print("\n--- Hoi! Welke spel wil je spelen? ---")
        print("1: Galgje")
        print("2: Raad het nummer")
        print("3: Stoppen")

        keuze = input("Maak een keuze (1, 2 of 3): ")

        if keuze == "1":
            galgje()  # Start het woordspel
        elif keuze == "2":
            raadhetgetal()  # Start het getalspel
        elif keuze == "3":
            print("Zo saai, doei.")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")

# Start het keuzemenu
if __name__ == "__main__":
    hoofdmenu()
