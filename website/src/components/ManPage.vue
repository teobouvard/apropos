<template>
  <div class="page">
    <h1>{{ name }}</h1>
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
    };
  },
  methods: {
    getManpage() {
      const path = 'http://192.168.0.95:5000/random';
      axios.get(path)
        .then((res) => {
          this.name = res.data.name;
          this.description = res.data.description;
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
</style>
