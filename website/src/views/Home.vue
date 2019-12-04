<template>
  <div class="home">
    <ManPage/>
  </div>
</template>

<script>
import ManPage from '@/components/ManPage.vue';

export default {
  name: 'home',
  components: {
    ManPage,
  },
  created() {
    this.$vuetify.theme.dark = true;
  },
};
</script>
