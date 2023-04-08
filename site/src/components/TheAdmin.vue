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


<div v-if="session==1">
  <button class="logout" @click.prevent="logout">Logout</button>
  <button class="adminButtons" v-on:click="choix=0">Show Users</button>
  <button class="adminButtons" v-on:click="choix=1">Add new user</button>
  <button class="adminButtons" v-on:click="choix=2">Delete user</button>
  <button class="adminButtons" v-on:click="choix=3">modify User</button>
  <button class="adminButtons" v-on:click="choix=4">Add new city</button>
  <button class="adminButtons" v-on:click="choix=5">Delete city</button>
</div>

<div v-if="choix == 1">
  <form>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Username </label>
    <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" v-model="createUsername">
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Email </label>
    <input type="email" class="form-control" id="exampleInputPassword1" v-model="createEmail">
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Password </label>
    <input type="password" class="form-control" id="exampleInputPassword1" v-model="createPassword">
  </div>
  <div class="form-check">
  <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" v-model="admin" @change="checkAdmin"/>
  <label class="form-check-label" for="flexCheckDefault">Admin</label>
</div>
 <button type="submit" class="btn btn-primary" @click.prevent="newUser">Submit</button>
</form>
</div>




</template>



<script setup>

import { onMounted, ref } from 'vue'

const email = ref('')
const password = ref('')
const createUsername = ref('')
const createEmail = ref('')
const createPassword = ref('')
const admin = ref(false)
/*const checkAdmin = () => {
  if(admin.value == true){
    admin.value = false
  }
  else{
    admin.value = true
  }
}*/
let res = ref('')
let session = ref('')
let choix = ref('')

//////////////////////////////////////////////////////////////////////////////////////////////

onMounted(() => {
  session.value = sessionStorage.getItem('user')
  console.log(session.value)
})

//////////////////////////////////////////////////////////////////////////////////////////////
//submit form
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

function newUser()
{
  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  let raw = JSON.stringify({
    "username": createUsername.value,
    "email": createEmail.value,
    "password": createPassword.value,
    "admin": admin.value
  });

  console.log(admin.value)
  
  let requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
  };
}

//////////////////////////////////////////////////////////////////////////////////////////////
//logout admin
function logout()
{
  sessionStorage.removeItem('user')
  session.value = 0
}
</script>

<style scoped>

.logout {
  background-color:red; /* red */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}
.adminButtons {
  background-color:grey; /* red */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}

</style>