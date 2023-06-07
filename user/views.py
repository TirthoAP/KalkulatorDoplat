from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserForm
import sqlite3

# Create your views here.

def register(request):
    """Rejestracja nowego użytkownika."""
    if request.method != 'POST':
        #Wyświetlanie pustego formularza rejestracji użytkownika.
#        form = UserCreationForm
        form = CustomUserForm()
    else:
        #Przetworzenie własnego formularza.
#        form = UserCreationForm(data=request.POST)
        form = CustomUserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            #Zalogowanie użytkownika, a następnie przekierowanie go na stronę główną.
            login(request, new_user)
            con = sqlite3.connect('db.sqlite3')
            # dostęp do kolumn przez indeksy i przez nazwy
            con.row_factory = sqlite3.Row
            # utworzenie obiektu kursora

            user = request.user
            if request.user.is_authenticated:
                cur = con.cursor()
                cur.execute('INSERT INTO Kalkulator_platnoscjpo  (wynikmr, wynikzaz, wynikredys, wynikjpo, dodanejpo, zmnjpo, czy_mr, uzytkownik_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                    (0, 0, 0, 0, 0, 0, 'nie', user.id))
                cur.execute('INSERT INTO Kalkulator_platnoscupp (wynikupp, dodaneupp, zmnupp, uzytkownik_id) VALUES (?, ?, ?, ?)',
                    (0, 0, 0, user.id))
                cur.execute('INSERT INTO Kalkulator_platnoscp_pas (wynikp_pas, dodanep_pas, zmnp_pas, uzytkownik_id) VALUES (?, ?, ?, ?)',
                    (0, 0, 0, user.id))
                cur.execute('INSERT INTO Kalkulator_platnoscp_str (wynikp_str, dodanep_str, zmnp_str, uzytkownik_id) VALUES (?, ?, ?, ?)',
                    (0, 0, 0, user.id))
                cur.execute('INSERT INTO Kalkulator_platnoscp_burak (wynikp_burak, dodanep_burak, zmnp_burak, uzytkownik_id) VALUES (?, ?, ?, ?)',
                    (0, 0, 0, user.id))
                cur.execute('INSERT INTO Kalkulator_platnoscp_skrobia (wynikp_skrobia, dodanep_skrobia, zmnp_skrobia, uzytkownik_id) VALUES (?, ?, ?, ?)',
                    (0, 0, 0, user.id))
                cur.execute('INSERT INTO Kalkulator_platnoscp_truskawka (wynikp_trus, dodanep_trus, zmnp_trus, uzytkownik_id) VALUES (?, ?, ?, ?)',
                    (0, 0, 0, user.id))
                cur.execute('INSERT INTO Kalkulator_platnoscpomidor (wynikpomidor, dodanepomidor, zmnpomidor, uzytkownik_id) VALUES (?, ?, ?, ?)',
                    (0, 0, 0, user.id))
                cur.execute('INSERT INTO Kalkulator_platnoscchmiel (wynikchmiel, dodanechmiel, zmnchmiel, uzytkownik_id) VALUES (?, ?, ?, ?)',
                    (0, 0, 0, user.id))
                cur.execute('INSERT INTO Kalkulator_platnosclen (wyniklen, dodanelen, zmnlen, uzytkownik_id) VALUES (?, ?, ?, ?)',
                    (0, 0, 0, user.id))
                cur.execute('INSERT INTO Kalkulator_platnosckonopie (wynikkonopie, dodanekonopie, zmnkonopie, uzytkownik_id) VALUES (?, ?, ?, ?)',
                    (0, 0, 0, user.id))
                cur.execute('INSERT INTO Kalkulator_platnosckrowy (wynikkrowy, dodanekrowy, zmnkrowy, uzytkownik_id) VALUES (?, ?, ?, ?)',
                    (0, 0, 0, user.id))
                cur.execute('INSERT INTO Kalkulator_platnoscbydlo (wynikbydlo, dodanebydlo, zmnbydlo, uzytkownik_id) VALUES (?, ?, ?, ?)',
                    (0, 0, 0, user.id))
                cur.execute('INSERT INTO Kalkulator_platnoscowce (wynikowce, dodaneowce, zmnowce, uzytkownik_id) VALUES (?, ?, ?, ?)',
                    (0, 0, 0, user.id))
                cur.execute('INSERT INTO Kalkulator_platnosckozy (wynikkozy, dodanekozy, zmnkozy, uzytkownik_id) VALUES (?, ?, ?, ?)',
                    (0, 0, 0, user.id))
                cur.execute('INSERT INTO Kalkulator_sankcjacc (dodanecc, uzytkownik_id) VALUES (?, ?)', (0, user.id))
                cur.execute('INSERT INTO Kalkulator_sankcjaterminowa (dodaneterm, uzytkownik_id) VALUES (?, ?)', (0, user.id))
                con.commit()

            return redirect('main_page')
    #Wyświetlanie pustego formularza.
    context = {'form': form}
    return render(request, 'registration/register.html', context)
