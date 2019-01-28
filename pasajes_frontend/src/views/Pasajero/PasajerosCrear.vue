<template>
    <div class="pasajeros-crear">
        <h1 v-if="pasajero.id==null">Agregar Pasajero</h1>
        <h1 v-else>Editar Pasajero</h1>
        <form action="">
            <div class="container">
                <label for="sel1">Nombre del Pasajero</label>
                <input type="text" class="form-control" id="sel1" v-model="pasajero.nombre"><br>
            </div>
            <button v-if="pasajero.id==null" type="button" class="btn btn-success" name="button" v-on:click="guardar">Crear</button>
            <button v-else type="button" name="button" class="btn btn-success" v-on:click="guardar">Editar</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'pasajeros-crear',
    mounted(){
        var id = this.$route.params.id
        if(id!=null){
            axios.get('http://localhost:8000/api/pasajeros/'+id+'/').then((respuesta) => {
                this.pasajero = respuesta.data
                console.log(this.pasajero)
            })
        }
    },
    data(){
        return{
            pasajero:{
                id:null, 
                nombre:'',
                creado:null, 
                modificado:null,
                rol:2
                }
        }
    },
    methods:{
        guardar(){
            var datos={
                nombre:this.pasajero.nombre,
                modificado: new Date(),
                rol:this.pasajero.rol
            }
            
                    console.log(datos)
            if(this.pasajero.id!=null){
                axios.put('http://localhost:8000/api/pasajeros/'+this.pasajero.id+'/', datos).then((respuesta) => {
                    if(respuesta.status==200){
                        alert('Pasajero modificado')
                        this.$router.push("/pasajeros/");
                    }else{
                        console.log('error ' + respuesta.data)
                        alert('Error al crear pasajero')
                    }
                })
            }else{
                console.log(datos)
                axios.post('http://localhost:8000/api/pasajeros/', datos).then((respuesta) => {
                    if(respuesta.statusText=='Created'){
                        alert('Pasajero creado')
                        this.$router.push("/pasajeros/");
                    }else{
                        console.log('error ' + respuesta.data)
                        alert('Error al crear pasajero')
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