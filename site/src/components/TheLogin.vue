<template>
<div class="formulaire">
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

function submit()
{
  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  var raw = JSON.stringify({
    "username": email.value,
    "password": password.value
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("http://localhost:5000//verifyUserPassword", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
}




</script>

<style>
</style>