# coding=utf-8
"""

1. Erstelle Generelle Brett Gewichtung (Mitte High Rand Low)
2. Erstelle Figuren Gewichtung auf Brett (Bauern am besten in letzter Reihe)

3. Erstelle Figuren Gewichte = Bauer 1, Pferd 3, Läufer 3....

4. Evaluierungs Funktion:
    Alle Figuren * Figuren Wert * Genereller Brett Gewichtung * Figuren gewicht auf Brett

5. Iterriere jeden möglichen Zug von jeder Figur:
    berechne Evaluierungs Funktions Wert

6. Mache den Zug mit dem höchsten Evaluierungs Wert


----------------------------- Detail -----------------------------
1. Static ? (masken mit Werten dahinter)
2. Static ? (masken mit Werten dahinter)

3. dictonary mit Werten Für Figuren Keys

4. Funktion()
    Input: Figur
    Berechung:
    Output: Evaluierungs Zahl

5. Funktion()
    Input: Figuren aus Main.py, Funktionen aus Main.py (Erlaubte Züge)
    Berechung:
    Output: Zug mit höchstem Wert

6. Rückgabe des Zuges an Aufrufenden Code


----------------------------- Ablauf -----------------------------
Evaluiere_schachbrett(schachbrett, Figuren):
    Gesamtwert_weiss = 0
    Gesamtwert_schwarz = 0

    1. Iterriere Über jede Figur:

        A: Ist die Figur weiss:
            Was ist es Für eine Figur:
            (Bsp Bauer): Multipliziere Bauern mit Figuren_Bauernwert 1 UND Allen gewichtungen
                Addiere Summe zu Gesamtwert_weiss


        B: Ist die Figur Schwarz:
            Mache wie in A

    return gesamtwert_weiss & Gesamtwert_schwarz ( !!! Bester Zug ist mit der Größten Differnez !!!)

Berechne_Alle_Möglichen_zÜge():
    Best Move = 0
    1. Iterriere Über Jede EIGENE Figur
        !!! Hier Müsste eine Art Binär Baum abgeklappert Werden (Jeder Mögliche Zug der Auf Zug folgt) !!!

        A: Bekomme Alle Legalen Züge von dieser Figur
        B: Iterriere Über jeden LEgalen Zug
            Berechne schachbrett & Figuren Für diesen Zug
            Rufe evaluierung() auf
            Speichere Best Move, wenn größer als Bestmove


+-+-+-+-+-+-+-++-+-+-+-+-+-+-+ FINISH BOT PLAN +-+-+-+-+-+-+-++-+-+-+-+-+-+-+

1. Ziel: Alpha Beta pruning Function (minimax)
    - Input: figuren, is_weiss_am_zug, tiefe
    - output Evaluation

2: get_legale_züge():
    - Input: figuren
    - process: is_zug_legal() --> get_angriffs_maske () !!= angruifsmaske_gegner & könig != 0 sein
    - output: [[a, b], [a, b], [00001, 10000]...] evtl [[a, b, isCapture, Figurenname]]
2a: Optimierung: sort_legale_zuege_nach_starken_zuegen():
    - Input: Legale_zuege_array[]
    - Zuege wo isCapture == True nach vorne im Array


##### PSEUDO #####

def minimax (figuren, tiefe, is_weiss_am_zug):
    legale_zuege = get_legale_zuege()

    if tiefe == 0 or isEmpty(legale_zuege):
        return evaluerie_position(figuren)

    if is_weiss_am_zug:
        maxEvaluierung = -10**17
        for zug in legale_zuege:
            temp_figuren = bewge_figur(zug[0], zug[1], figuren, is_weiss_am_zug, zug[3] FIGURENNAME)
            evaluierung = minimax(temp_figuren, tiefe - 1, not is_weiss_am_zug)
            maxEvaluierung = max(maxEvaluierung, evaluierung)

    else:
    minEvaluierung = 10**17
    for zug in legale_zuege:
        temp_figuren = bewge_figur(zug[0], zug[1], figuren, is_weiss_am_zug, zug[3] FIGURENNAME)
        evaluierung = minimax(temp_figuren, tiefe - 1, not is_weiss_am_zug)
        minEvaluierung = min(minEvaluierung, evaluierung)


def get_legale_zuege(figuren, ist_weiss_am_zug):
    sudo_legale_zuege = []

    if ist_weiss_am_zug:
        turn = "w_"
    else:
        turn = "s_"

    for figur in figuren:
        if turn in figur

            # OPTIERMUNGS POTENTIAL
            bsb_iterator_figur = biggest_single_bit_number
            # bit_figur = 2 ** floor log2(legale_bit_zuege) --> 00011 => 2 ** 1
            # figuren[figur] ^= bit_figur

            while bsb_iterator_figur > 0:
                if bsb_iterator_figur & figuren[figur]:
                    figur_bit_wert = bsb_iterator_figur

                    legale_figuren_zuge = 0

                    # Get alle legalen Züge von Figur
                    if "ba" in figur:
                        legale_figuren_zuge = get_legale_bauern_zuege(figur_bit_wert, figuren, ist_weiss_am_zug)
                    elif "pf" in figur:
                        legale_figuren_zuge = get_legale_pferd_zuge(figur_bit_wert, figuren, ist_weiss_am_zug)
                    elif "la" in figur:
                        legale_figuren_zuge = get_legale_laufer_zuge(figur_bit_wert, figuren, ist_weiss_am_zug)
                    elif "tu" in figur:
                        legale_figuren_zuge = get_legale_turm_zuge(figur_bit_wert, figuren, ist_weiss_am_zug)
                    elif "da" in figur:
                        legale_figuren_zuge = get_legale_damen_zuge(figur_bit_wert, figuren, ist_weiss_am_zug)
                    elif "ko" in figur:
                        legale_figuren_zuge = get_legale_konig_zuge(figur_bit_wert, figuren, ist_weiss_am_zug)

                    sudo_legale_zuege.append([figur_bit_wert, legale_figuren_zuge, False, figur]...)

                bsb_iterator_figur = bsb_iterator_figur >> 1

    sudo_legale_zuege.append([figur, 0000000100000000, isCaptcha, figurname]...)

    legale_zuege = check_legale_zuege(sudo_legale_zuege)
    return legale_zuege


# umformen zu [figur, 0001000000000000, isCaptcha, figurname] [figur, 0000000100000000, isCaptcha, figurname] ...
# optimerung isCaptcha --> zug_ziel: 0001000000000000 & genger_maske > 0 ist
def change_legale_zuege_format(figur_bit_iterator(figur_zug), legale_bit_zuege, figuren, figurenname):
    format_legale_zuege = []

    # Jedes bit der legale_bit_zuege iterieren
    for i in range(legale_bit_zuege.bitcount()):
        bit_wert_zug = 2 ** floor log2(legale_bit_zuege) --> 00011 => 2 ** 1
        is_captcha = if bit_wert_zug & get_gegner_maske(figuren) != 0: True
        legale_bit_zuege = legale_bit_zuege ^ bit_wert_zug

        format_legale_zuege.append([figur_bit_iterator, bit_wert_zug, is_captcha, figurname])

    return format_legale_zuege


# Überprüfen ob Zug Legal ist
--> Dann wenn eigener König nicht im Schach steht
def check_legale_zuege(figuren, sudo_legale_zuege, ist_weiss_am_zug):
    checked_legale_zuege = []

    for sudo_zug in sudo_legale_zuege:
        temp_figuren = bewege_figur()

        if is_king_in_schach(figuren, ist_weiss_am_zug):
            legale_zuege.append(sudo_zug)

    return checked_legale_zuege


def is_king_in_schach(figuren, is_weiss_am_zug):
    gegner_zuege = get_legale_zuege(figuren, not is_weiss_am_zug)
    gegner_angriffs_maske = for zug in zuege maske |= zug

    # Gegnger Greift könig NICHT an
    if figuren["w_konig" if is_weiss_am_zug else "s_konig"] & gegner_angriffs_maske == 0:
        return False

    return True

##### PSEUDO #####

+-+-+-+-+-+-+-++-+-+-+-+-+-+-++-+-+-+-+-+-+-++-+-+-+-+-+-+-++-+-+-+-+-+-+-++-+-+-+-+-+-+-+
"""

# -------------------------------------------- 0. imports ----------------------------------------------------
import math
import operator
import os
from random import randint
# from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor, as_completed
import time

# -------------------------------------------- Hilfsvariablen ----------------------------------------------------
laufer_end_calculation_maske = int("1000000110000001100000011000000110000001100000011000000110000001", 2)
brett_links_maske = int("1000000010000000100000001000000010000000100000001000000010000000", 2)
brett_rechts_maske = int("0000000100000001000000010000000100000001000000010000000100000001", 2)
uber_brett_hinaus_maske = int("1111111111111111111111111111111111111111111111111111111111111111", 2)

# -------------------------------------------- 1. Aufabu ----------------------------------------------------
schachbrett_groesse = 0
schachbrett_groesse_wurzel = 0

biggest_single_bit_number = 0

doppel_move_weis_maske = int("0000000000000000000000000000000000000000000000001111111100000000", 2)
doppel_move_schwarz_maske = int("0000000011111111000000000000000000000000000000000000000000000000", 2)

is_global_variablen_gesetzt = False

counter = 0
last_call = True

# -------------------------------------------- 2. Beast Mode ----------------------------------------------------
# ################ Weights #################
# PIECE WEIGHTS
w_bauer_gewichtung = 100
w_laufer_gewichtung = 305
w_pferd_gewichtung = 333
w_turm_gewichtung = 563
w_damen_gewichtung = 950
w_konig_gewichtung = 100000

s_bauer_gewichtung = 100
s_laufer_gewichtung = 305
s_pferd_gewichtung = 333
s_turm_gewichtung = 563
s_damen_gewichtung = 950
s_konig_gewichtung = 100000

# BOARD WEIGHTS
# -------------------------------------------- BLACK FIGS --------------------------------------------
"""
kings_end_game_table = [
    -50,-40,-30,-20,-20,-30,-40,-50,
    -30,-20,-10,  0,  0,-10,-20,-30,
    -30,-10, 20, 30, 30, 20,-10,-30,
    -30,-10, 30, 40, 40, 30,-10,-30,
    -30,-10, 30, 40, 40, 30,-10,-30,
    -30,-10, 20, 30, 30, 20,-10,-30,
    -30,-30,  0,  0,  0,  0,-30,-30,
    -50,-30,-30,-30,-30,-30,-30,-50]
"""
s_ko_maske_0 = int("0000000000000000000000000000000000011000000110000001100000011000", 2)
s_ko_maske_1 = int("0000000000000000000000000001100001100110011001100110011001100110", 2)
s_ko_maske_2 = int("0000000000000000000000000110011010000001100000011000000110000001", 2)
s_ko_maske_3 = int("0000000000000000011111101000000100000000000000000000000000000000", 2)
s_ko_maske_4 = int("0000000000000000100000010000000000000000000000000000000000000000", 2)
s_ko_maske_5 = int("0010010000000000000000000000000000000000000000000000000000000000", 2)
s_ko_maske_6 = int("1000000111000011000000000000000000000000000000000000000000000000", 2)
s_ko_maske_7 = int("0100001000000000000000000000000000000000000000000000000000000000", 2)

s_ko_maske_0_gewicht = -50
s_ko_maske_1_gewicht = -40
s_ko_maske_2_gewicht = -30
s_ko_maske_3_gewicht = -20
s_ko_maske_4_gewicht = -10
s_ko_maske_5_gewicht = 10
s_ko_maske_6_gewicht = 20
s_ko_maske_7_gewicht = 30

s_da_maske_0 = int("1000000100000000000000000000000000000000000000000000000010000001", 2)
s_da_maske_1 = int("0110011010000001100000010000000000000000100000011000000101100110", 2)
s_da_maske_2 = int("0001100000000000000000000000000110000001000000000000000000011000", 2)
s_da_maske_3 = int("0000000000000000011111000011110000111100001111000000000000000000", 2)

s_da_maske_0_gewicht = -20
s_da_maske_1_gewicht = -10
s_da_maske_2_gewicht = -5
s_da_maske_3_gewicht = 5

s_tu_maske_0 = int("0000000010000001100000011000000110000001100000010000000000000000", 2)
s_tu_maske_1 = int("0001100000000000000000000000000000000000000000001000000100000000", 2)
s_tu_maske_2 = int("0000000000000000000000000000000000000000000000000111111000000000", 2)

s_tu_maske_0_gewicht = -5
s_tu_maske_1_gewicht = 5
s_tu_maske_2_gewicht = 10

s_la_maske_0 = int("1000000100000000000000000000000000000000000000000000000010000001", 2)
s_la_maske_1 = int("0111111010000001100000011000000110000001100000011000000101111110", 2)
s_la_maske_2 = int("0000000001000010000000000000000001100110001001000000000000000000", 2)
s_la_maske_3 = int("0000000000000000011111100011110000011000000110000000000000000000", 2)

s_la_maske_0_gewicht = -20
s_la_maske_1_gewicht = -10
s_la_maske_2_gewicht = 5
s_la_maske_3_gewicht = 10


"""
knightstable = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50]
"""
s_pf_maske_0 = int("1000000100000000000000000000000000000000000000000000000010000001", 2)
s_pf_maske_1 = int("0100001010000001000000000000000000000000000000001000000101000010", 2)
s_pf_maske_2 = int("0011110000000000100000011000000110000001100000010000000000111100", 2)
s_pf_maske_3 = int("0000000001000010000000000000000000000000000000000100001000000000", 2)
s_pf_maske_4 = int("0000000000011000010000100000000001000010000000000000000000000000", 2)
s_pf_maske_5 = int("0000000000000000001001000000000000000000001001000000000000000000", 2)
s_pf_maske_6 = int("0000000000000000000110000010010000100100000110000000000000000000", 2)
s_pf_maske_7 = int("0000000000000000000000000001100000011000000000000000000000000000", 2)

s_pf_maske_0_gewicht = -50
s_pf_maske_1_gewicht = -40
s_pf_maske_2_gewicht = -30
s_pf_maske_3_gewicht = -20
s_pf_maske_4_gewicht = 5
s_pf_maske_5_gewicht = 10
s_pf_maske_6_gewicht = 15
s_pf_maske_7_gewicht = 20

s_ba_maske_0 = int("0000000000011000000000000000000000000000000000000000000000000000", 2)
s_ba_maske_1 = int("0000000000000000001001000000000000000000000000000000000000000000", 2)
s_ba_maske_2 = int("0000000000000000010000100000000000000000000000000000000000000000", 2)
s_ba_maske_3 = int("0000000010000001100000010000000011000011000000000000000000000000", 2)
s_ba_maske_4 = int("0000000001100110000000000000000000100100110000110000000000000000", 2)
s_ba_maske_5 = int("0000000000000000000000000001100000000000001001000000000000000000", 2)
s_ba_maske_6 = int("0000000000000000000000000000000000011000000000000000000000000000", 2)
s_ba_maske_7 = int("0000000000000000000000000000000000000000000110000000000000000000", 2)
s_ba_maske_8 = int("0000000000000000000000000000000000000000000000001111111100000000", 2)

s_ba_maske_0_gewicht = -20
s_ba_maske_1_gewicht = -10
s_ba_maske_2_gewicht = -5
s_ba_maske_3_gewicht = 5
s_ba_maske_4_gewicht = 10
s_ba_maske_5_gewicht = 20
s_ba_maske_6_gewicht = 25
s_ba_maske_7_gewicht = 30
s_ba_maske_8_gewicht = 50


# -------------------------------------------- WHITE FIGS --------------------------------------------
w_ko_maske_0 = int("0001100000011000000110000001100000000000000000000000000000000000", 2)
w_ko_maske_1 = int("0110011001100110011001100110011000011000000000000000000000000000", 2)
w_ko_maske_2 = int("1000000110000001100000011000000101100110000000000000000000000000", 2)
w_ko_maske_3 = int("0000000000000000000000000000000010000001011111100000000000000000", 2)
w_ko_maske_4 = int("0000000000000000000000000000000000000000100000010000000000000000", 2)
w_ko_maske_5 = int("0000000000000000000000000000000000000000000000000000000000100100", 2)
w_ko_maske_6 = int("0000000000000000000000000000000000000000000000001100001110000001", 2)
w_ko_maske_7 = int("0000000000000000000000000000000000000000000000000000000001000010", 2)

w_ko_maske_0_gewicht = -50
w_ko_maske_1_gewicht = -40
w_ko_maske_2_gewicht = -30
w_ko_maske_3_gewicht = -20
w_ko_maske_4_gewicht = -10
w_ko_maske_5_gewicht = 10
w_ko_maske_6_gewicht = 20
w_ko_maske_7_gewicht = 30

w_da_maske_0 = int("1000000100000000000000000000000000000000000000000000000010000001", 2)
w_da_maske_1 = int("0110011010000001100000010000000000000000100000011000000101100110", 2)
w_da_maske_2 = int("0001100000000000000000001000000110000000000000000000000000011000", 2)
w_da_maske_3 = int("0000000000000000001111000011110000111100001111100000000000000000", 2)

w_da_maske_0_gewicht = -20
w_da_maske_1_gewicht = -10
w_da_maske_2_gewicht = -5
w_da_maske_3_gewicht = 5

w_tu_maske_0 = int("0000000000000000100000011000000110000001100000011000000100000000", 2)
w_tu_maske_1 = int("0000000010000001000000000000000000000000000000000000000000011000", 2)
w_tu_maske_2 = int("0000000001111110000000000000000000000000000000000000000000000000", 2)

w_tu_maske_0_gewicht = -5
w_tu_maske_1_gewicht = 5
w_tu_maske_2_gewicht = 10

w_la_maske_0 = int("1000000100000000000000000000000000000000000000000000000010000001", 2)
w_la_maske_1 = int("0111111010000001100000011000000110000001100000011000000101111110", 2)
w_la_maske_2 = int("0000000000000000001001000110011000000000000000000100001000000000", 2)
w_la_maske_3 = int("0000000000000000000110000001100000111100011111100000000000000000", 2)

w_la_maske_0_gewicht = -20
w_la_maske_1_gewicht = -10
w_la_maske_2_gewicht = 5
w_la_maske_3_gewicht = 10

w_pf_maske_0 = int("1000000100000000000000000000000000000000000000000000000010000001", 2)
w_pf_maske_1 = int("0100001010000001000000000000000000000000000000001000000101000010", 2)
w_pf_maske_2 = int("0011110000000000100000011000000110000001100000010000000000111100", 2)
w_pf_maske_3 = int("0000000001000010000000000000000000000000000000000100001000000000", 2)
w_pf_maske_4 = int("0000000000000000000000000100001000000000010000100001100000000000", 2)
w_pf_maske_5 = int("0000000000000000001001000000000000000000001001000000000000000000", 2)
w_pf_maske_6 = int("0000000000000000000110000010010000100100000110000000000000000000", 2)
w_pf_maske_7 = int("0000000000000000000000000001100000011000000000000000000000000000", 2)

w_pf_maske_0_gewicht = -50
w_pf_maske_1_gewicht = -40
w_pf_maske_2_gewicht = -30
w_pf_maske_3_gewicht = -20
w_pf_maske_4_gewicht = 5
w_pf_maske_5_gewicht = 10
w_pf_maske_6_gewicht = 15
w_pf_maske_7_gewicht = 20

w_ba_maske_0 = int("0000000000000000000000000000000000000000000000000001100000000000", 2)
w_ba_maske_1 = int("0000000000000000000000000000000000000000001001000000000000000000", 2)
w_ba_maske_2 = int("0000000000000000000000000000000000000000010000100000000000000000", 2)
w_ba_maske_3 = int("0000000000000000000000001100001100000000100000011000000100000000", 2)
w_ba_maske_4 = int("0000000000000000110000110010010000000000000000000110011000000000", 2)
w_ba_maske_5 = int("0000000000000000001001000000000000011000000000000000000000000000", 2)
w_ba_maske_6 = int("0000000000000000000000000001100000000000000000000000000000000000", 2)
w_ba_maske_7 = int("0000000000000000000110000000000000000000000000000000000000000000", 2)
w_ba_maske_8 = int("0000000011111111000000000000000000000000000000000000000000000000", 2)

w_ba_maske_0_gewicht = -20
w_ba_maske_1_gewicht = -10
w_ba_maske_2_gewicht = -5
w_ba_maske_3_gewicht = 5
w_ba_maske_4_gewicht = 10
w_ba_maske_5_gewicht = 20
w_ba_maske_6_gewicht = 25
w_ba_maske_7_gewicht = 30
w_ba_maske_8_gewicht = 50

# ################ Weights #################
# ########### Evaluation Weights ############
angriffs_feld_gewicht = 1.5

# ########### ------------------ ############

# ############### Global Tracking #################

iteration_counter = 0

# ############### --------------- #################


def evaluiere_schachbrett(figuren):
    gesamtwert_weiss = 0
    gesamtwert_schwarz = 0

    # 1. Iterriere Über jede Figur:
    for figur in figuren:

        # A: Ist die Figur weiss:
        if "w_" in figur:
            if "_ba" in figur:
                number_of_bits = bin(figuren[figur]).count("1") * w_bauer_gewichtung
                w_ba = figuren[figur]

                gesamtwert_weiss += bin(w_ba_maske_0 & w_ba).count("1") * w_ba_maske_0_gewicht \
                                      + bin(w_ba_maske_1 & w_ba).count("1") * w_ba_maske_1_gewicht \
                                      + bin(w_ba_maske_2 & w_ba).count("1") * w_ba_maske_2_gewicht \
                                      + bin(w_ba_maske_3 & w_ba).count("1") * w_ba_maske_3_gewicht \
                                      + bin(w_ba_maske_4 & w_ba).count("1") * w_ba_maske_4_gewicht \
                                      + bin(w_ba_maske_5 & w_ba).count("1") * w_ba_maske_5_gewicht \
                                      + bin(w_ba_maske_6 & w_ba).count("1") * w_ba_maske_6_gewicht \
                                      + bin(w_ba_maske_7 & w_ba).count("1") * w_ba_maske_7_gewicht \
                                      + bin(w_ba_maske_8 & w_ba).count("1") * w_ba_maske_8_gewicht

                gesamtwert_weiss += number_of_bits
            elif "_la" in figur:
                number_of_bits = bin(figuren[figur]).count("1") * w_laufer_gewichtung
                w_la = figuren[figur]

                gesamtwert_weiss += bin(w_la_maske_0 & w_la).count("1") * w_la_maske_0_gewicht \
                                      + bin(w_la_maske_1 & w_la).count("1") * w_la_maske_1_gewicht \
                                      + bin(w_la_maske_2 & w_la).count("1") * w_la_maske_2_gewicht \
                                      + bin(w_la_maske_3 & w_la).count("1") * w_la_maske_3_gewicht

                gesamtwert_weiss += number_of_bits
            elif "_pf" in figur:
                number_of_bits = bin(figuren[figur]).count("1") * w_pferd_gewichtung
                w_pf = figuren[figur]

                gesamtwert_weiss += bin(w_pf_maske_0 & w_pf).count("1") * w_pf_maske_0_gewicht \
                                      + bin(w_pf_maske_1 & w_pf).count("1") * w_pf_maske_1_gewicht \
                                      + bin(w_pf_maske_2 & w_pf).count("1") * w_pf_maske_2_gewicht \
                                      + bin(w_pf_maske_3 & w_pf).count("1") * w_pf_maske_3_gewicht \
                                      + bin(w_pf_maske_4 & w_pf).count("1") * w_pf_maske_4_gewicht \
                                      + bin(w_pf_maske_5 & w_pf).count("1") * w_pf_maske_5_gewicht \
                                      + bin(w_pf_maske_6 & w_pf).count("1") * w_pf_maske_6_gewicht \
                                      + bin(w_pf_maske_7 & w_pf).count("1") * w_pf_maske_7_gewicht

                gesamtwert_weiss += number_of_bits
            elif "_tu" in figur:
                number_of_bits = bin(figuren[figur]).count("1") * w_turm_gewichtung
                w_tu = figuren[figur]

                gesamtwert_weiss += bin(w_tu_maske_0 & w_tu).count("1") * w_tu_maske_0_gewicht \
                                      + bin(w_tu_maske_1 & w_tu).count("1") * w_tu_maske_1_gewicht \
                                      + bin(w_tu_maske_2 & w_tu).count("1") * w_tu_maske_2_gewicht

                gesamtwert_weiss += number_of_bits
            elif "_da" in figur:
                number_of_bits = bin(figuren[figur]).count("1") * w_damen_gewichtung
                w_da = figuren[figur]

                gesamtwert_weiss += bin(w_da_maske_0 & w_da).count("1") * w_da_maske_0_gewicht \
                                      + bin(w_da_maske_1 & w_da).count("1") * w_da_maske_1_gewicht \
                                      + bin(w_da_maske_2 & w_da).count("1") * w_da_maske_2_gewicht \
                                      + bin(w_da_maske_3 & w_da).count("1") * w_da_maske_3_gewicht

                gesamtwert_weiss += number_of_bits
            elif "_ko" in figur:
                number_of_bits = bin(figuren[figur]).count("1") * w_konig_gewichtung
                w_ko = figuren[figur]

                gesamtwert_weiss += bin(w_ko_maske_0 & w_ko).count("1") * w_ko_maske_0_gewicht \
                                      + bin(w_ko_maske_1 & w_ko).count("1") * w_ko_maske_1_gewicht \
                                      + bin(w_ko_maske_2 & w_ko).count("1") * w_ko_maske_2_gewicht \
                                      + bin(w_ko_maske_3 & w_ko).count("1") * w_ko_maske_3_gewicht \
                                      + bin(w_ko_maske_4 & w_ko).count("1") * w_ko_maske_4_gewicht \
                                      + bin(w_ko_maske_5 & w_ko).count("1") * w_ko_maske_5_gewicht \
                                      + bin(w_ko_maske_6 & w_ko).count("1") * w_ko_maske_6_gewicht \
                                      + bin(w_ko_maske_7 & w_ko).count("1") * w_ko_maske_7_gewicht

                gesamtwert_weiss += number_of_bits

        #   B: Ist die Figur Schwarz:
        if "s_" in figur:
            if "_ba" in figur:
                number_of_bits = bin(figuren[figur]).count("1") * s_bauer_gewichtung
                s_ba = figuren[figur]

                gesamtwert_schwarz += bin(s_ba_maske_0 & s_ba).count("1") * s_ba_maske_0_gewicht \
                                      + bin(s_ba_maske_1 & s_ba).count("1") * s_ba_maske_1_gewicht \
                                      + bin(s_ba_maske_2 & s_ba).count("1") * s_ba_maske_2_gewicht \
                                      + bin(s_ba_maske_3 & s_ba).count("1") * s_ba_maske_3_gewicht \
                                      + bin(s_ba_maske_4 & s_ba).count("1") * s_ba_maske_4_gewicht \
                                      + bin(s_ba_maske_5 & s_ba).count("1") * s_ba_maske_5_gewicht \
                                      + bin(s_ba_maske_6 & s_ba).count("1") * s_ba_maske_6_gewicht \
                                      + bin(s_ba_maske_7 & s_ba).count("1") * s_ba_maske_7_gewicht \
                                      + bin(s_ba_maske_8 & s_ba).count("1") * s_ba_maske_8_gewicht

                gesamtwert_schwarz += number_of_bits
            elif "_la" in figur:
                number_of_bits = bin(figuren[figur]).count("1") * s_laufer_gewichtung
                s_la = figuren[figur]

                gesamtwert_schwarz += bin(s_la_maske_0 & s_la).count("1") * s_la_maske_0_gewicht \
                                      + bin(s_la_maske_1 & s_la).count("1") * s_la_maske_1_gewicht \
                                      + bin(s_la_maske_2 & s_la).count("1") * s_la_maske_2_gewicht \
                                      + bin(s_la_maske_3 & s_la).count("1") * s_la_maske_3_gewicht

                gesamtwert_schwarz += number_of_bits
            elif "_pf" in figur:
                number_of_bits = bin(figuren[figur]).count("1") * s_pferd_gewichtung
                s_pf = figuren[figur]

                gesamtwert_schwarz += bin(s_pf_maske_0 & s_pf).count("1") * s_pf_maske_0_gewicht \
                                      + bin(s_pf_maske_1 & s_pf).count("1") * s_pf_maske_1_gewicht \
                                      + bin(s_pf_maske_2 & s_pf).count("1") * s_pf_maske_2_gewicht \
                                      + bin(s_pf_maske_3 & s_pf).count("1") * s_pf_maske_3_gewicht \
                                      + bin(s_pf_maske_4 & s_pf).count("1") * s_pf_maske_4_gewicht \
                                      + bin(s_pf_maske_5 & s_pf).count("1") * s_pf_maske_5_gewicht \
                                      + bin(s_pf_maske_6 & s_pf).count("1") * s_pf_maske_6_gewicht \
                                      + bin(s_pf_maske_7 & s_pf).count("1") * s_pf_maske_7_gewicht

                gesamtwert_schwarz += number_of_bits
            elif "_tu" in figur:
                number_of_bits = bin(figuren[figur]).count("1") * s_turm_gewichtung
                s_tu = figuren[figur]

                gesamtwert_schwarz += bin(s_tu_maske_0 & s_tu).count("1") * s_tu_maske_0_gewicht \
                                      + bin(s_tu_maske_1 & s_tu).count("1") * s_tu_maske_1_gewicht \
                                      + bin(s_tu_maske_2 & s_tu).count("1") * s_tu_maske_2_gewicht

                gesamtwert_schwarz += number_of_bits
            elif "_da" in figur:
                number_of_bits = bin(figuren[figur]).count("1") * s_damen_gewichtung
                s_da = figuren[figur]

                gesamtwert_schwarz += bin(s_da_maske_0 & s_da).count("1") * s_da_maske_0_gewicht \
                                      + bin(s_da_maske_1 & s_da).count("1") * s_da_maske_1_gewicht \
                                      + bin(s_da_maske_2 & s_da).count("1") * s_da_maske_2_gewicht \
                                      + bin(s_da_maske_3 & s_da).count("1") * s_da_maske_3_gewicht

                gesamtwert_schwarz += number_of_bits
            elif "_ko" in figur:
                number_of_bits = bin(figuren[figur]).count("1") * s_konig_gewichtung
                s_ko = figuren[figur]

                gesamtwert_schwarz += bin(s_ko_maske_0 & s_ko).count("1") * s_ko_maske_0_gewicht \
                                      + bin(s_ko_maske_1 & s_ko).count("1") * s_ko_maske_1_gewicht \
                                      + bin(s_ko_maske_2 & s_ko).count("1") * s_ko_maske_2_gewicht \
                                      + bin(s_ko_maske_3 & s_ko).count("1") * s_ko_maske_3_gewicht \
                                      + bin(s_ko_maske_4 & s_ko).count("1") * s_ko_maske_4_gewicht \
                                      + bin(s_ko_maske_5 & s_ko).count("1") * s_ko_maske_5_gewicht \
                                      + bin(s_ko_maske_6 & s_ko).count("1") * s_ko_maske_6_gewicht \
                                      + bin(s_ko_maske_7 & s_ko).count("1") * s_ko_maske_7_gewicht

                gesamtwert_schwarz += number_of_bits

    # Angriffsfelder
    # Weiße angriffsfelder
    gesamtwert_weiss += bin(get_angriffs_maske(dict(figuren), True)).count("1") * angriffs_feld_gewicht

    # Schwarze angriffsfelder
    gesamtwert_schwarz += bin(get_angriffs_maske(dict(figuren), False)).count("1") * angriffs_feld_gewicht

    return round(gesamtwert_weiss - gesamtwert_schwarz)


# --------------------------------------- NEW CODE INSERTION BEAST 2.0 -------------------------------------------
# def get_big_babba_move(figuren, is_weiss_am_zug, tiefe):
#     legale_zuege = get_legale_zuege(figuren, is_weiss_am_zug)
#     legale_zuege = sort_liste_nach_capture(legale_zuege)
#     babba_move = legale_zuege[randint(0, len(legale_zuege) - 1)]
#
#     if is_weiss_am_zug:
#         big_babba_move_wert = -10 ** 17
#     else:
#         big_babba_move_wert = 10 ** 17
#
#     for zug in legale_zuege:
#         temp_figuren = bewege_figur(zug[0], zug[1], dict(figuren), is_weiss_am_zug, zug[3])
#
#         if is_schachmatt(dict(temp_figuren), not is_weiss_am_zug):
#             return zug, 0
#
#         evaluierung = minimax(temp_figuren, tiefe - 1, -10 ** 17, 10 ** 17, not is_weiss_am_zug)
#
#         if is_weiss_am_zug:
#             if evaluierung > big_babba_move_wert:
#                 big_babba_move_wert = evaluierung
#                 babba_move = zug
#             if evaluierung == big_babba_move_wert and "ko" not in zug[3]:
#                 if not randint(0, 3):
#                     big_babba_move_wert = evaluierung
#                     babba_move = zug
#         else:
#             if evaluierung < big_babba_move_wert:
#                 big_babba_move_wert = evaluierung
#                 babba_move = zug
#             if evaluierung == big_babba_move_wert and "ko" not in zug[3]:
#                 if not randint(0, 3):
#                     big_babba_move_wert = evaluierung
#                     babba_move = zug
#
#     return babba_move, big_babba_move_wert


# def get_big_babba_move(figuren, is_weiss_am_zug, tiefe):
#     legale_zuege = get_legale_zuege(figuren, is_weiss_am_zug)
#     legale_zuege = sort_liste_nach_capture(legale_zuege)
#     babba_move = legale_zuege[randint(0, len(legale_zuege) - 1)]
#
#     if is_weiss_am_zug:
#         big_babba_move_wert = -10 ** 17
#     else:
#         big_babba_move_wert = 10 ** 17
#
#     # Iterative deepening
#     # Suche wiederholen mit tiefe + i (i counter of loop)
#     # Den besten move als ersten move der Nächsten Suche ausführen
#     # (Zeit geben uns dann abbrechen) --> Zuerst nur Captcha moves suchen 3/5 Zeit?
#
#     for zug in legale_zuege:
#         temp_figuren = bewege_figur(zug[0], zug[1], dict(figuren), is_weiss_am_zug, zug[3])
#
#         if is_schachmatt(dict(temp_figuren), not is_weiss_am_zug):
#             return zug, 0
#
#
#         # print("TIEFE:", iterative_tiefe)
#         evaluierung = minimax(temp_figuren, tiefe - 1, -10 ** 17, 10 ** 17, not is_weiss_am_zug)
#
#         if is_weiss_am_zug:
#             if evaluierung > big_babba_move_wert:
#                 big_babba_move_wert = evaluierung
#                 babba_move = zug
#             if evaluierung == big_babba_move_wert and "ko" not in zug[3]:
#                 if not randint(0, 3):
#                     big_babba_move_wert = evaluierung
#                     babba_move = zug
#         else:
#             if evaluierung < big_babba_move_wert:
#                 big_babba_move_wert = evaluierung
#                 babba_move = zug
#             if evaluierung == big_babba_move_wert and "ko" not in zug[3]:
#                 if not randint(0, 3):
#                     big_babba_move_wert = evaluierung
#                     babba_move = zug
#
#         # Besten Move in index 0 inserten
#
#     return babba_move, big_babba_move_wert

def evaluate_move(zug, figuren, is_weiss_am_zug, current_depth):
    temp_figuren = bewege_figur(zug[0], zug[1], dict(figuren), is_weiss_am_zug, zug[3])
    if is_schachmatt(temp_figuren, not is_weiss_am_zug):
        return zug, 0  # Immediate checkmate found
    evaluierung = minimax(temp_figuren, current_depth - 1, -10 ** 17, 10 ** 17, not is_weiss_am_zug)
    return zug, evaluierung


def get_big_babba_move(figuren, is_weiss_am_zug, max_tiefe):
    babba_move = None
    legale_zuege = get_legale_zuege(figuren, is_weiss_am_zug)
    legale_zuege = sort_liste_nach_capture(legale_zuege)
    last_iteration_zug = legale_zuege[randint(0, len(legale_zuege) - 1)]

    # Iterative deepening loop
    for current_depth in range(1, max_tiefe + 1):
        if is_weiss_am_zug:
            big_babba_move_wert = -10 ** 17
        else:
            big_babba_move_wert = 10 ** 17

        # Evaluate moves concurrently using ThreadPoolExecutor
        with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
            future_to_move = {executor.submit(evaluate_move, zug, dict(figuren), is_weiss_am_zug, current_depth): zug for zug
                              in legale_zuege}

            for future in as_completed(future_to_move):
                zug, evaluierung = future.result()

                if is_weiss_am_zug:
                    if evaluierung > big_babba_move_wert:
                        big_babba_move_wert = evaluierung
                        babba_move = zug
                    elif evaluierung == big_babba_move_wert:
                        if not randint(0, 3):
                            babba_move = zug
                else:
                    if evaluierung < big_babba_move_wert:
                        big_babba_move_wert = evaluierung
                        babba_move = zug
                    elif evaluierung == big_babba_move_wert:
                        if not randint(0, 3):
                            babba_move = zug

        legale_zuege = [babba_move] + [zug for zug in legale_zuege if zug != babba_move]

    return babba_move, big_babba_move_wert


# ................................ TEST ................................
# def get_big_babba_move(figuren, is_weiss_am_zug, max_tiefe):
#     import time
#
#     babba_move = None
#     legale_zuege = get_legale_zuege(figuren, is_weiss_am_zug)
#     legale_zuege = sort_liste_nach_capture(legale_zuege)
#     last_iteration_zug = legale_zuege[randint(0, len(legale_zuege) - 1)]
#
#     # Iterative deepening loop
#     for current_depth in range(1, max_tiefe + 1):
#         # print("Sorttedlegale_zuege: ", legale_zuege)
#
#         if is_weiss_am_zug:
#             big_babba_move_wert = -10 ** 17
#         else:
#             big_babba_move_wert = 10 ** 17
#
#         for zug in legale_zuege:
#             temp_figuren = bewege_figur(zug[0], zug[1], dict(figuren), is_weiss_am_zug, zug[3])
#
#             if is_schachmatt(temp_figuren, not is_weiss_am_zug):
#                 return zug, 0  # Immediate checkmate found
#
#             # Call minimax with alpha-beta pruning
#             evaluierung = minimax(temp_figuren, current_depth - 1, -10 ** 17, 10 ** 17, not is_weiss_am_zug)
#
#             if is_weiss_am_zug:
#                 if evaluierung > big_babba_move_wert:
#                     big_babba_move_wert = evaluierung
#                     babba_move = zug
#                     # print("zug", zug, " W:", big_babba_move_wert)
#                 if evaluierung == big_babba_move_wert:
#                     if not randint(0, 3):
#                         big_babba_move_wert = evaluierung
#                         babba_move = zug
#
#             else:
#                 if evaluierung < big_babba_move_wert:
#                     big_babba_move_wert = evaluierung
#                     babba_move = zug
#                 if evaluierung == big_babba_move_wert:
#                     if not randint(0, 3):
#                         big_babba_move_wert = evaluierung
#                         babba_move = zug
#                     # print("zug", zug, " W:", big_babba_move_wert)
#
#         legale_zuege = [babba_move] + [zug for zug in legale_zuege if zug != babba_move]
#         # print("NEW::: ", legale_zuege)
#
#         # last_iteration_zug = babba_move
#
#     return babba_move, big_babba_move_wert
#


def minimax(figuren, tiefe, alpha, beta, is_weiss_am_zug):
    if tiefe == 0:
        return quiescence_search(figuren, alpha, beta, is_weiss_am_zug, 0)

    legale_zuege = get_legale_zuege(dict(figuren), is_weiss_am_zug)

    if not legale_zuege:
        if is_schachmatt(dict(figuren), is_weiss_am_zug):
            if is_weiss_am_zug:
                return -10 ** 17 + tiefe  # weiß schachmat
            else:
                return 10 ** 17 - tiefe  # Schwarz schachamt
        else:
            return 0

    if is_weiss_am_zug:
        max_evaluierung = -10 ** 17
        for zug in legale_zuege:
            temp_figuren = bewege_figur(zug[0], zug[1], dict(figuren), True, zug[3])
            evaluierung = minimax(dict(temp_figuren), tiefe - 1, alpha, beta, False)
            max_evaluierung = max(max_evaluierung, evaluierung)
            alpha = max(alpha, evaluierung)
            if beta <= alpha:  # Pruning
                break
        return max_evaluierung

    else:
        min_evaluierung = 10 ** 17
        for zug in legale_zuege:
            temp_figuren = bewege_figur(zug[0], zug[1], dict(figuren), False, zug[3])
            evaluierung = minimax(dict(temp_figuren), tiefe - 1, alpha, beta, True)
            min_evaluierung = min(min_evaluierung, evaluierung)
            beta = min(beta, evaluierung)
            if beta <= alpha:  # Pruning
                break
        return min_evaluierung


def quiescence_search(figuren, alpha, beta, is_weiss_am_zug, max_tiefe):
    # Stop if quiescence depth limit is reached
    if max_tiefe == 0:
        return evaluiere_schachbrett(figuren)  # Static evaluation

    # Get tactical moves (captures, checks, promotions)
    legale_zuege = get_legale_zuege(dict(figuren), is_weiss_am_zug)
    legale_zuege = filter_captcha_zuege(legale_zuege)

    # If there are no tactical moves, return static evaluation
    if not legale_zuege:
        return evaluiere_schachbrett(figuren)

    # White to move (maximizing player)
    if is_weiss_am_zug:
        max_evaluierung = -10 ** 17
        for zug in legale_zuege:
            temp_figuren = bewege_figur(zug[0], zug[1], dict(figuren), True, zug[3])
            evaluierung = quiescence_search(dict(temp_figuren), alpha, beta, False, max_tiefe - 1)
            max_evaluierung = max(max_evaluierung, evaluierung)
            alpha = max(alpha, evaluierung)
            if beta <= alpha:  # Beta pruning
                break
        return max_evaluierung

    # Black to move (minimizing player)
    else:
        min_evaluierung = 10 ** 17
        for zug in legale_zuege:
            temp_figuren = bewege_figur(zug[0], zug[1], dict(figuren), False, zug[3])
            evaluierung = quiescence_search(dict(temp_figuren), alpha, beta, True, max_tiefe - 1)
            min_evaluierung = min(min_evaluierung, evaluierung)
            beta = min(beta, evaluierung)
            if beta <= alpha:  # Alpha pruning
                break
        return min_evaluierung

# ................................ TEST END ................................


def get_legale_zuege(figuren, is_weiss_am_zug):
    sudo_legale_zuege = []

    if is_weiss_am_zug:
        turn = "w_"
    else:
        turn = "s_"

    for figur in figuren:
        if turn in figur:

            temp_figur_bit_wert = figuren[figur]
            if temp_figur_bit_wert != 0:
                for i in range(bin(figuren[figur]).count("1")):

                    figur_bit_wert = 2 ** math.floor(math.log2(temp_figur_bit_wert))
                    legale_figuren_zuge = 0

                    if "pf" in figur:
                        legale_figuren_zuge = get_legale_pferd_zuge(figur_bit_wert, figuren, is_weiss_am_zug)
                    elif "la" in figur:
                        legale_figuren_zuge = get_legale_laufer_zuge(figur_bit_wert, figuren, is_weiss_am_zug)
                    elif "da" in figur:
                        legale_figuren_zuge = get_legale_damen_zuge(figur_bit_wert, figuren, is_weiss_am_zug)
                    elif "tu" in figur:
                        legale_figuren_zuge = get_legale_turm_zuge(figur_bit_wert, figuren, is_weiss_am_zug)
                    elif "ba" in figur:
                        legale_figuren_zuge = get_legale_bauern_zuege(figur_bit_wert, figuren, is_weiss_am_zug)
                    elif "ko" in figur:
                        legale_figuren_zuge = get_legale_konig_zuge(figur_bit_wert, figuren, is_weiss_am_zug)

                    if legale_figuren_zuge == 0:
                        temp_figur_bit_wert = temp_figur_bit_wert ^ figur_bit_wert
                        continue

                    legale_zuege_formatted = change_legale_zuege_format(figur_bit_wert, legale_figuren_zuge, figuren,
                                                                        figur,
                                                                        is_weiss_am_zug)

                    sudo_legale_zuege.append(legale_zuege_formatted)

                    # Figuren bit aus Figuren nehmen
                    temp_figur_bit_wert = temp_figur_bit_wert ^ figur_bit_wert

    if not sudo_legale_zuege:
        return []

    legale_zuege = check_legale_zuege(figuren, sudo_legale_zuege, is_weiss_am_zug)
    sorted_legale_zuege = sort_liste_nach_capture(legale_zuege)
    return sorted_legale_zuege


def change_legale_zuege_format(figur_bit_iterator, legale_bit_zuege, figuren, figurenname, is_weiss_am_zug):
    format_legale_zuege = []

    # Jedes bit der legale_bit_zuege iterieren
    for i in range(bin(legale_bit_zuege).count("1")):
        bit_wert_zug = 2 ** math.floor(math.log2(legale_bit_zuege))

        if is_weiss_am_zug:
            maske = get_schwarz_figuren_maske(figuren)
        else:
            maske = get_weis_figuren_maske(figuren)

        if bit_wert_zug & maske != 0:
            is_captcha = True
        else:
            is_captcha = False

        legale_bit_zuege = legale_bit_zuege ^ bit_wert_zug
        format_legale_zuege.append([figur_bit_iterator, bit_wert_zug, is_captcha, figurenname])

    return format_legale_zuege


def check_legale_zuege(figuren, sudo_legale_zuege, is_weiss_am_zug):
    checked_legale_zuege = []
    sudo_legale_zuege_flat = [x for xs in sudo_legale_zuege for x in xs]

    for sudo_zug in sudo_legale_zuege_flat:
        temp_figuren = bewege_figur(sudo_zug[0], sudo_zug[1], dict(figuren), is_weiss_am_zug, sudo_zug[3])

        if not is_king_in_schach(temp_figuren, is_weiss_am_zug):
            checked_legale_zuege.append(sudo_zug)

    return checked_legale_zuege


def is_king_in_schach(figuren,
                      is_weiss_am_zug):  # Black King check?: is_weiss_am_zug: False | White King check?: is_weiss_am_zug: True
    gegner_angriffs_maske = get_angriffs_maske(dict(figuren), not is_weiss_am_zug)

    # Gegnger Greift könig an
    if figuren["w_ko" if is_weiss_am_zug else "s_ko"] & gegner_angriffs_maske > 0:
        return True

    return False


def get_angriffs_maske(figuren, is_weiss_am_zug):
    zuege = 0

    if is_weiss_am_zug:
        turn = "w_"
    else:
        turn = "s_"

    for figur in figuren:
        if turn in figur:

            temp_figur_bit_wert = figuren[figur]
            for i in range(bin(figuren[figur]).count("1")):
                # temp_figur_bit_wert: 10000100010 --> 10000000000 --> 100000 --> 10

                figur_bit_wert = 2 ** math.floor(math.log2(temp_figur_bit_wert))

                legale_figuren_zuge = 0

                # Get alle legalen Züge von Figur
                if "ba" in figur:
                    legale_figuren_zuge = get_legale_bauern_zuege(figur_bit_wert, figuren, is_weiss_am_zug)
                elif "pf" in figur:
                    legale_figuren_zuge = get_legale_pferd_zuge(figur_bit_wert, figuren, is_weiss_am_zug)
                elif "la" in figur:
                    legale_figuren_zuge = get_legale_laufer_zuge(figur_bit_wert, figuren, is_weiss_am_zug)
                elif "tu" in figur:
                    legale_figuren_zuge = get_legale_turm_zuge(figur_bit_wert, figuren, is_weiss_am_zug)
                elif "da" in figur:
                    legale_figuren_zuge = get_legale_damen_zuge(figur_bit_wert, figuren, is_weiss_am_zug)
                elif "ko" in figur:
                    legale_figuren_zuge = get_legale_konig_zuge(figur_bit_wert, figuren, is_weiss_am_zug)

                zuege = zuege | legale_figuren_zuge
                temp_figur_bit_wert = temp_figur_bit_wert ^ figur_bit_wert

    return zuege


def is_schachmatt(figuren, is_weiss_am_zug):
    if not get_legale_zuege(figuren, is_weiss_am_zug):
        if is_king_in_schach(figuren, is_weiss_am_zug):
            return True

    return False


def sort_liste_nach_capture(legale_zuege):
    # Sortiert nach da, tu..., ba
    skrt = sorted(legale_zuege, key=lambda x: x[3], reverse=True)
    sortierte_liste = sorted(skrt, key=lambda x: not x[2])
    return sortierte_liste


def filter_captcha_zuege(legale_zuege):
    return [element for element in legale_zuege if element[2]]


# --------------------------------------- NEW CODE INSERTION BEAST 2.0 END -------------------------------------------
# -------------------------------------------- Figuren Legale Züge --------------------------------------------
def get_legale_bauern_zuege(bauer, figuren, ist_weiss_am_zug):
    # Möglichkeiten an Bauern züge
    legale_bauern_zuge = 0
    schachbrett = get_schachbrett(figuren)

    if ist_weiss_am_zug:
        # normal fall weis Bauer bewegt sich um eins nach vorne
        # Steht etwas auf diesem Feld
        if (bauer << 8) & schachbrett == 0:
            legale_bauern_zuge = bauer << 8

        # Doppel Sprung
        if (bauer << (8 * 2) | (
                bauer << 8)) & schachbrett == 0:
            # falls der Bauer am Anfang steht
            if bauer & doppel_move_weis_maske:
                temp = bauer << (8 * 2)
                legale_bauern_zuge = legale_bauern_zuge | temp

        # Attack Move
        gegnerische_figuren = get_schwarz_figuren_maske(figuren)

        # Fall Angriff: Steht diagonal links ein Gegner dann füge zuege hinzu
        angriff_diagonal_links = bauer << (8 + 1)

        # Links darf nur geschlagen werden wenn log(bauer) % Wurzel != Wurzel - 1 ist (verhindert übern Rand schlagen)
        if math.log2(bauer) % 8 != 8 - 1:
            # Steht eine Gengerische Figur links diagonal
            if angriff_diagonal_links & gegnerische_figuren != 0:
                legale_bauern_zuge = legale_bauern_zuge | angriff_diagonal_links

        # Fall Angriff: Steht diagonal rechts ein Gegner dann füge zuege hinzu
        angriff_diagonal_rechts = bauer << (8 - 1)

        # Kein schlagen über die Brett KAnte
        if math.log2(bauer) % 8 != 0:
            if angriff_diagonal_rechts & gegnerische_figuren != 0:
                legale_bauern_zuge = legale_bauern_zuge | angriff_diagonal_rechts
    else:
        # Schwarz am Zug
        # normal fall schwarz Bauer bewegt sich um eins nach vorne
        # Steht etwas auf diesem Feld
        if (bauer >> 8) & schachbrett == 0:
            legale_bauern_zuge = bauer >> 8

        # Doppel Sprung
        if (bauer >> (8 * 2) | (
                bauer >> 8)) & schachbrett == 0:
            # falls der Bauer am Anfang steht
            if bauer & doppel_move_schwarz_maske:
                temp = bauer >> (8 * 2)
                legale_bauern_zuge = legale_bauern_zuge | temp

        # Attack Move
        gegnerische_figuren = get_weis_figuren_maske(figuren)

        # Fall Angriff: Steht diagonal links ein Gegner dann füge zuege hinzu
        angriff_diagonal_links = bauer >> (8 + 1)

        # Links darf nur geschlagen werden wenn log(bauer) % Wurzel != Wurzel - 1 ist (verhindert übern Rand schlagen)
        if math.log2(bauer) % 8 != 0:
            # Steht eine Gengerische Figur links diagonal
            if angriff_diagonal_links & gegnerische_figuren != 0:
                legale_bauern_zuge = legale_bauern_zuge | angriff_diagonal_links

        # Fall Angriff: Steht diagonal rechts ein Gegner dann füge zuege hinzu
        angriff_diagonal_rechts = bauer >> (8 - 1)

        # Kein schlagen über die Brett KAnte
        if math.log2(bauer) % 8 != 8 - 1:
            if angriff_diagonal_rechts & gegnerische_figuren != 0:
                legale_bauern_zuge = legale_bauern_zuge | angriff_diagonal_rechts

    return legale_bauern_zuge


def get_legale_laufer_zuge(laufer, figuren, ist_weiss_am_zug):
    legale_laufer_zuge = 0

    if laufer & brett_rechts_maske == 0:
        legale_laufer_zuge = legale_laufer_zuge | get_shift_movement_operation(laufer, figuren, 7, operator.lshift,
                                                                               ist_weiss_am_zug, "_la", 0,
                                                                               biggest_single_bit_number)

    if laufer & brett_links_maske == 0:
        legale_laufer_zuge = legale_laufer_zuge | get_shift_movement_operation(laufer, figuren, 9, operator.lshift,
                                                                               ist_weiss_am_zug, "_la", 0,
                                                                               biggest_single_bit_number)

    if laufer & brett_links_maske == 0:
        legale_laufer_zuge = legale_laufer_zuge | get_shift_movement_operation(laufer, figuren, 7, operator.rshift,
                                                                               ist_weiss_am_zug, "_la", 0,
                                                                               biggest_single_bit_number)

    if laufer & brett_rechts_maske == 0:
        legale_laufer_zuge = legale_laufer_zuge | get_shift_movement_operation(laufer, figuren, 9, operator.rshift,
                                                                               ist_weiss_am_zug, "_la", 0,
                                                                               biggest_single_bit_number)

    return legale_laufer_zuge


def get_legale_pferd_zuge(pferd, figuren, ist_weiss_am_zug):
    legal_moves = get_shift_movement_operation_pferd(pferd, figuren, 6, 1, operator.lshift, operator.rshift,
                                                     ist_weiss_am_zug) | \
                  get_shift_movement_operation_pferd(pferd, figuren, 10, 1, operator.lshift, operator.rshift,
                                                     ist_weiss_am_zug) | \
                  get_shift_movement_operation_pferd(pferd, figuren, 15, 2, operator.lshift, operator.rshift,
                                                     ist_weiss_am_zug) | \
                  get_shift_movement_operation_pferd(pferd, figuren, 17, 2, operator.lshift, operator.rshift,
                                                     ist_weiss_am_zug) | \
                  get_shift_movement_operation_pferd(pferd, figuren, 6, 1, operator.rshift, operator.lshift,
                                                     ist_weiss_am_zug) | \
                  get_shift_movement_operation_pferd(pferd, figuren, 10, 1, operator.rshift, operator.lshift,
                                                     ist_weiss_am_zug) | \
                  get_shift_movement_operation_pferd(pferd, figuren, 15, 2, operator.rshift, operator.lshift,
                                                     ist_weiss_am_zug) | \
                  get_shift_movement_operation_pferd(pferd, figuren, 17, 2, operator.rshift, operator.lshift,
                                                     ist_weiss_am_zug)

    return legal_moves


def get_legale_turm_zuge(turm, figuren, ist_weiss_am_zug):
    vertikales_movement = get_shift_movement_operation(turm, figuren, 8, operator.lshift, ist_weiss_am_zug, "_tu", 0,
                                                       biggest_single_bit_number) \
                          | get_shift_movement_operation(turm, figuren, 8, operator.rshift, ist_weiss_am_zug, "_tu", 0,
                                                         biggest_single_bit_number)

    # shift berechnung für Turm bit position in Byte
    bit_position = (math.log2(turm)) % 8
    lshift = 7 - bit_position
    rshift = bit_position

    horizontales_movement = 0

    if lshift > 0:
        horizontales_movement = get_shift_movement_operation(turm, figuren, 1, operator.lshift, ist_weiss_am_zug, "_tu",
                                                             2 ** (math.log2(turm) - rshift),
                                                             2 ** (math.log2(turm) + lshift))
    if rshift > 0:
        horizontales_movement = horizontales_movement | get_shift_movement_operation(turm, figuren, 1, operator.rshift,
                                                                                     ist_weiss_am_zug, "_tu",
                                                                                     2 ** (math.log2(turm) - rshift),
                                                                                     2 ** (math.log2(turm) + lshift))

    legale_turm_zuge = vertikales_movement | horizontales_movement
    return legale_turm_zuge


def get_legale_damen_zuge(dame, figuren, ist_weiss_am_zug):
    return get_legale_laufer_zuge(dame, figuren, ist_weiss_am_zug) | get_legale_turm_zuge(dame, figuren,
                                                                                          ist_weiss_am_zug)


def get_legale_konig_zuge(konig, figuren, ist_weiss_am_zug):
    # Same as pferde movement
    legal_moves = get_shift_movement_operation_pferd(konig, figuren, 1, 0, operator.lshift, operator.rshift,
                                                     ist_weiss_am_zug) | get_shift_movement_operation_pferd(konig,
                                                                                                            figuren, 1,
                                                                                                            0,
                                                                                                            operator.rshift,
                                                                                                            operator.lshift,
                                                                                                            ist_weiss_am_zug)

    legal_moves_down = get_shift_movement_operation_pferd(konig, figuren, 7, 1, operator.lshift, operator.rshift,
                                                          ist_weiss_am_zug) | \
                       get_shift_movement_operation_pferd(konig, figuren, 8, 1, operator.lshift, operator.rshift,
                                                          ist_weiss_am_zug) | \
                       get_shift_movement_operation_pferd(konig, figuren, 9, 1, operator.lshift, operator.rshift,
                                                          ist_weiss_am_zug)

    legal_moves_up = get_shift_movement_operation_pferd(konig, figuren, 7, 1, operator.rshift, operator.lshift,
                                                        ist_weiss_am_zug) | \
                     get_shift_movement_operation_pferd(konig, figuren, 8, 1, operator.rshift, operator.lshift,
                                                        ist_weiss_am_zug) | \
                     get_shift_movement_operation_pferd(konig, figuren, 9, 1, operator.rshift, operator.lshift,
                                                        ist_weiss_am_zug)

    return legal_moves | legal_moves_up | legal_moves_down


# ------------------------------------- Help Funktionen für Figuren movement ------------------------------------
def get_shift_movement_operation(figur, figuren, shift_number, operator, ist_weiss_am_zug, figurname, lower_limit,
                                 upper_limit):
    legale_zuge = 0
    schachbrett = get_schachbrett(figuren)
    temp_figur = figur

    while True:
        temp_figur = operator(temp_figur, shift_number)

        # if figurname == "_la":  # Ausnahmefall für Läufer berechnungen (verhidnert übern Rand schlagen)
        #     if temp_figur & laufer_end_calculation_maske != 0:
        #         return legale_zuge
        if temp_figur.bit_length() > 64:
            break

        if temp_figur & schachbrett == 0:
            legale_zuge = legale_zuge | temp_figur
        else:
            # Figur steht auf dem Feld
            # Ist sie feindlich füge hinzu, sonst brich ab
            if ist_weiss_am_zug:
                if temp_figur & get_schwarz_figuren_maske(figuren):
                    legale_zuge = legale_zuge | temp_figur
                return legale_zuge
            else:
                if temp_figur & get_weis_figuren_maske(figuren):
                    legale_zuge = legale_zuge | temp_figur
                return legale_zuge

        if figurname == "_la":  # Ausnahmefall für Läufer berechnungen (verhidnert übern Rand schlagen)
            if temp_figur & laufer_end_calculation_maske != 0:
                return legale_zuge

        if temp_figur <= lower_limit or temp_figur >= upper_limit:
            break

    return legale_zuge


def get_shift_movement_operation_pferd(pferd, figuren, shift_numer, byte_shifts, operator_shift,
                                       controll_operator_shift, ist_weiss_am_zug):
    legaler_zug = 0
    schachbrett = get_schachbrett(figuren)
    temp_figur = pferd
    pferd_byte_pos = math.ceil(pferd.bit_length() / 8)
    temp_figur = operator_shift(temp_figur, shift_numer)

    # ist Byte BYte_shifts höhfer/niedriger als Pferd?
    if pferd_byte_pos == math.ceil(controll_operator_shift(temp_figur, byte_shifts * 8).bit_length() / 8):

        # Pferd zug is korrekt
        if temp_figur & schachbrett == 0:
            legaler_zug = temp_figur
        else:
            if ist_weiss_am_zug:
                if temp_figur & get_schwarz_figuren_maske(figuren):
                    legaler_zug = temp_figur
            else:
                if temp_figur & get_weis_figuren_maske(figuren):
                    legaler_zug = temp_figur

    return legaler_zug & uber_brett_hinaus_maske


# ------------------------------------- Figuren Zug ausführungs Funktionen ------------------------------------
def bewege_figur(zug_start_pos, zug_ziel_pos, figuren, ist_weis_am_zug, figurname):
    if zug_start_pos.bit_length() > 66 or zug_ziel_pos.bit_length() > 66:
        print("ERROR: ")
        print(bin(zug_start_pos), bin(zug_ziel_pos), ist_weis_am_zug, figurname)

    if ist_weis_am_zug:
        # Wurde eine Figur genommen?
        if zug_ziel_pos & get_schwarz_figuren_maske(figuren):
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
        temp = figuren[figurname] ^ zug_start_pos
        figuren[figurname] = temp | zug_ziel_pos
    else:
        if zug_ziel_pos & get_weis_figuren_maske(figuren):
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
        temp = figuren[figurname] ^ zug_start_pos
        figuren[figurname] = temp | zug_ziel_pos

    return figuren


# ------------------------------------- Figuren & Schachbrett Masken Funktionen -------------------------------
def set_schachbrett_variablen(t_schachbrett_groesse, t_schachbrett_groesse_wurzel):
    global schachbrett_groesse, schachbrett_groesse_wurzel

    schachbrett_groesse = t_schachbrett_groesse
    schachbrett_groesse_wurzel = t_schachbrett_groesse_wurzel


def set_biggest_single_bit(schachbrett_groesse):
    global biggest_single_bit_number

    biggest_single_bit_number = int(bin(2 ** (schachbrett_groesse - 1)), 2)


def get_schachbrett(figuren):
    schachbrett = 0

    for figur in figuren:
        schachbrett = schachbrett | figuren[figur]

    return schachbrett


def get_schwarz_figuren_maske(figuren):
    schwarz_figuren_maske = 0

    for figur in figuren:
        if "s_" in figur:
            schwarz_figuren_maske = schwarz_figuren_maske | figuren[figur]

    return schwarz_figuren_maske


def get_weis_figuren_maske(figuren):
    weis_figuren_maske = 0

    for figur in figuren:
        if "w_" in figur:
            weis_figuren_maske = weis_figuren_maske | figuren[figur]

    return weis_figuren_maske


# ------------------------------------- Figuren & Schachbrett zu Koordinaten -------------------------------
def get_koordinaten_format(aktuelle_figuren, ziel_position_figuren, ist_weiss_am_zug):
    figuren = aktuelle_figuren
    best_move_figuren = ziel_position_figuren
    temp = 97 + schachbrett_groesse_wurzel + schachbrett_groesse_wurzel - 1
    counter1 = 0
    counter2 = 0

    start_pos = 0
    ziel_pos = 0
    key = 0  # Figur die bewegt wurde

    for figur in figuren:
        if ist_weiss_am_zug:
            if "w_" in figur:
                if figuren[figur] != best_move_figuren[figur]:
                    key = figur
                    move = figuren[key] ^ best_move_figuren[key]

                    start_pos = move & figuren[key]
                    ziel_pos = move & best_move_figuren[key]
        else:
            if "s_" in figur:
                if figuren[figur] != best_move_figuren[figur]:
                    key = figur
                    move = figuren[key] ^ best_move_figuren[key]

                    start_pos = move & figuren[key]
                    ziel_pos = move & best_move_figuren[key]

    # Koordinaten Start
    start_koordinate_buchstaben = int(temp - (schachbrett_groesse_wurzel + math.log2(start_pos) % 8))
    while start_pos > 0:
        counter1 = counter1 + 1
        start_pos = start_pos >> schachbrett_groesse_wurzel

    # Koordinaten Ziel
    ziel_koordinaten_buchstaben = int(temp - (schachbrett_groesse_wurzel + math.log2(ziel_pos) % 8))
    while ziel_pos > 0:
        counter2 = counter2 + 1
        ziel_pos = ziel_pos >> schachbrett_groesse_wurzel

    return [chr(start_koordinate_buchstaben), counter1, chr(ziel_koordinaten_buchstaben), counter2]


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


# -------------------------------------------- Bester Zug Funktion --------------------------------------------

def init_bot(schachbrett_groesse, schachbrett_groesse_wurzel, figuren):
    # --- Setter ---
    # Wird nur beim ersten Aufrufen ausgeführt
    set_schachbrett_variablen(schachbrett_groesse, schachbrett_groesse_wurzel)
    set_biggest_single_bit(schachbrett_groesse)
