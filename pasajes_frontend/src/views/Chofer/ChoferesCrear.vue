<template>
    <div class="choferes-crear">
        <h1 v-if="chofer.id==null">Agregar Choferes</h1>
        <h1 v-else>Editar Chofer</h1>
        <form action="">
            <div class="container">
                <label for="sel1">Nombre del chofer</label>
                <input type="text" class="form-control" id="sel1" v-model="chofer.nombre"><br>
            </div>
            <button v-if="chofer.id==null" type="button" class="btn btn-success" name="button" v-on:click="guardar">Crear</button>
            <button v-else type="button" name="button" class="btn btn-success" v-on:click="guardar">Editar</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'choferes-crear',
    mounted(){
        var id = this.$route.params.id
        if(id!=null){
            axios.get('http://localhost:8000/api/conductores/'+id+'/').then((respuesta) => {
                this.chofer = respuesta.data
                console.log(this.chofer)
            })
        }
    },
    data(){
        return{
            chofer:{
                id:null, 
                nombre:'',
                creado:null, 
                modificado:null,
                rol:1
                }
        }
    },
    methods:{
        guardar(){
            var datos={
                nombre:this.chofer.nombre,
                modificado: new Date(),
                rol:this.chofer.rol
            }
            
                    console.log(datos)
            if(this.chofer.id!=null){
                axios.put('http://localhost:8000/api/conductores/'+this.chofer.id+'/', datos).then((respuesta) => {
                    if(respuesta.status==200){
                        alert('Chofer modificado')
                        this.$router.push("/choferes/");
                    }else{
                        console.log('error ' + respuesta.data)
                        alert('Error al crear chofer')
                    }
                })
            }else{
                console.log(datos)
                axios.post('http://localhost:8000/api/conductores/', datos).then((respuesta) => {
                    if(respuesta.statusText=='Created'){
                        alert('Chofer creado')
                        this.$router.push("/choferes/");
                    }else{
                        console.log('error ' + respuesta.data)
                        alert('Error al crear chofer')
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