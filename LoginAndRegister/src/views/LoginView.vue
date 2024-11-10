<template>
<div>
    <header>
      <h1 class="text-center mt-3">Login Page</h1>
    </header>
    <div class="container mt-5" >
      <div class="mb-3">
        <label for="username" class="form-label" >Username</label>
        <input type="text" class="form-control" v-model="LoginForm.username" id="username" placeholder="admin">
      </div>
      <div class="mb-3">
        <label for="Password" class="form-label">Password</label>
        <input type="password" class="form-control" id="Password" v-model="LoginForm.password" placeholder="password">
      </div>
      <button type="submit" @click="submit()" class="btn btn-primary">Submit</button>
    </div>
    <div class="container mt-5">
      <div class="alert alert-danger" role="alert" v-if="error">
        {{ errorcontent }}
      </div>
    </div>
    <div class="mx-4 text-center" v-if="registersuccess">Siziň registrasiýa tokeniňiz: <span class="fw-bolder">{{ token }}</span></div>
</div>
</template>

<script>
import axios from "axios";
export default{
    name: "LoginView",
    data(){
        return{
            LoginForm: {
                username: "",
                password: "",
            },
            error: false,
            errorcontent: "",
            token: "",
            registersuccess: false
        }
    },
    methods:{
        submitForm(){
            try{
                const response = axios.post("http://localhost:8000/api/login", this.LoginForm);
                this.token = response.data.token;
                this.registersuccess = true;
            }
            catch(error){
                this.error = true;
                this.errorcontent = error.response.data.message;
            }
        },
        submit(){
            this.submitForm();
        }
    }
    
}

</script>