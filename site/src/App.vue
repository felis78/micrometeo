<script setup>

import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'

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
      start : ref(0)
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

</script>


########################################################################################################################
####################################################### HTML ###########################################################
########################################################################################################################

<template>
  <HelloWorld msg="rien"></HelloWorld>
  <main>
    <button class="button1" v-on:click="start=1"> Rambouillet </button>
    <button class="button2" v-on:click="start=2"> Sevres </button>
    <button class="button3" v-on:click="start=3"> Plaisir </button>
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
    <div v-if="start === 3">
    </div>


  </main>
</template>

########################################################################################################################
####################################################### Style ##########################################################
########################################################################################################################

<style scoped>

header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}

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
</style>
