<template>
    <div class="trayectos">
        <h1>Listado de Trayectos</h1>
        <div class="container">
            <button class="btn btn-primary" style="float: left;"><router-link to="/trayectos/crear" tag="span">Nuevo Trayecto</router-link></button>
            <table class="table table-bordered">
                <thead class="thead-dark">
                    <tr>
                        <th>ORIGEN</th>
                        <th>DESTINO</th>
                        <th>PASAJES VENDIDOS</th>
                        <th>PORCENTAJE BUSES</th>
                        <th>OPCIONES</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(trayecto, index) in trayectos">
                        <td>{{trayecto.origen}}</td>
                        <td>{{trayecto.destino}}</td>
                        <td>{{getVendidos(index)}}</td>
                        <td>{{getPorcentaje(index)}}</td>
                        <td>
                            <button class="btn btn-warning">
                                <router-link :to="{ name: 'trayecto-editar', params: { id: trayecto.id }}" tag="span">Editar</router-link>
                            </button>
                            <button type="button" class="btn btn-danger" v-on:click="eliminar(trayecto.id)">Borrar</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'trayectos',
    mounted(){
        this.cargarTrayectos()
        this.cargarVendidos()
        this.cargarBuses()
    },
    data(){
        return{
            trayectos:[],
            cantidad:[],
            buses:[]
        }
    },
    methods:{
        cargarTrayectos(){
            axios.get('http://localhost:8000/api/trayectos/').then((respuesta) => {
                this.trayectos = respuesta.data
                console.log(this.trayectos)
            })
        },
        eliminar(id){
            var op = window.confirm("¿Desea borrar este trayecto?")

            if(op){
                axios.delete('http://localhost:8000/api/trayectos/'+id+'/').then((respuesta) => {
                    console.log(respuesta)
                    this.cargarEntradas()
                })
            }
        },
        cargarVendidos(){
            axios.get('http://localhost:8000/api/trayectos/asientos/').then((respuesta) => {
                this.cantidad = respuesta.data
                console.log(this.cantidad)
            })
        },
        cargarBuses(){
            axios.get('http://localhost:8000/api/trayectos/buses/').then((respuesta) => {
                this.buses = respuesta.data
                console.log(this.buses)
            })
        },
        getVendidos(indice){
            return this.cantidad[indice]
            console.log
        },
        getPorcentaje(indice){
            var a = 0
            var bus = ""
            while(a < this.buses.length){
                if(this.buses[a+1] > 0 && this.buses[a] == indice){
                    bus += this.buses[a+2] + ": " + this.buses[a+1] + "0% vendido| "
                }
                a += 3
            }
            return bus
        }
    }
}
</script>

<style>
table{
    margin: 0 auto;
}
</style>
