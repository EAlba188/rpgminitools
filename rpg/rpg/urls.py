from django.contrib import admin
from django.urls import path
from game import views
from game.views import IndexView, AccionView, MoneyView, GearView, ObjectsView, DeleteObjView, DeleteEqpView, BattleView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', IndexView.as_view(), name='index'),
    path('accion/', AccionView.as_view(), name='accion'),
    path('money/', MoneyView.as_view(), name='money'),
    path('gear/', GearView.as_view(), name='gear'),
    path('objects/', ObjectsView.as_view(), name='objects'),
    path('delete_object/', DeleteObjView.as_view(), name='delete_object'),
    path('delete_equip/', DeleteEqpView.as_view(), name='delete_equip'),
    path('battle/', BattleView.as_view(), name='battle'),
]
