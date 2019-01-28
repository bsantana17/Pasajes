<template>
    <div class="buses">
        <h1>Lista de Buses</h1>
        <div class="container">
            <button class="btn btn-primary" style="float: left;"><router-link to="/buses/crear" tag="span">Nuevo Bus</router-link></button>
            <table class="table table-bordered">
                <thead class="thead-dark">
                    <tr>
                        <th>PATENTE</th>
                        <th>CHOFER</th>
                        <th>OPCIONES</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="bus in buses">
                        <td>{{bus.patente}}</td>
                        <td>{{getChofer(bus.chofer)}}</td>
                        <td>
                            <button class="btn btn-warning">
                                <router-link :to="{ name: 'bus-editar', params: { id: bus.id }}" tag="span">Editar</router-link>
                            </button>
                            <button type="button" class="btn btn-danger" v-on:click="eliminar(bus.id)">Borrar</button>
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
    name: 'buses',
    mounted(){
        this.cargarBuses()
        this.cargarChoferes()
    },
    data(){
        return{
            buses:[],
            choferes:[],
            nombre:''
        }
    },
    methods:{
        //Cargar choferes
        cargarChoferes(){
            axios.get('http://localhost:8000/api/conductores/').then((respuesta) => {
                this.choferes = respuesta.data
                console.log(this.choferes)
            })
        },
        cargarBuses(){
            axios.get('http://localhost:8000/api/buses/').then((respuesta) => {
                this.buses = respuesta.data
                console.log(this.buses)
            })
        },
        eliminar(id){
            var op = window.confirm("¿Desea borrar este bus?")

            if(op){
                axios.delete('http://localhost:8000/api/buses/'+id+'/').then((respuesta) => {
                    console.log(respuesta)
                    this.cargarBuses()
                })
            }
        },
        getChofer(id){
            if(id == null){return "Sin Chofer"}
            var nombre = 'Nombre'
            this.choferes.forEach(function (chofer) {
                if(chofer.id == id){
                    console.log(chofer.nombre)
                    nombre = chofer.nombre}
            });
            return nombre
        }
    },
    computed:{

    }
}
</script>

<style>
table{
    margin: 0 auto;
}
</style>