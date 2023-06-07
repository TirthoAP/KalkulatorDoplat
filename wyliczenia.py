# Projekt kalkulator do wyliczania płatności bezpośrednich

# by Tirtho

# Wersja próbna 1.0

# Konin, marzec, 2023r.


import sqlite3
#import psycopg2
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# utworzenie połączenia z bazą przechowywaną na dysku
con = sqlite3.connect('db.sqlite3')
# dostęp do kolumn przez indeksy i przez nazwy
con.row_factory = sqlite3.Row
# utworzenie obiektu kursora
cur = con.cursor()

user = User.objects.get(id)
if user.is_authenticated:
    # pobieranie danych z bazy
    cur.execute("SELECT * FROM Kalkulator_platnoscjpo WHERE id = user.id;")
    rows = cur.fetchall()
    for row in rows:
        powierzchnia_gospodarstwa = float(str(row[1]))
        zmniejszenia_jpo = float(str(row[2]))
        powierzchnia_po_zmniejszeniach = float(powierzchnia_gospodarstwa) - float(zmniejszenia_jpo)

    if float(powierzchnia_po_zmniejszeniach) > 3.00:
        if float(powierzchnia_po_zmniejszeniach) > 30.00:
            zmniejszenia_redystrybucja = 0
        else:
            zmniejszenia_redystrybucja = zmniejszenia_jpo
    else:
        zmniejszenia_redystrybucja = 0

    cur.execute("SELECT * FROM Kalkulator_platnoscupp WHERE id = user.id;")
    rows = cur.fetchall()
    for row in rows:
        powierzchnia_upp = float(str(row[1]))
        zmniejszenia_upp = float(str(row[2]))


    cur.execute("SELECT * FROM Kalkulator_platnoscjpo WHERE id = user.id;")
    rows = cur.fetchall()
    for row in rows:
        czy_mr = str(row[3])

    powierzchnia_mr = powierzchnia_gospodarstwa
    zmniejszenia_mr = zmniejszenia_jpo

    cur.execute("SELECT * FROM Kalkulator_platnoscp_str WHERE id = user.id;")
    rows = cur.fetchall()
    for row in rows:
        powierzchnia_p_str = float(str(row[1]))
        zmniejszenia_p_str = float(str(row[2]))

    cur.execute("SELECT * FROM Kalkulator_platnoscp_pas WHERE id = user.id;")
    rows = cur.fetchall()
    for row in rows:
        powierzchnia_p_pas = float(str(row[1]))
        zmniejszenia_p_pas = float(str(row[2]))

    cur.execute("SELECT * FROM Kalkulator_platnoscp_burak WHERE id = user.id;")
    rows = cur.fetchall()
    for row in rows:
        powierzchnia_p_burak = float(str(row[1]))
        zmniejszenia_p_burak = float(str(row[2]))

    cur.execute("SELECT * FROM Kalkulator_platnoscp_skrobia WHERE id = user.id;")
    rows = cur.fetchall()
    for row in rows:
        powierzchnia_p_skrobia = float(str(row[1]))
        zmniejszenia_p_skrobia = float(str(row[2]))

    cur.execute("SELECT * FROM Kalkulator_platnoscp_truskawka WHERE id = user.id;")
    rows = cur.fetchall()
    for row in rows:
        powierzchnia_p_truskawka = float(str(row[1]))
        zmniejszenia_p_truskawka = float(str(row[2]))

    cur.execute("SELECT * FROM Kalkulator_platnoscpomidor WHERE id = user.id;")
    rows = cur.fetchall()
    for row in rows:
        powierzchnia_pomidor = float(str(row[1]))
        zmniejszenia_pomidor = float(str(row[2]))

    cur.execute("SELECT * FROM Kalkulator_platnoscchmiel WHERE id = user.id;")
    rows = cur.fetchall()
    for row in rows:
        powierzchnia_chmiel = float(str(row[1]))
        zmniejszenia_chmiel = float(str(row[2]))

    cur.execute("SELECT * FROM Kalkulator_platnosclen WHERE id = user.id;")
    rows = cur.fetchall()
    for row in rows:
        powierzchnia_len = float(str(row[1]))
        zmniejszenia_len = float(str(row[2]))

    cur.execute("SELECT * FROM Kalkulator_platnosckonopie WHERE id = user.id;")
    rows = cur.fetchall()
    for row in rows:
        powierzchnia_konopie = float(str(row[1]))
        zmniejszenia_konopie = float(str(row[2]))

    cur.execute("SELECT * FROM Kalkulator_platnosckrowy WHERE id = user.id;")
    rows = cur.fetchall()
    for row in rows:
        liczba_krow = float(str(row[1]))
        zmniejszenia_krowy = float(str(row[2]))
        liczba_krow_po_zmniejszeniach = float(liczba_krow) - float(zmniejszenia_krowy)

    cur.execute("SELECT * FROM Kalkulator_platnoscbydlo WHERE id = user.id;")
    rows = cur.fetchall()
    for row in rows:
        liczba_bydla = float(str(row[1]))
        zmniejszenia_bydlo = float(str(row[2]))
        liczba_bydla_po_zmniejszeniach = float(liczba_bydla) - float(zmniejszenia_bydlo)

    cur.execute("SELECT * FROM Kalkulator_platnosckozy WHERE id = user.id;")
    rows = cur.fetchall()
    for row in rows:
        liczba_koz = float(str(row[1]))
        zmniejszenia_koz = float(str(row[2]))
        liczba_koz_po_zmniejszeniach = float(liczba_koz) - float(zmniejszenia_koz)

    cur.execute("SELECT * FROM Kalkulator_platnoscowce WHERE id = user.id;")
    rows = cur.fetchall()
    for row in rows:
        liczba_owiec = float(str(row[1]))
        zmniejszenia_owiec = float(str(row[2]))
        liczba_owiec_po_zmniejszeniach = float(liczba_owiec) - float(zmniejszenia_owiec)

    cur.execute("SELECT * FROM Kalkulator_sankcjacc WHERE id = user.id;")
    rows = cur.fetchall()
    for row in rows:
        sankcja_cc = float(str(row[1]))

    cur.execute("SELECT * FROM Kalkulator_sankcjaterminowa WHERE id = user.id;")
    rows = cur.fetchall()
    for row in rows:
        sankcje_terminowe = float(str(row[1]))

# Stawki płatności
stawki_platnosci = {
    'jpo': 518.01,
    'zazielenienie': 347.66,
    'redystrybucja': 196.14,
    'upp': 41.1,
    'mr': 360.91,
    'p_str': 673.5,
    'p_pas': 515.26,
    'p_burak': 1806.58,
    'p_skrobia': 1761.46,
    'p_truskawka': 1575.39,
    'pomidory': 3601.68,
    'chmiel': 2257.46,
    'len': 748.91,
    'konopie': 274.82,
    'krowy': 467.35,
    'bydło': 363.16,
    'kozy': 51.05,
    'owce': 121.47,
    'tytoń Virginia': 3.38,
    'tytoń': 2.44,
    }

# Sumowanie zmniejszeń
zmniejszenia = float(zmniejszenia_jpo) + float(zmniejszenia_redystrybucja) + float(zmniejszenia_upp) + float(zmniejszenia_mr) + float(zmniejszenia_p_burak) + float(zmniejszenia_p_skrobia)+ float(zmniejszenia_p_str) + float(zmniejszenia_p_pas) + float(zmniejszenia_p_truskawka) + float(zmniejszenia_pomidor) + float(zmniejszenia_chmiel) + float(zmniejszenia_len) + float(zmniejszenia_konopie)

# Wyliczanie płatności JPO
powierzchnia_po_zmniejszeniach = float(powierzchnia_gospodarstwa) - float(zmniejszenia_jpo)
if float(powierzchnia_gospodarstwa) == 0.0:
    procent_zmniejszenia = 0
elif float(zmniejszenia_jpo) == float(powierzchnia_gospodarstwa):
    procent_zmniejszenia = 0
else:
    procent_zmniejszenia = (float(zmniejszenia_jpo) / float(powierzchnia_po_zmniejszeniach) * 100)


if float(zmniejszenia) <= 0.10:
    platnosc_jpo = float(powierzchnia_gospodarstwa) * float(stawki_platnosci['jpo'])
else:
    if float(procent_zmniejszenia) < 3:
        platnosc_jpo = float(powierzchnia_po_zmniejszeniach) * float(stawki_platnosci['jpo'])
    elif float(procent_zmniejszenia) > 10:
        platnosc_jpo = (float(powierzchnia_po_zmniejszeniach) - (float(zmniejszenia_jpo) * 1.5)) * float(stawki_platnosci['jpo'])
    else:
        platnosc_jpo = (float(powierzchnia_po_zmniejszeniach) - (float(zmniejszenia_jpo) * 0.75)) * float(stawki_platnosci['jpo'])

# Wyliczenie płatności JPO po sankcjach terminowych i CC
platnoc_jpo_po_sankcjach = (float(platnosc_jpo) * ((100 - float(sankcje_terminowe)) / 100)) * ((100 - float(sankcja_cc)) / 100)

# Wyliczenie płatności za Zazielenienie
platnosc_zazielenienie = (float(powierzchnia_po_zmniejszeniach)) * float(stawki_platnosci['zazielenienie'])

# Wyliczanie płatności za Zazielenienie po sankcjach terminowych i CC
platnosc_zazielenienie_po_sankcjach = (float(platnosc_zazielenienie) * ((100 - float(sankcje_terminowe)) / 100)) * ((100 - float(sankcja_cc)) / 100)

# Wyliczenie płatności Redystrybucyjnej
platnosc_redystrybucyjna = 0
if float(zmniejszenia) <= 0.10:
    if float(powierzchnia_po_zmniejszeniach) > 3.00:
        if float(powierzchnia_po_zmniejszeniach) > 30.00:
            platnosc_redystrybucyjna = 27 * float(stawki_platnosci['redystrybucja'])
        else:
            platnosc_redystrybucyjna = (float(powierzchnia_gospodarstwa) - 3) * float(stawki_platnosci['redystrybucja'])
    else:
        platnosc_redystrybucyjna = 0
else:
    if float(powierzchnia_po_zmniejszeniach) > 3.00:
        if float(powierzchnia_po_zmniejszeniach) > 30.00:
            platnosc_redystrybucyjna = 27 * float(stawki_platnosci['redystrybucja'])
        else:
            if float(procent_zmniejszenia) < 3:
                platnosc_redystrybucyjna = (float(powierzchnia_po_zmniejszeniach) - 3) * float(stawki_platnosci['redystrybucja'])
            elif float(procent_zmniejszenia) > 10:
                platnosc_redystrybucyjna = ((float(powierzchnia_po_zmniejszeniach) - 3) - (float(zmniejszenia_jpo) * 1.5)) * float(stawki_platnosci['redystrybucja'])
            else:
                platnosc_redystrybucyjna = ((float(powierzchnia_po_zmniejszeniach) - 3) - (float(zmniejszenia_jpo) * 0.75)) * float(stawki_platnosci['redystrybucja'])
    else:
        platnosc_redystrybucyjna = 0

# Wyliczanie płatności za Redystrybucyjna po sankcjach terminowych i CC
platnosc_redystrybucyjna_po_sankcjach = (float(platnosc_redystrybucyjna) * ((100 - float(sankcje_terminowe)) / 100)) * ((100 - float(sankcja_cc)) / 100)

# Wyliczanie płatności UPP
powierzchnia_upp_po_zmniejszeniach = float(powierzchnia_upp) - float(zmniejszenia_upp)

# Przedstawinie powierzchni po zmniejszeniach oraz procentowego udziału zmniejszeń
if float(powierzchnia_upp) == 0:
    procent_zmniejszenia_upp = 0
else:
    procent_zmniejszenia_upp = (float(zmniejszenia_upp) / float(powierzchnia_upp_po_zmniejszeniach) * 100)

platnosc_upp = 0
if float(zmniejszenia) <= 0.10:
    platnosc_upp = float(powierzchnia_upp) * float(stawki_platnosci['upp'])
else:
    if float(procent_zmniejszenia_upp) < 3:
        platnosc_upp = float(powierzchnia_upp_po_zmniejszeniach) * float(stawki_platnosci['upp'])
    elif float(procent_zmniejszenia_upp) > 20:
        platnosc_upp = 0
    else:
        platnosc_upp = (float(powierzchnia_upp_po_zmniejszeniach) - (float(zmniejszenia_upp) * 2)) * float(stawki_platnosci['upp'])

# Wyliczenie płatności UPP po sankcjach terminowych i CC
platnoc_upp_po_sankcjach = (float(platnosc_upp) * ((100 - float(sankcje_terminowe)) / 100)) * ((100 - float(sankcja_cc)) / 100)

# Wyliczanie płatności MR
platnosc_mr = 0
if czy_mr == 'tak':
    if float(zmniejszenia) <= 0.10:
        platnosc_mr = float(powierzchnia_gospodarstwa) * float(stawki_platnosci['mr'])
    else:
        if float(procent_zmniejszenia) < 3:
            platnosc_mr = powierzchnia_po_zmniejszeniach * float(stawki_platnosci['mr'])
        elif float(procent_zmniejszenia) > 10:
            platnosc_mr = (float(powierzchnia_po_zmniejszeniach) - (float(zmniejszenia_jpo) * 1.5)) * float(stawki_platnosci['mr'])
        else:
            platnosc_mr = (float(powierzchnia_po_zmniejszeniach) - (float(zmniejszenia_jpo) * 0.75)) * float(
                stawki_platnosci['mr'])

    # Wyliczenie płatności MR po sankcjach terminowych i CC
    if float(powierzchnia_po_zmniejszeniach) <= 50:
        platnoc_mr_po_sankcjach = (float(platnosc_mr) * ((100 - float(sankcje_terminowe)) / 100)) * ((100 - float(sankcja_cc)) / 100)
    else:
        platnoc_mr_po_sankcjach = (50 * float(stawki_platnosci['mr']) * ((100 - float(sankcje_terminowe)) / 100)) * ((100 - float(sankcja_cc)) / 100)
else:
    platnoc_mr_po_sankcjach = 0

# Wyliczanie płatności P_STR
powierzchnia_p_str_po_zmniejszeniach = (float(powierzchnia_p_str) - float(zmniejszenia_p_str))

# Przedstawinie powierzchni po zmniejszeniach oraz procentowego udziału zmniejszeń
if float(powierzchnia_p_str) == 0:
    procent_zmniejszenia_p_str = 0
else:
    procent_zmniejszenia_p_str = (float(zmniejszenia_p_str) / float(powierzchnia_p_str_po_zmniejszeniach) * 100)

if float(powierzchnia_p_str_po_zmniejszeniach) == 0:
    procent_zmniejszenia_p_str = 0
else:
    procent_zmniejszenia_p_str = (float(zmniejszenia_p_str) / float(powierzchnia_p_str_po_zmniejszeniach) * 100)

platnosc_p_str = 0
if float(zmniejszenia) <= 0.10:
    platnosc_p_str = float(powierzchnia_p_str) * float(stawki_platnosci['p_str'])
else:
    if float(procent_zmniejszenia_p_str) < 3:
        platnosc_p_str = float(powierzchnia_p_str_po_zmniejszeniach) * float(stawki_platnosci['p_str'])
    elif float(procent_zmniejszenia_p_str) > 20:
        platnosc_p_str = 0
    else:
        platnosc_p_str = (float(powierzchnia_p_str_po_zmniejszeniach) - (float(zmniejszenia_p_str) * 2)) * float(stawki_platnosci['p_str'])

# Wyliczenie płatności P_STR po sankcjach terminowych i CC
platnoc_p_str_po_sankcjach = ((float(platnosc_p_str) * ((100 - float(sankcje_terminowe)) / 100)) * ((100 - float(sankcja_cc)) / 100))

# Wyliczanie płatności P_PAS
powierzchnia_p_pas_po_zmniejszeniach = float(powierzchnia_p_pas) - float(zmniejszenia_p_pas)

# Przedstawinie powierzchni po zmniejszeniach oraz procentowego udziału zmniejszeń
if float(powierzchnia_p_pas) == 0:
    procent_zmniejszenia_p_pas = 0
else:
    procent_zmniejszenia_p_pas = (float(zmniejszenia_p_pas) / float(powierzchnia_p_pas_po_zmniejszeniach) * 100)


if float(powierzchnia_p_pas_po_zmniejszeniach) == 0:
    procent_zmniejszenia_p_pas = 0
else:
    procent_zmniejszenia_p_pas = (float(zmniejszenia_p_pas) / float(powierzchnia_p_pas_po_zmniejszeniach) * 100)

platnosc_p_pas = 0
if float(zmniejszenia) <= 0.10:
    platnosc_p_pas = float(powierzchnia_p_pas) * float(stawki_platnosci['p_pas'])
else:
    if float(procent_zmniejszenia_p_pas) < 3:
        platnosc_p_pas = float(powierzchnia_p_pas_po_zmniejszeniach) * float(stawki_platnosci['p_pas'])
    elif float(procent_zmniejszenia_p_pas) > 20:
        platnosc_p_pas = 0
    else:
        platnosc_p_pas = (float(powierzchnia_p_pas_po_zmniejszeniach) - (float(zmniejszenia_p_pas) * 2)) * float(stawki_platnosci['p_pas'])

# Wyliczenie płatności P_PAS po sankcjach terminowych i CC
platnoc_p_pas_po_sankcjach = ((float(platnosc_p_pas) * ((100 - float(sankcje_terminowe)) / 100)) * ((100 - float(sankcja_cc)) / 100))

# Wyliczanie płatności P_Burak
powierzchnia_p_burak_po_zmniejszeniach = float(powierzchnia_p_burak) - float(zmniejszenia_p_burak)

# Przedstawinie powierzchni po zmniejszeniach oraz procentowego udziału zmniejszeń
if float(powierzchnia_p_burak) == 0:
    procent_zmniejszenia_p_burak = 0
else:
    procent_zmniejszenia_p_burak = (float(zmniejszenia_p_burak) / float(powierzchnia_p_burak_po_zmniejszeniach) * 100)


if float(powierzchnia_p_burak_po_zmniejszeniach) == 0:
    procent_zmniejszenia_p_burak = 0
else:
    procent_zmniejszenia_p_burak = (float(zmniejszenia_p_burak) / float(powierzchnia_p_burak_po_zmniejszeniach) * 100)

platnosc_p_burak = 0
if float(zmniejszenia) <= 0.10:
    platnosc_p_burak = float(powierzchnia_p_burak) * float(stawki_platnosci['p_burak'])
else:
    if float(procent_zmniejszenia_p_burak) < 3:
        platnosc_p_burak = float(powierzchnia_p_burak_po_zmniejszeniach) * float(stawki_platnosci['p_burak'])
    elif float(procent_zmniejszenia_p_burak) > 20:
        platnosc_p_burak = 0
    else:
        platnosc_p_burak = (float(powierzchnia_p_burak_po_zmniejszeniach) - (float(zmniejszenia_p_burak) * 2)) * float(stawki_platnosci['p_burak'])

# Wyliczenie płatności P_Burak po sankcjach terminowych i CC
platnoc_p_burak_po_sankcjach = ((float(platnosc_p_burak) * ((100 - float(sankcje_terminowe)) / 100)) * ((100 - float(sankcja_cc)) / 100))

# Wyliczanie płatności P_skrobia
powierzchnia_p_skrobia_po_zmniejszeniach = float(powierzchnia_p_skrobia) - float(zmniejszenia_p_skrobia)

# Przedstawinie powierzchni po zmniejszeniach oraz procentowego udziału zmniejszeń

if float(powierzchnia_p_skrobia) == 0:
    procent_zmniejszenia_p_skrobia = 0
else:
    procent_zmniejszenia_p_skrobia = (float(zmniejszenia_p_skrobia) / float(powierzchnia_p_skrobia_po_zmniejszeniach) * 100)


if float(powierzchnia_p_skrobia_po_zmniejszeniach) == 0:
    procent_zmniejszenia_p_skrobia = 0
else:
    procent_zmniejszenia_p_skrobia = (float(zmniejszenia_p_skrobia) / float(powierzchnia_p_skrobia_po_zmniejszeniach) * 100)

platnosc_p_skrobia = 0
if float(zmniejszenia) <= 0.10:
    platnosc_p_skrobia = float(powierzchnia_p_skrobia) * float(stawki_platnosci['p_skrobia'])
else:
    if float(procent_zmniejszenia_p_skrobia) < 3:
        platnosc_p_skrobia = float(powierzchnia_p_skrobia_po_zmniejszeniach) * float(stawki_platnosci['p_skrobia'])
    elif float(procent_zmniejszenia_p_skrobia) > 20:
        platnosc_p_skrobia = 0
    else:
        platnosc_p_skrobia = (float(powierzchnia_p_skrobia_po_zmniejszeniach) - (float(zmniejszenia_p_skrobia) * 2)) * float(stawki_platnosci['p_burak'])

# Wyliczenie płatności P_skrobia po sankcjach terminowych i CC
platnoc_p_skrobia_po_sankcjach = ((float(platnosc_p_skrobia) * ((100 - float(sankcje_terminowe)) / 100)) * ((100 - float(sankcja_cc)) / 100))

# Wyliczanie płatności P_truskawka
powierzchnia_p_truskawka_po_zmniejszeniach = float(powierzchnia_p_truskawka) - float(zmniejszenia_p_truskawka)

# Przedstawinie powierzchni po zmniejszeniach oraz procentowego udziału zmniejszeń
if float(powierzchnia_p_truskawka) == 0:
    procent_zmniejszenia_p_truskawka = 0
else:
    procent_zmniejszenia_p_truskawka = (float(zmniejszenia_p_truskawka) / float(powierzchnia_p_truskawka_po_zmniejszeniach) * 100)


if float(powierzchnia_p_truskawka_po_zmniejszeniach) == 0:
    procent_zmniejszenia_p_truskawka = 0
else:
    procent_zmniejszenia_p_truskawka = (float(zmniejszenia_p_truskawka) / float(powierzchnia_p_truskawka_po_zmniejszeniach) * 100)

platnosc_p_truskawka = 0

if float(zmniejszenia) <= 0.10:
    platnosc_p_truskawka = float(powierzchnia_p_truskawka) * float(stawki_platnosci['p_truskawka'])
else:
    if float(procent_zmniejszenia_p_truskawka) < 3:
        platnosc_p_truskawka = float(powierzchnia_p_truskawka_po_zmniejszeniach) * float(stawki_platnosci['p_truskawka'])
    elif float(procent_zmniejszenia_p_truskawka) > 20:
        platnosc_p_truskawka = 0
    else:
        platnosc_p_truskawka = (float(powierzchnia_p_truskawka_po_zmniejszeniach) - (float(zmniejszenia_p_truskawka) * 2)) * float(stawki_platnosci['p_truskawka'])

# Wyliczenie płatności P_truskawka po sankcjach terminowych i CC
platnoc_p_truskawka_po_sankcjach = ((float(platnosc_p_truskawka) * ((100 - float(sankcje_terminowe)) / 100)) * ((100 - float(sankcja_cc)) / 100))

# Wyliczanie płatności Pomidor
powierzchnia_pomidor_po_zmniejszeniach = float(powierzchnia_pomidor) - float(zmniejszenia_pomidor)

# Przedstawinie powierzchni po zmniejszeniach oraz procentowego udziału zmniejszeń
if float(powierzchnia_pomidor) == 0:
    procent_zmniejszenia_pomidor = 0
else:
    procent_zmniejszenia_pomidor = (float(zmniejszenia_pomidor) / float(powierzchnia_pomidor_po_zmniejszeniach) * 100)

if float(powierzchnia_pomidor_po_zmniejszeniach) == 0:
    procent_zmniejszenia_p_pomidor = 0
else:
    procent_zmniejszenia_pomidor = (float(zmniejszenia_pomidor) / float(powierzchnia_pomidor_po_zmniejszeniach) * 100)

platnosc_pomidor = 0
if float(zmniejszenia) <= 0.10:
    platnosc_pomidor = float(powierzchnia_pomidor) * float(stawki_platnosci['pomidory'])
else:
    if float(procent_zmniejszenia_pomidor) < 3:
        platnosc_pomidor = float(powierzchnia_pomidor_po_zmniejszeniach) * float(stawki_platnosci['pomidory'])
    elif float(procent_zmniejszenia_pomidor) > 20:
        platnosc_pomidor = 0
    else:
        platnosc_pomidor = (float(powierzchnia_pomidor_po_zmniejszeniach) - (float(zmniejszenia_pomidor) * 2)) * float(stawki_platnosci['pomidory'])

# Wyliczenie płatności Pomidor po sankcjach terminowych i CC
platnoc_pomidor_po_sankcjach = ((float(platnosc_pomidor) * ((100 - float(sankcje_terminowe)) / 100)) * ((100 - float(sankcja_cc)) / 100))

#Wyliczanie płatności Chmiel
powierzchnia_chmiel_po_zmniejszeniach = float(powierzchnia_chmiel) - float(zmniejszenia_chmiel)

# Przedstawinie powierzchni po zmniejszeniach oraz procentowego udziału zmniejszeń
if float(powierzchnia_chmiel) == 0:
    procent_zmniejszenia_chmiel = 0
else:
    procent_zmniejszenia_chmiel = (float(zmniejszenia_chmiel) / float(powierzchnia_chmiel_po_zmniejszeniach)*100)


if float(powierzchnia_chmiel_po_zmniejszeniach) == 0:
    procent_zmniejszenia_chmiel = 0
else:
    procent_zmniejszenia_chmiel = (float(zmniejszenia_chmiel) / float(powierzchnia_chmiel_po_zmniejszeniach) * 100)

platnosc_chmiel = 0
if float(zmniejszenia) <= 0.10:
    platnosc_chmiel = float(powierzchnia_chmiel) * float(stawki_platnosci['chmiel'])
else:
    if float(procent_zmniejszenia_chmiel) < 3:
        platnosc_chmiel = float(powierzchnia_chmiel_po_zmniejszeniach) * float(stawki_platnosci['chmiel'])
    elif float(procent_zmniejszenia_chmiel) > 20:
        platnosc_chmiel = 0
    else:
        platnosc_chmiel = (float(powierzchnia_chmiel_po_zmniejszeniach) - (float(zmniejszenia_chmiel) * 2)) * float(stawki_platnosci['chmiel'])

#Wyliczenie płatności do Chmielu po sankcjach terminowych i CC
platnoc_chmiel_po_sankcjach = ((float(platnosc_chmiel) * ((100 - float(sankcje_terminowe)) / 100)) * ((100 - float(sankcja_cc)) / 100))

#Wyliczanie płatności Len
powierzchnia_len_po_zmniejszeniach = (float(powierzchnia_len) - float(zmniejszenia_len))

# Przedstawinie powierzchni po zmniejszeniach oraz procentowego udziału zmniejszeń
if float(powierzchnia_len) == 0:
    procent_zmniejszenia_len = 0
else:
    procent_zmniejszenia_len = (float(zmniejszenia_len) / float(powierzchnia_len_po_zmniejszeniach) * 100)


if float(powierzchnia_len_po_zmniejszeniach) == 0:
    procent_zmniejszenia_len = 0
else:
    procent_zmniejszenia_len = (float(zmniejszenia_len) / float(powierzchnia_len_po_zmniejszeniach) * 100)

platnosc_len = 0
if float(zmniejszenia) <= 0.10:
    platnosc_len = float(powierzchnia_len) * float(stawki_platnosci['len'])
else:
    if float(procent_zmniejszenia_len) < 3:
        platnosc_len = float(powierzchnia_len_po_zmniejszeniach) * float(stawki_platnosci['len'])
    elif float(procent_zmniejszenia_len) > 20:
        platnosc_len = 0
    else:
        platnosc_len = (float(powierzchnia_len_po_zmniejszeniach) - (float(zmniejszenia_len) * 2)) * float(stawki_platnosci['len'])

#Wyliczenie płatności do Lnu po sankcjach terminowych i CC
platnoc_len_po_sankcjach = ((float(platnosc_len) * ((100 - float(sankcje_terminowe)) / 100)) * ((100 - float(sankcja_cc)) / 100))

#Wyliczanie płatności do Konopii
powierzchnia_konopie_po_zmniejszeniach = (float(powierzchnia_konopie) - float(zmniejszenia_konopie))

# Przedstawinie powierzchni po zmniejszeniach oraz procentowego udziału zmniejszeń
if float(powierzchnia_konopie) == 0:
    procent_zmniejszenia_konopie = 0
else:
    procent_zmniejszenia_konopie = (float(zmniejszenia_konopie) / float(powierzchnia_konopie_po_zmniejszeniach) * 100)


if float(powierzchnia_konopie_po_zmniejszeniach) == 0:
    procent_zmniejszenia_konopie = 0
else:
    procent_zmniejszenia_konopie = (float(zmniejszenia_konopie) / float(powierzchnia_konopie_po_zmniejszeniach) * 100)

platnosc_konopie = 0
if float(zmniejszenia) <= 0.10:
    platnosc_konopien = float(powierzchnia_konopie) * float(stawki_platnosci['konopie'])
else:
    if float(procent_zmniejszenia_konopie) < 3:
        platnosc_konopie = float(powierzchnia_konopie_po_zmniejszeniach) * float(stawki_platnosci['konopie'])
    elif float(procent_zmniejszenia_konopie) > 20:
        platnosc_konopie = 0
    else:
        platnosc_konopie = (float(powierzchnia_konopie_po_zmniejszeniach) - (float(zmniejszenia_konopie) * 2)) * float(stawki_platnosci['konopie'])

#Wyliczenie płatności Konopie po sankcjach terminowych i CC
platnoc_konopie_po_sankcjach = ((float(platnosc_konopie) * ((100 - float(sankcje_terminowe)) / 100)) * ((100 - float(sankcja_cc)) / 100))

# Wyliczenie płatności do krów
if int(liczba_krow_po_zmniejszeniach) < 3:
    liczba_krow_do_wyliczen = 0
else:
    if int(liczba_krow_po_zmniejszeniach) > 20:
        liczba_krow_do_wyliczen = 20
    else:
        liczba_krow_do_wyliczen = int(liczba_krow_po_zmniejszeniach)

# Wyliczanie procentu przedeklarowania
if (int(liczba_krow) - int(zmniejszenia_krowy)) == 0:
    procent_przedeklarowania_krow = 0
else:
    procent_przedeklarowania_krow = int(zmniejszenia_krowy) / (int(liczba_krow) - int(zmniejszenia_krowy))

# Wyliczenie płatności do krów po sankcjach i sprawdza czy sankcje za przedeklarowanie mają być podwojone
if int(zmniejszenia_krowy) <= 3:

    platnoc_krowy_po_sankcjach = int(liczba_krow_do_wyliczen) * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcja_cc)) / 100) * float(stawki_platnosci['krowy'])
else:
    platnoc_krowy_po_sankcjach = float((int(liczba_krow_do_wyliczen) * (float(procent_przedeklarowania_krow) * 2))) * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcja_cc)) / 100) * float(stawki_platnosci['krowy'])

# Wyliczenie płatności do bydła
if int(liczba_bydla_po_zmniejszeniach) < 3:
    liczba_bydla_do_wyliczen = 0
else:
    if int(liczba_bydla_po_zmniejszeniach) > 20:
        liczba_bydla_do_wyliczen = 20
    else:
        liczba_bydla_do_wyliczen = int(liczba_bydla_po_zmniejszeniach)

# Wyliczanie procentu przedeklarowania
if (int(liczba_bydla) - int(zmniejszenia_bydlo)) == 0:
    procent_przedeklarowania_bydla = 0
else:
    procent_przedeklarowania_bydla = int(zmniejszenia_bydlo) / (int(liczba_bydla) - int(zmniejszenia_bydlo))

# Wyliczenie płatności do bydła po sankcjach i sprawdza czy sankcje za przedeklarowanie mają być podwojone
if int(zmniejszenia_bydlo) <= 3:
    platnoc_bydlo_po_sankcjach = int(liczba_bydla_do_wyliczen) * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcja_cc)) / 100) * float(stawki_platnosci['bydło'])
else:
    platnoc_bydlo_po_sankcjach = float((int(liczba_bydla_do_wyliczen) * (float(procent_przedeklarowania_bydla) * 2))) * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcja_cc)) / 100) * float(stawki_platnosci['bydło'])

    # Wyliczenie płatności do kóz
if int(liczba_koz_po_zmniejszeniach) < 5:
    liczba_koz_do_wyliczen = 0
else:
    liczba_koz_do_wyliczen = int(liczba_koz_po_zmniejszeniach)

# Wyliczanie procentu przedeklarowania
if (int(liczba_koz) - int(zmniejszenia_koz)) == 0:
    procent_przedeklarowania_koz = 0
else:
    procent_przedeklarowania_koz = int(zmniejszenia_koz) / (int(liczba_koz) - int(zmniejszenia_koz))

# Wyliczenie płatności do koz po sankcjach i sprawdza czy sankcje za przedeklarowanie mają być podwojone
if int(zmniejszenia_koz) <= 5:
    platnoc_koz_po_sankcjach = int(liczba_koz_do_wyliczen) * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcja_cc)) / 100) * float(stawki_platnosci['kozy'])
else:
    platnoc_koz_po_sankcjach = float((int(liczba_koz_do_wyliczen) * (float(procent_przedeklarowania_koz) * 2))) * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcja_cc)) / 100) * float(stawki_platnosci['kozy'])

# Wyliczenie płatności do owiec
if int(liczba_owiec_po_zmniejszeniach) < 10:
    liczba_owiec_do_wyliczen = 0
else:
    liczba_owiec_do_wyliczen = int(liczba_owiec_po_zmniejszeniach)

# Wyliczanie procentu przedeklarowania
if (int(liczba_owiec) - int(zmniejszenia_owiec)) == 0:
    procent_przedeklarowania_owiec = 0
else:
    procent_przedeklarowania_owiec = int(zmniejszenia_owiec) / (int(liczba_owiec) - int(zmniejszenia_owiec))

# Wyliczenie płatności do koz po sankcjach i sprawdza czy sankcje za przedeklarowanie mają być podwojone
if int(zmniejszenia_owiec) <= 10:
    platnoc_owiec_po_sankcjach = int(liczba_owiec_do_wyliczen) * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcja_cc)) / 100) * float(stawki_platnosci['owce'])
else:
    platnoc_owiec_po_sankcjach = float((int(liczba_owiec_do_wyliczen) * (float(procent_przedeklarowania_owiec) * 2))) * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcja_cc)) / 100) * float(stawki_platnosci['owce'])

print(f"Twoja płatność do JPO wynosi: {round(float(platnoc_jpo_po_sankcjach), 2)} zł.")
if platnosc_redystrybucyjna_po_sankcjach >= 0:
    print(f"Twoja płatność redystrybucyjna wynosi: {round(float(platnosc_redystrybucyjna_po_sankcjach), 2)} zł.")
print(f"Twoja płatność do zazielenienia wynosi: {round(float(platnosc_zazielenienie_po_sankcjach), 2)} zł.")
if powierzchnia_upp >= 0:
    print(f"Twoja płatność UPP wynosi: {round(float(platnoc_upp_po_sankcjach), 2)} zł.")
if platnoc_mr_po_sankcjach >= 0:
    print(f"Twoja płatność MR wynosi: {round(float(platnoc_mr_po_sankcjach), 2)} zł.")
if powierzchnia_p_str >= 0:
    print(f"Twoja płatność P_STR wynosi: {round(float(platnoc_p_str_po_sankcjach), 2)} zł.")
if powierzchnia_p_pas >= 0:
    print(f"Twoja płatność P_PAS wynosi: {round(float(platnoc_p_pas_po_sankcjach), 2)} zł.")
if powierzchnia_p_burak >= 0:
    print(f"Twoja płatność P_Burak wynosi: {round(float(platnoc_p_burak_po_sankcjach), 2)} zł.")
if powierzchnia_p_skrobia >= 0:
    print(f"Twoja płatność P_skrobia wynosi: {round(float(platnoc_p_skrobia_po_sankcjach), 2)} zł.")
if powierzchnia_p_truskawka >= 0:
    print(f"Twoja płatność do truskawek wynosi: {round(float(platnoc_p_truskawka_po_sankcjach), 2)} zł.")
if powierzchnia_pomidor >= 0:
    print(f"Twoja płatność do pomidorów wynosi: {round(float(platnoc_pomidor_po_sankcjach), 2)} zł.")
if powierzchnia_chmiel >= 0:
    print(f"Twoja płatność do chmielu wynosi: {round(float(platnoc_chmiel_po_sankcjach), 2)} zł.")
if powierzchnia_len >= 0:
    print(f"Twoja płatność do lnu wynosi: {round(float(platnoc_len_po_sankcjach), 2)} zł.")
if liczba_krow >= 0:
    print(f"Twoja płatność dla krów wynosi: {round(platnoc_krowy_po_sankcjach, 2)} zł.")
if liczba_bydla >= 0:
    print(f"Twoja płatność dla bydła wynosi: {round(platnoc_bydlo_po_sankcjach, 2)} zł.")
if liczba_koz >= 0:
    print(f"Twoja płatność dla kóz wynosi: {round(platnoc_koz_po_sankcjach, 2)} zł.")
if liczba_owiec >= 0:
    print(f"Twoja płatność dla owiec wynosi: {round(platnoc_owiec_po_sankcjach, 2)} zł.")


# wstawiamy wyliczenia do bazy danych
#user = authenticate(request, user_id=id)
#if user is not None:
#user = User
if User.is_authenticated:
    cur.execute('UPDATE Kalkulator_platnoscjpo SET wynikjpo = ? WHERE id = ?;', (round(float(platnoc_jpo_po_sankcjach), 2), user.id))
    cur.execute('UPDATE Kalkulator_platnoscupp SET wynikupp = ? WHERE id = ?;', (round(float(platnoc_upp_po_sankcjach), 2), user.id))
    cur.execute('UPDATE Kalkulator_platnoscjpo SET wynikmr = ? WHERE id = ?;', (round(float(platnoc_mr_po_sankcjach), 2), user.id))
    cur.execute('UPDATE Kalkulator_platnoscp_str SET wynikp_str = ? WHERE id = ?;', (round(float(platnoc_p_str_po_sankcjach), 2), user.id))
    cur.execute('UPDATE Kalkulator_platnoscp_pas SET wynikp_pas = ? WHERE id = ?;', (round(float(platnoc_p_pas_po_sankcjach), 2), user.id))
    cur.execute('UPDATE Kalkulator_platnoscp_burak SET wynikp_burak = ? WHERE id = ?;', (round(float(platnoc_p_burak_po_sankcjach), 2), user.id))
    cur.execute('UPDATE Kalkulator_platnoscp_skrobia SET wynikp_skrobia = ? WHERE id = ?;', (round(float(platnoc_p_skrobia_po_sankcjach), 2), user.id))
    cur.execute('UPDATE Kalkulator_platnoscp_truskawka SET wynikp_trus = ? WHERE id = ?;', (round(float(platnoc_p_truskawka_po_sankcjach), 2), user.id))
    cur.execute('UPDATE Kalkulator_platnoscpomidor SET wynikpomidor = ? WHERE id = ?;', (round(float(platnoc_pomidor_po_sankcjach), 2), user.id))
    cur.execute('UPDATE Kalkulator_platnoscchmiel SET wynikchmiel = ? WHERE id = ?;', (round(float(platnoc_chmiel_po_sankcjach), 2), user.id))
    cur.execute('UPDATE Kalkulator_platnosclen SET wyniklen = ? WHERE id = ?;', (round(float(platnoc_len_po_sankcjach), 2), user.id))
    cur.execute('UPDATE Kalkulator_platnosckonopie SET wynikkonopie = ? WHERE id = ?;', (round(float(platnoc_konopie_po_sankcjach), 2), user.id))
    cur.execute('UPDATE Kalkulator_platnosckrowy SET wynikkrowy = ? WHERE id = ?;', (round(float(platnoc_krowy_po_sankcjach), 2), user.id))
    cur.execute('UPDATE Kalkulator_platnoscbydlo SET wynikbydlo = ? WHERE id = ?;', (round(float(platnoc_bydlo_po_sankcjach), 2), user.id))
    cur.execute('UPDATE Kalkulator_platnosckozy SET wynikkozy = ? WHERE id = ?;', (round(float(platnoc_koz_po_sankcjach), 2), user.id))
    cur.execute('UPDATE Kalkulator_platnoscowce SET wynikowce = ? WHERE id = ?;', (round(float(platnoc_owiec_po_sankcjach), 2), user.id))
    cur.execute('UPDATE Kalkulator_platnoscjpo SET wynikzaz = ? WHERE id = ?;', (round(float(platnosc_zazielenienie_po_sankcjach), 2), user.id))
    cur.execute('UPDATE Kalkulator_platnoscjpo SET wynikredys = ? WHERE id = ?;', (round(float(platnosc_redystrybucyjna_po_sankcjach), 2), user.id))
    con.commit()
