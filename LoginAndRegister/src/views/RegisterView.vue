<template>
<div>
    <header>
      <h1 class="text-center mt-3">Register Page</h1>
    </header>
    <div class="container mt-5" >
      <div class="mb-3">
        <label for="username" class="form-label" >Username</label>
        <input type="text" class="form-control" v-model="Register.username" id="username" placeholder="admin">
      </div>
      <div class="mb-3">
        <label for="exampleFormControlInput1" class="form-label">Email address</label>
        <input type="email" class="form-control" v-model="Register.email" id="exampleFormControlInput1" placeholder="admin@gmail.com">
      </div>
      <div class="mb-3">
        <label for="FirstName" class="form-label">First Name</label>
        <input type="text" class="form-control" id="FirstName" v-model="Register.first_name" placeholder="first_name">
      </div>
      <div class="mb-3">
        <label for="LastName" class="form-label">Last Name</label>
        <input type="text" class="form-control" id="LastName" v-model="Register.last_name" placeholder="last_name">
      </div>
      <div class="mb-3">
        <label for="Password" class="form-label">Password</label>
        <input type="password" class="form-control" id="Password" v-model="Register.password" placeholder="password">
      </div>
      <div class="mb-3">
        <label for="Password2" class="form-label">Confirm Password</label>
        <input type="password" class="form-control" id="Password2" v-model="Register.password2" placeholder="password">
      </div>
      <div class="mb-3 form-check">
        <input type="checkbox" class="form-check-input" id="exampleCheck1">
        <label class="form-check-label" for="exampleCheck1">Check me out</label>
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
import axios from 'axios'

export default {
  name: 'RegisterView',
  data (){
    return {
      Register: {
        username: '',
        email: '',
        password: '',
        first_name: '',
        last_name: '',
      },
      token : "",
      error : false,
      errorcontent: "",
      registersuccess : false,
    }
  },
  methods:{
    async submitRegister(){
      try{
        if (this.Register.password == this.Register.password2){
         if (this.Register.password.length < 8){
           this.error= true;
           this.registersuccess = false;
           this.errorcontent=("Parol 8 simwoldan az bolmaly däl")
           return;
         }
        console.log("api worked")
        const response = await axios.post('http://localhost:8000/accounts/api/register/', this.Register)
        this.error= false;
        this.registersuccess = true;
        console.log(response)
        this.token = response.data.token
        }
        else{
          this.error= true;
          this.registersuccess = false;
          this.errorcontent=("Parollar gabat gelenok")
          return;
        }
      }
      catch(error){
        console.log(error)
      }
    },
    submit(){
      this.submitRegister()
    },
    async login(){
      try{
        const response = await axios.post('http://localhost:8000/accounts/login', this.Register)
        console.log(response)
      }
      catch(error){
        console.log(error)
      }
    }
  }
}

</script>