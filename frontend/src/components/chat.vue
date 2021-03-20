<template>
  <div class="chat-container">
    <div class="heading">
      <div class="name" v-if="black === username">Chat with {{ white }}</div>
      <div class="name" v-else>Chat with {{ black }}</div>
    </div>
    <div class="body">
      <div class="table">
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
export default {
  name: "chat",
  data () {
    return {
      message: null,
      chat: null,
      username: null,
      white: this.$route.params.white,
      black: this.$route.params.black,
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
    }
  },
  mounted () {
    this.chat = new WebSocket("ws://" + window.location.host + "/wss/chat/" + this.white + "/" + this.black)
    const headers = {'headers': {'X-CSRFToken': this.$cookie.getCookie('csrftoken')}}
    this.axios
      .get('/api/accounts/profile/', headers)
      .then(response => {
        this.username = response.data.username
      })
      .catch(error => {
        console.log(error)
    })

  }
}
</script>

<style scoped>
.message-input {
  display: table-row;
  width: 100%;
  height: 26px;
}
textarea {
  width: 98%;
  height: 30px;
  padding: 0 5px;
  margin: 0;
  box-sizing: border-box;
  line-height: 20pt;
  resize: none;
  outline: none;
  font-size: 14px;
  border: solid 1px #AAAAAA;
  border-radius: 3px;
  font-family: Helvetica;
}
</style>
