<template>
  <chessboard></chessboard>
  <form onsubmit="return false">
    <input id="orig" v-model="orig" name="orig">
    <input id="dest" v-model="dest" name="dest">
    <button class="confirm" type="submit" v-on:click="sendMove">Send move</button>
  </form>
</template>

<script>
import chessboard from '../components/Chessboard.vue'

export default {
  components: {
    chessboard
  },
  data () {
    return {
      orig: null,
      dest: null,
    }
  },
  methods: {
    sendMove () {
      this.ws.send(JSON.stringify({"orig": this.orig, "dest": this.dest}))
    }
  }
}
</script>
