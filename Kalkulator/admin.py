from django.contrib import admin

# Register your models here.

from .models import PlatnoscJPO
from .models import PlatnoscUPP
from .models import PlatnoscP_PAS
from .models import PlatnoscP_STR
from .models import PlatnoscPomidor
from .models import PlatnoscP_Burak
from .models import PlatnoscP_Skrobia
from .models import PlatnoscP_Truskawka
from .models import PlatnoscChmiel
from .models import PlatnoscLen
from .models import PlatnoscKonopie
from .models import PlatnoscKrowy
from .models import PlatnoscBydlo
from .models import PlatnoscOwce
from .models import PlatnoscKozy
from .models import PlatnoscTyton
from .models import PlatnoscVirginia
from .models import SankcjaCC
from .models import SankcjaTerminowa
from .models import SankcjaEFA
from .models import SankcjaNiezadekl
admin.site.register(PlatnoscJPO)
admin.site.register(PlatnoscUPP)
admin.site.register(PlatnoscP_PAS)
admin.site.register(PlatnoscP_STR)
admin.site.register(PlatnoscP_Burak)
admin.site.register(PlatnoscP_Skrobia)
admin.site.register(PlatnoscP_Truskawka)
admin.site.register(PlatnoscPomidor)
admin.site.register(PlatnoscChmiel)
admin.site.register(PlatnoscLen)
admin.site.register(PlatnoscKonopie)
admin.site.register(PlatnoscKrowy)
admin.site.register(PlatnoscBydlo)
admin.site.register(PlatnoscOwce)
admin.site.register(PlatnoscKozy)
admin.site.register(PlatnoscTyton)
admin.site.register(PlatnoscVirginia)
admin.site.register(SankcjaCC)
admin.site.register(SankcjaTerminowa)
admin.site.register(SankcjaEFA)
admin.site.register(SankcjaNiezadekl)