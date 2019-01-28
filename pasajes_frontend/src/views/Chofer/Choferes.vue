<template>
    <div class="choferes">
        <h1>Choferes</h1>
        <div class="container">
            <button class="btn btn-primary" style="float: left;"><router-link to="/choferes/crear" tag="span">Nuevo Chofer</router-link></button>
            <table class="table table-bordered">
                <thead class="thead-dark">
                    <tr>
                        <th>NOMBRE</th>
                        <th>OPCIONES</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="chofer in choferes">
                        <td>{{chofer.nombre}}</td>
                        <td>
                            <button class="btn btn-warning">
                                <router-link :to="{ name: 'chofer-editar', params: { id: chofer.id }}" tag="span">Editar</router-link>
                            </button>
                            <button type="button" class="btn btn-danger" v-on:click="eliminar(chofer.id)">Borrar</button>
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
    name: 'choferes',
    mounted(){
        this.cargarEntradas()
    },
    data(){
        return{
            choferes:[]
        }
    },
    methods:{
        cargarEntradas(){
            axios.get('http://localhost:8000/api/conductores/').then((respuesta) => {
                this.choferes = respuesta.data
                console.log(this.choferes)
            })
        },
        eliminar(id){
            var op = window.confirm("¿Desea borrar este chofer?")

            if(op){
                axios.delete('http://localhost:8000/api/conductores/'+id+'/').then((respuesta) => {
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