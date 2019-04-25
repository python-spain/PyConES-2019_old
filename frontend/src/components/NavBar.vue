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
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">

        <b-nav-item-dropdown text="Lang" right>
          <b-dropdown-item v-on:click="$i18n.locale='es'">ES</b-dropdown-item>
          <b-dropdown-item v-on:click="$i18n.locale='en'">EN</b-dropdown-item>
        </b-nav-item-dropdown>

      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
    name: "NavBar",
    components: {
    },
}
</script>

