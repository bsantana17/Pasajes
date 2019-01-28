from rest_framework import routers
from buses.api_views import *
from usuarios.api_views import *

router = routers.DefaultRouter()
router.register(r'buses', BusViewSet)
router.register(r'asientos', AsientoViewSet)
router.register(r'pasajeros', PasajeroViewSet)
router.register(r'conductores', ChoferViewSet)
router.register(r'roles', RolViewSet)
router.register(r'trayectos', TrayectoViewSet)
router.register(r'horarios', HorarioViewSet)