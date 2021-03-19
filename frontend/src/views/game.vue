<template>
  <div class="namecontainer">
    <div class="name" v-if="this.black === this.username">{{ this.white }}</div>
    <div class="name" v-else>{{ this.black }}</div>
    <br>
    <chessboard id="chess"></chessboard>
    <div class="name">{{ this.username }}</div><div class="rating">{{ this.rating }}</div>
  </div>

</template>

<script>
import chessboard from '../components/Chessboard.vue'

export default {
  components: {
    chessboard
  },
  data () {
    return {
      white: this.$route.params.white,
      black: this.$route.params.black,
      username: null,
      rating: null,
    }
  },
  mounted () {
    const headers = {'headers': {'X-CSRFToken': this.$cookie.getCookie('csrftoken')}}
    this.axios
      .get('/api/accounts/profile/', headers)
      .then(response => {
        this.username = response.data.username
        this.rating = response.data.rating
      })
      .catch(error => {
        console.log(error)
   })
  }
}
</script>

<style>
#chess {
  margin-top: 20px;
}

.namecontainer {
  width: 320px;
  height: 420px;
  background: var(--lightgrey);
  margin: 0 auto 0 auto;
}

.name {
  height: 40px;
  padding: 5px 5px 5px 5px;
  float: left;
}

.rating {
  height: 40px;
  padding: 5px 5px 5px 5px;
  float: right;
}
</style>
