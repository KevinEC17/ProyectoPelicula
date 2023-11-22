<template>
  <navbar-component-vue @getSearchText="search"/>
  <div class="about" style="height: 32rem;">
    <h2 class="container mt-3">Página de alquiler de películas</h2>
    <hr>
    <p class="container fs-4">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
  </div>
  <hr>
  <footer-component-vue/>
</template>

<script setup>
  import NavbarComponentVue from '../components/NavbarComponent.vue'
  import FooterComponentVue from '../components/FooterComponent.vue'
</script>