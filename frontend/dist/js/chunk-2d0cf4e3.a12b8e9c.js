(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0cf4e3"],{"62c4":function(e,s,t){"use strict";t.r(s);var n=t("7a23"),r=Object(n["e"])("h1",null,"Aanmelden",-1),a={class:"form-group"},o=Object(n["e"])("label",{for:"username"},"Gebruikersnaam",-1),u=Object(n["e"])("br",null,null,-1),c=Object(n["e"])("br",null,null,-1),i={class:"form-group"},l=Object(n["e"])("label",{for:"password"},"Wachtwoord",-1),d=Object(n["e"])("br",null,null,-1),h=Object(n["e"])("br",null,null,-1),p={class:"form-group"},b=Object(n["e"])("label",{for:"passwordcheck"},"Wachtwoord herhalen",-1),m=Object(n["e"])("br",null,null,-1),w=Object(n["e"])("br",null,null,-1),f={class:"error"};function j(e,s,t,j,O,k){return Object(n["n"])(),Object(n["c"])("form",null,[r,Object(n["e"])("div",a,[o,u,Object(n["y"])(Object(n["e"])("input",{type:"text","onUpdate:modelValue":s[1]||(s[1]=function(e){return O.username=e}),id:"username"},null,512),[[n["v"],O.username]]),c]),Object(n["e"])("div",i,[l,d,Object(n["y"])(Object(n["e"])("input",{type:"password","onUpdate:modelValue":s[2]||(s[2]=function(e){return O.password=e}),id:"password"},null,512),[[n["v"],O.password]]),h]),Object(n["e"])("div",p,[b,m,Object(n["y"])(Object(n["e"])("input",{type:"password","onUpdate:modelValue":s[3]||(s[3]=function(e){return O.passwordcheck=e}),id:"passwordcheck"},null,512),[[n["v"],O.passwordcheck]]),w,Object(n["e"])("span",f,Object(n["t"])(O.message),1)]),Object(n["e"])("button",{class:"confirm",type:"submit",disabled:O.disable_button,onClick:s[4]||(s[4]=function(){return k.signup&&k.signup.apply(k,arguments)})},"Aanmelden",8,["disabled"])])}var O={name:"aanmelden",data:function(){return{user:null,username:"",password:"",passwordcheck:"",message:"",disable_button:!0}},watch:{password:function(){this.passwords_match()},passwordcheck:function(){this.passwords_match()}},methods:{passwords_match:function(){0!=this.password.length&&0!=this.passwordcheck.length?this.password===this.passwordcheck?(this.message="",this.disable_button=!1):(this.message="Wachtwoorden komen niet overeen!",this.disable_button=!0):(this.message="",this.disable_button=!0)},signup:function(){var e=this,s={username:this.username,password:this.password};this.axios.post("http://localhost/api/accounts/register/",s).then((function(){})).catch((function(s){e.used_username(),console.log(s)}))},used_username:function(){this.password="",this.passwordcheck="",this.username="",this.message="Gebruikersnaam is al in gebruik!"},redirect:function(){void 0===this.$route.query.redirect?this.$router.push(this.user+"/game"):this.$router.push(this.$route.query.redirect)}},mounted:function(){this.$cookie.isCookieAvailable(this.user)&&this.redirect()}};O.render=j;s["default"]=O}}]);
//# sourceMappingURL=chunk-2d0cf4e3.a12b8e9c.js.map