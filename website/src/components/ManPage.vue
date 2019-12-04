<template>
  <div class="page">
    <v-btn @click=getManpage()>RANDOM</v-btn>
    <h1>{{ name }}</h1>
    <p>{{ synopsis }}</p>
    <p>{{ description }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ManPage',
  data() {
    return {
      name: '',
      description: '',
      synopsis: '',
    };
  },
  methods: {
    getManpage() {
      const path = 'http://192.168.0.95:5000/random';
      axios.get(path)
        .then((res) => {
          this.name = res.data.name;
          this.description = res.data.description;
          this.synopsis = res.data.synopsis;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getManpage();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
div {
  width: 60em;
  text-align: justify;
  margin: auto;
}
</style>
