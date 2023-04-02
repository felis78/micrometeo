<script>

/*######################################################################################################################
########################################### Import des lib utiles ######################################################
########################################################################################################################
 */

import { Line } from "vue-chartjs"
import {Chart as ChartJS, Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement} from "chart.js"

ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement)
/*
########################################################################################################################
################################## Création des fonctions de récupération de données ###################################
########################################################################################################################
 */
export default {
  name:'TheWelcome',
  components: { Line },

  props: ['temperature', 'pressure'],

  data() {

    return {
      temperaturesDatas: {
        labels: [ '0', '1', '2', '3', '4' , '5', '6', '7'],
        datasets: [  {data: this.temperature } ],
      },
      chartOptionsTemp: {
        responsive: true
      },

      pressureDatas: {
        labels: [ '0', '1', '2', '3', '4' , '5', '6', '7'],
        datasets: [  {data: this.pressure } ],
      },
      chartOptionsPress: {
        responsive: true
      },
    };
  },
};


</script>


########################################################################################################################
############################################################ HTML ######################################################
########################################################################################################################


<template>

  <div class = "test">
  <Line
    id="my-chart-id"
    :options="chartOptionsTemp"
    :data="temperaturesDatas"
  />
  </div>

  <div class = "test">
  <Line
    id="my-chart-id"
    :options="chartOptionsPress"
    :data="temperaturesDatas"
  />
  </div>


  </template>


########################################################################################################################
################################################# CSS ##################################################################
########################################################################################################################


<style scoped>
.test
{
  background-color: #f2f2f2;
}
</style>