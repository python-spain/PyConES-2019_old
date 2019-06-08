<template>
  <b-navbar toggleable="lg" type="dark" variant="info" :sticky=true>
    <b-navbar-brand href="#">
        <img class="navbar-logo" src="static/logo_pycones_horizontal.png" alt="PyConEs2019"/>
    </b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="#info">{{ $t("nav_info")}}</b-nav-item>
        <b-nav-item href="#keyspeakers">{{ $t("nav_speakers")}}</b-nav-item>
        <b-nav-item href="/blog">Blog</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">

        <b-nav-item-dropdown text="Lang" right>
          <b-dropdown-item v-on:click="changeLocale('es')">ES</b-dropdown-item>
          <b-dropdown-item v-on:click="changeLocale('en')">EN</b-dropdown-item>

        </b-nav-item-dropdown>

      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
import axios from 'axios'
export default {
    name: "NavBar",
    components: {
    },
    methods: {
        changeLocale(new_locale){
            this.$i18n.locale=new_locale;
            axios.defaults.headers.common['Accept-Language'] = new_locale
            this.$eventBus.$emit('locale-change', new_locale);
        }
    }
}
</script>

