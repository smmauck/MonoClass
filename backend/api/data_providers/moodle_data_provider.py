from typing import List, Dict
from bs4 import BeautifulSoup

from datetime import datetime
import requests

from .data_provider import DataProvider


class MoodleDataProvider(DataProvider):
    def score_to_grade(self, score: float) -> str:
        if score < 60:
            return "F"
        if score < 70:
            return "D"
        if score < 80:
            return "C"
        if score < 90:
            return "B"
        return "A"
    
    def parse_course_data_from_html(self, raw_response: str) -> Dict:
        html_struct = BeautifulSoup(raw_response, 'html.parser')
        course_total_score = html_struct.find_all("td", class_="column-grade")[-1].text;
        course_total_grade = -1
        
        if course_total_score == "-":
            course_total_grade = "-"
        else:
            course_total_grade = self.score_to_grade(
                (float(course_total_score)/100)
            );

        return {
            "course_score":course_total_score,
            "course_grade":course_total_grade
        }

    def parse_assignments_from_html(self, raw_response: str) -> Dict:
        assignments = []
        grades = []
        points_possible = []
        return_list = []
        html_struct = BeautifulSoup(raw_response, 'html.parser')
        for grade_header in html_struct.find_all("a", class_="gradeitemheader"):
            assignments.append(grade_header.get_text())
        for grade in html_struct.find_all("td", class_="column-grade"):
            grades.append(grade.get_text())
        for points in html_struct.find_all("td", class_="column-range"):
            if "–" in points:
                points_possible.append(points.get_text().split("–")[1])
            else:
                points_possible.append("-")
        for asst in range(len(assignments)):
            assignment_obj = {
                "assignment_name":assignments[asst],
                "assignment_score":grades[asst],
                "assignment_due_date":"",
                "points_possible": points_possible[asst]
            }
            return_list.append(assignment_obj)
        return return_list

    def get_overview(self, session: requests.Session) -> List[Dict]:
        base_html = session.get("https://moodle.cs.colorado.edu/").content.decode("utf-8")
        moodle_sesskey = base_html.split('"sesskey":"')[1].split('",')[0]

        api_json = session.post(
            f"https://moodle.cs.colorado.edu/lib/ajax/service.php?sesskey={moodle_sesskey}",
            json=[{
                "index": 0,
                "methodname": "core_course_get_enrolled_courses_by_timeline_classification",
                "args": {"classification":"inprogress"}
            }]
        ).json()[0]["data"]["courses"] 

        overview = []
        for course in api_json:
            course_grade_overview = self.parse_course_data_from_html(
                session.get(
                    f"https://moodle.cs.colorado.edu/grade/report/user/index.php?id={course['id']}",
            ).text)

            if datetime.fromtimestamp(int(course["startdate"])) >= datetime.fromtimestamp(1566799200):
                course_obj = {
                    "course_id": course["id"],
                    "course_type": "moodle",
                    "course_number": course["shortname"],
                    "course_name": course["fullname"].rsplit("-", 1)[1].lstrip() if "-" in course["fullname"] else course["fullname"],
                    "course_score": course_grade_overview["course_score"],
                    "course_grade": course_grade_overview["course_grade"],
                    "course_source": "moodle"
                }
                overview.append(course_obj)

        return overview

    def get_grade_data(self, session: requests.Session, course_id: int) -> List[Dict]:
        return self.parse_assignments_from_html(
            session.get(
                f"https://moodle.cs.colorado.edu/grade/report/user/index.php?id={course_id}",
            ).text
        )
