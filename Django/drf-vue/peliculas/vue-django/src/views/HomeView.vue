<template>
  <navbar-component-vue @getSearchText="search"/>
  <navigation-component-vue @getCategoryID="categoryID"/>
  <button class="btn btn btn-warning align-content-end" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight"><img src="https://cdn-icons-png.flaticon.com/512/3144/3144456.png" style="width: 1.5rem; height: 1.5rem" v-if="$route.path == '/'"/></button>
  <div v-if="showAlert">
    <div class="alert alert-success alert-dismissible mt-2" role="alert">
      Tu pelicula ha sido alquilada.
      <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close" @click="resetAlert"></button>
    </div>
  </div>
  <hr>
  <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
    <div class="offcanvas-header">
      <h5 class="offcanvas-title" id="offcanvasRightLabel">Peliculas alquiladas</h5>
      <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
    </div>
    <div class="offcanvas-body" v-for="rfilm in rentFilms" :key="rfilm.id">
      <div class="border border-dark bg-warning-subtle d-flex">
        <div class="">
          <img :src="rfilm.image" id="imgPel" class="img-fluid p-3" alt="Poster de {{ film.title }}" style="width: 10rem; height: 7rem">
        </div>
        <div class="container m-3">
          <h5 class="mb-1">{{ rfilm.title }}</h5>
          <p class="mb-1">{{ rfilm.description }}</p>
        </div>
      </div>
    </div>
  </div>

  <div v-if="searchTextRule">
    <h3>Busqueda de "<strong>{{  searchTextRule }}</strong>"</h3>
    <button class="btn btn-info" @click="resetFilter">Mostrar todas las peliculas</button>
    <div class="alert alert-danger m-3" role="alert" v-if="filteredFilms.length === 0">
      No se encuentran peliculas con el texto <strong>{{  searchTextRule  }}</strong>
    </div>
  </div>

  <div v-if="categoryRecived">
    <h3>Peliculas de {{  categoryRecived }}</h3>
    <button class="btn btn-info" @click="resetFilter">Mostrar todas las peliculas</button>
    <div class="alert alert-danger m-3" role="alert" v-if="filteredFilms.length === 0">
      No existen peliculas de esta categoria
    </div>
  </div>
  <div>
    
    <div class="d-flex flex-wrap">
      <div class="card m-3 bg-danger-subtle" style="width: 15rem;" v-for="film in filteredFilms" :key="film.id">
        <img :src="film.image" id="imgPel" class="img-fluid p-3" alt="Poster de {{ film.title }}" style="width: 15rem; height: 21rem">
        <div class="card-body border-dark">
          <h3 class="card-title mb-1">{{ film.title }}</h3>
          <p class="card-text mb-1">{{ film.description }}</p>
          <p class="card-text mb-1">{{ film.publication }}</p>
          <p class="card-text mb-1">{{ film.category_name }}</p>
          <button class="btn btn-danger mt-3" @click="getRent(film)">Alquilar</button>
        </div>
      </div>
    </div>
    <hr>
    
  </div>
  <footer-component-vue/>
</template>

<script setup>
  import axios from 'axios'
  import NavigationComponentVue from '../components/NavigationComponent.vue'
  import FooterComponentVue from '../components/FooterComponent.vue'
  import NavbarComponentVue from '../components/NavbarComponent.vue'
  import { ref, onMounted } from 'vue'
  
  const films = ref([])
  const allFilms = ref([])
  const filteredFilms = ref([])
  const categoryRecived = ref(null)

  const searchTextRule = ref(null)

  const showAlert = ref(false);

  const rentFilms = ref([])

  const getRent = (film) => {
    rentFilms.value.push(film)
    showAlert.value = true;
  }

  const resetAlert = () => {
    showAlert.value = false;
  }

  const search = (searchText) => {
    searchTextRule.value = searchText
    if(searchText){
      filteredFilms.value = films.value.filter((film) => {
        const filmTitle = film.title.toLowerCase();
        const filmDescription = film.title.toLowerCase();
        const searchTerm = searchText.toLowerCase();
        return (
          filmTitle.includes(searchTerm) || filmDescription.includes(searchTerm)
        )
      })
    }else{
      filteredFilms.value = allFilms.value
    }
  }

  const categoryID = (categoryID, categoryName) => {
    searchTextRule.value = null
    categoryRecived.value = categoryName
    if(categoryID){
      filteredFilms.value = films.value.filter((film) => film.category === categoryID)
    } else{
      filteredFilms.value = films.value
    }
  }
  
  const resetFilter = () => {
    categoryRecived.value = null
    searchTextRule.value = null
    filteredFilms.value = films.value
  }
    
  onMounted (() => {
    axios.get('http://127.0.0.1:8000/api/films/')
    .then( response => {
      films.value = response.data
      filteredFilms.value = films.value
    })
    .catch( error => {
      console.log(error)
    })
  })
</script>

<style>

</style>