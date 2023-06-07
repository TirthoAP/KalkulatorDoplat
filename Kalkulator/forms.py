from django import forms
from .models import PlatnoscJPO
from .models import PlatnoscUPP
from .models import PlatnoscP_PAS
from .models import PlatnoscP_STR
from .models import PlatnoscP_Burak
from .models import PlatnoscP_Skrobia
from .models import PlatnoscP_Truskawka
from .models import PlatnoscPomidor
from .models import PlatnoscChmiel
from .models import PlatnoscLen
from .models import PlatnoscKonopie
from .models import PlatnoscTyton
from .models import PlatnoscVirginia
from .models import PlatnoscKrowy
from .models import PlatnoscBydlo
from .models import PlatnoscOwce
from .models import PlatnoscKozy
from .models import SankcjaCC
from .models import SankcjaTerminowa
from .models import SankcjaEFA
from .models import SankcjaNiezadekl

class PodsumowanieJPOForm(forms.ModelForm):
    class Meta:
        model = PlatnoscJPO
        fields = ['dodanejpo', 'zmnjpo', 'czy_mr']
        labels = {'dodanejpo': 'Wprowadź dane', 'zmnjpo': 'Wprowadź zmniejszenia', 'czy_mr': 'Czy Młody rolnik?'}

class PodsumowanieUPPForm(forms.ModelForm):
    class Meta:
        model = PlatnoscUPP
        fields = ['dodaneupp', 'zmnupp']
        labels = {'dodaneupp': 'Wprowadź dane', 'zmnupp': 'Wprowadź zmniejszenia'}

class PodsumowanieP_PASForm(forms.ModelForm):
    class Meta:
        model = PlatnoscP_PAS
        fields = ['dodanep_pas', 'zmnp_pas']
        labels = {'dodanep_pas': 'Wprowadź dane', 'zmnp_pas': 'Wprowadź zmniejszenia'}

class PodsumowanieP_STRForm(forms.ModelForm):
    class Meta:
        model = PlatnoscP_STR
        fields = ['dodanep_str', 'zmnp_str']
        labels = {'dodanep_str': 'Wprowadź dane', 'zmnp_str': 'Wprowadź zmniejszenia'}

class PodsumowanieP_BurakForm(forms.ModelForm):
    class Meta:
        model = PlatnoscP_Burak
        fields = ['dodanep_burak', 'zmnp_burak']
        labels = {'dodanep_burak': 'Wprowadź dane', 'zmnp_burak': 'Wprowadź zmniejszenia'}

class PodsumowanieP_SkrobiaForm(forms.ModelForm):
    class Meta:
        model = PlatnoscP_Skrobia
        fields = ['dodanep_skrobia', 'zmnp_skrobia']
        labels = {'dodanep_skrobia': 'Wprowadź dane', 'zmnp_skrobia': 'Wprowadź zmniejszenia'}

class PodsumowanieP_TruskawkaForm(forms.ModelForm):
    class Meta:
        model = PlatnoscP_Truskawka
        fields = ['dodanep_trus', 'zmnp_trus']
        labels = {'dodanep_trus': 'Wprowadź dane', 'zmnp_trus': 'Wprowadź zmniejszenia'}

class PodsumowaniePomidorForm(forms.ModelForm):
    class Meta:
        model = PlatnoscPomidor
        fields = ['dodanepomidor', 'zmnpomidor']
        labels = {'dodanepomidor': 'Wprowadź dane', 'zmnpomidor': 'Wprowadź zmniejszenia'}

class PodsumowanieChmielForm(forms.ModelForm):
    class Meta:
        model = PlatnoscChmiel
        fields = ['dodanechmiel', 'zmnchmiel']
        labels = {'dodanechmiel': 'Wprowadź dane', 'zmnchmiel': 'Wprowadź zmniejszenia'}

class PodsumowanieLenForm(forms.ModelForm):
    class Meta:
        model = PlatnoscLen
        fields = ['dodanelen', 'zmnlen']
        labels = {'dodanelen': 'Wprowadź dane', 'zmnlen': 'Wprowadź zmniejszenia'}

class PodsumowanieKonopieForm(forms.ModelForm):
    class Meta:
        model = PlatnoscKonopie
        fields = ['dodanekonopie', 'zmnkonopie']
        labels = {'dodanekonopie': 'Wprowadź dane', 'zmnkonopie': 'Wprowadź zmniejszenia'}

class PodsumowanieTytonForm(forms.ModelForm):
    class Meta:
        model = PlatnoscTyton
        fields = ['dodanetyton']
        labels = {'dodanetyton': 'Wprowadź dane'}

class PodsumowanieVirginiaForm(forms.ModelForm):
    class Meta:
        model = PlatnoscVirginia
        fields = ['dodanevirginia']
        labels = {'dodanevirginia': 'Wprowadź dane'}

class PodsumowanieKrowyForm(forms.ModelForm):
    class Meta:
        model = PlatnoscKrowy
        fields = ['dodanekrowy', 'zmnkrowy']
        labels = {'dodanekrowy': 'Wprowadź dane', 'zmnkrowy': 'Wprowadź zmniejszenia'}

class PodsumowanieBydloForm(forms.ModelForm):
    class Meta:
        model = PlatnoscBydlo
        fields = ['dodanebydlo', 'zmnbydlo']
        labels = {'dodanebydlo': 'Wprowadź dane', 'zmnbydlo': 'Wprowadź zmniejszenia'}

class PodsumowanieOwceForm(forms.ModelForm):
    class Meta:
        model = PlatnoscOwce
        fields = ['dodaneowce', 'zmnowce']
        labels = {'dodaneowce': 'Wprowadź dane', 'zmnowce': 'Wprowadź zmniejszenia'}

class PodsumowanieKozyForm(forms.ModelForm):
    class Meta:
        model = PlatnoscKozy
        fields = ['dodanekozy', 'zmnkozy']
        labels = {'dodanekozy': 'Wprowadź dane', 'zmnkozy': 'Wprowadź zmniejszenia'}

class PodsumowaniesankCCForm(forms.ModelForm):
    class Meta:
        model = SankcjaCC
        fields = ['dodanecc']
        labels = {'dodanecc': 'Wartość sankcji CC'}

class PodsumowaniesankTerminowaForm(forms.ModelForm):
    class Meta:
        model = SankcjaTerminowa
        fields = ['dodaneterm']
        labels = {'dodaneterm': 'Wartość sankcji Terminowych'}

class PodsumowaniesankEFAForm(forms.ModelForm):
    class Meta:
        model = SankcjaEFA
        fields = ['pow_go', 'pow_efa']
        labels = {'pow_go': 'Powierzchnia GO', 'pow_efa': 'Powierzchnia EFA'}

class PodsumowaniesankNiezadeklForm(forms.ModelForm):
    class Meta:
        model = SankcjaNiezadekl
        fields = ['dodaneniezad']
        labels = {'dodaneniezad': 'Wartość sankcji za niedeklarowanie'}




