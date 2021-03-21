<template>
  <form onsubmit="return false">
    <h1>Log in</h1>
    <div class=form-group>
      <label for="username">Username</label><br>
      <input type="text" v-model="username" id="username"/><br>
    </div>
    <div class=from-group>
      <label for="password">Password</label><br>
      <input type="password" v-model="password" id="password"/><br>
      <span class=error>{{ errormsg }}</span><br>
    </div>
    <div class=form-group> 
      <button class="confirm" type="submit" :disabled="disable_button" v-on:click="login">Log in</button><br><br>
      <router-link tag="a" :to="{ name: 'signup' }">No account yet?</router-link>
    </div>
  </form>
</template>

<script>
export default {
  data() {
    return {
      user: null,
      username: '',
      password: '',
      disable_button: true,
      errormsg: ''
    }
  },
  watch: {
    username: function() {
      if(this.password != '' && this.username != '') {
        this.disable_button = false
      }
      else {
        this.disable_button = true
      }
    },
    password: function() {
      if(this.password != '' && this.username != '') {
        this.disable_button = false
      }
      else {
        this.disable_button = true
      }
    }
  },
  methods: {
    login() {
      const headers = {'headers': {'X-CSRFToken': this.$cookie.getCookie('csrftoken')}}
      const data = { 'password': this.password, 'username': this.username }
      this.axios
        .post('api/accounts/authenticate/', data, headers)
        .then(() => {
          this.$router.push({ name: 'play' })
        })
        .catch(error => {
          console.log(error)
          this.password = ''
          this.errormsg = 'Inloggegevens verkeerd'
      })
    }
  }
}
</script>
