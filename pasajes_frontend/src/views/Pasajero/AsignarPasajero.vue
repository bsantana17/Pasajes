<template>
    <div class="asignar-pasajero">
        <h1>Asignar Pasajero</h1>
        <div class="container">
          <label for="sel3">Seleccione un pasajero:</label>
          <select class="form-control" v-model="selPasajero"  id="sel3" name="sellist3">
            <option v-for="pasajero in pasajeros" :value="pasajero">Nombre: {{pasajero.nombre}}</option>
          </select>
          <label for="sel1">Seleccione un trayecto:</label>
          <select class="form-control" v-model="selTrayecto" v-on:change="cargaHorarios(selTrayecto.id)" id="sel1" name="sellist1">
            <option v-for="trayecto in trayectos" :value="trayecto">Desde: {{trayecto.origen}} Hacia: {{trayecto.destino}}</option>
          </select>
          <label for="sel2" v-if="horarios.length > 0">Seleccione un horario:</label>
          <select class="form-control" v-if="horarios.length > 0" v-model="selHorario" v-on:change="cargaAsientos(selHorario.id)" id="sel2" name="sellist2">
            <option v-for="horario in horarios" :value="horario">Fecha Partida: {{horario.partida}} Fecha Llegada: {{horario.llegada}}</option>
          </select>
          <label for="sel4" v-if="asientos.length > 0 && horarios.length > 0">Seleccione un asiento:</label>
          <label for="sel4" v-else><b>Sin asientos o buses disponibles</b> </label>
          <select v-if="asientos.length > 0 && horarios.length > 0" class="form-control" v-model="selAsiento"  id="sel4" name="sellist4">
            <option  v-for="asiento in asientos" :value="asiento">Asiento numero: {{asiento.numero}}</option>
          </select>
          
          <button v-if="selAsiento!=null && asientos.length > 0 && horarios.length > 0" type="button" class="btn btn-success" style="float: right;" 
            name="button" v-on:click="guardar">Asignar</button>

        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'asignar-pasajero',
    mounted(){
        this.cargaTrayectos()
        this.cargarPasajeros()
    },
    data(){
        return{
            pasajeros:[],
            trayectos:[],
            horarios:[],
            asientos:[],
            selTrayecto:null,
            selHorario:null,
            selPasajero:null,
            selAsiento:null
        }
    },
    methods:{
        cargarPasajeros(){
            axios.get('http://localhost:8000/api/pasajeros/').then((respuesta) => {
                this.pasajeros = respuesta.data
                console.log(this.pasajeros)
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
            this.horarios = []
          axios.get('http://localhost:8000/api/trayectos/'+id+'/horarios/').then((respuesta) => {
            console.log(respuesta)
            this.asientos = []
            this.horarios = respuesta.data
          })
        },
        //Cargar asientos dinamicamente
        cargaAsientos(id){
            this.asientos = []
          axios.get('http://localhost:8000/api/horarios/'+id+'/asientos/').then((respuesta) => {
            console.log(respuesta)
            this.asientos = respuesta.data
          })
        },
        //Función que guarda el pasajero seleccionado en el asiento del bus con horario seleccionado.
        guardar(){
          var datos={
                pasajero:this.selPasajero.id,
                bus:this.selAsiento.bus
            }
            console.log(datos)
            if(this.selAsiento.id!=null){
              axios.put('http://localhost:8000/api/asientos/'+this.selAsiento.id+'/', datos).then((respuesta) => {
                if(respuesta.status==200){
                  alert('Asiento asignado')
                    this.$router.push("/");
                  }else{
                      console.log('error ' + respuesta.data)
                      alert('Error al crear trayecto')}
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
