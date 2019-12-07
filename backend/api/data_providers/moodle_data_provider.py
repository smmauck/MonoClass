from typing import List, Dict

from datetime import datetime
import requests

from .data_provider import DataProvider


class MoodleDataProvider(DataProvider):

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
            if datetime.fromtimestamp(int(course["startdate"])) >= datetime.fromtimestamp(1566799200):
                course_obj = {
                    "course_id": course["id"],
                    "course_type": "moodle",
                    "course_number": course["shortname"],
                    "course_name": course["fullname"].rsplit("-", 1)[1].lstrip() if "-" in course["fullname"] else course["fullname"],
                    # TODO Add course_score and course_grade to object
                    "course_score": None,
                    "course_grade": None,

                }
                overview.append(course_obj)

        return overview

    def get_grade_data(self, session: requests.Session, course_id: int) -> List[Dict]:
        pass
