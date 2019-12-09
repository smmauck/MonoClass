<template>
      <v-container
        fluid
        fill-height
      >
        <v-layout child-flex>
            <v-data-table
                :headers="dashheaders"
                :items="dashitems"
                hide-default-footer
            >
          </v-data-table>
        </v-layout>
    </v-container>
</template>

<script>
export default {
  name: 'ClassDetail',
  props: {},
  data() {
    return {
      dashheaders: [
        { text: 'Assignment', value: 'assignment_name' },
        { text: 'Due Date', value: 'assignment_due_date' },
        { text: 'Score', value: 'assignment_score' },
        { text: 'Possible Points', value: 'points_possible' },
      ],
      dashitems: [
      ],
    };
  },
  mounted() {
    const { classid } = this.$route.params;
    this.axios.get(`grades/canvas/${classid}`).then(
      (response) => {
        console.log(response.data);
        this.dashitems = response.data;
      },
    );
  },
};
</script>
