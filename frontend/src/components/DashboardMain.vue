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
  name: 'DashboardMain',
  props: {},
  data() {
    return {
      dashheaders: [
        { text: 'Course Name', value: 'course_name' },
        { text: 'Course Code', value: 'course_number' },
        { text: 'Standing Grade', value: 'course_grade' },
      ],
      dashitems: [
      ],
    };
  },
  mounted() {
    this.axios.get('grades/overview').then(
      (response) => {
        this.dashitems = response.data;
      },
    );
  },
};
</script>
