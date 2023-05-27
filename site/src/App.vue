<script setup>

import TheWelcome from './components/TheWelcome.vue'
import TheAdmin from './components/TheAdmin.vue'
</script>

<script>

/*######################################################################################################################
########################################### Import des lib utiles ######################################################
########################################################################################################################
 */

/*
########################################################################################################################
################################## Création des fonctions de récupération de données ###################################
########################################################################################################################
 */
import {ref} from "vue"

export default {
  name:'fetch',

  data() {
    return {
      datas: [],
      tempRambouillet: [],
      tempSevres: [],
      pressRambou : [],
      pressSevres :[],
      event : 0,
      start : ref(0),


    };
  },

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

  methods: {
    async getDatas() {
      try {
        await fetch("http://localhost:5000/globalDatas")
            .then(response => response.json())
            .then(result => this.datas = result)
            .catch(error => console.log('error', error))

      } catch (error) {
        console.log(error)
      }
      this.tempRambouillet=this.datas.rambouillet[0];
      this.pressRambou = this.datas.rambouillet[1];
      this.tempSevres = this.datas.sevres[0];
      this.pressSevres = this.datas.sevres[1];
    },
   },


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

  created() {
     this.getDatas()

  },
};

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

</script>


########################################################################################################################
####################################################### HTML ###########################################################
########################################################################################################################

<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNavDropdown">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Features</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Pricing</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Dropdown link
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
          <a class="dropdown-item" href="#">Action</a>
          <a class="dropdown-item" href="#">Another action</a>
          <a class="dropdown-item" href="#">Something else here</a>
        </div>
      </li>
    </ul>
  </div>
</nav>
  <main>
    <button class="button1" v-on:click="start=1"> Rambouillet </button>
    <button class="button2" v-on:click="start=2"> Sevres </button>
    <button class="button3" v-on:click="start=3"> Plaisir </button>
    <button class="button4" v-on:click="start='adm'"> Admin </button>
    <div v-if="start === 1">
      <TheWelcome
      :temperature="tempRambouillet"
      :pression="pressRambou"/>
    </div>
    <div v-if="start === 2">
      <TheWelcome
      :temperature="tempSevres"
      :pression = "pressSevres"/>
    </div>
    <div v-if="start === 'adm'">
      <TheAdmin/>
    </div>



  </main>
</template>

########################################################################################################################
####################################################### Style ##########################################################
########################################################################################################################

<style scoped>

.button1 {
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  float: left;
}

button1:hover {
  box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
}

.button2 {
  background-color: #FF0000; /* red */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}

.button3 {
   background-color: #318CE7; /* Bleu roi */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}

.button4 {
  background-color: #000000; /* black */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}
</style>
