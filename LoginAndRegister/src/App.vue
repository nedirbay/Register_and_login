<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<template>
  <div>
   <div>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid bg-dark p-3">
    <a class="navbar-brand text-white" href="#" style="font-size: 25px;font-family: Arial, Helvetica, sans-serif;text-transform: uppercase;">Project</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <RouterLink class="nav-link active text-white" aria-current="page"  to="/">Home</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link active text-white" aria-current="page"  to="/about">About</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link active text-white" aria-current="page"  to="/register">Register</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link active text-white" aria-current="page"  to="/login">Login</RouterLink>
        </li>
       
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
   </div>
  </div>
  <div>
    <RouterView />
  </div>
</template>

