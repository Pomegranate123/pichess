<template>
  <chessboard></chessboard>
</template>

<script>
import chessboard from '../components/Chessboard.vue'

export default {
  components: {
    chessboard
  },
  mounted () {
    this.axios
    .get('http://localhost/api/admin')
    .then(response => {
      console.log(response)
    })
    .catch(error => {
      console.log(error)
    })
  }
}
</script>
