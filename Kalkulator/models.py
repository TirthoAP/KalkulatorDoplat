from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# Create your models here.
class PlatnoscJPO(models.Model):
    Tak = 'tak'
    Nie = 'nie'
    Mlody_rolnik = (
        (Tak, 'tak'),
        (Nie, 'nie'),
    )
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa = "JPO"
    dodanejpo = models.FloatField(validators=[MinValueValidator(0.0, message="Powierzchnia gospodarstwa nie może być wartością ujemną")], default=0)
    zmnjpo = models.FloatField(validators=[MinValueValidator(0.0, message="Powierzchnia zmniejszeń nie może być wartością ujemną")], default=0)
    czy_mr = models.CharField(max_length=3, choices=Mlody_rolnik, default=Nie)
    wynikjpo = models.FloatField(default=0)
    wynikzaz = models.FloatField(default=0)
    wynikredys = models.FloatField(default=0)
    wynikmr = models.FloatField(default=0)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "PlatnoscJPO"
        verbose_name_plural = "PlatnoscJPO"


class PlatnoscUPP(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa = "UPP"
    dodaneupp = models.FloatField(validators=[MinValueValidator(0.0, message="Powierzchnia UPP nie może być wartością ujemną")], default=0)
    zmnupp = models.FloatField(validators=[MinValueValidator(0.0, message="Powierzchnia zmniejszeń nie może być wartością ujemną")], default=0)
    wynikupp = models.FloatField(default=0)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "PlatnoscUPP"
        verbose_name_plural = "PlatnoscUPP"

class PlatnoscP_STR(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa = "P_STR"
    dodanep_str = models.FloatField(validators=[MinValueValidator(0.0, message="Powierzchnia P_STR nie może być wartością ujemną")], default=0)
    zmnp_str = models.FloatField(validators=[MinValueValidator(0.0, message="Powierzchnia zmniejszeń nie może być wartością ujemną")], default=0)
    wynikp_str = models.FloatField(default=0)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "PlatnoscP_STR"
        verbose_name_plural = "PlatnoscP_STR"

class PlatnoscP_PAS(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa = "P_PAS"
    dodanep_pas = models.FloatField(validators=[MinValueValidator(0.0, message="Powierzchnia P_PAS nie może być wartością ujemną")], default=0)
    zmnp_pas = models.FloatField(validators=[MinValueValidator(0.0, message="Powierzchnia zmniejszeń nie może być wartością ujemną")], default=0)
    wynikp_pas = models.FloatField(default=0)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "PlatnoscP_PAS"
        verbose_name_plural = "PlatnoscP_PAS"

class PlatnoscP_Burak(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa = "P_Burak"
    dodanep_burak = models.FloatField(validators=[MinValueValidator(0.0, message="Powierzchnia P_Burak nie może być wartością ujemną")], default=0)
    zmnp_burak = models.FloatField(validators=[MinValueValidator(0.0, message="Powierzchnia zmniejszeń nie może być wartością ujemną")], default=0)
    wynikp_burak = models.FloatField(default=0)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "PlatnoscP_Burak"
        verbose_name_plural = "PlatnoscP_Burak"

class PlatnoscP_Skrobia(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa = "P_Skrobia"
    dodanep_skrobia = models.FloatField(validators=[MinValueValidator(0.0, message="Powierzchnia P_Skrobia nie może być wartością ujemną")], default=0)
    zmnp_skrobia = models.FloatField(validators=[MinValueValidator(0.0, message="Powierzchnia zmniejszeń nie może być wartością ujemną")], default=0)
    wynikp_skrobia = models.FloatField(default=0)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "PlatnoscP_Skrobia"
        verbose_name_plural = "PlatnoscP_Skrobia"

class PlatnoscP_Truskawka(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa = "P_Truskawka"
    dodanep_trus = models.FloatField(validators=[MinValueValidator(0.0, message="Powierzchnia P_Truskawka nie może być wartością ujemną")], default=0)
    zmnp_trus = models.FloatField(validators=[MinValueValidator(0.0, message="Powierzchnia zmniejszeń nie może być wartością ujemną")], default=0)
    wynikp_trus = models.FloatField(default=0)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "PlatnoscP_Truskawka"
        verbose_name_plural = "PlatnoscP_Truskawka"

class PlatnoscPomidor(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa = "Pomidor"
    dodanepomidor = models.FloatField(default=0)
    zmnpomidor = models.FloatField(default=0)
    wynikpomidor = models.FloatField(default=0)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "PlatnoscPomidor"
        verbose_name_plural = "PlatnoscPomidor"

class PlatnoscChmiel(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa = "Chmiel"
    dodanechmiel = models.FloatField(validators=[MinValueValidator(0.0, message="Powierzchnia uprawy chmielu nie może być wartością ujemną")], default=0)
    zmnchmiel = models.FloatField(validators=[MinValueValidator(0.0, message="Powierzchnia zmniejszeń nie może być wartością ujemną")], default=0)
    wynikchmiel = models.FloatField(default=0)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "PlatnoscChmiel"
        verbose_name_plural = "PlatnoscChmiel"

class PlatnoscLen(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa = "Len"
    dodanelen = models.FloatField(validators=[MinValueValidator(0.0, message="Powierzchnia uprawy lnu nie może być wartością ujemną")], default=0)
    zmnlen = models.FloatField(validators=[MinValueValidator(0.0, message="Powierzchnia zmniejszeń nie może być wartością ujemną")], default=0)
    wyniklen = models.FloatField(default=0)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "PlatnoscLen"
        verbose_name_plural = "PlatnoscLen"

class PlatnoscKonopie(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa = "Konopie"
    dodanekonopie = models.FloatField(validators=[MinValueValidator(0.0, message="Powierzchnia uprawy konopii nie może być wartością ujemną")], default=0)
    zmnkonopie = models.FloatField(validators=[MinValueValidator(0.0, message="Powierzchnia zmniejszeń nie może być wartością ujemną")], default=0)
    wynikkonopie = models.FloatField(default=0)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "PlatnoscKonopie"
        verbose_name_plural = "PlatnoscKonopie"

class PlatnoscKrowy(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa = "Krowy"
    dodanekrowy = models.PositiveIntegerField(default=0)
    zmnkrowy = models.PositiveIntegerField(default=0)
    wynikkrowy = models.FloatField(default=0)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "PlatnoscKrowy"
        verbose_name_plural = "PlatnoscKrowy"


class PlatnoscBydlo(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa = "Bydło"
    dodanebydlo = models.PositiveIntegerField(default=0)
    zmnbydlo = models.PositiveIntegerField(default=0)
    wynikbydlo = models.FloatField(default=0)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "PlatnoscBydlo"
        verbose_name_plural = "PlatnoscBydlo"

class PlatnoscOwce(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa = "Owce"
    dodaneowce = models.PositiveIntegerField(default=0)
    zmnowce = models.PositiveIntegerField(default=0)
    wynikowce = models.FloatField(default=0)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "PlatnoscOwce"
        verbose_name_plural = "PlatnoscOwce"

class PlatnoscKozy(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa = "Kozy"
    dodanekozy = models.PositiveIntegerField(default=0)
    zmnkozy = models.PositiveIntegerField(default=0)
    wynikkozy = models.FloatField(default=0)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "PlatnoscKozy"
        verbose_name_plural = "PlatnoscKozy"

class SankcjaCC(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa = "sankcja CC"
    dodanecc = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "SankcjaCC"
        verbose_name_plural = "SankcjaCC"

class SankcjaTerminowa(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa = "Sankcja Terminowa"
    dodaneterm = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "SankcjaTerminowa"
        verbose_name_plural = "SankcjaTerminowa"

class SankcjaNiezadekl(models.Model):
    zero = '0'
    jeden = '1'
    dwa = '2'
    trzy = '3'
    Sankcja_niezad = (
        (zero, '0'),
        (jeden, '1'),
        (dwa, '2'),
        (trzy, '3'),
    )
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa = "Sankcja niedeklarowane"
    dodaneniezad = models.CharField(max_length=1, choices=Sankcja_niezad, default=zero)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "SankcjaNiedeklarowane"
        verbose_name_plural = "SankcjaNiedeklarowane"

class SankcjaEFA(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa = "Sankcja EFA"
    pow_go = models.FloatField(
        validators=[MinValueValidator(0.0, message="Powierzchnia P_Truskawka nie może być wartością ujemną")],
        default=0)
    pow_efa = models.FloatField(
        validators=[MinValueValidator(0.0, message="Powierzchnia zmniejszeń nie może być wartością ujemną")], default=0)
    piecproc_efa = models.FloatField(default=0)
    proc_efa = models.FloatField(default=0)
    braku_efa = models.FloatField(default=0)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "SankcjaEFA"
        verbose_name_plural = "SankcjaEFA"

class PlatnoscTyton(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa = "Tytoń"
    dodanetyton = models.PositiveIntegerField(default=0)
    zmntyton = models.PositiveIntegerField(default=0)
    wyniktyton = models.FloatField(default=0)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "PlatnoscTyton"
        verbose_name_plural = "PlatnoscTyton"

class PlatnoscVirginia(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa = "Tytoń Virginia"
    dodanevirginia = models.PositiveIntegerField(default=0)
    zmnvirginia = models.PositiveIntegerField(default=0)
    wynikvirginia = models.FloatField(default=0)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "PlatnoscVirginia"
        verbose_name_plural = "PlatnoscVirginia"

