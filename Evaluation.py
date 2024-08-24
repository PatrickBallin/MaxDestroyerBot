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
"""

# -------------------------------------------- 0. imports ----------------------------------------------------
import math
import operator

# -------------------------------------------- Hilfsvariablen ----------------------------------------------------
laufer_end_calculation_maske = int("1000000110000001100000011000000110000001100000011000000110000001", 2)
uber_brett_hinaus_maske = int("1111111111111111111111111111111111111111111111111111111111111111", 2)

# -------------------------------------------- 1. Aufabu ----------------------------------------------------
schachbrett_groesse = 0
schachbrett_groesse_wurzel = 0

biggest_single_bit_number = 0

doppel_move_weis_maske = int("0000000000000000000000000000000000000000000000001111111100000000", 2)
doppel_move_schwarz_maske = int("0000000011111111000000000000000000000000000000000000000000000000", 2)

is_global_variablen_gesetzt = False

counter = 0


# -------------------------------------------- 2. Beast Mode ----------------------------------------------------
# ################ Weights #################

bauer_gewichtung = 1
laufer_gewichtung = 3.2
pferd_gewichtung = 3
turm_gewichtung = 5
damen_gewichtung = 8
konig_gewichtung = 1000

# ################ Weights #################


def evaluiere_schachbrett(figuren):
    gesamtwert_weiss = 0
    gesamtwert_schwarz = 0

    # 1. Iterriere Über jede Figur:
    for figur in figuren:

        # A: Ist die Figur weiss:
        if "w_" in figur:
            if "_ba" in figur:
                number_of_bits = bin(figuren[figur]).count("1")
                gesamtwert_weiss += number_of_bits
            elif "_la" in figur:
                number_of_bits = bin(figuren[figur]).count("1")
                gesamtwert_weiss += number_of_bits * laufer_gewichtung
            elif "_pf" in figur:
                number_of_bits = bin(figuren[figur]).count("1")
                gesamtwert_weiss += number_of_bits * pferd_gewichtung
            elif "_tu" in figur:
                number_of_bits = bin(figuren[figur]).count("1")
                gesamtwert_weiss += number_of_bits * turm_gewichtung
            elif "_da" in figur:
                number_of_bits = bin(figuren[figur]).count("1")
                gesamtwert_weiss += number_of_bits * damen_gewichtung
            elif "_ko" in figur:
                number_of_bits = bin(figuren[figur]).count("1")
                gesamtwert_weiss += number_of_bits * konig_gewichtung

        #   B: Ist die Figur Schwarz:
        if "s_" in figur:
            if "_ba" in figur:
                number_of_bits = bin(figuren[figur]).count("1")
                gesamtwert_schwarz += number_of_bits
            elif "_la" in figur:
                number_of_bits = bin(figuren[figur]).count("1")
                gesamtwert_schwarz += number_of_bits * laufer_gewichtung
            elif "_pf" in figur:
                number_of_bits = bin(figuren[figur]).count("1")
                gesamtwert_schwarz += number_of_bits * pferd_gewichtung
            elif "_tu" in figur:
                number_of_bits = bin(figuren[figur]).count("1")
                gesamtwert_schwarz += number_of_bits * turm_gewichtung
            elif "_da" in figur:
                number_of_bits = bin(figuren[figur]).count("1")
                gesamtwert_schwarz += number_of_bits * damen_gewichtung
            elif "_ko" in figur:
                number_of_bits = bin(figuren[figur]).count("1")
                gesamtwert_schwarz += number_of_bits * konig_gewichtung

    return gesamtwert_weiss - gesamtwert_schwarz


# TODO: !!!!!!!!!!!!!!!!!!! Veraltet !!!!!!!!!!!!!!!!!!!
# def berechne_besten_zug(figuren, ist_weiss_am_zug, zug_tiefe):
#     best_move_figuren = []
#     best_move_wert = 0
#     global counter
#
#     if ist_weiss_am_zug:
#         turn = "w_"
#         best_move_wert = -10**17
#     else:
#         turn = "s_"
#         best_move_wert = 10**17
#
#     for figur in figuren:
#         # Für welche Farbe sollen alle Züge berechnet werden
#         if turn in figur:
#
#             # Um Welche Figur handelt es sich?
#             if "_ba" in figur:
#                 # iterrie Über jede Figur(1) in diesen Figuren (00001111)
#                 bsb_iterator_bauern = biggest_single_bit_number
#
#                 while bsb_iterator_bauern > 0:
#                     if bsb_iterator_bauern & figuren[figur]:
#                         bauer = bsb_iterator_bauern & figuren[figur]  # bauer = 0000 1000
#                         bsb_iterator_bauern_zuege = biggest_single_bit_number  # Um über jeden Möglichen Zug der Figur zu iterriern
#
#                         # Get alle legalen Züge von diesem einzelnen Bauern
#                         legale_bauer_zuge = get_legale_bauern_zuege(bauer, figuren, ist_weiss_am_zug)
#                         if legale_bauer_zuge is None:
#                             bsb_iterator_bauern = bsb_iterator_bauern >> 1
#                             continue
#
#                         # 1. Itiere Über jeden Zug und berechne Figuren
#                         while bsb_iterator_bauern_zuege > 0:
#                             if bsb_iterator_bauern_zuege & legale_bauer_zuge:
#                                 # dann handelt es sich um einen legalen Zug vom Bauern
#                                 # Zug ist von bsb_iterator_bauern nach bsb_iterator_bauern_zuege
#                                 # Berechne Figuren von diesem Zug
#                                 temp_figuren = bewege_figur(bsb_iterator_bauern, bsb_iterator_bauern_zuege,
#                                                             dict(figuren), ist_weiss_am_zug, "_ba")
#
#                                 # Evaluiere Wert von Zug
#                                 zug_wert = evaluiere_schachbrett(temp_figuren)
#
#                                 # TODO: 2. Tiefe einbauen Versuch: 1
#                                 if zug_tiefe > 1:
#                                     # Berechne daraufgolgende Züge
#                                     best_folgender_zug = berechne_besten_zug(temp_figuren, not ist_weiss_am_zug,
#                                                                              zug_tiefe - 1)
#                                     best_move_gegner = best_folgender_zug[0]
#
#                                     # Berechne Zug + bester folgender gegnerischer Zug
#                                     # und return die höchste Summe für weis und niedrigste für schwarz
#
#                                     zug_wert = zug_wert + best_move_gegner
#
#                                 # weiß will möglichst hohen Wert > 0
#                                 if ist_weiss_am_zug:
#                                     if zug_wert > best_move_wert:
#                                         best_move_wert = zug_wert
#                                         best_move_figuren = temp_figuren
#                                         # print("Best White: ", zug_wert,
#                                         #       [bin(i) for i in best_move_figuren.values()])
#                                 # schwarz will möglichst niedrigen Wert < 0
#                                 else:
#                                     if zug_wert < best_move_wert:
#                                         # print("Bester Move Wert Schwarz: tiefe", zug_tiefe, "Wert", zug_wert)
#                                         best_move_wert = zug_wert
#                                         best_move_figuren = temp_figuren
#
#                             # Nächster Zug
#                             bsb_iterator_bauern_zuege = bsb_iterator_bauern_zuege >> 1
#
#                     # Näcshter Bauer
#                     bsb_iterator_bauern = bsb_iterator_bauern >> 1
#
#     # print("Return best move Wert Farbe ", "weiß" if ist_weiss_am_zug else "schwarz", best_move_wert)
#     if best_move_wert != 10**17 and best_move_wert != -10**17:
#         return [best_move_wert, best_move_figuren, figuren]
#     else:
#         return [evaluiere_schachbrett(figuren), best_move_figuren, figuren]


# TODO: !!!!!!!!!!!!!!!!!!! Neue Funktion !!!!!!!!!!!!!!!!!!!
def berechne_besten_zug(figuren, ist_weiss_am_zug, zug_tiefe):
    best_move_figuren = []
    best_move_wert = 0
    global counter

    if ist_weiss_am_zug:
        turn = "w_"
        best_move_wert = -10**17
    else:
        turn = "s_"
        best_move_wert = 10**17

    for figur in figuren:
        # Für welche Farbe sollen alle Züge berechnet werden
        if turn in figur:

            bsb_iterator_figur = biggest_single_bit_number

            while bsb_iterator_figur > 0:
                if bsb_iterator_figur & figuren[figur]:
                    figur_bit_wert = bsb_iterator_figur & figuren[figur]  # figur = 0000 1000
                    bsb_iterator_figur_zuge = biggest_single_bit_number  # Um über jeden Möglichen Zug der Figur zu iterriern

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

                    if legale_figuren_zuge is None:
                        bsb_iterator_figur = bsb_iterator_figur >> 1
                        continue

                    # 1. Itiere Über jeden Zug
                    while bsb_iterator_figur_zuge > 0:
                        if bsb_iterator_figur_zuge & legale_figuren_zuge:
                            # dann handelt es sich um einen legalen Zug vom Bauern
                            # Zug ist von bsb_iterator_bauern nach bsb_iterator_bauern_zuege
                            # Berechne Figuren von diesem Zug
                            temp_figuren = bewege_figur(figur_bit_wert, bsb_iterator_figur_zuge,
                                                        dict(figuren), ist_weiss_am_zug, figur)

                            # Evaluiere Wert von Zug
                            zug_wert = evaluiere_schachbrett(temp_figuren)

                            # TODO: 2. Tiefe einbauen Versuch: 1
                            if zug_tiefe > 1:
                                # Berechne daraufgolgende Züge
                                best_folgender_zug = berechne_besten_zug(temp_figuren, not ist_weiss_am_zug,
                                                                         zug_tiefe - 1)
                                best_move_gegner = best_folgender_zug[0]

                                # Berechne Zug + bester folgender gegnerischer Zug
                                # und return die höchste Summe für weis und niedrigste für schwarz

                                zug_wert = zug_wert + best_move_gegner

                            # weiß will möglichst hohen Wert > 0
                            if ist_weiss_am_zug:
                                if zug_wert > best_move_wert:
                                    best_move_wert = zug_wert
                                    best_move_figuren = temp_figuren
                                    # print("Best White: ", zug_wert,
                                    #       [bin(i) for i in best_move_figuren.values()])
                            # schwarz will möglichst niedrigen Wert < 0
                            else:
                                if zug_wert < best_move_wert:
                                    # print("Bester Move Wert Schwarz: tiefe", zug_tiefe, "Wert", zug_wert)
                                    best_move_wert = zug_wert
                                    best_move_figuren = temp_figuren

                        # Nächster Zug
                        bsb_iterator_figur_zuge = bsb_iterator_figur_zuge >> 1

                # Näcshter Bauer
                bsb_iterator_figur = bsb_iterator_figur >> 1

    # print("Return best move Wert Farbe ", "weiß" if ist_weiss_am_zug else "schwarz", best_move_wert)
    if best_move_wert != 10**17 and best_move_wert != -10**17:
        return [best_move_wert, best_move_figuren, figuren]
    else:
        return [evaluiere_schachbrett(figuren), best_move_figuren, figuren]


# -------------------------------------------- Figuren Legale Züge --------------------------------------------
def get_legale_bauern_zuege(bauer, figuren, ist_weiss_am_zug):
    # Möglichkeiten an Bauern züge
    legale_bauern_zuge = 0
    schachbrett = get_schachbrett(figuren)

    if ist_weiss_am_zug:
        # normal fall weis Bauer bewegt sich um eins nach vorne
        # Steht etwas auf diesem Feld
        if (bauer << schachbrett_groesse_wurzel) & schachbrett == 0:
            legale_bauern_zuge = bauer << schachbrett_groesse_wurzel

        # Doppel Sprung
        if (bauer << (schachbrett_groesse_wurzel * 2) | (
                bauer << schachbrett_groesse_wurzel)) & schachbrett == 0:
            # falls der Bauer am Anfang steht
            if bauer & doppel_move_weis_maske:
                temp = bauer << (schachbrett_groesse_wurzel * 2)
                legale_bauern_zuge = legale_bauern_zuge | temp

        # Attack Move
        gegnerische_figuren = get_schwarz_figuren_maske(figuren)

        # Fall Angriff: Steht diagonal links ein Gegner dann füge zuege hinzu
        angriff_diagonal_links = bauer << (schachbrett_groesse_wurzel + 1)

        # Links darf nur geschlagen werden wenn log(bauer) % Wurzel != Wurzel - 1 ist (verhindert übern Rand schlagen)
        if math.log2(bauer) % schachbrett_groesse_wurzel != schachbrett_groesse_wurzel - 1:
            # Steht eine Gengerische Figur links diagonal
            if angriff_diagonal_links & gegnerische_figuren != 0:
                legale_bauern_zuge = legale_bauern_zuge | angriff_diagonal_links

        # Fall Angriff: Steht diagonal rechts ein Gegner dann füge zuege hinzu
        angriff_diagonal_rechts = bauer << (schachbrett_groesse_wurzel - 1)

        # Kein schlagen über die Brett KAnte
        if math.log2(bauer) % schachbrett_groesse_wurzel != 0:
            if angriff_diagonal_rechts & gegnerische_figuren != 0:
                legale_bauern_zuge = legale_bauern_zuge | angriff_diagonal_rechts
    else:
        # Schwarz am Zug
        # normal fall schwarz Bauer bewegt sich um eins nach vorne
        # Steht etwas auf diesem Feld
        if (bauer >> schachbrett_groesse_wurzel) & schachbrett == 0:
            legale_bauern_zuge = bauer >> schachbrett_groesse_wurzel

        # Doppel Sprung
        if (bauer >> (schachbrett_groesse_wurzel * 2) | (
                bauer >> schachbrett_groesse_wurzel)) & schachbrett == 0:
            # falls der Bauer am Anfang steht
            if bauer & doppel_move_schwarz_maske:
                temp = bauer >> (schachbrett_groesse_wurzel * 2)
                legale_bauern_zuge = legale_bauern_zuge | temp

        # Attack Move
        gegnerische_figuren = get_weis_figuren_maske(figuren)

        # Fall Angriff: Steht diagonal links ein Gegner dann füge zuege hinzu
        angriff_diagonal_links = bauer >> (schachbrett_groesse_wurzel + 1)

        # Links darf nur geschlagen werden wenn log(bauer) % Wurzel != Wurzel - 1 ist (verhindert übern Rand schlagen)
        if math.log2(bauer) % schachbrett_groesse_wurzel != 0:
            # Steht eine Gengerische Figur links diagonal
            if angriff_diagonal_links & gegnerische_figuren != 0:
                legale_bauern_zuge = legale_bauern_zuge | angriff_diagonal_links

        # Fall Angriff: Steht diagonal rechts ein Gegner dann füge zuege hinzu
        angriff_diagonal_rechts = bauer >> (schachbrett_groesse_wurzel - 1)

        # Kein schlagen über die Brett KAnte
        if math.log2(bauer) % schachbrett_groesse_wurzel != schachbrett_groesse_wurzel - 1:
            if angriff_diagonal_rechts & gegnerische_figuren != 0:
                legale_bauern_zuge = legale_bauern_zuge | angriff_diagonal_rechts

    return legale_bauern_zuge


def get_legale_laufer_zuge(laufer, figuren, ist_weiss_am_zug):
    legale_laufer_zuge = get_shift_movement_operation(laufer, figuren, 7, operator.lshift,
                                                      ist_weiss_am_zug, "_la", 0, biggest_single_bit_number) \
                         | get_shift_movement_operation(laufer, figuren, 9, operator.lshift,
                                                        ist_weiss_am_zug, "_la", 0, biggest_single_bit_number) \
                         | get_shift_movement_operation(laufer, figuren, 7, operator.rshift,
                                                        ist_weiss_am_zug, "_la", 0, biggest_single_bit_number) \
                         | get_shift_movement_operation(laufer, figuren, 9, operator.rshift,
                                                        ist_weiss_am_zug, "_la", 0, biggest_single_bit_number)

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


# def bewege_bauer(zug_start_pos, zug_ziel_pos, figuren, ist_weis_am_zug):
#     # welche Figur bewegt sich? --> Figurname wird übergeben!
#     #
#
#     # Weiß am Zug
#     if ist_weis_am_zug:
#         # Weis hat Figur genommen
#         if zug_ziel_pos & get_schwarz_figuren_maske(figuren):
#             # !!! WELCHE FIGUR Oder für jede figur das ausführen?!!!
#             figuren["s_ba"] = zug_ziel_pos ^ figuren["s_ba"]
#
#         # Zug Ziel position aktualisieren
#         temp = figuren["w_ba"] ^ zug_start_pos
#         figuren["w_ba"] = temp | zug_ziel_pos
#     else:
#         # Schwarz hat Figur genommen
#         if zug_ziel_pos & get_weis_figuren_maske(figuren):
#             figuren["w_ba"] = zug_ziel_pos ^ figuren["w_ba"]
#
#         # Zug Ziel position aktualisieren
#         temp = figuren["s_ba"] ^ zug_start_pos
#         figuren["s_ba"] = temp | zug_ziel_pos
#
#     return figuren


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
        bit_number = int(bin(2**(schachbrett_groesse - 1)), 2)
        for i in range(schachbrett_groesse):
            if figuren[figur] & bit_number:
                schachbrett_darstellung_mit_bezeichnungen[i] = figur
            bit_number = bit_number >> 1

    for i in range(0, schachbrett_groesse, schachbrett_groesse_wurzel):
        print(schachbrett_darstellung_mit_bezeichnungen[i: i + schachbrett_groesse_wurzel], end="")
        if i % schachbrett_groesse_wurzel == 0:
            print()


# -------------------------------------------- Bester Zug Funktion --------------------------------------------
def beast_get_best_move(figuren, ist_weiss_am_zug, zug_tiefe):
    # --- Best Move ---
    best_move = berechne_besten_zug(figuren, ist_weiss_am_zug, zug_tiefe)

    # Sollte es keinen Legalen Move mehr geben:
    if not best_move[1]:
        return 0

    # print(best_move[1])
    # print(best_move[2])
    # print("ZUG VON: ")
    # print_custom_schachbrett_mit_bezeichnungen(best_move[2])
    # print("NACH: ")
    # print_custom_schachbrett_mit_bezeichnungen(best_move[1])
    best_move_koordinaten = get_koordinaten_format(best_move[2], best_move[1], ist_weiss_am_zug)

    print("-------- Max Killer Bot --------")
    print("Bester Move Wert: ", best_move[0])
    print("BeastZug: ", best_move_koordinaten[0], best_move_koordinaten[1], " --> ", best_move_koordinaten[2],
          best_move_koordinaten[3])

    # --- Überprüfung ---
    brett_evaluierung = evaluiere_schachbrett(figuren)
    print("Jetzige Schachbrett Evaluierung:", brett_evaluierung)

    return [best_move_koordinaten[0], best_move_koordinaten[1], best_move_koordinaten[2], best_move_koordinaten[3]]


def init_bot(schachbrett_groesse, schachbrett_groesse_wurzel, figuren):
    # --- Setter ---
    # Wird nur beim ersten Aufrufen ausgeführt
    set_schachbrett_variablen(schachbrett_groesse, schachbrett_groesse_wurzel)
    set_biggest_single_bit(schachbrett_groesse)
