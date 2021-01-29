<template>
  <chessboard></chessboard>
</template>

<script>
import chessboard from './components/Chessboard.vue'

export default {
  name: 'App',
  components: {
    chessboard
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
