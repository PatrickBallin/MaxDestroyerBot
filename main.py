"""
DO do's:
    Get LEgale Züge und Aktualisierung des Brettes so bauen das die Funktion nur die neuen Felder zurückgibt
    aber nicht global äöndert --> Damit kann ich aus BestBot Funktion aufrufen und bekomme Figuren / Schachbrett
    Für mögliche Züge zurück
"""
import operator

# -------------------------------------------- 0. imports ----------------------------------------------------
# import math
import time

from Evaluation import beast_get_best_move
from Evaluation import init_bot

from Evaluation import get_legale_laufer_zuge
from Evaluation import get_legale_turm_zuge


# -------------------------------------------- 1. Aufabu ----------------------------------------------------
# Ändern zu figuren_weiss_maske und schwarz
schachbrett = 0
figuren_weiss = 0
figuren_schwarz = 0

schachbrett_groesse = 0
schachbrett_groesse_wurzel = 0

biggest_single_bit_number = 0

ist_weis_am_zug = True
ist_zug_legal = True


# ---- Figuren ----

# 8 * 8 Daten:
figuren = {
    "w_ba": int("0000000000000000000000000000000010000000000000000000000000000000", 2),
    # "w_ko": int("0000000000000000000000000000000000000000000000000000000000001000", 2),
    "w_la": int("0000000000000000000000000000000000000000000000100000000000000000", 2),
    "w_tu": int("0000000000000000000000000000000000000100000000000000000000000000", 2),

    "s_ba": int("0000000000000000000000000000000000110000000000000000000000000000", 2),
    # "s_ko": int("0000100000000000000000000000000000000000000000000000000000000000", 2)
    "s_la": int("0000001000000000000000000000000000000000000000000000000000000000", 2),
    "s_tu": int("0000000000000000001000000000000000000000000000000000000000000000", 2),
}


# # 4 * 4 Daten:
# figuren = {
#     "w_ba": int("0000000000001111", 2),
#     "w_ko": int("0000000000010000", 2),
#     # weiss_pferde = int("101000000", 2)
#
#     "s_ba": int("1111000000000000", 2),
#     "s_ko": int("0000100000000000", 2)
#     # schwarz_pferde = int("000000101", 2)
# }

# Schleifen gehen keys durch --> Keys löschen wenn Figur nicht mehr auf Brett
weiss_keys = ["w_ba", "w_la", "w_tu"]  # "w_ko"
schwarz_keys = ["s_ba", "s_la", "s_tu"]  # "s_ko"

doppel_move_weis_maske = figuren.get("w_ba")
doppel_move_schwarz_maske = figuren.get("s_ba")


# -------------------------------------------- 1. a ----------------------------------------------------
def init_schachbrett():
    global schachbrett, figuren_schwarz, figuren_weiss, biggest_single_bit_number

    # Dic Figuren muss verändert werden
    schachbrett = get_weiss_figuren_maske() | get_schwarz_figuren_maske()
    figuren_weiss = get_weiss_figuren_maske()
    figuren_schwarz = get_schwarz_figuren_maske()

    biggest_single_bit_number = int(bin(2**(schachbrett_groesse - 1)), 2)


# -------------------------------------------- Figurenn Movement --------------------------------------------
def bewege_figur(zug_auswahl, zug_ziel):
    figuren_name = ""

    # Ist es ein Feld mit Figur darauf
    if schachbrett & zug_auswahl != 0:
        # Um welche Figur von "mir" handelt es sich (Eine Figur die weis/schwarz bewegen darf)
        if ist_weis_am_zug:
            for key in weiss_keys:
                bit_wert_figur = figuren.get(key)

                if bit_wert_figur & zug_auswahl != 0:
                    # dann ist der Key die Figur die ausgewählt wurde
                    figuren_name = key

        # schwarz ist am zug
        else:
            for key in schwarz_keys:
                bit_wert_figur = figuren.get(key)

                if bit_wert_figur & zug_auswahl != 0:
                    # dann ist der Key die Figur die ausgewählt wurde
                    figuren_name = key

        if figuren_name == "":
            # keine legale Figur ausgewählt
            return False
    else:
        # Kein legaler Zug
        return False

    # Legale Auswhal an Figur
    # Bewege Figur sofern legaler Zug
    if "_ba" in figuren_name:
        ziehe_figur(zug_auswahl, zug_ziel, "_ba")
    if "_ko" in figuren_name:
        ziehe_figur(zug_auswahl, zug_ziel, "_ko")


def ziehe_figur(zug_auswahl, zug_ziel, figurname):
    if ist_weis_am_zug:
        # wurde Figur genommen?
        if zug_ziel & get_schwarz_figuren_maske() != 0:
            for key in schwarz_keys:
                if figuren[key] & zug_ziel != 0:
                    # Dann ist key Figur die genommen wurde
                    # lösche Gegner Figur
                    figuren[key] = figuren.get(key) ^ zug_ziel

        # aktualisiere gezogene Figur
        temp = figuren.get("w" + figurname) ^ zug_auswahl
        figuren["w" + figurname] = temp | zug_ziel
    else:
        # schwarzer zug
        # wurde Figur genommen?
        if zug_ziel & get_weiss_figuren_maske() != 0:
            for key in weiss_keys:
                if figuren[key] & zug_ziel != 0:
                    # Dann ist key Figur die genommen wurde
                    # lösche Gegner Figur
                    figuren[key] = figuren.get(key) ^ zug_ziel

        # aktualisiere gezogene Figur
        temp = figuren.get("s" + figurname) ^ zug_auswahl
        figuren["s" + figurname] = temp | zug_ziel


# -------------------------------------------- Figuren Legale Züge --------------------------------------------
# TODO: Kann man löschen
def get_legale_bauern_zuege(zug_auswahl):
    legale_bauern_zuge = 0

    # Möglichkeiten an Bauern züge
    if ist_weis_am_zug:
        # normal fall weis Bauer bewegt sich um eins nach vorne
        # Steht etwas auf diesem Feld
        if (zug_auswahl << schachbrett_groesse_wurzel) & schachbrett == 0:
            legale_bauern_zuge = zug_auswahl << schachbrett_groesse_wurzel

        # Doppel Sprung
        if (zug_auswahl << (schachbrett_groesse_wurzel * 2) | (zug_auswahl << schachbrett_groesse_wurzel)) & schachbrett == 0:
            # falls der Bauer am Anfang steht
            if zug_auswahl & doppel_move_weis_maske:
                temp = zug_auswahl << (schachbrett_groesse_wurzel * 2)
                legale_bauern_zuge = legale_bauern_zuge | temp

        # Attack Move
        gegnerische_figuren = get_schwarz_figuren_maske()

        # Fall Angriff: Steht diagonal links ein Gegner dann füge zuege hinzu
        angriff_diagonal_links = zug_auswahl << (schachbrett_groesse_wurzel + 1)

        # TODO: Übers BRett schlagen ist möglich aber nicht im Bot
        # Steht eine Gengerische Figur links diagonal
        if angriff_diagonal_links & gegnerische_figuren != 0:
            legale_bauern_zuge = legale_bauern_zuge | angriff_diagonal_links

        # Fall Angriff: Steht diagonal rechts ein Gegner dann füge zuege hinzu
        angriff_diagonal_rechts = zug_auswahl << (schachbrett_groesse_wurzel - 1)

        if angriff_diagonal_rechts & gegnerische_figuren != 0:
            legale_bauern_zuge = legale_bauern_zuge | angriff_diagonal_rechts

    else:
        # normal fall schwarz Bauer bewegt sich um eins nach vorne
        # Steht etwas auf diesem Feld
        if (zug_auswahl >> schachbrett_groesse_wurzel) & schachbrett == 0:
            legale_bauern_zuge = zug_auswahl >> schachbrett_groesse_wurzel

        # Doppel Sprung
        if ((zug_auswahl >> (schachbrett_groesse_wurzel * 2)) | zug_auswahl >> schachbrett_groesse_wurzel) & schachbrett == 0:
            # falls der Bauer am Anfang steht
            if zug_auswahl & doppel_move_schwarz_maske:
                temp = zug_auswahl >> (schachbrett_groesse_wurzel * 2)
                legale_bauern_zuge = legale_bauern_zuge | temp

        # Attack Move
        gegnerische_figuren = get_weiss_figuren_maske()

        # Fall Angriff: Steht diagonal links ein Gegner dann füge zuege hinzu
        angriff_diagonal_links = zug_auswahl >> (schachbrett_groesse_wurzel + 1)

        # Steht eine Gengerische Figur links diagonal

        if angriff_diagonal_links & gegnerische_figuren != 0:
            legale_bauern_zuge = legale_bauern_zuge | angriff_diagonal_links

        # Fall Angriff: Steht diagonal rechts ein Gegner dann füge zuege hinzu
        angriff_diagonal_rechts = zug_auswahl >> (schachbrett_groesse_wurzel - 1)

        if angriff_diagonal_rechts & gegnerische_figuren != 0:
            legale_bauern_zuge = legale_bauern_zuge | angriff_diagonal_rechts

    return legale_bauern_zuge


# -------------------------------------- Daten Funktionen --------------------------------------------------
def aktualisiere_brett_und_zug():
    global schachbrett, ist_weis_am_zug
    brettstand = 0

    # Alle FigurenWerte OR mit 0
    for figur in figuren:
        brettstand = brettstand | figuren.get(figur)
        # Neuer Brett stand

    # Wurde ein Zug gemacht
    if schachbrett ^ brettstand != 0:
        ist_zug_legal = True
    else:
        ist_zug_legal = False

    if ist_zug_legal:
        # Brett aktualisieren
        global figuren_weiss, figuren_schwarz
        schachbrett = brettstand

        # Figuren aktualisiern
        figuren_schwarz = get_schwarz_figuren_maske()
        figuren_weiss = get_weiss_figuren_maske()

        # Turns ändern
        if ist_weis_am_zug:
            ist_weis_am_zug = False
        else:
            ist_weis_am_zug = True


def get_schwarz_figuren_maske():
    schwarz_figuren_maske = 0

    for key in schwarz_keys:
        schwarz_figuren_maske = schwarz_figuren_maske | figuren.get(key)

    return schwarz_figuren_maske


def get_weiss_figuren_maske():
    weiss_figuren_maske = 0

    for key in weiss_keys:
        weiss_figuren_maske = weiss_figuren_maske | figuren.get(key)

    return weiss_figuren_maske


# -------------------------------------- Bewegungs Hilfsfunktion ------------------------------------------
def get_bit_wert_von_input(figur_auswahl):   # string "a3" --> "b3"  || a->h & 1->8
    position_bit_nummber = biggest_single_bit_number
    auswahl_alphabet_nummer = ord(figur_auswahl[0]) - 96    # a = 1, b = 2...
    auswahl_feldnummber = figur_auswahl[1]

    # Fall b2
    # Buchstaben shift: alphabet nummer - 1 --> b = 2 - 1 => 1 shift
    buchstaben_shifts = int(auswahl_alphabet_nummer) - 1
    position_bit_nummber = position_bit_nummber >> buchstaben_shifts

    # Nummern shift: brettgroese_wurzel * (brettgroese_wurzel - Zahl) || 3 * (3 - 2) => 3 shifts
    nummern_shifts = schachbrett_groesse_wurzel * (schachbrett_groesse_wurzel - int(auswahl_feldnummber))
    position_bit_nummber = position_bit_nummber >> nummern_shifts

    return position_bit_nummber


# -----------------------------------Spiel Setter und Getter ----------------------------------------------
def set_schachbrett_groesse(anzahl_felder, wurzel_anzahl_felder):
    global schachbrett_groesse, schachbrett_groesse_wurzel

    schachbrett_groesse = int(anzahl_felder)
    schachbrett_groesse_wurzel = int(wurzel_anzahl_felder)


def get_schachbrett_groesse():
    return schachbrett_groesse


def get_schachbrett_groesse_wurzel():
    return schachbrett_groesse_wurzel


def get_schachbrett():
    return schachbrett


# -------------------------------------------- Eingabe ----------------------------------------------------
def get_zug_eingabe():
    if ist_weis_am_zug:
        print("-------------------------- Weiss Am Zug --------------------------")
    else:
        print("-------------------------- Schwarz Am Zug --------------------------")

    figur_ausgewaehlt = input("Figur auswählen:")
    figur_zielposition = input("Figur Zielposition:")

    return [figur_ausgewaehlt, figur_zielposition]


# -------------------------------------------- Ausgabe ----------------------------------------------------
def print_schachbrett():
    bit_number = int(bin(2**(schachbrett_groesse - 1)), 2)
    schachbrett_darstellung = []

    while bit_number > 0:
        if (schachbrett & bit_number) > 0:
            schachbrett_darstellung.append(1)
        else:
            schachbrett_darstellung.append(0)
        bit_number = bit_number >> 1

    for i in range(0, schachbrett_groesse, schachbrett_groesse_wurzel):
        print(schachbrett_darstellung[i: i + schachbrett_groesse_wurzel], end="")
        if i % schachbrett_groesse_wurzel == 0:
            print()


def print_custom_schachbrett(darstellung):
    bit_number = biggest_single_bit_number
    schachbrett_darstellung = []

    while bit_number > 0:
        if (darstellung & bit_number) > 0:
            schachbrett_darstellung.append(1)
        else:
            schachbrett_darstellung.append(0)
        bit_number = bit_number >> 1

    for i in range(0, schachbrett_groesse, schachbrett_groesse_wurzel):
        print(schachbrett_darstellung[i: i + schachbrett_groesse_wurzel], end="")
        if i % schachbrett_groesse_wurzel == 0:
            print()


def print_schachbrett_mit_bezeichnungen():
    schachbrett_darstellung_mit_bezeichnungen = [" 0  " for x in range(schachbrett_groesse)]

    for figur in figuren:
        bit_number = int(bin(2**(schachbrett_groesse - 1)), 2)
        for i in range(schachbrett_groesse):
            if figuren[figur] & bit_number:
                schachbrett_darstellung_mit_bezeichnungen[i] = figur
            bit_number = bit_number >> 1

    for i in range(0, schachbrett_groesse, schachbrett_groesse_wurzel):
        print(schachbrett_darstellung_mit_bezeichnungen[i: i + schachbrett_groesse_wurzel], end="")
        if i % schachbrett_groesse_wurzel == 0:
            print()


# -------------------------------------------- Main Funktion ----------------------------------------------------
if __name__ == '__main__':
    set_schachbrett_groesse(64, 8)
    print("Schachfeld:")
    init_schachbrett()
    init_bot(schachbrett_groesse, schachbrett_groesse_wurzel, figuren)

    # while True:
    print_schachbrett()
    print()
    print_schachbrett_mit_bezeichnungen()


        # start_time = time.time()
        #
        # # Zeigt den Besten move an
        # beast_get_best_move(figuren, ist_weis_am_zug, zug_tiefe=3)
        # end_time = time.time()
        #
        #
        # print("Calculation Time: ", round(end_time - start_time, 3), " Sekunden")
        # zug = get_zug_eingabe()
        # bit_zug_auswahl = get_bit_wert_von_input(zug[0])
        # bit_zug_ziel = get_bit_wert_von_input(zug[1])
        #
        # bewege_figur(bit_zug_auswahl, bit_zug_ziel)
        # aktualisiere_brett_und_zug()

        # --------------------------- TEST ---------------------------
        # temp = get_legale_laufer_zuge(figuren.get("w_la"), figuren, ist_weis_am_zug)

    tampo = get_legale_turm_zuge(figuren.get("s_tu"), figuren, False)
    # tampo = get_legale_laufer_zuge(figuren.get("w_la"), figuren, True)

    print("Erlaubte Züge::::::::::::::::")
    print_custom_schachbrett(tampo)
    print("Ergebniss", bin(tampo))
