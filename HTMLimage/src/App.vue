<template>
  <v-app>
    <v-main>
      <HelloWorld/>
    </v-main>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',

  components: {
    HelloWorld,
  },

  data: () => ({
    //
  }),
}
</script>

<style>
body {
  font-family: 'Work Sans', serif !important;
}
html, body {
  overflow-y: auto !important;
}

@media (min-width: 1921px) {
  * {
    font-size: 30px;
  }
  h2 {
    font-size: 60px;
  }

}
</style>
