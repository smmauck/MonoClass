<template>
  <div class="dashboard">
    <DashboardMain></DashboardMain>
  </div>
</template>

<script>
import DashboardMain from '@/components/DashboardMain.vue';

export default {
  name: 'Dashboard',
  components: {
    DashboardMain,
  },
};
</script>
