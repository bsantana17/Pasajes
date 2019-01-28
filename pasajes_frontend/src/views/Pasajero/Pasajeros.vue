<template>
    <div class="pasajeros">
        <h1>HOLA AQUI HAY PASAJEROS</h1>
        <div class="container">
            <button class="btn btn-primary" style="float: left;"><router-link to="/pasajeros/crear" tag="span">Nuevo Pasajero</router-link></button>
            <table class="table table-bordered">
                <thead class="thead-dark">
                    <tr>
                        <th>NOMBRE</th>
                        <th>OPCIONES</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="pasajero in pasajeros">
                        <td>{{pasajero.nombre}}</td>
                        <td>
                            <button class="btn btn-warning">
                                <router-link :to="{ name: 'pasajero-editar', params: { id: pasajero.id }}" tag="span">Editar</router-link>
                            </button>
                            <button type="button" class="btn btn-danger" v-on:click="eliminar(pasajero.id)">Borrar</button>
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
    name: 'pasajeros',
    mounted(){
        this.cargarEntradas()
    },
    data(){
        return{
            pasajeros:[]
        }
    },
    methods:{
        cargarEntradas(){
            axios.get('http://localhost:8000/api/pasajeros/').then((respuesta) => {
                this.pasajeros = respuesta.data
                console.log(this.pasajeros)
            })
        },
        eliminar(id){
            var op = window.confirm("¿Desea borrar este pasajero?")

            if(op){
                axios.delete('http://localhost:8000/api/pasajeros/'+id+'/').then((respuesta) => {
                    console.log(respuesta)
                    this.cargarEntradas()
                })
            }
        }
    }
}
</script>

<style>
table{
    margin: 0 auto;
}
</style>