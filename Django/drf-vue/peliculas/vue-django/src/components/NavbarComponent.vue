<template>
    <nav class="navbar navbar-expand-lg bg-black">
        <div class="container-fluid">
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon bg-secondary"></span>
          </button>
          <div class="collapse navbar-collapse bg-black" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <router-link to="/" class="nav-link active text-white" aria-current="page" href="#">Inicio</router-link>
              </li>
              <li class="nav-item">
                <router-link to="/about" class="nav-link text-white" href="#">Acerca de nosotros</router-link>
              </li>
            </ul>
            <!--<div class="rounded-3 bg-white p-2 me-3">
              <router-link to="/cart"><img src="https://cdn-icons-png.flaticon.com/512/3144/3144456.png" style="width: 1.5rem; height: 1.5rem" v-if="$route.path == '/'"/></router-link>
            </div>-->
            <form class="d-flex" role="search" @submit.prevent="submitForm" v-if="$route.path == '/'">
              <input id="search" class="form-control me-2" type="search" placeholder="Search" autocomplete="off" aria-label="Search" v-model="searchText">
              <button class="btn btn-warning" type="submit" @click="getSearch">Buscar</button>
            </form>
          </div>
        </div>
    </nav>
</template>

<script setup>
  import { ref,defineEmits } from 'vue'

  const searchText = ref('')
  const emitSearch = defineEmits(['getSearchText'])

  const getSearch = () => {
    emitSearch('getSearchText', searchText.value)
  }
</script>