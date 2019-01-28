import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Trayectos from './views/Trayecto/Trayectos.vue'
import TrayectosCrear from './views/Trayecto/TrayectosCrear.vue'
import Buses from './views/Bus/Buses.vue'
import BusesCrear from './views/Bus/BusesCrear.vue'
import Pasajeros from './views/Pasajero/Pasajeros.vue'
import PasajerosCrear from './views/Pasajero/PasajerosCrear.vue'
import AsignarPasajero from './views/Pasajero/AsignarPasajero.vue'
import Choferes from './views/Chofer/Choferes.vue'
import ChoferCrear from './views/Chofer/ChoferesCrear.vue'
import ItinerarioCrear from './views/Itinerario/ItinerarioCrear.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/asignar-pasajero',
      name: 'asignar-pasajero',
      component: AsignarPasajero
    },
    {
      path: '/trayectos',
      name: 'trayectos',
      component: Trayectos
    },
    {
      path: '/trayectos/crear',
      name: 'trayectos-crear',
      component: TrayectosCrear
    },
    {
      path: '/trayectos/:id/editar',
      name: 'trayecto-editar',
      component: TrayectosCrear
    },
    {
      path: '/buses',
      name: 'buses',
      component: Buses
    },
    {
      path: '/buses/crear',
      name: 'bus-crear',
      component: BusesCrear
    },
    {
      path: '/buses/:id/editar',
      name: 'bus-editar',
      component: BusesCrear
    },
    {
      path: '/pasajeros',
      name: 'pasajeros',
      component: Pasajeros
    },
    {
      path: '/pasajeros/crear',
      name: 'pasajero-crear',
      component: PasajerosCrear
    },
    {
      path: '/pasajeros/:id/editar',
      name: 'pasajero-editar',
      component: PasajerosCrear
    },
    {
      path: '/choferes',
      name: 'choferes',
      component: Choferes
    },
    {
      path: '/choferes/crear',
      name: 'chofer-crear',
      component: ChoferCrear
    },
    {
      path: '/choferes/:id/editar',
      name: 'chofer-editar',
      component: ChoferCrear
    },
    {
      path: '/itinerarios/crear',
      name: 'itinerario-crear',
      component: ItinerarioCrear
    },
    
  ]
})
