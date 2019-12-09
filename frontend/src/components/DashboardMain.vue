<template>
    <v-container
        fluid
        fill-height
    >
        <div class="v-data-table theme--light" style="width:100%">
            <div class="v-data-table__wrapper" style="width:100%">
                <table class="v-data-table table" style="width:100%">
                    <colgroup>
                        <col class="">
                        <col class="">
                        <col class="">
                    </colgroup>
                    <thead class="v-data-table-header">
                        <tr>
                            <th><span>Course Name</span></th>
                            <th><span>Course Grade</span></th>
                            <th><span>Course Score</span></th>
                        </tr>
                    </thead>
                    <div v-if="loading">
                        <v-progress-circular
                            indeterminate
                            color="primary"
                        >
                        </v-progress-circular>
                    </div>
                    <tbody class="v-data-table theme--light">
                        <tr v-for="item in dashitems" v-bind:key="item.id">
                            <td>
                                <a v-bind:href="'/class/'+ item.course_id"
                                    style="text-decoration:none; color:black">
                                    {{ item["course_name"] }}
                                </a>
                            </td>
                            <td>{{ item["course_grade"] }}</td>
                            <td>{{ item["course_score"] }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
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
