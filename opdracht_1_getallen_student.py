#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Final assignment: getallen

(c) 2019 Hogeschool Utrecht,
Peter van den Berg (peter.vandenberg@hu.nl)
Bart van Eijkelenburg
Tijmen Muller (tijmen.muller@hu.nl)


Opdracht:
Beantwoord onderstaande vragen en werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van `pytest`, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""

# TODO: Vul hier je naam, klas en studentnummer in.
naam = "Abdellah Hafid"
klas = "1VR"
studentnummer = -1886727

"""
1.  Pseudocode ceil

    Schrijf Nederlandse pseudocode voor een algoritme voor de functie ceil() (zie onder).
    Schrijf je pseudocode keywords met alleen hoofdletters (ALS, VOOR, etc...).

"""
#   TODO: [geef hier je antwoord]

# PSEUDOCODE CEIL:

# ONT vang een reëel getal 'real'

# Verkrijg het gehele getal door het getal naar beneden af te ronden
# geheel_deel = het gehele deel van 'real'

# ALS 'real' al een geheel getal is (dus zonder decimale cijfers)
    # Geef het gehele getal 'geheel_deel' terug, zonder verdere afronding

# ANDERS, als het getal positief is:
    # Voeg 1 toe aan 'geheel_deel' om het getal naar boven af te ronden
    # Geef het afgeronde getal terug

# ANDERS, als het getal negatief is:
    # Geef gewoon het gehele getal 'geheel_deel' terug, omdat negatieve getallen naar beneden afronden



"""
2. Implementatie ceil
    Implementeer onderstaande functie om naar boven af te ronden.

"""


def ceil(real):
    """
    Bepaal het kleinste gehele getal (int), groter dan of gelijk aan het gegeven reële getal (float).

    Args:
        real (float): Een reëel getal.

    Returns:
        int: Het kleinste gehele getal (int), groter dan of gelijk aan het gegeven reële getal (float).
    """
    # Haal het gehele deel van het getal op (door het af te ronden naar beneden)
    geheel_deel = int(real)

    # Controleer of het getal al een geheel getal is; zo ja, geef het direct terug
    if real == geheel_deel:
        return geheel_deel

    # Als het getal positief is, moet het naar boven worden afgerond door 1 op te tellen
    return geheel_deel + 1 if real > 0 else geheel_deel


"""
3. Implementatie is_even
    Implementeer onderstaande functie om te bepalen of een geheel getal even is.

"""


def is_even(n):
    """
    Bepaal of een geheel getal even is.

    Args:
        n (int): Een geheel getal.

    Returns:
        bool: True als even, False als oneven.
    """
    # Controleer of n deelbaar is door 2. Als dat zo is, is n even
    return n % 2 == 0



"""
4. Implementatie is_odd
    Implementeer onderstaande functie om te bepalen of een geheel getal oneven is.

"""


def is_odd(n):
    """
    Bepaal of een geheel getal oneven is.

    Args:
        n (int): Een geheel getal.

    Returns:
        bool: True als oneven, False als even.
    """
    # Controleer of n niet deelbaar is door 2. Als dat zo is, is n oneven
    return n % 2 != 0



"""
5. Implementatie nround
    Implementeer onderstaande functie om af te ronden naar een geheel getal.

"""


def nround(real):
    """
    Bepaal het gehele getal (int) dat het dichtst bij het gegeven reële getal (float) zit.

    Args:
        real (float): Een reëel getal.

    Returns:
        int: Het gehele getal (int) dat het dichtst bij het gegeven reële getal (float) zit.
    """
    # Haal het gehele deel op door het getal naar beneden af te ronden
    geheel_deel = int(real)

    # Controleer of het decimale deel van real >= 0.5 is voor positieve getallen
    if real - geheel_deel >= 0.5:
        return geheel_deel + 1
    # Controleer of het decimale deel van real <= -0.5 is voor negatieve getallen
    elif real - geheel_deel <= -0.5:
        return geheel_deel - 1
    else:
        return geheel_deel





"""
6. Implementatie dec2bin rij
    Implementeer onderstaande functie om de binaire representatie van een decimaal getal te berekenen.

"""


def dec2bin(n):
    """
    Bepaal de binaire representatie van een getal uit het decimale talstelsel.

    Args:
        n (int): Een geheel, positief getal uit het decimale talstelsel.

    Returns:
        tuple: Binaire representatie van het gegeven getal.

    Examples:
        >> dec2bin(0)
        (0,)

        >> dec2bin(2)
        (1, 0)

        >> dec2bin(3)
        (1, 1)

        >> dec2bin(16)
        (1, 0, 0, 0, 0)
    """
    # Speciale case voor het getal 0
    if n == 0:
        return (0,)

    # Lijst om de binaire cijfers in omgekeerde volgorde op te slaan
    binaire_cijfers = []

    # Zet het getal om naar binaire representatie door steeds te delen door 2
    while n > 0:
        rest = n % 2  # Bereken de rest (0 of 1)
        binaire_cijfers.append(rest)  # Voeg de rest toe aan de lijst
        n = n // 2  # Deel n door 2 om verder te gaan met het volgende bit

    # Keer de lijst om, zodat de bits in de juiste volgorde staan, en geef deze als tuple terug
    return tuple(binaire_cijfers[::-1])


"""
7. Implementatie sqrt_heron
    Implementeer onderstaande functie om de vierkantswortel van een getal te berekenen.
"""


def sqrt_heron(n, tolerantie=0.00000001):
    """
    Bepaal de vierkantswortel van een gegeven waarde n met de methode van Heron: https://nl.wikipedia.org/wiki/Methode_van_Heron.
    De methode benadert de vierkantswortel en convergeert naar de daadwerkelijke waarde.
    Implementeer volgens onderstaande pseudocode:
        ONTVANG POSITIEF GETAL n EN GETAL t
        resultaat = n
        ZOLANG VERSCHIL resultaat^2 EN n GROTER DAN t:
            BEREKEN resultaat = (resultaat + n / resultaat) / 2

        GEEF resultaat TERUG

    Args:
        n (int): Een positief reëel getal.
        tolerantie (float): Het maximale verschil dat getolereerd wordt tussen n en oplossing x^2.

    Returns:
        float: De benaderde vierkantswortel
    """
    # Startwaarde van de benadering instellen als het gegeven getal zelf
    resultaat = n

    # Blijf herhalen totdat het kwadraat van de huidige benadering dichtbij genoeg is bij n
    while abs(resultaat * resultaat - n) > tolerantie:
        # Update de benadering volgens Heron's methode
        resultaat = (resultaat + n / resultaat) / 2

    # Geef de benaderde vierkantswortel terug
    return resultaat



"""
(Optioneel)
8. Implementatie meetkundige_rij
    Implementeer onderstaande functie om een meetkundige rij  genereren.

"""


def meetkundige_rij(start, factor, exponent):
    """
    Bereken een meetkundige rij (a_n = a_0 · r^n) gegeven een startgetal, een factor en een exponent.

    Args:
        start (int): Het getal waar de rij mee begint.
        factor (int): De factor van de rij.
        exponent (int): Het aantal termen in de rij.

    Returns:
        list of int: De meetkundige rij.
    """
    rij = []  # Lege lijst om de rij op te slaan

    # Genereer de rij door de formule a_n = a_0 * r^n toe te passen
    for n in range(exponent):
        rij.append(start * (factor ** n))  # Voeg elke berekende waarde toe aan de rij

    return rij



"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""


# import random


def __my_assert_args(function, args, expected_output, check_type=True):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.

    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output)} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"
    if type(expected_output) is float:
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def test_id():
    assert naam != "", "Je moet je naam nog invullen!"
    assert studentnummer != -1, "Je moet je studentnummer nog invullen!"
    assert klas != "", "Je moet je klas nog invullen!"


def test_ceil():
    testcases = [
        ((1.05,), 2),
        ((1.95,), 2),
        ((-1.05,), -1),
        ((-1.95,), -1),
        ((0.05,), 1),
        ((-0.05,), 0),
        ((0.0,), 0),
        ((1.0,), 1),
        ((-1.0,), -1)
    ]

    for case in testcases:
        __my_assert_args(ceil, case[0], case[1])


def test_is_even():
    testcases = [
        ((1,), False),
        ((2,), True),
        ((3,), False),
        ((4,), True),
        ((-1,), False),
        ((-2,), True)
    ]

    for case in testcases:
        __my_assert_args(is_even, case[0], case[1])


def test_is_odd():
    testcases = [
        ((1,), True),
        ((2,), False),
        ((3,), True),
        ((4,), False),
        ((-1,), True),
        ((-2,), False)
    ]

    for case in testcases:
        __my_assert_args(is_odd, case[0], case[1])


def test_nround():
    testcases = [
        ((1.05,), 1),
        ((1.95,), 2),
        ((-1.05,), -1),
        ((-1.95,), -2),
        ((0.05,), 0),
        ((-0.05,), 0),
        ((0.0,), 0),
        ((1.0,), 1),
        ((-1.0,), -1)
    ]

    for case in testcases:
        __my_assert_args(nround, case[0], case[1])


def test_dec2bin():
    testcases = [
        ((0,), (0,)),
        ((1,), (1,)),
        ((2,), (1, 0)),
        ((3,), (1, 1)),
        ((7,), (1, 1, 1)),
        ((8,), (1, 0, 0, 0)),
        ((255,), (1, 1, 1, 1, 1, 1, 1, 1)),
    ]

    for case in testcases:
        __my_assert_args(dec2bin, case[0], case[1])


def test_sqrt_heron():
    testcases = [
        ((2,), 1.41421356),
        ((4,), 2.0),
        ((9,), 3.0),
        ((15,), 3.8729833),
        ((16,), 4.0),
        ((25,), 5.0),
        ((26,), 5.0990195),
    ]

    for case in testcases:
        __my_assert_args(sqrt_heron, case[0], case[1])


def test_meetkundige_rij():
    testcases = [
        ((1, 2, 3), [1, 2, 4]),
        ((3, 4, 5), [3, 12, 48, 192, 768]),
        ((3, 5, 7), [3, 15, 75, 375, 1875, 9375, 46875]),
        ((5, 2, 5), [5, 10, 20, 40, 80]),
        ((5, 3, 5), [5, 15, 45, 135, 405]),
        ((10, 10, 10), [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000])
    ]

    for case in testcases:
        __my_assert_args(meetkundige_rij, case[0], case[1])
    return 1


def __main():
    """ Test alle functies. """
    # Noodzakelijk voor gekleurde tekst binnen een Windows terminal
    import os
    os.system("")

    try:
        print("\x1b[32m")
        test_id()

        test_ceil()
        print("Je functie ceil() werkt goed!")

        test_is_even()
        print("Je functie is_even() werkt goed!")

        test_is_odd()
        print("Je functie is_odd() werkt goed!")

        test_nround()
        print("Je functie nround() werkt goed!")

        test_dec2bin()
        print("Je functie dec2bin() werkt goed!")

        test_sqrt_heron()
        print("Je functie sqrt_heron() werkt goed!")

        test_meetkundige_rij()
        print("Je functie meetkundige_rij() werkt goed!")

    except AssertionError as ae:
        print("\x1b[31m")  # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)
        print("\x1b[0m")  # Reset tekstkleur


if __name__ == '__main__':
    __main()
