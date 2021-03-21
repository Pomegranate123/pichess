<template>
<div v-if="loggedin">
  Profile<br>
  Username: {{ username }}<br>
  Rating: {{ rating }}<br>
  <button v-on:click="this.logout()">Uitloggen</button> 
</div>
</template>

<script>
export default {
  data () {
    return {
      loggedin: false,
      rating: null,
      username: null,
    }
  },
  methods: {
    logout () {
      const headers = {'headers': {'X-CSRFToken': this.$cookie.getCookie('csrftoken')}}
      this.axios
        .get("/api/accounts/logout", headers)
        .then(() => {
          this.ws.send('{"type":"remove"}')
          this.$router.push({ name: 'login' })
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  mounted () {
    this.reload = !this.reload
    const headers = {'headers': {'X-CSRFToken': this.$cookie.getCookie('csrftoken')}}
    this.axios
      .get('/api/accounts/profile/', headers)
      .then(response => {
        this.loggedin = true
        this.username = response.data.username
        this.rating = response.data.rating
      })
      .catch(error => {
        this.$router.push({ name: 'login' })
        console.log(error)
   })
  }
}
</script>
