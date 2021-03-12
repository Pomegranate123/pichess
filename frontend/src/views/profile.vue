<template>
Profile
Username: {{ username }}
Rating: {{ rating }}
</template>

<script>
export default {
  data () {
    return {
      rating: null,
      username: null,
    }
  },
  mounted () {
    const headers = {'headers': {'X-CSRFToken': this.$cookie.getCookie('csrftoken')}}
    this.axios
      .get('http://localhost/api/accounts/profile/', headers)
      .then(response => {
        this.username = response.data.username
        this.rating = response.data.rating
        //this.$cookie.setCookie(this.user, auth)
        //this.redirect()
      })
      .catch(error => {
        this.used_username()
        console.log(error)
   })
  }
}
</script>
