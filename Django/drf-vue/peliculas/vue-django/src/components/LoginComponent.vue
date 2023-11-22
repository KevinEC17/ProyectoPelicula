<template>
    <div class="d-flex container-fluid rounded-3 mt-4 justify-content-center align-items-center" style="background-color:#ED6A5A; height:38rem">
        <div class="d-flex rounded-5 m-5 justify-content-center align-items-center" style="background-color:#F4F1BB; width: 27rem; height:27rem">
            <img src="https://cdn-icons-png.flaticon.com/512/306/306337.png" style="width: 18rem; height: 18rem" />
        </div>
        <form @submit.prevent="submitForm" class="d-flex container justify-content-center align-items-center flex-column m-5 rounded-5"  style="background-color:#F4F1BB; width: 34rem">
            <!--{% csrf_token %}-->
            <h1 class="mb-5 mt-5"><strong>Inicio de Sesión</strong></h1>
            <div v-if="errors.wrong_credentials" class="form-group col-md-7 flex-column mb-1 mt-3 text-start">
                <small class="text-danger">{{errors.wrong_credentials}}</small>
            </div>
            <!--Username-->
            <div class="form-group col-md-7 flex-column mb-1 mt-3 text-start">
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
            <!--Button Login-->
            <div class="form-group p-3 align-items-center mt-3">
                <button class="btn btn-warning fs-5 text-white" type="submit">Ingresar</button>
            </div>
            <div class="">
                <p>
                    <router-link class="text-decoration-none" to="/signup">Regístrate aquí.</router-link>
                </p>
            </div>
        </form>
    </div>
</template>

<script>
    import axios from 'axios';
    export default{
        name: 'Login',
        data() {
            return {
                username: "",
                password: "",
                errors: {
                    username: "",
                    password:"",
                    wrong_credentials: "",
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
                if(this.errors.username || this.errors.password ){
                    valid = false;
                }
                return valid;
            },
            submitForm(){
                if(this.isValidForm()){
                    axios.post('http://127.0.0.1:8000/login/', {username: this.username, password: this.password})
                    .then(response => {
                        this.$store.commit('setToken', response.data);
                        this.username = "";
                        this.password = "";
                        this.$router.push('/');
                    })
                    .catch(error => {
                        if(error.response.data.non_field_errors) {
                            this.errors.wrong_credentials = error.response.data.non_field_errors.join('');
                        }
                        else{
                            this.errors.wrong_credentials = "";
                        }
                    })
                }
            },
        }
    }
</script>