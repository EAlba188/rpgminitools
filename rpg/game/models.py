from django.db import models


class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    fuerza = models.IntegerField()
    destreza = models.IntegerField()
    inteligencia = models.IntegerField()
    sigilo = models.IntegerField()
    percepcion = models.IntegerField()
    persuasion = models.IntegerField()
    atletismo = models.IntegerField()
    craft = models.IntegerField()
    dinero = models.DecimalField(default=0, max_digits=19, decimal_places=0)

    nfuerza = models.IntegerField(default=0)
    ndestreza = models.IntegerField(default=0)
    ninteligencia = models.IntegerField(default=0)
    nsigilo = models.IntegerField(default=0)
    npercepcion = models.IntegerField(default=0)
    npersuasion = models.IntegerField(default=0)
    natletismo = models.IntegerField(default=0)
    ncraft = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

    @property
    def inventario_capacidad(self):
        if self.caballo.exists():
            caballo_inventario = self.caballo.first()
            return 10+caballo_inventario.inventario
        else:
            return 10

    @property
    def inventario_uso(self):
        return self.objeto.all().count()
    @property
    def casco(self):
        return self.equipamiento.get(tipo="casco")
    @property
    def arma(self):
        return self.equipamiento.get(tipo="arma")
    @property
    def armadura(self):
        return self.equipamiento.get(tipo="armadura")
    @property
    def escudo(self):
        return self.equipamiento.get(tipo="escudo")
    @property
    def get_caballo(self):
        return self.caballo.get()


class Caballo(models.Model):
    nombre = models.CharField(max_length=100)
    personaje = models.ForeignKey(Personaje, blank=True, null=True, on_delete=models.CASCADE, related_name="caballo")
    inventario = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre


class Equipamiento(models.Model):
    nombre = models.CharField(max_length=100)
    personaje = models.ForeignKey(Personaje, blank=True, null=True, on_delete=models.CASCADE, related_name="equipamiento")
    tipo = models.CharField(max_length=50, blank=True, null=True)
    puntos_armadura = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre


class Objeto(models.Model):
    nombre = models.CharField(max_length=100)
    personaje = models.ForeignKey(Personaje, blank=True, null=True, on_delete=models.CASCADE, related_name="objeto")

    def __str__(self):
        return self.nombre