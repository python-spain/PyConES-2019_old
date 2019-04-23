<template>
  <div id="app">
  <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
    <NavBar />
    <router-view/>
    <Footer />
  </div>
</template>

<script>
import Footer from './components/Footer.vue'
import NavBar from './components/NavBar.vue'

export default {
    name: 'App',
    components: {
        NavBar,
        Footer
    }
}
</script>

