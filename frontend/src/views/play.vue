<template>
  <form onsubmit="return false">
    <h1>Challenge friend</h1>
    <label for="opponent" :key="reload">Username:</label><br>
    <input id="opponent" v-model="opponent" name="opponent"><br>
    <br>
    Play as: <br>
    <input id="white" type="radio" v-model="color" name="color" value="white" checked>
    <label for="white"> White</label><br>
    <input id="black" type="radio" v-model="color" name="color" value="black">
    <label for="black"> Black</label><br>
    <br>
    Time control: <br>
    <input class="num" id="min" type="number" v-model="min" value="10" min="0">
    <label for="min"> Minutes</label><br>
    <input class="num" id="sec" type="number" v-model="sec" value="0" min="0">
    <label for="sec"> Seconds</label><br>
    <input class="num" id="inc" type="number" v-model="inc" value="0" min="0">
    <label for="inc"> Increment</label><br>

    <br>
    <button class="confirm" type="submit" v-on:click="challengePlayer">Challenge</button><br><br>
    <button class="confirm" type="submit" v-on:click="getLink">Copy link</button>

    <h1>Currently online:</h1>
    <table v-if="players.length > 0">
      <tbody>
        <tr v-for="(player, index) in players" :key="index">
          <td v-if="player != username"><a @click="selectPlayer(player)">{{ player }} ({{ ratings[index] }})</a></td>
        </tr>
      </tbody>
    </table>
  </form>
</template>

<script>
export default {
  data () {
    return {
      reload: false,
      min: 10,
      sec: 0,
      inc: 0,
      color: "white",
      white: null,
      black: null,
      opponent: '',
      username: "Guest",
      players: [],
      ratings: [],
    }
  },
  methods: {
    challengePlayer () {
      let time = parseInt(this.min) * 60 + parseInt(this.sec)
      if (this.opponent != '' && time >= 1) {
        if (this.color === "white") {
          this.white = this.username
          this.black = this.opponent
        } else {
          this.black = this.username
          this.white = this.opponent
        }
        let challenge = {"type": "challenge", "white": this.white, "black": this.black, "time": time, "inc": this.inc}
        this.ws.send(JSON.stringify(challenge))
      } else {
        alert("Invalid challenge. A valid challenge has at least one second on the clock and a valid username.")
      }
    },
    selectPlayer (player) {
      this.opponent = player
    },
    getLink () {
      let time = parseInt(this.min) * 60 + parseInt(this.sec)
      if (this.opponent != '' && time >= 1) {
        if (this.color === "white") {
          this.white = this.username
          this.black = this.opponent
        } else {
          this.black = this.username
          this.white = this.opponent
        }
        let link = window.location.protocol + "//" + window.location.host + "/#/game/" + this.white + "/" + this.black + "/" + time + "/" + this.inc

        var dummy = document.createElement("textarea")
        document.body.appendChild(dummy)
        dummy.value = link 
        dummy.select()
        document.execCommand("copy")
        document.body.removeChild(dummy)
      } else {
        alert("Invalid challenge. A valid challenge has at least one second on the clock and a valid username.")
      }
    },
    getOpponentRating (opponent) {
      const headers = {'headers': {'X-CSRFToken': this.$cookie.getCookie('csrftoken')}}
      this.axios
        .get('/api/home/get_rating?username=' + opponent, headers)
        .then(response => {
          this.ratings.push(response.data.rating)
        })
        .catch(error => {
          console.log(error)
      })
    },
    getOnlinePlayers () {
      const headers = {'headers': {'X-CSRFToken': this.$cookie.getCookie('csrftoken')}}
      this.axios
        .get('/api/home/players', headers)
        .then((response) => {
          this.players = response.data.online
          this.ratings = []
          for (let i = 0; i < this.players.length; i++) {
            this.getOpponentRating(this.players[i])
          }
        })
        .catch(error => {
          console.log(error)
      })
    },
    update() {
      return (event => {
        let data = JSON.parse(event.data)
        if (data.type === "update") {
          this.getOnlinePlayers()
        }
      })
    }
  },
  mounted () {
    this.reload = !this.reload
    this.ws.addEventListener('message', this.update(event))
    const headers = {'headers': {'X-CSRFToken': this.$cookie.getCookie('csrftoken')}}
    this.axios
      .get('/api/accounts/profile', headers)
      .then((response) => {
        this.username = response.data.username
      })
      .catch(error => {
        console.log(error)
    })
    this.getOnlinePlayers()
  }
}
</script>

<style>
input.num {
  width: 40px;
}
</style>
