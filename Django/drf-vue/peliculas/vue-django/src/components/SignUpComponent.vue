<template>
    <div class="d-flex container-fluid rounded-3 mt-4 justify-content-center align-items-center" style="background-color:#ED6A5A; height:38rem">
        <div class="d-flex rounded-5 m-5 justify-content-center align-items-center" style="background-color:#F4F1BB; width: 27rem; height:27rem">
            <img src="https://ciberprotector.com/wp-content/uploads/2019/05/informacion-ciberprotector.png" style="width: 20rem; height: 20rem" />
        </div>
        <form @submit.prevent="submitForm" class="d-flex container justify-content-center align-items-center flex-column m-5 rounded-5"  style="background-color:#F4F1BB; width: 34rem">
            <!--{% csrf_token %}-->
            <h1 class="mt-5 mb-5"><strong>Registro</strong></h1>
            <!--Username-->
            <div class="form-group col-md-7 flex-column text-start">
                <label for="username" class="form-label fs-6"><strong>Nombre de Usuario:</strong></label>
                <input type="username" id="username" name="username" class="form-control" autocomplete="off" v-model="username"/>
                <small v-if="errors.username" class="text-danger">{{errors.username}}</small>
            </div>
            <!--Password-->
            <div class="form-group col-md-7 flex-column mt-3 text-start">
                <label for="password" class=" form-label fs-6"><strong>Contraseña:</strong></label>
                <input type="password" id="password" name="password" class="form-control" autocomplete="off" v-model="password"/>
                <small v-if="errors.password" class="text-danger">{{errors.password}}</small>
            </div>
            <!--Password2-->
            <div class="form-group col-md-7 flex-column mt-3 text-start">
                <label for="password2" class=" form-label fs-6"><strong>Repite la contraseña:</strong></label>
                <input type="password" id="password2" name="password2" class="form-control" autocomplete="off" v-model="password2"/>
                <small v-if="errors.password2" class="text-danger">{{errors.password2}}</small>
            </div>
            <!--Button Register-->
            <div class="p-3 mt-2">
                <button class="btn btn-warning fs-5 text-white" type="submit">Registrarse</button>
            </div>
            <!--Login-->
            <div class="">
                <p>
                    <router-link class="text-decoration-none" to="/login">Inicia sesión aquí.</router-link>
                </p>
            </div>
        </form>
    </div>
</template>


<script>
    import axios from 'axios';
    export default{
        name: 'Signup',
        data() {
            return {
                username: "",
                password: "",
                password2: "",
                errors: {
                    username: "",
                    password: "",
                    password2: "",
                }
            }
        },
        methods: {
            isValidForm(){
                let valid = true;
                if(!this.username){
                    this.errors.username = "Este campo no puede estar en blanco";
                }
                else{
                    this.errors.username = "";
                }
                if(!this.password){
                    this.errors.password = "Este campo no puede estar en blanco";
                }
                else{
                    this.errors.password = "";
                }
                if(!this.password2){
                    this.errors.password2 = "Este campo no puede estar en blanco";
                }
                else{
                    this.errors.password2 = "";
                }
                if(this.password && this.password2 && (this.password != this.password2)){
                    this.errors.password2 = "Las contraseñas no coinciden";
                }
                else{
                    this.errors.password2 = "";
                }
                if(this.errors.username || this.errors.password || this.errors.password2 ){
                    valid = false;
                }
                return valid;
            },
            submitForm(){
                if(this.isValidForm()){
                    axios.post('http://127.0.0.1:8000/auth/users/', {username: this.username, password: this.password})
                    .then(response => {
                        this.$router.push('/login');
                        this.username = "";
                        this.password = "";
                        this.password2 = "";
                    })
                    .catch(error => {
                        console.log(error.response.data);
                        if(error.response.data.username) {
                            this.errors.username = error.response.data.username.join('');
                        }
                        else{
                            this.errors.username = "";
                        }
                    })
                }
            },
        }
    }
</script>