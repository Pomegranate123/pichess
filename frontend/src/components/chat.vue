<template>
  <div class="chatcontainer">
    <div class="heading">
      <div class="name" v-if="black === username">Chat with {{ white }}</div>
      <div class="name" v-else>Chat with {{ black }}</div>
    </div>
    <div class="body">
      <div class="table">
        <div id="chat-log" class="chat-log">
          <div v-for="(message, index) in history" :key="index" class="bubble">
            <div class="msg me" v-if="message.user === username">
              {{message.msg}}
            </div>
            <div class="msg notme" v-else>
              {{message.msg}}
            </div>
            <br>
          </div>
        </div>
        <div class="message-input">
          <textarea
          v-model="message"
          placeholder="message..."
          maxlength="20000"
          @keydown.enter="submitMessage"
          ></textarea>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
function scrollBottom() {
  let container = this.$el.querySelector("#chat-log")
  container.scrollTop = container.scrollHeight
}

export default {
  name: "chat",
  data () {
    return {
      message: null,
      chat: null,
      username: "test",
      white: this.$route.params.white,
      black: this.$route.params.black,
      history: [],
    }
  },
  methods: {
    submitMessage(event) {
      if (!event.shiftKey) {
        event.preventDefault()
      } else {
        return
      }
      if (this.message.length === 0) {
        return
      }
      this.chat.send(JSON.stringify({'msg': this.message, 'user': this.username}))
      this.message = ''
    },
    addMessage() {
      return (event => {
        let message = JSON.parse(event.data)
        this.history.push(message)
        this.$nextTick(scrollBottom)
      })
    },
  },
  mounted () {
    const headers = {'headers': {'X-CSRFToken': this.$cookie.getCookie('csrftoken')}}
    this.axios
      .get('/api/accounts/profile/', headers)
      .then(response => {
        this.username = response.data.username
      })
      .catch(error => {
        console.log(error)
    })

    this.chat = new WebSocket("ws://" + window.location.host + "/wss/chat/" + this.white + "/" + this.black)
    if (this.chat != undefined) {
      this.chat.onopen = function() {
        console.log("<chat> [open] Connected to websocket")
      }

      this.chat.onmessage = function(event) {
        console.log(`<chat> [message] Data received from websocket: ${event.data}`)
      }

      this.chat.onclose = function(event) {
        if (event.wasClean) {
          console.log(`<chat> [close] Connection closed cleanly, code=${event.code} reason=${event.reason}`)
        } else {
          console.log("<chat> [close] Connection died")
        }
      }
      this.chat.addEventListener('message', this.addMessage(event))
    }
    this.$nextTick(scrollBottom)
  },
}
</script>

<style scoped>
.chatcontainer {
  width: 320px;
  height: 420px;
  background: var(--lightgrey);
  margin: 0 10px 0 10px;
}

.chat-log {
  display: block;
  height: 340px;
  width: 100%;
  padding: 2% 4%;
  box-sizing: border-box;
  overflow-y: scroll;
}

.chat-log::-webkit-scrollbar {
  display: none;
}

.bubble {
}

.msg {
  padding: 4px;
  margin: 6px;
  border-radius: 4px;
  text-align: left;
  display: block;
  clear: both;
}

.me {
  float: right;
  background: var(--lightgreen);
}

.notme {
  float: left;
  background: var(--faintgreen);
}

.message-input {
  width: 314px;
  height: 30px;
  padding: 5px 3px;
}

textarea {
  height: 30px;
  width: 98%;
  padding: 0 5px;
  margin: 0;
  box-sizing: border-box;
  line-height: 20pt;
  resize: none;
  outline: none;
  font-size: 14px;
  border: solid 1px #AAAAAA;
  border-radius: 3px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
}
</style>
