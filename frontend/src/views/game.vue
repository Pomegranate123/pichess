<template>
  <div class="gamecontainer">
    <chessboard id="board"/>
    <chat id="chat"/>
  </div>

</template>

<script>
import chessboard from '../components/chessboard.vue'
import chat from '../components/chat.vue'

export default {
  components: {
    chessboard,
    chat
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
.gamecontainer {
  width: 680px;
  margin: 0 auto 0 auto;
}

#board {
  float: left;
}

#chat {
  float: left;
}
</style>
