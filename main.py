# coding=utf-8
"""
DO do's:
    Get LEgale Züge und Aktualisierung des Brettes so bauen das die Funktion nur die neuen Felder zurückgibt
    aber nicht global äöndert --> Damit kann ich aus BestBot Funktion aufrufen und bekomme Figuren / Schachbrett
    Für mögliche Züge zurück
"""
import math
import operator

# -------------------------------------------- 0. imports ----------------------------------------------------
# import math
import time

import pygame

from Evaluation import get_legale_zuege, get_angriffs_maske, minimax, get_big_babba_move, \
    bewege_figur, get_weis_figuren_maske, get_schwarz_figuren_maske, get_koordinaten_format, is_king_in_schach, \
    is_schachmatt
from Evaluation import init_bot

# from Evaluation import bewege_bauer
from Evaluation import get_legale_bauern_zuege
from Evaluation import get_legale_laufer_zuge
from Evaluation import get_legale_pferd_zuge
from Evaluation import get_legale_turm_zuge
from Evaluation import get_legale_damen_zuge
from Evaluation import get_legale_bauern_zuege
from Evaluation import get_legale_konig_zuge

from Chessboard import update_board, init_this_thing

# from Evaluation import get_schwarz_figuren_maske
# from Evaluation import get_weis_figuren_maske


# -------------------------------------------- 1. Aufabu ----------------------------------------------------
# Ändern zu figuren_weiss_maske und schwarz
schachbrett = 0
figuren_weiss = 0
figuren_schwarz = 0

schachbrett_groesse_wurzel = 0

schachbrett_groesse = 0
biggest_single_bit_number = 0

ist_weis_am_zug = True
ist_zug_legal = True

# ---- Figuren ----

# 8 * 8 Daten:
figuren = {
    "w_ba": int("0000000000000000000000000000000000000000000000001111111100000000", 2),
    "w_la": int("0000000000000000000000000000000000000000000000000000000000100100", 2),
    "w_pf": int("0000000000000000000000000000000000000000000000000000000001000010", 2),
    "w_tu": int("0000000000000000000000000000000000000000000000000000000010000001", 2),
    "w_da": int("0000000000000000000000000000000000000000000000000000000000010000", 2),
    "w_ko": int("0000000000000000000000000000000000000000000000000000000000001000", 2),

    "s_ba": int("0000000011111111000000000000000000000000000000000000000000000000", 2),
    "s_la": int("0010010000000000000000000000000000000000000000000000000000000000", 2),
    "s_pf": int("0100001000000000000000000000000000000000000000000000000000000000", 2),
    "s_tu": int("1000000100000000000000000000000000000000000000000000000000000000", 2),
    "s_da": int("0001000000000000000000000000000000000000000000000000000000000000", 2),
    "s_ko": int("0000100000000000000000000000000000000000000000000000000000000000", 2)
}

# figuren = {
#     "w_ba": int("0000000000000000000000000000000000000000000000001111111100000000", 2),
#     "w_la": int("0000000000000000000000000000000010000000000000000000000000100000", 2),
#     "w_pf": int("0000000000000000000000000000000000000000000000000000000001000010", 2),
#     "w_tu": int("0000000000000000000000000000000000000000000000000000000010000001", 2),
#     "w_da": int("0000000000000000000000000000000000000000000000000000000000010000", 2),
#     "w_ko": int("0000000000000000000000000000000000000000000000000000000000001000", 2),
#
#     "s_ba": int("0000000011101111000000000000000000000000000000000000000000000000", 2),
#     "s_la": int("0010010000000000000000000000000000000000000000000000000000000000", 2),
#     "s_pf": int("0100001000000000000000000000000000000000000000000000000000000000", 2),
#     "s_tu": int("1000000100000000000000000000000000000000000000000000000000000000", 2),
#     "s_da": int("0001000000000000000000000000000000000000000000000000000000000000", 2),
#     "s_ko": int("0000100000000000000000000000000000000000000000000000000000000000", 2)
# }

# figuren = {
#     "w_ba": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "w_la": int("0000000000000000000000000000000000000000000000000000000000100100", 2),
#     "w_pf": int("0000000000000000000000000000000000000000000000000000000001000010", 2),
#     "w_tu": int("0000000000000000000000000000000000000000000000100000000000000000", 2),
#     "w_da": int("0000000000000000000000000000000000000000000000000000000000010000", 2),
#     "w_ko": int("0000000000000000000000000000000000000000000000000000000000001000", 2),
#
#     "s_ba": int("0000000000000000000000000000000000000110000000000000000000000000", 2),
#     "s_la": int("0010010000000000000000000000000000000000000000000000000000000000", 2),
#     "s_pf": int("0100001000000000000000000000000000000000000000000000000000000000", 2),
#     "s_tu": int("1000000100000000000000000000000000000000000000000000000000000000", 2),
#     "s_da": int("0001000000000000000000000000000000000000000000000000000000000000", 2),
#     "s_ko": int("0000100000000000000000000000000000000000000000000000000000000000", 2)
# }

# figuren = {
#     "w_ba": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "w_la": int("0000000000000000000100000000000000000000000000000000000000000000", 2),
#     "w_pf": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "w_tu": int("0000000000000000000000000000000000000000000000000000000000001100", 2),
#     "w_da": int("0000000000000000000000000000000000000000000000000000000001000000", 2),
#     "w_ko": int("0000000000000000000000000000000000000000000000000000000010000000", 2),
#
#     "s_ba": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "s_la": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "s_pf": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "s_tu": int("0010000100000000000000000000000000000000000000000000000000000000", 2),
#     "s_da": int("0000010000000000000000000000000000000000000000000000000000000000", 2),
#     "s_ko": int("0000001000000000000000000000000000000000000000000000000000000000", 2)
# }

# figuren = {
#     "w_ba": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "w_la": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "w_pf": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "w_tu": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "w_da": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "w_ko": int("0010000000000000000000000000000000000000000000000000000000000000", 2),
#
#     "s_ba": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "s_la": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "s_pf": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "s_tu": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "s_da": int("0000000000000000100000000000000000000000000000000000000000000000", 2),
#     "s_ko": int("0000000000000000000100000000000000000000000000000000000000000000", 2)
# }

# figuren = {
#     "w_ba": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "w_la": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "w_pf": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "w_tu": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "w_da": int("0000000000000000000000000100000000000000000000000000000000000000", 2),
#     "w_ko": int("0000000000000000000100000000000000000000000000000000000000000000", 2),
#
#     "s_ba": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "s_la": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "s_pf": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "s_tu": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "s_da": int("0000000000000000000000000000000000000000000000000000000000000000", 2),
#     "s_ko": int("1000000000000000000000000000000000000000000000000000000000000000", 2)
# }

# 0000000000000000000011111111110010100000000000000000000000000000
# figuren = {
#     "w_ba": int("0000000000000000000000000000000000000000000000000111111100000000", 2),
#     "w_la": int("0000000000000000000000000000000000000000000000000000000000100100", 2),
#     "w_pf": int("0000000000000000000000000010000000000000000000000000000001000000", 2),
#     "w_tu": int("0000000000000000000000000000000000000000000000000000000010000001", 2),
#     "w_da": int("0000000000000000000000000000000000000000000000000000000000010000", 2),
#     "w_ko": int("0000000000000000000000000000000000000000000000000000000000001000", 2),
#
#     "s_ba": int("0000000000000000000011111111110010100000000000000000000000000000", 2),
#     "s_la": int("0010010000000000000000000000000000000000000000000000000000000000", 2),
#     "s_pf": int("0100001000000000000000000000000000000000000000000000000000000000", 2),
#     "s_tu": int("1000000100000000000000000000000000000000000000000000000000000000", 2),
#     "s_da": int("0001000000000000000000000000000000000000000000000000000000000000", 2),
#     "s_ko": int("0000100000000000000000000000000000000000000000000000000000000000", 2)
# }

# # ------------------------------------- ENDGAME TESTING -------------------------------------
# figuren = {
#     "w_ba": int("0000000000000000000000001000000000000000000000000111111100000000", 2),
#     "w_la": int("0000000000000000000000000000000000000000000000000000000000100100", 2),
#     "w_pf": int("0000000000000000000000000010000000000000000000000000000001000010", 2),
#     "w_tu": int("0000000000000000000000000000000000000000000000000000000010000001", 2),
#     "w_da": int("0000000000000000000000000000000000000000000000000000000000010000", 2),
#     "w_ko": int("0000000000000000000000000000000000000000000000000000000000001000", 2),
#
#     "s_ba": int("0000000000000111101110000100000000000000000000000000000000000000", 2),
#     "s_la": int("0010010000000000000000000000000000000000000000000000000000000000", 2),
#     "s_pf": int("0100001000000000000000000000000000000000000000000000000000000000", 2),
#     "s_tu": int("1000000100000000000000000000000000000000000000000000000000000000", 2),
#     "s_da": int("0001000000000000000000000000000000000000000000000000000000000000", 2),
#     "s_ko": int("0000100000000000000000000000000000000000000000000000000000000000", 2)
# }

# ------------------------------------- ERRORS -------------------------------------


# Schleifen gehen keys durch --> Keys löschen wenn Figur nicht mehr auf Brett
weiss_keys = ["w_ba", "w_la", "w_pf", "w_tu", "w_da", "w_ko"]
schwarz_keys = ["s_ba", "s_la", "s_pf", "s_tu", "s_da", "s_ko"]

doppel_move_weis_maske = int("0000000000000000000000000000000000000000000000001111111100000000", 2)
doppel_move_schwarz_maske = int("0000000011111111000000000000000000000000000000000000000000000000", 2)


# -------------------------------------------- 1. a ----------------------------------------------------
def init_schachbrett():
    global schachbrett, figuren_schwarz, figuren_weiss, biggest_single_bit_number

    # Dic Figuren muss verändert werden
    schachbrett = get_weiss_figuren_maske() | get_schwarzz_figuren_maske()
    figuren_weiss = get_weiss_figuren_maske()
    figuren_schwarz = get_schwarzz_figuren_maske()

    biggest_single_bit_number = int(bin(2 ** (schachbrett_groesse - 1)), 2)


# -------------------------------------------- Figurenn Movement --------------------------------------------
def bewege_figur_ineffektiv(zug_start_pos, zug_ziel_pos, figuren, ist_weis_am_zug):
    if ist_weis_am_zug:
        # Wurde eine Figur genommen?
        if zug_ziel_pos & get_schwarzz_figuren_maske():
            # Figur wurde genommen --> Von jeder Geg Fig. bit dort löschen
            if figuren["s_ba"] & zug_ziel_pos:
                figuren["s_ba"] = zug_ziel_pos ^ figuren["s_ba"]
            elif figuren["s_la"] & zug_ziel_pos:
                figuren["s_la"] = zug_ziel_pos ^ figuren["s_la"]
            elif figuren["s_pf"] & zug_ziel_pos:
                figuren["s_pf"] = zug_ziel_pos ^ figuren["s_pf"]
            elif figuren["s_tu"] & zug_ziel_pos:
                figuren["s_tu"] = zug_ziel_pos ^ figuren["s_tu"]
            elif figuren["s_da"] & zug_ziel_pos:
                figuren["s_da"] = zug_ziel_pos ^ figuren["s_da"]
            elif figuren["s_ko"] & zug_ziel_pos:
                figuren["s_ko"] = zug_ziel_pos ^ figuren["s_ko"]

        # Zug Ziel Position aktualisieren
        if figuren["w_ba"] & zug_start_pos:
            temp = figuren["w_ba"] ^ zug_start_pos
            figuren["w_ba"] = temp | zug_ziel_pos
        elif figuren["w_la"] & zug_start_pos:
            temp = figuren["w_la"] ^ zug_start_pos
            figuren["w_la"] = temp | zug_ziel_pos
        elif figuren["w_pf"] & zug_start_pos:
            temp = figuren["w_pf"] ^ zug_start_pos
            figuren["w_pf"] = temp | zug_ziel_pos
        elif figuren["w_tu"] & zug_start_pos:
            temp = figuren["w_tu"] ^ zug_start_pos
            figuren["w_tu"] = temp | zug_ziel_pos
        elif figuren["w_da"] & zug_start_pos:
            temp = figuren["w_da"] ^ zug_start_pos
            figuren["w_da"] = temp | zug_ziel_pos
        elif figuren["w_ko"] & zug_start_pos:
            temp = figuren["w_ko"] ^ zug_start_pos
            figuren["w_ko"] = temp | zug_ziel_pos
    else:
        if zug_ziel_pos & get_weiss_figuren_maske():
            # Figur wurde genommen --> Von jeder Geg Fig. bit dort löschen
            if figuren["w_ba"] & zug_ziel_pos:
                figuren["w_ba"] = zug_ziel_pos ^ figuren["w_ba"]
            elif figuren["w_la"] & zug_ziel_pos:
                figuren["w_la"] = zug_ziel_pos ^ figuren["w_la"]
            elif figuren["w_pf"] & zug_ziel_pos:
                figuren["w_pf"] = zug_ziel_pos ^ figuren["w_pf"]
            elif figuren["w_tu"] & zug_ziel_pos:
                figuren["w_tu"] = zug_ziel_pos ^ figuren["w_tu"]
            elif figuren["w_da"] & zug_ziel_pos:
                figuren["w_da"] = zug_ziel_pos ^ figuren["w_da"]
            elif figuren["w_ko"] & zug_ziel_pos:
                figuren["w_ko"] = zug_ziel_pos ^ figuren["w_ko"]

        # Zug Ziel Position aktualisieren
        if figuren["s_ba"] & zug_start_pos:
            temp = figuren["s_ba"] ^ zug_start_pos
            figuren["s_ba"] = temp | zug_ziel_pos
        elif figuren["s_la"] & zug_start_pos:
            temp = figuren["s_la"] ^ zug_start_pos
            figuren["s_la"] = temp | zug_ziel_pos
        elif figuren["s_pf"] & zug_start_pos:
            temp = figuren["s_pf"] ^ zug_start_pos
            figuren["s_pf"] = temp | zug_ziel_pos
        elif figuren["s_tu"] & zug_start_pos:
            temp = figuren["s_tu"] ^ zug_start_pos
            figuren["s_tu"] = temp | zug_ziel_pos
        elif figuren["s_da"] & zug_start_pos:
            temp = figuren["s_da"] ^ zug_start_pos
            figuren["s_da"] = temp | zug_ziel_pos
        elif figuren["s_ko"] & zug_start_pos:
            temp = figuren["s_ko"] ^ zug_start_pos
            figuren["s_ko"] = temp | zug_ziel_pos

    return figuren


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
        figuren_schwarz = get_schwarzz_figuren_maske()
        figuren_weiss = get_weiss_figuren_maske()

        # Turns ändern
        if ist_weis_am_zug:
            ist_weis_am_zug = False
        else:
            ist_weis_am_zug = True


def get_schwarzz_figuren_maske():
    schwarz_figuren_maske = 0

    for key in schwarz_keys:
        schwarz_figuren_maske = schwarz_figuren_maske | figuren.get(key)

    return schwarz_figuren_maske


def get_weiss_figuren_maske():
    weiss_figuren_maske = 0

    for key in weiss_keys:
        weiss_figuren_maske = weiss_figuren_maske | figuren.get(key)

    return weiss_figuren_maske


def aktualisiere_figuren(new_figuren):
    global figuren, schachbrett, ist_weis_am_zug

    figuren = dict(new_figuren)
    schachbrett = get_weiss_figuren_maske() | get_schwarzz_figuren_maske()
    ist_weis_am_zug = not ist_weis_am_zug


# -------------------------------------- Bewegungs Hilfsfunktion ------------------------------------------
def get_bit_wert_von_input(figur_auswahl):  # string "a3" --> "b3"  || a->h & 1->8
    position_bit_nummber = biggest_single_bit_number
    auswahl_alphabet_nummer = ord(figur_auswahl[0]) - 96  # a = 1, b = 2...
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
    bit_number = int(bin(2 ** (schachbrett_groesse - 1)), 2)
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
        bit_number = int(bin(2 ** (schachbrett_groesse - 1)), 2)
        for i in range(schachbrett_groesse):
            if figuren[figur] & bit_number:
                schachbrett_darstellung_mit_bezeichnungen[i] = figur
            bit_number = bit_number >> 1

    for i in range(0, schachbrett_groesse, schachbrett_groesse_wurzel):
        print(schachbrett_darstellung_mit_bezeichnungen[i: i + schachbrett_groesse_wurzel], end="")
        if i % schachbrett_groesse_wurzel == 0:
            print()


def print_custom_schachbrett_mit_bezeichnungen(figuren):
    schachbrett_darstellung_mit_bezeichnungen = [" 0  " for x in range(schachbrett_groesse)]

    for figur in figuren:
        bit_number = int(bin(2 ** (schachbrett_groesse - 1)), 2)
        for i in range(schachbrett_groesse):
            if figuren[figur] & bit_number:
                schachbrett_darstellung_mit_bezeichnungen[i] = figur
            bit_number = bit_number >> 1

    for i in range(0, schachbrett_groesse, schachbrett_groesse_wurzel):
        print(schachbrett_darstellung_mit_bezeichnungen[i: i + schachbrett_groesse_wurzel], end="")
        if i % schachbrett_groesse_wurzel == 0:
            print()


def get_legale_zug_darstellung(zug_formatted):
    zug_maske = 0

    for zug in zug_formatted:
        zug_maske = zug_maske | zug[1]

    return zug_maske


# -------------------------------------------- Main Funktion ----------------------------------------------------
if __name__ == '__main__':
    testing = 0
    set_schachbrett_groesse(64, 8)
    print("Schachfeld:")
    init_schachbrett()
    win = 0
    init_bot(schachbrett_groesse, schachbrett_groesse_wurzel, figuren)
    zug_counter = 0
    time_adder = 0

    tiefen_berechung = 1

    # ---------------------------------------------------------- BOTOOOO START ----------------------------------------------------------
    if testing == 0:
        # Chessboard represnation
        pygame.init()
        init_this_thing()
        pygame.time.Clock().tick(10)  # Clock to control the frame rate

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
       # while True:
            zug_counter = zug_counter + 1
            update_board(figuren)

            # print_schachbrett()
            # print()
            # print_schachbrett_mit_bezeichnungen()

            # Unterbricht wenn MATT
            legal_zuege = get_legale_zuege(dict(figuren), ist_weis_am_zug)
            if not legal_zuege:
                win = 1
                break

            start_time = time.time()
            causeImmaBeast = get_big_babba_move(figuren, ist_weis_am_zug, tiefen_berechung)
            end_time = time.time()

            # print()
            # print("+-+-+-+-+-+-+-+-+-+-+-+-+-+ Max Killer Bot +-+-+-+-+-+-+-+-+-+-+-+-+-+")

            try:
                temp_figuren = bewege_figur(causeImmaBeast[0][0], causeImmaBeast[0][1], dict(figuren), ist_weis_am_zug,
                                            causeImmaBeast[0][3])
            except:
                print("An exception occurred")
                break

            # legale_zuege_print_format = get_legale_zug_darstellung(legal_zuege)
            koordinaten = get_koordinaten_format(figuren, temp_figuren, ist_weis_am_zug)
            time_adder += round(end_time - start_time, 3)
            print("Zug : ", zug_counter, " Zug-Wert: ", causeImmaBeast[1], f"{koordinaten[0]}{koordinaten[1]} --> {koordinaten[2]}{koordinaten[3]}",  "|||", round(end_time - start_time, 3), " Sekunden")
            # print()
            # print("Legale Züge von", " Weis: " if ist_weis_am_zug  else " Schwarz")
            # print_custom_schachbrett(legale_zuege_print_format)

            # if not ist_weis_am_zug:
            #     print("-------------------------- Weiß Am Zug --------------------------")
            # else:
            #     print("-------------------------- Schwarz Am Zug --------------------------")

            # Winning/Draw Conditions
            if not figuren["w_ko"] or not legal_zuege:
                print()
                print("*********** Schwarz gewinnt! *********** ")
                update_board(figuren)
                time.sleep(60)
                break

            if not figuren["s_ko"] or not legal_zuege:
                print()
                print("*********** Weiß gewinnt! *********** ")
                update_board(figuren)
                time.sleep(60)
                break

            if bin(get_weis_figuren_maske(figuren)).count("1") == 1 and bin(get_schwarz_figuren_maske(figuren)).count(
                    "1") == 1:
                print()
                print("***********  Draw *********** ")
                update_board(figuren)
                time.sleep(60)
                break

            aktualisiere_figuren(temp_figuren)

        if win == 1:
            if ist_weis_am_zug:
                print("*********** Schwarz gewinnt! *********** ")
                update_board(figuren)
                print("Durchsch. Zug Zeit: ", round(time_adder / zug_counter, 3) ," Sek.")
                time.sleep(60)
            else:
                print("*********** Weiß gewinnt! *********** ")
                update_board(figuren)
                print("Durchsch. Zug Zeit: ", round(time_adder / zug_counter, 3) ," Sek.")
                time.sleep(60)

    print_schachbrett_mit_bezeichnungen()

    # ---------------------------------------------------------- BOTOOOO ENDE ----------------------------------------------------------

    if testing == 1:
        print_schachbrett()
        print_schachbrett_mit_bezeichnungen()

        start_time2 = time.time()
        legal_zuege = get_legale_zuege(figuren, ist_weis_am_zug)
        end_time2 = time.time()

        print("+-+-+-+-+-+-+-+-+-+-+-+- Erlaubte Züge +-+-+-+-+-+-+-+-+-+-+-+-")
        print("Legale Moves: ", legal_zuege)
        print()
        legale_zuege_print_format = get_legale_zug_darstellung(legal_zuege)
        print_custom_schachbrett(legale_zuege_print_format)

        print("+-+-+-+-+-+-+-+-+-+-+-+- Testing +-+-+-+-+-+-+-+-+-+-+-+-")

        # best_move = get_big_babba_move(figuren, ist_weis_am_zug, 3)

        # da = get_legale_damen_zuge(figuren["w_da"], figuren, ist_weis_am_zug)
        # fig_move = get_legale_damen_zuge(figuren["w_da"], figuren, ist_weis_am_zug)
        while figuren["w_la"] > 0:
            fig_move = get_legale_laufer_zuge(figuren["w_la"], figuren, ist_weis_am_zug)

            if fig_move.bit_length() > 64:
                print("Illegal Move")
                print(bin(fig_move), fig_move.bit_length())
                print_custom_schachbrett(fig_move)

            figuren["w_la"] = figuren["w_la"] >> 1

        # figuren = bewege_figur(best_move[0][0], best_move[0][1], dict(figuren), ist_weis_am_zug, best_move[0][3])
        # print_custom_schachbrett_mit_bezeichnungen(figuren)

        # print("LA Züge::::::::::::::::")
        # print_custom_schachbrett(la)

    if testing == 2:
        print_schachbrett()
        legal_zuege = get_legale_zuege(figuren, not ist_weis_am_zug)
        print(legal_zuege)

    if testing == 3:
        pygame.init()

        init_this_thing()
        tt = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            update_board(figuren)
            if tt == 0:
                temp_figuren = bewege_figur(int("0000000000000000000000000000000000000000000000001111111100000000", 2), int("0000000000000000000000000000000000000010000000001111110100000000", 2), figuren, ist_weis_am_zug, "w_ba")

            tt = tt + 1
            aktualisiere_figuren(temp_figuren)
            print_schachbrett_mit_bezeichnungen()
            pygame.time.delay(100)  # Delay to slow down the loop for demonstration

    if testing == 4:
        print()
        print_schachbrett_mit_bezeichnungen()
        lz = get_legale_zuege(figuren, False)
        print("get_legale_zuege: ", lz)

        lbz = 0
        for i in range(64):
            iterator = 1 << i
            if figuren["s_ba"] & iterator:
                lbz = lbz | get_legale_bauern_zuege(iterator, figuren, False)

        lbzWrong = get_legale_bauern_zuege(int("0000000000000000000100000000000000000000000000000000000000000000", 2), figuren, False)

        print("Angeblich Legal Moves: ")
        print_custom_schachbrett(lbz)
        print("--- LBZ WRONG --- ")
        print_custom_schachbrett(lbzWrong)
        print()
        # pygame.quit()

    if testing == 5:
        # Player VS Bot
        pygame.init()
        init_this_thing()
        pygame.time.Clock().tick(10)  # Clock to control the frame rate
        player_farbe = True  # True : Weiss | False : Schwarz

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # while True:
            zug_counter = zug_counter + 1
            update_board(figuren)

            # Unterbricht wenn MATT
            legal_zuege = get_legale_zuege(dict(figuren), ist_weis_am_zug)
            if not legal_zuege:
                win = 1
                break

            if ist_weis_am_zug != player_farbe:
                start_time = time.time()
                causeImmaBeast = get_big_babba_move(figuren, ist_weis_am_zug, tiefen_berechung)
                end_time = time.time()

            # print()
            # print("+-+-+-+-+-+-+-+-+-+-+-+-+-+ Max Killer Bot +-+-+-+-+-+-+-+-+-+-+-+-+-+")

                try:
                    temp_figuren = bewege_figur(causeImmaBeast[0][0], causeImmaBeast[0][1], dict(figuren), ist_weis_am_zug,
                                            causeImmaBeast[0][3])
                except:
                    print("An exception occurred")
                    break

            # legale_zuege_print_format = get_legale_zug_darstellung(legal_zuege)
                koordinaten = get_koordinaten_format(figuren, temp_figuren, ist_weis_am_zug)
                time_adder += round(end_time - start_time, 3)
                print("Zug : ", zug_counter, " Zug-Wert: ", causeImmaBeast[1], f"{koordinaten[0]}{koordinaten[1]} --> {koordinaten[2]}{koordinaten[3]}", "|||",
                round(end_time - start_time, 3), " Sekunden")
            # print()
            # print("Legale Züge von", " Weis: " if ist_weis_am_zug  else " Schwarz")
            # print_custom_schachbrett(legale_zuege_print_format)

            # if not ist_weis_am_zug:
            #     print("-------------------------- Weiß Am Zug --------------------------")
            # else:
            #     print("-------------------------- Schwarz Am Zug --------------------------")
            if ist_weis_am_zug == player_farbe:
                print("-------------------------- Zug Eingabe --------------------------")
                zug = get_zug_eingabe()
                zug_start = get_bit_wert_von_input(zug[0])
                zug_ziel = get_bit_wert_von_input(zug[1])

                temp_figuren = bewege_figur_ineffektiv(zug_start, zug_ziel, figuren, ist_weis_am_zug)

            # Winning/Draw Conditions
            if not figuren["w_ko"] or not legal_zuege:
                print()
                print("*********** Schwarz gewinnt! *********** ")
                update_board(figuren)
                time.sleep(60)
                break

            if not figuren["s_ko"] or not legal_zuege:
                print()
                print("*********** Weiß gewinnt! *********** ")
                update_board(figuren)
                time.sleep(60)
                break

            if bin(get_weis_figuren_maske(figuren)).count("1") == 1 and bin(get_schwarz_figuren_maske(figuren)).count(
                    "1") == 1:
                print()
                print("***********  Draw *********** ")
                update_board(figuren)
                time.sleep(60)
                break

            aktualisiere_figuren(temp_figuren)

        if win == 1:
            if ist_weis_am_zug:
                print("*********** Schwarz gewinnt! *********** ")
                update_board(figuren)
                print("Durchsch. Zug Zeit: ", round(time_adder / zug_counter, 3), " Sek.")
                time.sleep(60)
            else:
                print("*********** Weiß gewinnt! *********** ")
                update_board(figuren)
                print("Durchsch. Zug Zeit: ", round(time_adder / zug_counter, 3), " Sek.")
                time.sleep(60)
