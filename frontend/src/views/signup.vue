<template>
  <form on-submit="return false">
    <h1>Sign up</h1>
    <div class=form-group>
      <label for="username">Username</label><br>
      <input type="text" v-model="username" id="username"/><br>
    </div>
    <div class=form-group>
      <label for="password">Password</label><br>
      <input type="password" v-model="password" id="password"/><br>
    </div>
    <div class=form-group>
      <label for="passwordcheck">Repeat password</label><br>
      <input type="password" v-model="passwordcheck" id="passwordcheck"/><br>
    <span class="error">{{ message }}</span>   
    </div>
    <button class="confirm" type="submit" :disabled="disable_button" v-on:click="signup">Sign up</button>
  </form>
</template>

<script>
export default {
  name: "aanmelden",
  data() {
    return {
      user: null,
      username: '',
      password: '',
      passwordcheck: '',
      message: '',
      disable_button: true
    }
  },
  watch: {
    password: function() {
      this.passwords_match()
    },
    passwordcheck: function() {
      this.passwords_match()
    }
  },
  methods: {
    passwords_match() {
      if(this.password.length != 0 && this.passwordcheck.length != 0) {
        if(this.password === this.passwordcheck) {
          this.message=""
          this.disable_button=false
        }
        else {
          this.message="Wachtwoorden komen niet overeen!"
          this.disable_button=true
        }
      }
      else {
        this.message=""
        this.disable_button=true
      }
    },
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
      })
    },
    signup() {
      const headers = {'headers': {'X-CSRFToken': this.$cookie.getCookie('csrftoken')}}
      const data = { 'password': this.password, 'username': this.username }
      this.axios
        .post('/api/accounts/register/', data, headers)
        .then(() => {
          this.login()
        })
        .catch(error => {
          this.used_username()
          console.log(error)
     })
    },
    used_username() {
      this.password = ''
      this.passwordcheck = ''
      this.username = ''
      this.message = 'Gebruikersnaam is al in gebruik!'
    }
  }
}
</script>
 
