<template>
    <div class="itinerario-crear">
        <h1>Agregar Itinerario</h1>
        <div class="container">
        <form action="">
            <label for="ex1">Horario de partida:</label>
            <input class="form-control" id="ex1" type="datetime-local" v-model="itinerario.partida"><br>
            <label for="ex2">Horario de llegada:</label>
            <input class="form-control" id="ex2" type="datetime-local" v-model="itinerario.llegada"><br>
            <select class="form-control" v-model="selTrayecto" id="sel1" name="sellist1">
                <option v-for="trayecto in trayectos" :value="trayecto">Desde: {{trayecto.origen}} Hacia: {{trayecto.destino}}</option>
            </select>
            <button type="button" name="button" class="btn btn-success" v-on:click="guardar">Crear</button>
        </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'itinerarios-crear',
    mounted(){
        this.cargaTrayectos()
    },
    data(){
        return{
            itinerario:{
                id:null, 
                llegada:null, 
                partida:null,
                trayecto:null
                },
            trayectos:[],
            selTrayecto:null
        }
    },
    methods:{
        //Cargar trayectos
        cargaTrayectos(){
            axios.get('http://localhost:8000/api/trayectos/').then((respuesta) => {
                this.trayectos = respuesta.data
                console.log(this.trayectos)
            })
        },
        guardar(){
            //Datos a guardar del itinerario
            var datos={
                llegada:this.itinerario.llegada,
                partida:this.itinerario.partida,
                trayecto:this.selTrayecto.id
            }
            console.log(datos)
            axios.post('http://localhost:8000/api/horarios/', datos).then((respuesta) => {
                if(respuesta.statusText=='Created'){
                    alert('Itinerario creado')
                    this.$router.push("/");
                }else{
                    console.log('error ' + respuesta.data)
                    alert('Error al crear itinerario')
                }
            })
            
        }
    }
}
</script>

<style>
table{
    margin: 0 auto;
    border: 1;
}
</style>