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
    const { classid, classsource } = this.$route.params;
    this.axios.get(`grades/${classsource}/${classid}`).then(
      (response) => {
        this.dashitems = response.data;
      },
    );
  },
};
</script>
