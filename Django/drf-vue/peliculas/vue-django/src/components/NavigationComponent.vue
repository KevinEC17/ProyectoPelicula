<template>
    <section>
        <h1 class="mt-3">Películas</h1>
        <div class="mt-3" v-if="$route.path != '/about'">
            <button type="button" class="btn btn-warning m-2" v-for="category in categories" :key="category.id" @click="getCategory(category.id, category.name)">{{ category.name }}</button>
            <hr>
        </div>
    </section>
</template>

<script setup>
    import axios from 'axios'
    import { ref, onMounted, defineEmits } from 'vue'

    const categories = ref([])

    const emit = defineEmits(['getCategoryID'])

    const getCategory = (id, name) => {
        emit('getCategoryID', id, name)
    }

    onMounted (() => {
        axios.get('http://127.0.0.1:8000/api/categories/')
        .then(response => {
            categories.value = response.data
        })
        .catch( error => {
            console.log(error)
        })
    })
</script>