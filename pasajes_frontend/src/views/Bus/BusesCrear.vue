<template>
    <div class="buses-crear">
        <h1 v-if="bus.id==null">Agregar Bus</h1>
        <h1 v-else>Editar Bus</h1>
        <form action="">
        <div class="container">
            <label for="ex1">Patente del bus</label>
            <input class="form-control" id="ex1" type="text" v-model="bus.patente"><br>
            <label for="sel1">Seleccione un trayecto:</label>
            <select class="form-control" v-model="selTrayecto" v-on:change="cargaHorarios(selTrayecto.id)" id="sel1" name="sellist1">
                <option v-for="trayecto in trayectos" :value="trayecto">Desde: {{trayecto.origen}} Hacia: {{trayecto.destino}}</option>
            </select>
            <label for="sel2">Seleccione un horario:</label>
            <select class="form-control" v-model="selHorario" id="sel2" name="sellist2">
                <option v-for="horario in horarios" :value="horario"> Partida: {{horario.partida}} Llegada: {{horario.llegada}}</option>
            </select>
            <label for="sel3">Chofer a cargo:</label>
            <select class="form-control" v-model="selChofer" id="sel3" name="sellist3">
                <option v-for="chofer in choferes" :value="chofer"> {{chofer.nombre}}</option>
            </select>
        </div>
            <button v-if="bus.id==null" type="button" name="button" class="btn btn-success" v-on:click="guardar">Crear</button>
            <button v-else type="button" name="button" class="btn btn-success" v-on:click="guardar">Editar</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'buses-crear',
    mounted(){
        var id = this.$route.params.id
        if(id!=null){
            axios.get('http://localhost:8000/api/buses/'+id+'/').then((respuesta) => {
                this.bus = respuesta.data
                console.log(this.bus)
            })
        }
        this.selChofer = this.bus.chofer
        this.cargarChoferes()
        this.cargaTrayectos()
    },
    data(){
        return{
            bus:{
                id:null, 
                patente:'', 
                chofer:null,
                horario:null,
                modificado:null
                },
            choferes:[],
            horarios:[],
            trayectos:[],
            selHorario:null,
            selChofer:null,
            selTrayecto:null
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
        //Cargar trayectos
        cargaTrayectos(){
            axios.get('http://localhost:8000/api/trayectos/').then((respuesta) => {
                this.trayectos = respuesta.data
                console.log(this.trayectos)
            })
        },
        //Cargar horarios dinamicamente
        cargaHorarios(id){
          axios.get('http://localhost:8000/api/trayectos/'+id+'/sinbus/').then((respuesta) => {
            console.log(respuesta)
            this.horarios = respuesta.data
          })
        },
        guardar(){
            //Datos a guardar del bus
            var datos={
                patente:this.bus.patente,
                chofer:this.selChofer.id,
                horario:this.selHorario.id
            }
            if(this.bus.id!=null){
                axios.put('http://localhost:8000/api/buses/'+this.bus.id+'/', datos).then((respuesta) => {
                    if(respuesta.status==200){
                        alert('Bus modificado')
                        this.$router.push("/buses/");
                    }else{
                        console.log('error ' + respuesta.data)
                        alert('Error al crear bus')
                    }
                })
            }else{
                console.log(datos)
                axios.post('http://localhost:8000/api/buses/', datos).then((respuesta) => {
                    if(respuesta.statusText=='Created'){
                        alert('Bus creado')
                        this.$router.push("/buses/");
                    }else{
                        console.log('error ' + respuesta.data)
                        alert('Error al crear bus')
                    }
                })
            }
            
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