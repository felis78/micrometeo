<template>
<div class="formulaire" v-if="session!=1">
    <form>

  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Username </label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" v-model="email">
    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Password </label>
    <input type="password" class="form-control" id="exampleInputPassword1" v-model="password">
  </div>
 
  <button type="submit" class="btn btn-primary" @click.prevent="submit">Submit</button>
</form>
</div>
</template>

<script setup>

import { ref } from 'vue'

const email = ref('')
const password = ref('')
let res = ref('')
let session = ref('')

function submit()
{
  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  let raw = JSON.stringify({
    "username": email.value,
    "password": password.value
  });

let requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
  };

fetch("http://localhost:5000//verifyUserPassword", requestOptions)
  .then(response => response.text())
  .then(result => res.value = JSON.parse(result))
  .catch(error => console.log('error', error));

console.log(res['_value'])
if (res['_value'][0] == "success")
{
  sessionStorage.setItem('user', res['_value'][1])
  session.value = sessionStorage.getItem('user')
}
}


</script>

<style>
</style>