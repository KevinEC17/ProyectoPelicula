<template>
    <div class="signup">
        <SignUpComponentVue/>
    </div>
</template>
  
<script>
    import SignUpComponentVue from '@/components/SignUpComponent.vue'

    export default {
        name: 'SignUpView',
        components: {
            SignUpComponentVue,
        }
    }
</script>