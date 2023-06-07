from django.shortcuts import render
#import psycopg2
import sqlite3

# Create your views here.
from Kalkulator.models import PlatnoscJPO
from Kalkulator.models import PlatnoscUPP
from Kalkulator.models import PlatnoscP_PAS
from Kalkulator.models import PlatnoscP_STR
from Kalkulator.models import PlatnoscP_Burak
from Kalkulator.models import PlatnoscP_Skrobia
from Kalkulator.models import PlatnoscP_Truskawka
from Kalkulator.models import PlatnoscPomidor
from Kalkulator.models import PlatnoscChmiel
from Kalkulator.models import PlatnoscLen
from Kalkulator.models import PlatnoscKonopie
from Kalkulator.models import PlatnoscTyton
from Kalkulator.models import PlatnoscVirginia
from Kalkulator.models import PlatnoscKrowy
from Kalkulator.models import PlatnoscBydlo
from Kalkulator.models import PlatnoscOwce
from Kalkulator.models import PlatnoscKozy
from Kalkulator.models import SankcjaCC
from Kalkulator.models import SankcjaEFA
from Kalkulator.models import SankcjaNiezadekl
from Kalkulator.models import SankcjaTerminowa
from .forms import PodsumowanieJPOForm
from .forms import PodsumowanieUPPForm
from .forms import PodsumowanieP_STRForm
from .forms import PodsumowanieP_PASForm
from .forms import PodsumowanieP_BurakForm
from .forms import PodsumowanieP_SkrobiaForm
from .forms import PodsumowanieP_TruskawkaForm
from .forms import PodsumowaniePomidorForm
from .forms import PodsumowanieChmielForm
from .forms import PodsumowanieLenForm
from .forms import PodsumowanieKonopieForm
from .forms import PodsumowanieTytonForm
from .forms import PodsumowanieVirginiaForm
from .forms import PodsumowanieKrowyForm
from .forms import PodsumowanieBydloForm
from .forms import PodsumowanieOwceForm
from .forms import PodsumowanieKozyForm
from .forms import PodsumowaniesankCCForm
from .forms import PodsumowaniesankEFAForm
from .forms import PodsumowaniesankNiezadeklForm
from .forms import PodsumowaniesankTerminowaForm

def main_page(request):
    return render(request, 'Kalkulator/index.html')

def platnosci(request):
    platnoscijpo = PlatnoscJPO.objects.all()
    platnosciupp = PlatnoscUPP.objects.all()
    platnoscip_str = PlatnoscP_STR.objects.all()
    platnoscip_pas = PlatnoscP_PAS.objects.all()
    platnoscip_burak = PlatnoscP_Burak.objects.all()
    platnoscip_skrobia = PlatnoscP_Skrobia.objects.all()
    platnoscip_trus = PlatnoscP_Truskawka.objects.all()
    platnoscipomidor = PlatnoscPomidor.objects.all()
    platnoscichmiel = PlatnoscChmiel.objects.all()
    platnoscilen = PlatnoscLen.objects.all()
    platnoscikonopie = PlatnoscKonopie.objects.all()
    platnoscityton = PlatnoscTyton.objects.all()
    platnoscivirginia = PlatnoscVirginia.objects.all()
    platnoscikrowy = PlatnoscKrowy.objects.all()
    platnoscibydlo = PlatnoscBydlo.objects.all()
    platnosciowce = PlatnoscOwce.objects.all()
    platnoscikozy = PlatnoscKozy.objects.all()
    sankcjecc = SankcjaCC.objects.all()
    sankcjeefa = SankcjaEFA.objects.all()
    sankcjeniezad = SankcjaNiezadekl.objects.all()
    sankcjeterm = SankcjaTerminowa.objects.all()
    dane = {'platnoscijpo': platnoscijpo,
            'platnosciupp': platnosciupp,
            'platnoscip_str': platnoscip_str,
            'platnoscip_pas': platnoscip_pas,
            'platnoscip_burak': platnoscip_burak,
            'platnoscip_skrobia': platnoscip_skrobia,
            'platnoscip_trus': platnoscip_trus,
            'platnoscipomidor': platnoscipomidor,
            'platnoscichmiel': platnoscichmiel,
            'platnoscilen': platnoscilen,
            'platnoscikonopie': platnoscikonopie,
            'platnoscityton': platnoscityton,
            'platnoscivirginia': platnoscivirginia,
            'platnoscikrowy': platnoscikrowy,
            'platnoscibydlo': platnoscibydlo,
            'platnosciowce': platnosciowce,
            'platnoscikozy': platnoscikozy,
            'sankcjecc': sankcjecc,
            'sankcjeefa': sankcjeefa,
            'sankcjeniezad': sankcjeniezad,
            'sankcjeterm': sankcjeterm,
            }
    return render(request, 'Kalkulator/platnosci.html', dane)

def wyczysc(request):
    # utworzenie połączenia z bazą przechowywaną na dysku
    con = sqlite3.connect('db.sqlite3')
    # dostęp do kolumn przez indeksy i przez nazwy
    con.row_factory = sqlite3.Row
    # utworzenie obiektu kursora

    user = request.user
    if request.user.is_authenticated:
        cur = con.cursor()
        cur.execute('UPDATE Kalkulator_platnoscjpo SET wynikmr = ?, wynikzaz = ?, wynikredys = ?, wynikjpo = ?, dodanejpo = ?, zmnjpo = ?, czy_mr = ? WHERE id= ?;', (0, 0, 0, 0, 0, 0, 'nie', user.id))
        cur.execute('UPDATE Kalkulator_platnoscupp SET wynikupp = ?, dodaneupp = ?, zmnupp = ? WHERE id= ?;', (0, 0, 0, user.id))
        cur.execute('UPDATE Kalkulator_platnoscp_pas SET wynikp_pas = ?, dodanep_pas = ?, zmnp_pas = ? WHERE id= ?;', (0, 0, 0, user.id))
        cur.execute('UPDATE Kalkulator_platnoscp_str SET wynikp_str = ?, dodanep_str = ?, zmnp_str = ? WHERE id= ?;', (0, 0, 0, user.id))
        cur.execute('UPDATE Kalkulator_platnoscp_burak SET wynikp_burak = ?, dodanep_burak = ?, zmnp_burak = ? WHERE id= ?;', (0, 0, 0, user.id))
        cur.execute('UPDATE Kalkulator_platnoscp_skrobia SET wynikp_skrobia = ?, dodanep_skrobia = ?, zmnp_skrobia = ? WHERE id= ?;', (0, 0, 0, user.id))
        cur.execute('UPDATE Kalkulator_platnoscp_truskawka SET wynikp_trus = ?, dodanep_trus = ?, zmnp_trus = ? WHERE id= ?;', (0, 0, 0, user.id))
        cur.execute('UPDATE Kalkulator_platnoscpomidor SET wynikpomidor = ?, dodanepomidor = ?, zmnpomidor = ? WHERE id= ?;', (0, 0, 0, user.id))
        cur.execute('UPDATE Kalkulator_platnoscchmiel SET wynikchmiel = ?, dodanechmiel = ?, zmnchmiel = ? WHERE id= ?;', (0, 0, 0, user.id))
        cur.execute('UPDATE Kalkulator_platnosclen SET wyniklen = ?, dodanelen = ?, zmnlen = ? WHERE id= ?;', (0, 0, 0, user.id))
        cur.execute('UPDATE Kalkulator_platnosckonopie SET wynikkonopie = ?, dodanekonopie = ?, zmnkonopie = ? WHERE id= ?;', (0, 0, 0, user.id))
        cur.execute('UPDATE Kalkulator_platnosctyton SET wyniktyton = ?, dodanetyton = ?, zmntyton = ? WHERE id= ?;', (0, 0, 0, user.id))
        cur.execute('UPDATE Kalkulator_platnoscvirginia SET wynikvirginia = ?, dodanevirginia = ?, zmnvirginia = ? WHERE id= ?;', (0, 0, 0, user.id))
        cur.execute('UPDATE Kalkulator_platnosckrowy SET wynikkrowy = ?, dodanekrowy = ?, zmnkrowy = ? WHERE id= ?;', (0, 0, 0, user.id))
        cur.execute('UPDATE Kalkulator_platnoscbydlo SET wynikbydlo = ?, dodanebydlo = ?, zmnbydlo = ? WHERE id= ?;', (0, 0, 0, user.id))
        cur.execute('UPDATE Kalkulator_platnoscowce SET wynikowce = ?, dodaneowce = ?, zmnowce = ? WHERE id= ?;', (0, 0, 0, user.id))
        cur.execute('UPDATE Kalkulator_platnosckozy SET wynikkozy = ?, dodanekozy = ?, zmnkozy = ? WHERE id= ?;', (0, 0, 0, user.id))
        cur.execute('UPDATE Kalkulator_sankcjacc SET dodanecc = ? WHERE id= ?;', (0, user.id))
        cur.execute('UPDATE Kalkulator_sankcjaterminowa SET dodaneterm = ? WHERE id= ?;', (0, user.id))
        cur.execute('UPDATE Kalkulator_sankcjaniezadekl SET dodaneniezad = ? WHERE id= ?;', (0, user.id))
        cur.execute('UPDATE Kalkulator_sankcjaefa SET pow_go = ?, pow_efa = ? WHERE id= ?;', (0, 0, user.id))
        con.commit()
    return render(request, 'Kalkulator/podsumowanieplatnosci.html')

def platnoscjpo(request, id):
    form = PodsumowanieJPOForm()
    platnoscjpo = PlatnoscJPO.objects.get(pk=id)
    jpo_id = id
    dane = {'platnoscjpo': platnoscjpo, 'jpo_id': jpo_id, 'form':form}
    return render(request, 'Kalkulator/platnoscjpo.html', dane)

def dodajwartoscjpo(request, id):
    platnoscjpo = PlatnoscJPO.objects.get(pk=id)
    jpo_id = id
    if request.method != 'POST':
        form = PodsumowanieJPOForm(instance=platnoscjpo)
    else:
        form = PodsumowanieJPOForm(instance=platnoscjpo, data=request.POST)
        if form.is_valid():
            form.save()
    dane = {'platnoscjpo': platnoscjpo, 'jpo_id': jpo_id, 'form':form}
    return render(request, 'Kalkulator/platnoscjpo.html', dane)

def platnoscupp(request, id):
    form = PodsumowanieUPPForm()
    platnoscupp = PlatnoscUPP.objects.get(pk=id)
    upp_id = id
    dane = {'platnoscupp': platnoscupp, 'upp_id': upp_id, 'form':form}
    return render(request, 'Kalkulator/platnoscupp.html', dane)

def dodajwartoscupp(request, id):
    platnoscupp = PlatnoscUPP.objects.get(pk=id)
    upp_id = id
    if request.method != 'POST':
        form = PodsumowanieUPPForm(instance=platnoscupp)
    else:
        form = PodsumowanieUPPForm(instance=platnoscupp, data=request.POST)
        if form.is_valid():
            form.save()
    dane = {'platnoscupp': platnoscupp, 'upp_id': upp_id, 'form':form}
    return render(request, 'Kalkulator/platnoscupp.html', dane)

def platnoscp_str(request, id):
    form = PodsumowanieP_STRForm()
    platnoscp_str = PlatnoscP_STR.objects.get(pk=id)
    p_str_id = id
    dane = {'platnoscp_str': platnoscp_str, 'p_str_id': p_str_id, 'form':form}
    return render(request, 'Kalkulator/platnoscp_str.html', dane)

def dodajwartoscp_str(request, id):
    platnoscp_str = PlatnoscP_STR.objects.get(pk=id)
    p_str_id = id
    if request.method != 'POST':
        form = PodsumowanieP_STRForm(instance=platnoscp_str)
    else:
        form = PodsumowanieP_STRForm(instance=platnoscp_str, data=request.POST)
        if form.is_valid():
            form.save()
    dane = {'platnoscp_str': platnoscp_str, 'p_str_id': p_str_id, 'form':form}
    return render(request, 'Kalkulator/platnoscp_str.html', dane)

def platnoscp_pas(request, id):
    form = PodsumowanieP_PASForm()
    platnoscp_pas = PlatnoscP_PAS.objects.get(pk=id)
    p_pas_id = id
    dane = {'platnoscp_pas': platnoscp_pas, 'p_pas_id': p_pas_id, 'form':form}
    return render(request, 'Kalkulator/platnoscp_pas.html', dane)

def dodajwartoscp_pas(request, id):
    platnoscp_pas = PlatnoscP_PAS.objects.get(pk=id)
    p_pas_id = id
    if request.method != 'POST':
        form = PodsumowanieP_PASForm(instance=platnoscp_pas)
    else:
        form = PodsumowanieP_PASForm(instance=platnoscp_pas, data=request.POST)
        if form.is_valid():
            form.save()
    dane = {'platnoscp_pas': platnoscp_pas, 'p_pas_id': p_pas_id, 'form':form}
    return render(request, 'Kalkulator/platnoscp_pas.html', dane)

def platnoscp_burak(request, id):
    form = PodsumowanieP_BurakForm()
    platnoscp_burak = PlatnoscP_Burak.objects.get(pk=id)
    p_burak_id = id
    dane = {'platnoscp_burak': platnoscp_burak, 'p_burak_id': p_burak_id, 'form':form}
    return render(request, 'Kalkulator/platnoscp_burak.html', dane)

def dodajwartoscp_burak(request, id):
    platnoscp_burak = PlatnoscP_Burak.objects.get(pk=id)
    p_burak_id = id
    if request.method != 'POST':
        form = PodsumowanieP_BurakForm(instance=platnoscp_burak)
    else:
        form = PodsumowanieP_BurakForm(instance=platnoscp_burak, data=request.POST)
        if form.is_valid():
            form.save()
    dane = {'platnoscp_burak': platnoscp_burak, 'p_burak_id': p_burak_id, 'form':form}
    return render(request, 'Kalkulator/platnoscp_burak.html', dane)

def platnoscp_skrobia(request, id):
    form = PodsumowanieP_SkrobiaForm()
    platnoscp_skrobia = PlatnoscP_Skrobia.objects.get(pk=id)
    p_skrobia_id = id
    dane = {'platnoscp_skrobia': platnoscp_skrobia, 'p_skrobia_id': p_skrobia_id, 'form':form}
    return render(request, 'Kalkulator/platnoscp_skrobia.html', dane)

def dodajwartoscp_skrobia(request, id):
    platnoscp_skrobia = PlatnoscP_Skrobia.objects.get(pk=id)
    p_skrobia_id = id
    if request.method != 'POST':
        form = PodsumowanieP_SkrobiaForm(instance=platnoscp_skrobia)
    else:
        form = PodsumowanieP_SkrobiaForm(instance=platnoscp_skrobia, data=request.POST)
        if form.is_valid():
            form.save()
    dane = {'platnoscp_skrobia': platnoscp_skrobia, 'p_skrobia_id': p_skrobia_id, 'form':form}
    return render(request, 'Kalkulator/platnoscp_skrobia.html', dane)

def platnoscp_trus(request, id):
    form = PodsumowanieP_TruskawkaForm()
    platnoscp_trus = PlatnoscP_Truskawka.objects.get(pk=id)
    p_trus_id = id
    dane = {'platnoscp_trus': platnoscp_trus, 'p_trus_id': p_trus_id, 'form':form}
    return render(request, 'Kalkulator/platnoscp_trus.html', dane)

def dodajwartoscp_trus(request, id):
    platnoscp_trus = PlatnoscP_Truskawka.objects.get(pk=id)
    p_trus_id = id
    if request.method != 'POST':
        form = PodsumowanieP_TruskawkaForm(instance=platnoscp_trus)
    else:
        form = PodsumowanieP_TruskawkaForm(instance=platnoscp_trus, data=request.POST)
        if form.is_valid():
            form.save()
    dane = {'platnoscp_trus': platnoscp_trus, 'p_trus_id': p_trus_id, 'form':form}
    return render(request, 'Kalkulator/platnoscp_trus.html', dane)

def platnoscpomidor(request, id):
    form = PodsumowaniePomidorForm()
    platnoscpomidor = PlatnoscPomidor.objects.get(pk=id)
    pomidor_id = id
    dane = {'platnoscpomidor': platnoscpomidor, 'pomidor_id': pomidor_id, 'form':form}
    return render(request, 'Kalkulator/platnoscpomidor.html', dane)

def dodajwartoscpomidor(request, id):
    platnoscpomidor = PlatnoscPomidor.objects.get(pk=id)
    pomidor_id = id
    if request.method != 'POST':
        form = PodsumowaniePomidorForm(instance=platnoscpomidor)
    else:
        form = PodsumowaniePomidorForm(instance=platnoscpomidor, data=request.POST)
        if form.is_valid():
            form.save()
    dane = {'platnoscpomidor': platnoscpomidor, 'pomidor_id': pomidor_id, 'form':form}
    return render(request, 'Kalkulator/platnoscpomidor.html', dane)

def platnoscchmiel(request, id):
    form = PodsumowanieChmielForm()
    platnoscchmiel = PlatnoscChmiel.objects.get(pk=id)
    chmiel_id = id
    dane = {'platnoscchmiel': platnoscchmiel, 'chmiel_id': chmiel_id, 'form':form}
    return render(request, 'Kalkulator/platnoscchmiel.html', dane)

def dodajwartoscchmiel(request, id):
    platnoscchmiel = PlatnoscChmiel.objects.get(pk=id)
    chmiel_id = id
    if request.method != 'POST':
        form = PodsumowanieChmielForm(instance=platnoscchmiel)
    else:
        form = PodsumowanieChmielForm(instance=platnoscchmiel, data=request.POST)
        if form.is_valid():
            form.save()
    dane = {'platnoscchmiel': platnoscchmiel, 'chmiel_id': chmiel_id, 'form':form}
    return render(request, 'Kalkulator/platnoscchmiel.html', dane)

def platnosclen(request, id):
    form = PodsumowanieLenForm()
    platnosclen = PlatnoscLen.objects.get(pk=id)
    len_id = id
    dane = {'platnosclen': platnosclen, 'len_id': len_id, 'form':form}
    return render(request, 'Kalkulator/platnosclen.html', dane)

def dodajwartosclen(request, id):
    platnosclen = PlatnoscLen.objects.get(pk=id)
    len_id = id
    if request.method != 'POST':
        form = PodsumowanieLenForm(instance=platnosclen)
    else:
        form = PodsumowanieLenForm(instance=platnosclen, data=request.POST)
        if form.is_valid():
            form.save()
    dane = {'platnosclen': platnosclen, 'len_id': len_id, 'form':form}
    return render(request, 'Kalkulator/platnosclen.html', dane)

def platnosckonopie(request, id):
    form = PodsumowanieKonopieForm()
    platnosckonopie = PlatnoscKonopie.objects.get(pk=id)
    konopie_id = id
    dane = {'platnosckonopie': platnosckonopie, 'konopie_id': konopie_id, 'form':form}
    return render(request, 'Kalkulator/platnosckonopie.html', dane)

def dodajwartosckonopie(request, id):
    platnosckonopie = PlatnoscKonopie.objects.get(pk=id)
    konopie_id = id
    if request.method != 'POST':
        form = PodsumowanieKonopieForm(instance=platnosckonopie)
    else:
        form = PodsumowanieKonopieForm(instance=platnosckonopie, data=request.POST)
        if form.is_valid():
            form.save()
    dane = {'platnosckonopie': platnosckonopie, 'konopie_id': konopie_id, 'form':form}
    return render(request, 'Kalkulator/platnosckonopie.html', dane)

def platnosctyton(request, id):
    form = PodsumowanieTytonForm()
    platnosctyton = PlatnoscTyton.objects.get(pk=id)
    tyton_id = id
    dane = {'platnosctyton': platnosctyton, 'tyton_id': tyton_id, 'form':form}
    return render(request, 'Kalkulator/platnosctyton.html', dane)

def dodajwartosctyton(request, id):
    platnosctyton = PlatnoscTyton.objects.get(pk=id)
    tyton_id = id
    if request.method != 'POST':
        form = PodsumowanieTytonForm(instance=platnosctyton)
    else:
        form = PodsumowanieTytonForm(instance=platnosctyton, data=request.POST)
        if form.is_valid():
            form.save()
    dane = {'platnosctyton': platnosctyton, 'tyton_id': tyton_id, 'form':form}
    return render(request, 'Kalkulator/platnosctyton.html', dane)

def platnoscvirginia(request, id):
    form = PodsumowanieVirginiaForm()
    platnoscvirginia = PlatnoscVirginia.objects.get(pk=id)
    virginia_id = id
    dane = {'platnoscvirginia': platnoscvirginia, 'virginia_id': virginia_id, 'form':form}
    return render(request, 'Kalkulator/platnoscvirginia.html', dane)

def dodajwartoscvirginia(request, id):
    platnoscvirginia = PlatnoscVirginia.objects.get(pk=id)
    virginia_id = id
    if request.method != 'POST':
        form = PodsumowanieVirginiaForm(instance=platnoscvirginia)
    else:
        form = PodsumowanieVirginiaForm(instance=platnoscvirginia, data=request.POST)
        if form.is_valid():
            form.save()
    dane = {'platnoscvirginia': platnoscvirginia, 'virginia_id': virginia_id, 'form':form}
    return render(request, 'Kalkulator/platnoscvirginia.html', dane)

def platnosckrowy(request, id):
    form = PodsumowanieKrowyForm()
    platnosckrowy = PlatnoscKrowy.objects.get(pk=id)
    krowy_id = id
    dane = {'platnosckrowy': platnosckrowy, 'krowy_id': krowy_id, 'form':form}
    return render(request, 'Kalkulator/platnosckrowy.html', dane)

def dodajwartosckrowy(request, id):
    platnosckrowy = PlatnoscKrowy.objects.get(pk=id)
    krowy_id = id
    if request.method != 'POST':
        form = PodsumowanieKrowyForm(instance=platnosckrowy)
    else:
        form = PodsumowanieKrowyForm(instance=platnosckrowy, data=request.POST)
        if form.is_valid():
            form.save()
    dane = {'platnosckrowy': platnosckrowy, 'krowy_id': krowy_id, 'form':form}
    return render(request, 'Kalkulator/platnosckrowy.html', dane)

def platnoscbydlo(request, id):
    form = PodsumowanieBydloForm()
    platnoscbydlo = PlatnoscBydlo.objects.get(pk=id)
    bydlo_id = id
    dane = {'platnoscbydlo': platnoscbydlo, 'bydlo_id': bydlo_id, 'form':form}
    return render(request, 'Kalkulator/platnoscbydlo.html', dane)

def dodajwartoscbydlo(request, id):
    platnoscbydlo = PlatnoscBydlo.objects.get(pk=id)
    bydlo_id = id
    if request.method != 'POST':
        form = PodsumowanieBydloForm(instance=platnoscbydlo)
    else:
        form = PodsumowanieBydloForm(instance=platnoscbydlo, data=request.POST)
        if form.is_valid():
            form.save()
    dane = {'platnoscbydlo': platnoscbydlo, 'bydlo_id': bydlo_id, 'form':form}
    return render(request, 'Kalkulator/platnoscbydlo.html', dane)

def platnoscowce(request, id):
    form = PodsumowanieOwceForm()
    platnoscowce = PlatnoscOwce.objects.get(pk=id)
    owce_id = id
    dane = {'platnoscowce': platnoscowce, 'owce_id': owce_id, 'form':form}
    return render(request, 'Kalkulator/platnoscowce.html', dane)

def dodajwartoscowce(request, id):
    platnoscowce = PlatnoscOwce.objects.get(pk=id)
    owce_id = id
    if request.method != 'POST':
        form = PodsumowanieOwceForm(instance=platnoscowce)
    else:
        form = PodsumowanieOwceForm(instance=platnoscowce, data=request.POST)
        if form.is_valid():
            form.save()
    dane = {'platnoscowce': platnoscowce, 'owce_id': owce_id, 'form':form}
    return render(request, 'Kalkulator/platnoscowce.html', dane)

def platnosckozy(request, id):
    form = PodsumowanieKozyForm()
    platnosckozy = PlatnoscKozy.objects.get(pk=id)
    kozy_id = id
    dane = {'platnosckozy': platnosckozy, 'kozy_id': kozy_id, 'form':form}
    return render(request, 'Kalkulator/platnosckozy.html', dane)

def dodajwartosckozy(request, id):
    platnosckozy = PlatnoscKozy.objects.get(pk=id)
    kozy_id = id
    if request.method != 'POST':
        form = PodsumowanieKozyForm(instance=platnosckozy)
    else:
        form = PodsumowanieKozyForm(instance=platnosckozy, data=request.POST)
        if form.is_valid():
            form.save()
    dane = {'platnosckozy': platnosckozy, 'kozy_id': kozy_id, 'form':form}
    return render(request, 'Kalkulator/platnosckozy.html', dane)

def sankcjacc(request, id):
    form = PodsumowaniesankCCForm()
    sankcjacc = SankcjaCC.objects.get(pk=id)
    cc_id = id
    dane = {'sankcjacc': sankcjacc, 'cc_id': cc_id, 'form':form}
    return render(request, 'Kalkulator/sankcjacc.html', dane)

def dodajwartosccc(request, id):
    sankcjacc = SankcjaCC.objects.get(pk=id)
    cc_id = id
    if request.method != 'POST':
        form = PodsumowaniesankCCForm(instance=sankcjacc)
    else:
        form = PodsumowaniesankCCForm(instance=sankcjacc, data=request.POST)
        if form.is_valid():
            form.save()
    dane = {'sankcjacc': sankcjacc, 'cc_id': cc_id, 'form':form}
    return render(request, 'Kalkulator/sankcjacc.html', dane)

def sankcjaterm(request, id):
    form = PodsumowaniesankTerminowaForm()
    sankcjaterm = SankcjaTerminowa.objects.get(pk=id)
    term_id = id
    dane = {'sankcjaterm': sankcjaterm, 'term_id': term_id, 'form':form}
    return render(request, 'Kalkulator/sankcjaterm.html', dane)

def dodajwartoscterm(request, id):
    sankcjaterm = SankcjaTerminowa.objects.get(pk=id)
    term_id = id
    if request.method != 'POST':
        form = PodsumowaniesankTerminowaForm(instance=sankcjaterm)
    else:
        form = PodsumowaniesankTerminowaForm(instance=sankcjaterm, data=request.POST)
        if form.is_valid():
            form.save()
    dane = {'sankcjaterm': sankcjaterm, 'term_id': term_id, 'form':form}
    return render(request, 'Kalkulator/sankcjaterm.html', dane)

def sankcjaefa(request, id):
    form = PodsumowaniesankEFAForm()
    sankcjaefa = SankcjaEFA.objects.get(pk=id)
    efa_id = id
    dane = {'sankcjaefa': sankcjaefa, 'efa_id': efa_id, 'form':form}
    return render(request, 'Kalkulator/sankcjaefa.html', dane)

def dodajwartoscefa(request, id):
    sankcjaefa = SankcjaEFA.objects.get(pk=id)
    efa_id = id
    if request.method != 'POST':
        form = PodsumowaniesankEFAForm(instance=sankcjaefa)
    else:
        form = PodsumowaniesankEFAForm(instance=sankcjaefa, data=request.POST)
        if form.is_valid():
            form.save()
    # utworzenie połączenia z bazą przechowywaną na dysku
    con = sqlite3.connect('db.sqlite3')
    # dostęp do kolumn przez indeksy i przez nazwy
    con.row_factory = sqlite3.Row

    user = request.user
    if request.user.is_authenticated:
        # utworzenie obiektu kursora
        cur = con.cursor()

        cur.execute(f"SELECT * FROM Kalkulator_sankcjaefa WHERE id = {user.id};")
        rows = cur.fetchall()
        for row in rows:
            pow_go = float(str(row[1]))
            pow_efa = float(str(row[2]))
            if float(pow_go) != 0:
                piecproc_efa = round((float(pow_go) * 0.05), 4)
                proc_efa = round((float(pow_efa * 100) / float(pow_go)), 2)
                pow_proc_efa = pow_go * (proc_efa / 100)
                if piecproc_efa >= pow_proc_efa:
                    braku_efa = round((float(piecproc_efa) - round(pow_proc_efa, 2)), 4)
                else:
                    braku_efa = 0
            else:
                piecproc_efa = 0
                proc_efa = 0
                braku_efa = 0

#            # utworzenie połączenia z bazą przechowywaną na dysku
#            con = sqlite3.connect('db.sqlite3')
#            # dostęp do kolumn przez indeksy i przez nazwy
#            con.row_factory = sqlite3.Row

#            cur = con.cursor()
            cur.execute('UPDATE Kalkulator_sankcjaefa SET piecproc_efa = ? WHERE id = ?;', (float(piecproc_efa), user.id))
            cur.execute('UPDATE Kalkulator_sankcjaefa SET proc_efa = ? WHERE id = ?;', (float(proc_efa), user.id))
            cur.execute('UPDATE Kalkulator_sankcjaefa SET braku_efa = ? WHERE id = ?;', (float(braku_efa), user.id))
            con.commit()

    dane = {'sankcjaefa': sankcjaefa, 'efa_id': efa_id, 'form':form, 'piecproc_efa': piecproc_efa, 'proc_efa': proc_efa, 'braku_efa': braku_efa}
    return render(request, 'Kalkulator/sankcjaefa.html', dane)

def sankcjaniezad(request, id):
    form = PodsumowaniesankNiezadeklForm()
    sankcjaniezad = SankcjaNiezadekl.objects.get(pk=id)
    nie_id = id
    dane = {'sankcjaniezad': sankcjaniezad, 'nie_id': nie_id, 'form':form}
    return render(request, 'Kalkulator/sankcjaniezad.html', dane)

def dodajwartoscniezad(request, id):
    sankcjaniezad = SankcjaNiezadekl.objects.get(pk=id)
    nie_id = id
    if request.method != 'POST':
        form = PodsumowaniesankNiezadeklForm(instance=sankcjaniezad)
    else:
        form = PodsumowaniesankNiezadeklForm(instance=sankcjaniezad, data=request.POST)
        if form.is_valid():
            form.save()
    dane = {'sankcjaniezad': sankcjaniezad, 'nie_id': nie_id, 'form':form}
    return render(request, 'Kalkulator/sankcjaniezad.html', dane)

def podsumowanie(request):
    platnoscjpo_podsumowanie = PlatnoscJPO.objects.exclude(dodanejpo='0')
    dodanejpo = 0
    for platnoscjpo in platnoscjpo_podsumowanie:
        dodanejpo = dodanejpo + float(platnoscjpo.dodanejpo)
        dodanejpo = float(round(dodanejpo, 2))
    platnoscupp_podsumowanie = PlatnoscUPP.objects.exclude(dodaneupp='0')
    dodaneupp = 0
    for platnoscupp in platnoscupp_podsumowanie:
        dodaneupp = dodaneupp + float(platnoscupp.dodaneupp)
        dodaneupp = float(round(dodaneupp, 2))
    platnoscp_str_podsumowanie = PlatnoscP_STR.objects.exclude(dodanep_str='0')
    dodanep_str = 0
    for platnoscp_str in platnoscp_str_podsumowanie:
        dodanep_str = dodanep_str + float(platnoscp_str.dodanep_str)
        dodanep_str = float(round(dodanep_str, 2))
    platnoscp_pas_podsumowanie = PlatnoscP_PAS.objects.exclude(dodanep_pas='0')
    dodanep_pas = 0
    for platnoscp_pas in platnoscp_pas_podsumowanie:
        dodanep_pas = dodanep_pas + float(platnoscp_pas.dodanep_pas)
        dodanep_pas = float(round(dodanep_pas, 2))
    platnoscp_burak_podsumowanie = PlatnoscP_Burak.objects.exclude(dodanep_burak='0')
    dodanep_burak = 0
    for platnoscp_burak in platnoscp_burak_podsumowanie:
        dodanep_burak = dodanep_burak + float(platnoscp_burak.dodanep_burak)
        dodanep_burak = float(round(dodanep_burak, 2))
    platnoscp_skrobia_podsumowanie = PlatnoscP_Skrobia.objects.exclude(dodanep_skrobia='0')
    dodanep_skrobia = 0
    for platnoscp_skrobia in platnoscp_skrobia_podsumowanie:
        dodanep_skrobia = dodanep_skrobia + float(platnoscp_skrobia.dodanep_skrobia)
        dodanep_skrobia = float(round(dodanep_skrobia, 2))
    platnoscp_trus_podsumowanie = PlatnoscP_Truskawka.objects.exclude(dodanep_trus='0')
    dodanep_trus = 0
    for platnoscp_trus in platnoscp_trus_podsumowanie:
        dodanep_trus = dodanep_trus + float(platnoscp_trus.dodanep_trus)
        dodanep_trus = float(round(dodanep_trus, 2))
    platnoscpomidor_podsumowanie = PlatnoscPomidor.objects.exclude(dodanepomidor='0')
    dodanepomidor = 0
    for platnoscpomidor in platnoscpomidor_podsumowanie:
        dodanepomidor = dodanepomidor + float(platnoscpomidor.dodanepomidor)
        dodanepomidor = float(round(dodanepomidor, 2))
    platnoscchmiel_podsumowanie = PlatnoscChmiel.objects.exclude(dodanechmiel='0')
    dodanechmiel = 0
    for platnoscchmiel in platnoscchmiel_podsumowanie:
        dodanechmiel = dodanechmiel + float(platnoscchmiel.dodanechmiel)
        dodanechmiel = float(round(dodanechmiel, 2))
    platnosclen_podsumowanie = PlatnoscLen.objects.exclude(dodanelen='0')
    dodanelen = 0
    for platnosclen in platnosclen_podsumowanie:
        dodanelen = dodanelen + float(platnosclen.dodanelen)
        dodanelen = float(round(dodanelen, 2))
    platnosckonopie_podsumowanie = PlatnoscKonopie.objects.exclude(dodanekonopie='0')
    dodanekonopie = 0
    for platnosckonopie in platnosckonopie_podsumowanie:
        dodanekonopie = dodanekonopie + float(platnosckonopie.dodanekonopie)
        dodanekonopie = float(round(dodanekonopie, 2))
    platnosctyton_podsumowanie = PlatnoscTyton.objects.exclude(dodanetyton='0')
    dodanetyton = 0
    for platnosctyton in platnosctyton_podsumowanie:
        dodanetyton = dodanetyton + float(platnosctyton.dodanetyton)
        dodanetyton = float(round(dodanetyton, 2))
    platnoscvirginia_podsumowanie = PlatnoscVirginia.objects.exclude(dodanevirginia='0')
    dodanevirginia = 0
    for platnoscvirginia in platnoscvirginia_podsumowanie:
        dodanevirginia = dodanevirginia + float(platnoscvirginia.dodanevirginia)
        dodanevirginia = float(round(dodanevirginia, 2))
    platnosckrowy_podsumowanie = PlatnoscKrowy.objects.exclude(dodanekrowy='0')
    dodanekrowy = 0
    for platnosckrowy in platnosckrowy_podsumowanie:
        dodanekrowy = dodanekrowy + float(platnosckrowy.dodanekrowy)
        dodanekrowy = float(round(dodanekrowy, 2))
    platnoscbydlo_podsumowanie = PlatnoscBydlo.objects.exclude(dodanebydlo='0')
    dodanebydlo = 0
    for platnoscbydlo in platnoscbydlo_podsumowanie:
        dodanebydlo = dodanebydlo + float(platnoscbydlo.dodanebydlo)
        dodanebydlo = float(round(dodanebydlo, 2))
    platnoscowce_podsumowanie = PlatnoscOwce.objects.exclude(dodaneowce='0')
    dodaneowce = 0
    for platnoscowce in platnoscowce_podsumowanie:
        dodaneowce = dodanebydlo + float(platnoscowce.dodaneowce)
        dodaneowce = float(round(dodaneowce, 2))
    platnosckozy_podsumowanie = PlatnoscKozy.objects.exclude(dodanekozy='0')
    dodanekozy = 0
    for platnosckozy in platnosckozy_podsumowanie:
        dodanekozy = dodanekozy + float(platnosckozy.dodanekozy)
        dodanekozy = float(round(dodanekozy, 2))
    sankcjacc_podsumowanie = SankcjaCC.objects.exclude(dodanecc='0')
    dodanecc = 0
    for sankcjacc in sankcjacc_podsumowanie:
        dodanecc = dodanecc + float(sankcjacc.dodanecc)
        dodanecc = float(round(dodanecc, 2))
    sankcjaefa_podsumowanie = SankcjaEFA.objects.exclude(pow_go='0')
    pow_go = 0
    for sankcjaefa in sankcjaefa_podsumowanie:
        pow_go = pow_go + float(sankcjaefa.pow_go)
        pow_go = float(round(pow_go, 2))
    sankcjaterm_podsumowanie = SankcjaTerminowa.objects.exclude(dodaneterm='0')
    dodaneterm = 0
    for sankcjaterm in sankcjaterm_podsumowanie:
        dodaneterm= dodaneterm + float(sankcjaterm.dodaneterm)
        dodaneterm = float(round(dodaneterm, 2))
    sankcjaniezad_podsumowanie = SankcjaNiezadekl.objects.exclude(dodaneniezad='0')
    dodaneniezad = 0
    for sankcjaniezad in sankcjaniezad_podsumowanie:
        dodaneniezad = dodaneniezad + float(sankcjaniezad.dodaneniezad)
        dodaneniezad = float(round(dodaneniezad, 2))
    dane = {'platnoscjpo_podsumowanie': platnoscjpo_podsumowanie,
            'dodanejpo': dodanejpo,
            'platnoscupp_podsumowanie': platnoscupp_podsumowanie,
            'dodaneupp': dodaneupp,
            'platnoscp_str_podsumowanie': platnoscp_str_podsumowanie,
            'dodanep_str': dodanep_str,
            'platnoscp_pas_podsumowanie': platnoscp_pas_podsumowanie,
            'dodanep_pas': dodanep_pas,
            'platnoscp_burak_podsumowanie': platnoscp_burak_podsumowanie,
            'dodanep_burak': dodanep_burak,
            'platnoscp_skrobia_podsumowanie': platnoscp_skrobia_podsumowanie,
            'dodanep_skrobia': dodanep_skrobia,
            'platnoscp_trus_podsumowanie': platnoscp_trus_podsumowanie,
            'dodanep_trus': dodanep_trus,
            'platnoscpomidor_podsumowanie': platnoscpomidor_podsumowanie,
            'dodanepomidor': dodanepomidor,
            'platnoscchmiel_podsumowanie': platnoscchmiel_podsumowanie,
            'dodanechmiel': dodanechmiel,
            'platnosclen_podsumowanie': platnosclen_podsumowanie,
            'dodanelen': dodanelen,
            'platnosckonopie_podsumowanie': platnosckonopie_podsumowanie,
            'dodanekonopie': dodanekonopie,
            'platnosctyton_podsumowanie': platnosctyton_podsumowanie,
            'dodanetyton': dodanetyton,
            'platnoscvirginia_podsumowanie': platnoscvirginia_podsumowanie,
            'dodanevirginia': dodanevirginia,
            'platnosckrowy_podsumowanie': platnosckrowy_podsumowanie,
            'dodanekrowy': dodanekrowy,
            'platnoscbydlo_podsumowanie': platnoscbydlo_podsumowanie,
            'dodanebydlo': dodanebydlo,
            'platnoscowce_podsumowanie': platnoscowce_podsumowanie,
            'dodaneowce': dodaneowce,
            'platnosckozy_podsumowanie': platnosckozy_podsumowanie,
            'dodanekozy': dodanekozy,
            'sankcjacc_podsumowanie': sankcjacc_podsumowanie,
            'dodanecc': dodanecc,
            'sankcjaefa_podsumowanie': sankcjaefa_podsumowanie,
            'pow_go': pow_go,
            'sankcjaterm_podsumowanie': sankcjaterm_podsumowanie,
            'dodaneterm': dodaneterm,
            'sankcjaniezad_podsumowanie': sankcjaniezad_podsumowanie,
            'dodaneniezad': dodaneniezad,
            }
    return render(request, 'Kalkulator/podsumowanie.html', dane)

def podsumowanieplatnosci(request):
    platnoscjpo_podsumowanieplatnosci = PlatnoscJPO.objects.exclude(dodanejpo='0')
    dodanejpo = 0
    dodanezaz = 0
    dodaneredys = 0
    for platnoscjpo in platnoscjpo_podsumowanieplatnosci:
        dodanejpo = dodanejpo + float(platnoscjpo.wynikjpo)
        dodanejpo = float(round(dodanejpo, 2))
        dodanezaz = dodanezaz + float(platnoscjpo.wynikzaz)
        dodanezaz = float(round(dodanezaz, 2))
        dodaneredys = dodaneredys + float(platnoscjpo.wynikredys)
        dodaneredys = float(round(dodaneredys, 2))
    platnoscupp_podsumowanieplatnosci = PlatnoscUPP.objects.exclude(dodaneupp='0')
    dodaneupp = 0
    for platnoscupp in platnoscupp_podsumowanieplatnosci:
        dodaneupp = dodaneupp + float(platnoscupp.wynikupp)
        dodaneupp = float(round(dodaneupp, 2))
    platnoscp_str_podsumowanieplatnosci = PlatnoscP_STR.objects.exclude(dodanep_str='0')
    dodanep_str = 0
    for platnoscp_str in platnoscp_str_podsumowanieplatnosci:
        dodanep_str = dodanep_str + float(platnoscp_str.wynikp_str)
        dodanep_str = float(round(dodanep_str, 2))
    platnoscp_pas_podsumowanieplatnosci = PlatnoscP_PAS.objects.exclude(dodanep_pas='0')
    dodanep_pas = 0
    for platnoscp_pas in platnoscp_pas_podsumowanieplatnosci:
        dodanep_pas = dodanep_pas + float(platnoscp_pas.wynikp_pas)
        dodanep_pas = float(round(dodanep_pas, 2))
    platnoscp_burak_podsumowanieplatnosci = PlatnoscP_Burak.objects.exclude(dodanep_burak='0')
    dodanep_burak = 0
    for platnoscp_burak in platnoscp_burak_podsumowanieplatnosci:
        dodanep_burak = dodanep_burak + float(platnoscp_burak.wynikp_burak)
        dodanep_burak = float(round(dodanep_burak, 2))
    platnoscp_skrobia_podsumowanieplatnosci = PlatnoscP_Skrobia.objects.exclude(dodanep_skrobia='0')
    dodanep_skrobia = 0
    for platnoscp_skrobia in platnoscp_skrobia_podsumowanieplatnosci:
        dodanep_skrobia = dodanep_skrobia + float(platnoscp_skrobia.wynikp_skrobia)
        dodanep_skrobia = float(round(dodanep_skrobia, 2))
    platnoscp_trus_podsumowanieplatnosci = PlatnoscP_Truskawka.objects.exclude(dodanep_trus='0')
    dodanep_trus = 0
    for platnoscp_trus in platnoscp_trus_podsumowanieplatnosci:
        dodanep_trus = dodanep_trus + float(platnoscp_trus.wynikp_trus)
        dodanep_trus = float(round(dodanep_trus, 2))
    platnoscpomidor_podsumowanieplatnosci = PlatnoscPomidor.objects.exclude(dodanepomidor='0')
    dodanepomidor = 0
    for platnoscpomidor in platnoscpomidor_podsumowanieplatnosci:
        dodanepomidor = dodanepomidor + float(platnoscpomidor.wynikpomidor)
        dodanepomidor = float(round(dodanepomidor, 2))
    platnoscchmiel_podsumowanieplatnosci = PlatnoscChmiel.objects.exclude(dodanechmiel='0')
    dodanechmiel = 0
    for platnoscchmiel in platnoscchmiel_podsumowanieplatnosci:
        dodanechmiel = dodanechmiel + float(platnoscchmiel.wynikchmiel)
        dodanechmiel = float(round(dodanechmiel, 2))
    platnosclen_podsumowanieplatnosci = PlatnoscLen.objects.exclude(dodanelen='0')
    dodanelen = 0
    for platnosclen in platnosclen_podsumowanieplatnosci:
        dodanelen = dodanelen + float(platnosclen.wyniklen)
        dodanelen = float(round(dodanelen, 2))
    platnosckonopie_podsumowanieplatnosci = PlatnoscKonopie.objects.exclude(dodanekonopie='0')
    dodanekonopie = 0
    for platnosckonopie in platnosckonopie_podsumowanieplatnosci:
        dodanekonopie = dodanekonopie + float(platnosckonopie.wynikkonopie)
        dodanekonopie = float(round(dodanekonopie, 2))
    platnosctyton_podsumowanieplatnosci = PlatnoscTyton.objects.exclude(dodanetyton='0')
    dodanetyton = 0
    for platnosctyton in platnosctyton_podsumowanieplatnosci:
        dodanetyton = dodanetyton + float(platnosctyton.wyniktyton)
        dodanetyton = float(round(dodanetyton, 2))
    platnoscvirginia_podsumowanieplatnosci = PlatnoscVirginia.objects.exclude(dodanevirginia='0')
    dodanevirginia = 0
    for platnoscvirginia in platnoscvirginia_podsumowanieplatnosci:
        dodanevirginia = dodanevirginia + float(platnoscvirginia.wynikvirginia)
        dodanevirginia = float(round(dodanevirginia, 2))
    platnosckrowy_podsumowanieplatnosci = PlatnoscKrowy.objects.exclude(dodanekrowy='0')
    dodanekrowy = 0
    for platnosckrowy in platnosckrowy_podsumowanieplatnosci:
        dodanekrowy = dodanekrowy + float(platnosckrowy.wynikkrowy)
        dodanekrowy = float(round(dodanekrowy, 2))
    platnoscbydlo_podsumowanieplatnosci = PlatnoscBydlo.objects.exclude(dodanebydlo='0')
    dodanebydlo = 0
    for platnoscbydlo in platnoscbydlo_podsumowanieplatnosci:
        dodanebydlo = dodanebydlo + float(platnoscbydlo.wynikbydlo)
        dodanebydlo = float(round(dodanebydlo, 2))
    platnoscowce_podsumowanieplatnosci = PlatnoscOwce.objects.exclude(dodaneowce='0')
    dodaneowce = 0
    for platnoscowce in platnoscowce_podsumowanieplatnosci:
        dodaneowce = dodaneowce + float(platnoscowce.wynikowce)
        dodaneowce = float(round(dodaneowce, 2))
    platnosckozy_podsumowanieplatnosci = PlatnoscKozy.objects.exclude(dodanekozy='0')
    dodanekozy = 0
    for platnosckozy in platnosckozy_podsumowanieplatnosci:
        dodanekozy = dodanekozy + float(platnosckozy.wynikkozy)
        dodanekozy = float(round(dodanekozy, 2))
    dane = {'platnoscjpo_podsumowanieplatnosci': platnoscjpo_podsumowanieplatnosci,
            'dodanejpo': dodanejpo,
            'dodanezaz': dodanezaz,
            'dodaneredys': dodaneredys,
            'platnoscupp_podsumowanieplatnosci': platnoscupp_podsumowanieplatnosci,
            'dodaneupp': dodaneupp,
            'platnoscp_str_podsumowanieplatnosci': platnoscp_str_podsumowanieplatnosci,
            'dodanep_str': dodanep_str,
            'platnoscp_pas_podsumowanieplatnosci': platnoscp_pas_podsumowanieplatnosci,
            'dodanep_pas': dodanep_pas,
            'platnoscp_burak_podsumowanieplatnosci': platnoscp_burak_podsumowanieplatnosci,
            'dodanep_burak': dodanep_burak,
            'platnoscp_skrobia_podsumowanieplatnosci': platnoscp_skrobia_podsumowanieplatnosci,
            'dodanep_skrobia': dodanep_skrobia,
            'platnoscp_trus_podsumowanieplatnosci': platnoscp_trus_podsumowanieplatnosci,
            'dodanep_trus': dodanep_trus,
            'platnoscpomidor_podsumowanieplatnosci': platnoscpomidor_podsumowanieplatnosci,
            'dodanepomidor': dodanepomidor,
            'platnoscchmiel_podsumowanieplatnosci': platnoscchmiel_podsumowanieplatnosci,
            'dodanechmiel': dodanechmiel,
            'platnosclen_podsumowanieplatnosci': platnosclen_podsumowanieplatnosci,
            'dodanelen': dodanelen,
            'platnosckonopie_podsumowanieplatnosci': platnosckonopie_podsumowanieplatnosci,
            'dodanekonopie': dodanekonopie,
            'platnosctyton_podsumowanieplatnosci': platnosctyton_podsumowanieplatnosci,
            'dodanetyton': dodanetyton,
            'platnoscvirginia_podsumowanieplatnosci': platnoscvirginia_podsumowanieplatnosci,
            'dodanevirginia': dodanevirginia,
            'platnosckrowy_podsumowanieplatnosci': platnosckrowy_podsumowanieplatnosci,
            'dodanekrowy': dodanekrowy,
            'platnoscbydlo_podsumowanieplatnosci': platnoscbydlo_podsumowanieplatnosci,
            'dodanebydlo': dodanebydlo,
            'platnoscowce_podsumowanieplatnosci': platnoscowce_podsumowanieplatnosci,
            'dodaneowce': dodaneowce,
            'platnosckozy_podsumowanieplatnosci': platnosckozy_podsumowanieplatnosci,
            'dodanekozy': dodanekozy,
            }
    return render(request, 'Kalkulator/podsumowanieplatnosci.html', dane)

def oblicz(request):
    # utworzenie połączenia z bazą przechowywaną na dysku
    con = sqlite3.connect('db.sqlite3')
    # dostęp do kolumn przez indeksy i przez nazwy
    con.row_factory = sqlite3.Row


    user = request.user
    if request.user.is_authenticated:

        # utworzenie obiektu kursora
        cur = con.cursor()

        # pobieranie danych z bazy
        cur.execute(f"SELECT * FROM Kalkulator_platnoscjpo WHERE id = {user.id};")
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

        cur.execute(f"SELECT * FROM Kalkulator_platnoscupp WHERE id = {user.id};")
        rows = cur.fetchall()
        for row in rows:
            powierzchnia_upp = float(str(row[1]))
            zmniejszenia_upp = float(str(row[2]))

        cur.execute(f"SELECT * FROM Kalkulator_platnoscjpo WHERE id = {user.id};")
        rows = cur.fetchall()
        for row in rows:
            czy_mr = str(row[3])

        powierzchnia_mr = powierzchnia_gospodarstwa
        zmniejszenia_mr = zmniejszenia_jpo

        cur.execute(f"SELECT * FROM Kalkulator_platnoscp_str WHERE id = {user.id};")
        rows = cur.fetchall()
        for row in rows:
            powierzchnia_p_str = float(str(row[1]))
            zmniejszenia_p_str = float(str(row[2]))

        cur.execute(f"SELECT * FROM Kalkulator_platnoscp_pas WHERE id = {user.id};")
        rows = cur.fetchall()
        for row in rows:
            powierzchnia_p_pas = float(str(row[1]))
            zmniejszenia_p_pas = float(str(row[2]))

        cur.execute(f"SELECT * FROM Kalkulator_platnoscp_burak WHERE id = {user.id};")
        rows = cur.fetchall()
        for row in rows:
            powierzchnia_p_burak = float(str(row[1]))
            zmniejszenia_p_burak = float(str(row[2]))

        cur.execute(f"SELECT * FROM Kalkulator_platnoscp_skrobia WHERE id = {user.id};")
        rows = cur.fetchall()
        for row in rows:
            powierzchnia_p_skrobia = float(str(row[1]))
            zmniejszenia_p_skrobia = float(str(row[2]))

        cur.execute(f"SELECT * FROM Kalkulator_platnoscp_truskawka WHERE id = {user.id};")
        rows = cur.fetchall()
        for row in rows:
            powierzchnia_p_truskawka = float(str(row[1]))
            zmniejszenia_p_truskawka = float(str(row[2]))

        cur.execute(f"SELECT * FROM Kalkulator_platnoscpomidor WHERE id = {user.id};")
        rows = cur.fetchall()
        for row in rows:
            powierzchnia_pomidor = float(str(row[1]))
            zmniejszenia_pomidor = float(str(row[2]))

        cur.execute(f"SELECT * FROM Kalkulator_platnoscchmiel WHERE id = {user.id};")
        rows = cur.fetchall()
        for row in rows:
            powierzchnia_chmiel = float(str(row[1]))
            zmniejszenia_chmiel = float(str(row[2]))

        cur.execute(f"SELECT * FROM Kalkulator_platnosclen WHERE id = {user.id};")
        rows = cur.fetchall()
        for row in rows:
            powierzchnia_len = float(str(row[1]))
            zmniejszenia_len = float(str(row[2]))

        cur.execute(f"SELECT * FROM Kalkulator_platnosckonopie WHERE id = {user.id};")
        rows = cur.fetchall()
        for row in rows:
            powierzchnia_konopie = float(str(row[1]))
            zmniejszenia_konopie = float(str(row[2]))

        cur.execute(f"SELECT * FROM Kalkulator_platnosctyton WHERE id = {user.id};")
        rows = cur.fetchall()
        for row in rows:
            masa_tyton = float(str(row[1]))


        cur.execute(f"SELECT * FROM Kalkulator_platnoscvirginia WHERE id = {user.id};")
        rows = cur.fetchall()
        for row in rows:
            masa_virginia = float(str(row[1]))

        cur.execute(f"SELECT * FROM Kalkulator_platnosckrowy WHERE id = {user.id};")
        rows = cur.fetchall()
        for row in rows:
            liczba_krow = float(str(row[1]))
            zmniejszenia_krowy = float(str(row[2]))
            liczba_krow_po_zmniejszeniach = float(liczba_krow) - float(zmniejszenia_krowy)

        cur.execute(f"SELECT * FROM Kalkulator_platnoscbydlo WHERE id = {user.id};")
        rows = cur.fetchall()
        for row in rows:
            liczba_bydla = float(str(row[1]))
            zmniejszenia_bydlo = float(str(row[2]))
            liczba_bydla_po_zmniejszeniach = float(liczba_bydla) - float(zmniejszenia_bydlo)

        cur.execute(f"SELECT * FROM Kalkulator_platnosckozy WHERE id = {user.id};")
        rows = cur.fetchall()
        for row in rows:
            liczba_koz = float(str(row[1]))
            zmniejszenia_koz = float(str(row[2]))
            liczba_koz_po_zmniejszeniach = float(liczba_koz) - float(zmniejszenia_koz)

        cur.execute(f"SELECT * FROM Kalkulator_platnoscowce WHERE id = {user.id};")
        rows = cur.fetchall()
        for row in rows:
            liczba_owiec = float(str(row[1]))
            zmniejszenia_owiec = float(str(row[2]))
            liczba_owiec_po_zmniejszeniach = float(liczba_owiec) - float(zmniejszenia_owiec)

        cur.execute(f"SELECT * FROM Kalkulator_sankcjacc WHERE id = {user.id};")
        rows = cur.fetchall()
        for row in rows:
            sankcja_cc = float(str(row[1]))

        cur.execute(f"SELECT * FROM Kalkulator_sankcjaterminowa WHERE id = {user.id};")
        rows = cur.fetchall()
        for row in rows:
            sankcje_terminowe = float(str(row[1]))

        cur.execute(f"SELECT * FROM Kalkulator_sankcjaefa WHERE id = {user.id};")
        rows = cur.fetchall()
        for row in rows:
            pow_go = float(str(row[1]))
            pow_efa = float(str(row[2]))
            if float(pow_go) != 0:
                piecproc_efa = round((float(pow_go) * 0.05), 4)
                proc_efa = round((float(pow_efa * 100) / float(pow_go)), 2)
                pow_proc_efa = pow_go * (proc_efa / 100)
                if piecproc_efa >= pow_proc_efa:
                    braku_efa = round((float(piecproc_efa) - round(pow_proc_efa, 2)), 4)
                else:
                    braku_efa = 0
            else:
                piecproc_efa = 0
                proc_efa = 0
                braku_efa = 0

        cur.execute(f"SELECT * FROM Kalkulator_sankcjaniezadekl WHERE id = {user.id};")
        rows = cur.fetchall()
        for row in rows:
            sankcje_niezadekl = float(str(row[1]))

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
    platnoc_jpo_po_sankcjach = (float(platnosc_jpo) * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcje_niezadekl)) / 100) * ((100 - float(sankcja_cc)) / 100))

    # Wyliczenie płatności za Zazielenienie
    platnosc_zazielenienie = (float(powierzchnia_po_zmniejszeniach)-(10*float(braku_efa))) * float(stawki_platnosci['zazielenienie'])

    # Wyliczanie płatności za Zazielenienie po sankcjach terminowych i CC
    platnosc_zazielenienie_po_sankcjach = (float(platnosc_zazielenienie) * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcje_niezadekl)) / 100) * ((100 - float(sankcja_cc)) / 100))

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
    platnosc_redystrybucyjna_po_sankcjach = (float(platnosc_redystrybucyjna) * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcje_niezadekl)) / 100) * ((100 - float(sankcja_cc)) / 100))

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
    platnoc_upp_po_sankcjach = (float(platnosc_upp) * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcje_niezadekl)) / 100))

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
            platnoc_mr_po_sankcjach = (float(platnosc_mr) * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcje_niezadekl)) / 100) * ((100 - float(sankcja_cc)) / 100))
        else:
            platnoc_mr_po_sankcjach = (50 * float(stawki_platnosci['mr']) * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcje_niezadekl)) / 100) * ((100 - float(sankcja_cc)) / 100))
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
    if float(powierzchnia_p_str_po_zmniejszeniach) <= 75:
        platnoc_p_str_po_sankcjach = (float(platnosc_p_str) * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcje_niezadekl)) / 100) * ((100 - float(sankcja_cc)) / 100))
    else:
        platnoc_p_str_po_sankcjach = (75 * ((1 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcje_niezadekl)) / 100) * ((100 - float(sankcja_cc)) / 100))

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
    if float(powierzchnia_p_pas_po_zmniejszeniach) <= 75:
        platnoc_p_pas_po_sankcjach = (float(platnosc_p_pas) * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcje_niezadekl)) / 100) * ((100 - float(sankcja_cc)) / 100))
    else:
        platnoc_p_pas_po_sankcjach = (75 * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcje_niezadekl)) / 100) * ((100 - float(sankcja_cc)) / 100))

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
    platnoc_p_burak_po_sankcjach = (float(platnosc_p_burak) * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcje_niezadekl)) / 100) * ((100 - float(sankcja_cc)) / 100))

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
    platnoc_p_skrobia_po_sankcjach = (float(platnosc_p_skrobia) * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcje_niezadekl)) / 100) * ((100 - float(sankcja_cc)) / 100))

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
    platnoc_p_truskawka_po_sankcjach = (float(platnosc_p_truskawka) * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcje_niezadekl)) / 100) * ((100 - float(sankcja_cc)) / 100))

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
    platnoc_pomidor_po_sankcjach = (float(platnosc_pomidor) * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcje_niezadekl)) / 100) * ((100 - float(sankcja_cc)) / 100))

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
    platnoc_chmiel_po_sankcjach = (float(platnosc_chmiel) * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcje_niezadekl)) / 100) * ((100 - float(sankcja_cc)) / 100))

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
    platnoc_len_po_sankcjach = (float(platnosc_len) * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcje_niezadekl)) / 100) * ((100 - float(sankcja_cc)) / 100))

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
        platnosc_konopie = float(powierzchnia_konopie) * float(stawki_platnosci['konopie'])
    else:
        if float(procent_zmniejszenia_konopie) < 3:
            platnosc_konopie = float(powierzchnia_konopie_po_zmniejszeniach) * float(stawki_platnosci['konopie'])
        elif float(procent_zmniejszenia_konopie) > 20:
            platnosc_konopie = 0
        else:
            platnosc_konopie = (float(powierzchnia_konopie_po_zmniejszeniach) - (float(zmniejszenia_konopie) * 2)) * float(stawki_platnosci['konopie'])

    #Wyliczenie płatności Konopie po sankcjach terminowych i CC
    platnoc_konopie_po_sankcjach = (float(platnosc_konopie) * ((100 - float(sankcje_terminowe)) / 100) * ((100 - float(sankcje_niezadekl)) / 100) * ((100 - float(sankcja_cc)) / 100))

    #Wyliczanie płatności Tytoń
    platnosc_tyton = 0
    if float(masa_tyton) != 0:
        platnosc_tyton = float(masa_tyton) * float(stawki_platnosci['tytoń'])
    else:
        platnosc_tyton = 0

    #Wyliczenie płatności do Tytoniu po sankcjach terminowych
    platnoc_tyton_po_sankcjach = (float(platnosc_tyton) * ((100 - float(sankcje_terminowe)) / 100))

    #Wyliczanie płatności Tytoń Virginia
    platnosc_virginia = 0
    if float(masa_virginia) != 0:
        platnosc_virginia = float(masa_virginia) * float(stawki_platnosci['tytoń Virginia'])
    else:
        platnosc_virginia = 0

    #Wyliczenie płatności do Tytoniu Virginia po sankcjach terminowych
    platnoc_virginia_po_sankcjach = (float(platnosc_virginia) * ((100 - float(sankcje_terminowe)) / 100))

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
    if powierzchnia_konopie >= 0:
        print(f"Twoja płatność do konopii wynosi: {round(float(platnoc_konopie_po_sankcjach), 2)} zł.")
    if masa_tyton >= 0:
        print(f"Twoja płatność do tytoniu wynosi: {round(float(platnoc_tyton_po_sankcjach), 2)} zł.")
    if masa_virginia >= 0:
        print(f"Twoja płatność do tytoniu Virginia wynosi: {round(float(platnoc_virginia_po_sankcjach), 2)} zł.")
    if liczba_krow >= 0:
        print(f"Twoja płatność dla krów wynosi: {round(platnoc_krowy_po_sankcjach, 2)} zł.")
    if liczba_bydla >= 0:
        print(f"Twoja płatność dla bydła wynosi: {round(platnoc_bydlo_po_sankcjach, 2)} zł.")
    if liczba_koz >= 0:
        print(f"Twoja płatność dla kóz wynosi: {round(platnoc_koz_po_sankcjach, 2)} zł.")
    if liczba_owiec >= 0:
        print(f"Twoja płatność dla owiec wynosi: {round(platnoc_owiec_po_sankcjach, 2)} zł.")


    user = request.user
    if request.user.is_authenticated:
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
        cur.execute('UPDATE Kalkulator_platnosctyton SET wyniktyton = ? WHERE id = ?;', (round(float(platnoc_tyton_po_sankcjach), 2), user.id))
        cur.execute('UPDATE Kalkulator_platnoscvirginia SET wynikvirginia = ? WHERE id = ?;', (round(float(platnoc_virginia_po_sankcjach), 2), user.id))
        cur.execute('UPDATE Kalkulator_platnosckrowy SET wynikkrowy = ? WHERE id = ?;', (round(float(platnoc_krowy_po_sankcjach), 2), user.id))
        cur.execute('UPDATE Kalkulator_platnoscbydlo SET wynikbydlo = ? WHERE id = ?;', (round(float(platnoc_bydlo_po_sankcjach), 2), user.id))
        cur.execute('UPDATE Kalkulator_platnosckozy SET wynikkozy = ? WHERE id = ?;', (round(float(platnoc_koz_po_sankcjach), 2), user.id))
        cur.execute('UPDATE Kalkulator_platnoscowce SET wynikowce = ? WHERE id = ?;', (round(float(platnoc_owiec_po_sankcjach), 2), user.id))
        cur.execute('UPDATE Kalkulator_platnoscjpo SET wynikzaz = ? WHERE id = ?;', (round(float(platnosc_zazielenienie_po_sankcjach), 2), user.id))
        cur.execute('UPDATE Kalkulator_platnoscjpo SET wynikredys = ? WHERE id = ?;', (round(float(platnosc_redystrybucyjna_po_sankcjach), 2), user.id))
        con.commit()
    return render(request, 'Kalkulator/podsumowanie.html')

def linki(request):
    return render(request, 'Kalkulator/linki.html')


