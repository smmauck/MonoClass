<template>
    <v-container
        fluid
        fill-height
    >
        <!--
        <v-layout child-flex>
            <v-data-table
                :headers="dashheaders"
                :items="dashitems"
                hide-default-footer
            >
          </v-data-table>
        </v-layout>
        -->
        <table style="width:100%">
            <tr v-for="item in dashitems" v-bind:key="item.id">
                <a v-bind:href="'/class/'+ item.course_id">
                    <td>{{ item["course_name"] }}</td>
                    <td>{{ item["course_grade"] }}</td>
                    <td>{{ item["course_score"] }}</td>
                </a>
            </tr>
        </table>
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
        console.log(response.data);
      },
    );
  },
};
</script>
