from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Personaje
import random
from .models import Objeto, Equipamiento, Caballo
from django.shortcuts import redirect


class IndexView(View):
    def get(self, request):
        template = "index.html"
        personajes = Personaje.objects.all()
        return render(request, template, {"personajes": personajes})


class GearView(View):
    def get(self, request):
        template = "gear.html"
        personaje = Personaje.objects.get(nombre=request.GET.get("per"))
        return render(request, template, {"personaje": personaje})

    def post(self, request):
        personaje = Personaje.objects.get(nombre=request.GET.get("per"))
        tipo = request.POST.get("articulo")
        puntos = request.POST.get("puntos")
        nombre = request.POST.get("nombre")

        if tipo == "caballo":
            personaje.caballo.all().delete()
            nuevo_objeto = Caballo(nombre=nombre)
            nuevo_objeto.personaje = personaje
            nuevo_objeto.inventario = puntos
            nuevo_objeto.save()
        else:
            print("Entra")
            personaje.equipamiento.filter(tipo=tipo).delete()
            nuevo_objeto = Equipamiento(nombre=nombre)
            nuevo_objeto.personaje = personaje
            nuevo_objeto.tipo = tipo
            nuevo_objeto.puntos_armadura = puntos
            nuevo_objeto.save()

        return redirect('index')


class ObjectsView(View):
    def get(self, request):
        template = "objetos.html"
        personaje = Personaje.objects.get(nombre=request.GET.get("per"))
        return render(request, template, {"personaje": personaje})

    def post(self, request):
        template = "index.html"
        objeto = request.POST.get("objeto")
        nuevo_objeto = Objeto(nombre=objeto)
        personaje = Personaje.objects.get(nombre=request.GET.get("per"))
        nuevo_objeto.personaje = personaje
        nuevo_objeto.save()
        return redirect('index')


class MoneyView(View):
    def get(self, request):
        personaje = Personaje.objects.get(nombre=request.GET.get("per"))
        template = "money.html"
        return render(request, template, {"personaje": personaje})

    def post(self, request):
        personaje = Personaje.objects.get(nombre=request.GET.get("per"))
        template = "money.html"
        add = request.POST.get("add", None)
        take = request.POST.get("take", None)
        if add is not None:
            personaje.dinero += int(add)
            personaje.save()
        if take is not None:
            personaje.dinero -= int(take)
            personaje.save()
        return redirect('index')


class DeleteObjView(View):
    def get(self, request):
        personaje = Personaje.objects.get(nombre=request.GET.get("per"))
        objeto = Objeto.objects.filter(nombre=request.GET.get("obj"), personaje=personaje)
        objeto[0].delete()

        return redirect('index')


class DeleteEqpView(View):
    def get(self, request):
        personaje = Personaje.objects.get(nombre=request.GET.get("per"))
        caballo_bool = request.GET.get("horse")
        if caballo_bool == "yes":
            objeto = Caballo.objects.filter(nombre=request.GET.get("obj"), personaje=personaje)
        else:
            objeto = Equipamiento.objects.filter(nombre=request.GET.get("obj"), personaje=personaje)
        objeto[0].delete()

        return redirect('index')


class AccionView(View):
    def get(self, request):

        template = "accion.html"
        personaje = request.GET.get("per")
        print(personaje)
        atributo = request.GET.get("atb")
        personaje = Personaje.objects.get(nombre=personaje)
        nivel = request.GET.get("lvl")

        numero = random.randint(0, 100)
        probabilidades = int(nivel)*8

        if atributo == "fuerza":
            if personaje.fuerza == 10:
                level_up = False
                pass
            elif personaje.nfuerza==7:
                personaje.nfuerza = 0
                personaje.fuerza += 1
                level_up = True
            else:
                personaje.nfuerza += 1
                level_up = False

            personaje.save()
        elif atributo == "destreza":
            if personaje.destreza == 10:
                level_up = False
                pass
            elif personaje.ndestreza==7:
                personaje.ndestreza = 0
                personaje.destreza += 1
                level_up = True
            else:
                personaje.ndestreza += 1
                level_up = False

            personaje.save()
        elif atributo == "inteligencia":
            if personaje.inteligencia == 10:
                level_up = False
                pass
            elif personaje.ninteligencia==7:
                personaje.ninteligencia = 0
                personaje.inteligencia += 1
                level_up = True
            else:
                personaje.ninteligencia += 1
                level_up = False

            personaje.save()
        elif atributo == "sigilo":
            if personaje.sigilo == 10:
                level_up = False
                pass
            elif personaje.nsigilo==7:
                personaje.nsigilo = 0
                personaje.sigilo += 1
                level_up = True
            else:
                personaje.nsigilo += 1
                level_up = False

            personaje.save()
        elif atributo == "percepcion":
            if personaje.percepcion == 10:
                level_up = False
                pass
            elif personaje.npercepcion==7:
                personaje.npercepcion = 0
                personaje.percepcion += 1
                level_up = True
            else:
                personaje.npercepcion += 1
                level_up = False

            personaje.save()
        elif atributo == "persuasion":
            if personaje.persuasion == 10:
                level_up = False
                pass
            elif personaje.npersuasion==7:
                personaje.npersuasion = 0
                personaje.persuasion += 1
                level_up = True
            else:
                personaje.npersuasion += 1
                level_up = False

            personaje.save()
        elif atributo == "atletismo":
            if personaje.atletismo == 10:
                level_up = False
                pass
            elif personaje.natletismo==7:
                personaje.natletismo = 0
                personaje.atletismo += 1
                level_up = True
            else:
                personaje.natletismo += 1
                level_up = False

            personaje.save()
        elif atributo == "craft":
            if personaje.craft == 10:
                level_up = False
                pass
            elif personaje.ncraft==7:
                personaje.ncraft = 0
                personaje.craft += 1
                level_up = True
            else:
                personaje.ncraft += 1
                level_up = False

            personaje.save()

        if numero <= probabilidades:
            success = True
        else:
            success = False

        return render(request, template, {"personaje": personaje, "atributo": atributo, "success": success, "level_up":level_up})


class BattleView(View):
    def get(self, request):
        template = "battle.html"
        return render(request, template, {})



