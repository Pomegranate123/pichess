<template>
  <table class="players">
    <thead>
      <tr>
        <th v-for="(column, index) in this.columns" :key="index"> {{column}}</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(klas, index) in this.players" :key="index">
        <td>{{ players }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  name: 'klastabel',
  data () {
    return {
      user: null,
      columns: ['Naam', 'Leerlingen'],
      klasinfo: [],
      players: null,
      loading: false,
    }
  },
  mounted () {
    const headers = {'headers': {'X-CSRFToken': this.$cookie.getCookie('csrftoken')}}
    this.axios
      .get('http://localhost/api/home/players', headers)
      .then((response) => {
        this.players = response.data
        //this.$cookie.setCookie(this.user, auth)
        //this.redirect()
      })
      .catch(error => {
        console.log(error)
        this.wrong_info()
    })
  }
}
</script>
