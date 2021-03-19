<template>
  <form onsubmit="return false">
    <h1>Challenge friend</h1>
    <label for="opponent">Username:</label><br>
    <input id="opponent" v-model="opponent" name="opponent"><br>
    <br>
    Play as: <br>
    <input id="white" type="radio" v-model="color" name="color" value="white" checked>
    <label for="white">White</label><br>
    <input id="black" type="radio" v-model="color" name="color" value="black">
    <label for="black">Black</label><br>
    <br>
    <button class="confirm" type="submit" v-on:click="getLink">Get link</button>

  </form>
</template>

<script>
export default {
  name: 'klastabel',
  data () {
    return {
      color: "white",
      white: null,
      black: null,
      opponent: null,
      username: null,
    }
  },
  methods: {
    getLink () {
      if (this.color === "white") {
        this.white = this.username
        this.black = this.opponent
      } else {
        this.black = this.username
        this.white = this.opponent
      }
      let link = window.location.protocol + "//" + window.location.host + "/#/game/" + this.white + "/" + this.black

      var dummy = document.createElement("textarea")
      document.body.appendChild(dummy)
      dummy.value = link 
      dummy.select()
      document.execCommand("copy")
      document.body.removeChild(dummy)
    }
  },
  mounted () {
    const headers = {'headers': {'X-CSRFToken': this.$cookie.getCookie('csrftoken')}}
    this.axios
      .get('/api/accounts/profile', headers)
      .then((response) => {
        this.username = response.data.username
      })
      .catch(error => {
        console.log(error)
    })
  }
}
</script>
