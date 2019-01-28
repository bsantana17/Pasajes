<template>
    <div class="trayectos-crear">
        <h1 v-if="trayecto.id==null">Agregar Trayecto</h1>
        <h1 v-else>Editar Trayecto</h1>
        <form action="">
            <div class="container">
                <label for="sel1">Ciudad Origen:</label>
                <input type="text" class="form-control" id="sel1" v-model="trayecto.origen"><br>
                <label for="sel2">Ciudad Destino</label>
                <input type="text" class="form-control" id="sel2" v-model="trayecto.destino"><br>
            <button v-if="trayecto.id==null" type="button" class="btn btn-success" name="button" v-on:click="guardar">Crear</button>
            <button v-else type="button" name="button" class="btn btn-success" v-on:click="guardar">Editar</button>
            </div>
        </form>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'trayectos-crear',
    mounted(){
        var id = this.$route.params.id
        if(id!=null){
            axios.get('http://localhost:8000/api/trayectos/'+id+'/').then((respuesta) => {
                this.trayecto = respuesta.data
                console.log(this.trayecto)
            })
        }
    },
    data(){
        return{
            trayecto:{
                id:null, 
                origen:'', 
                destino:'', 
                creado:null, 
                modificado:null
                }
        }
    },
    methods:{
        guardar(){
            var datos={
                origen:this.trayecto.origen,
                destino:this.trayecto.destino,
                modificado: new Date()
            }
            
                    console.log(datos)
            if(this.trayecto.id!=null){
                axios.put('http://localhost:8000/api/trayectos/'+this.trayecto.id+'/', datos).then((respuesta) => {
                    if(respuesta.status==200){
                        alert('Trayecto modificado')
                        this.$router.push("/trayectos/");
                    }else{
                        console.log('error ' + respuesta.data)
                        alert('Error al crear trayecto')
                    }
                })
            }else{
                console.log(datos)
                axios.post('http://localhost:8000/api/trayectos/', datos).then((respuesta) => {
                    if(respuesta.statusText=='Created'){
                        alert('Trayecto creado')
                        this.$router.push("/trayectos/");
                    }else{
                        console.log('error ' + respuesta.data)
                        alert('Error al crear trayecto')
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