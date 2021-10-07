<template>
  <h1>Numbers:</h1>
  <ul>
    <NumberLi v-for="number in numbers" :key="number" :number="number" />
  </ul>
  <h1 class="text-primary">Cities:</h1>
  <ul>
    <CityLi v-for="city in cities" :key="city.id" :city="city" />
  </ul>
</template>

<script>
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css';

import NumberLi from './components/NumberLi.vue'
import CityLi from './components/CityLi.vue'

export default {
  name: 'App',
  components: {
    NumberLi,
    CityLi
  },
  data() {
    return {
      numbers: [1, 2, 3, 4, 5],
      cities: []
    }
  },
  methods: {
    getCities() {
      axios({
        method: 'get',
        url: 'http://localhost:8000/api'
      }).then(response => this.cities = response.data)
      .catch(err => console.log(err))
    }
  },
  created() {
    this.getCities()
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
