<template>
  <form>
    <h1>Inloggen</h1>
    <div class=form-group>
      <label for="username">Gebruikersnaam</label><br>
      <input type="text" v-model="username" id="username"/><br>
    </div>
    <div class=from-group>
      <label for="password">Wachtwoord</label><br>
      <input type="password" v-model="password" id="password"/><br>
      <span class=error>{{ errormsg }}</span><br>
    </div>
    <div class=form-group> 
      <button class="confirm" type="submit" :disabled="disable_button" v-on:click="login">Login</button><br><br>
      <router-link tag="a" :to="{ name: 'aanmelden', query: { redirect: this.$route.fullPath } }">Nog geen account?</router-link>
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
      this.axios
        .get('http://localhost/api/login', { password: this.password, username: this.username})
        .then(() => {
          //this.$cookie.setCookie(this.user, auth)
          //this.redirect()
        })
        .catch(error => {
          console.log(error)
          this.wrong_info()
      })
    },  
    wrong_info() {
      this.password = ''
      this.errormsg = 'Inloggegevens verkeerd'
    },
    redirect() {
      if (this.$route.query.redirect === undefined) {
        this.$router.push({ name: 'game'})
      }
      else {
        this.$router.push(this.$route.query.redirect)
      }
    },
  },
  mounted() {
    if (this.$cookie.isCookieAvailable(this.user)) {
      this.redirect()
    }
  }
}
</script>
