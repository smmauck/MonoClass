import json
from typing import List, Dict

import requests

from .data_provider import DataProvider


class CanvasDataProvider(DataProvider):

    def get_overview(self, session: requests.Session, page: int = 1) -> List[Dict]:
        api_res = session.get(
            f"https://canvas.colorado.edu/api/v1/courses?include[]=total_scores&page={page}"
        )

        overview_json = json.loads(api_res.content[9:].decode("utf-8"))

        overview = []
        for course in overview_json:
            if "name" in course:
                course_obj = {
                    "course_id": course["id"],
                    "course_type": "canvas",
                    "course_number": course["course_code"],
                    "course_name": course["name"].split(":")[1].lstrip() if ":" in course["name"] else course["name"],
                    "course_score": course["enrollments"][0]["computed_current_score"],
                    "course_grade": course["enrollments"][0]["computed_current_grade"],
                }
                if not course_obj["course_score"]:
                    course_obj["course_score"] = "-"
                if not course_obj["course_grade"]:
                    course_obj["course_grade"] = "-"

                overview.append(course_obj)

        if 'rel="next"' in api_res.headers["Link"]:
            return overview + self.get_overview(session, page + 1)
        else:
            return overview

    def get_grade_data(self, session: requests.Session, course_id: int, page: int = 1) -> List[Dict]:
        api_res = session.get(
            f"https://canvas.colorado.edu/api/v1/courses/{course_id}/assignments?include[]=submission&page={page}"
        )

        assignments_json = json.loads(api_res.content[9:].decode("utf-8"))

        assignments = []
        for assignment in assignments_json:
            assignment_obj = {
                "assignment_name": assignment["name"],
                "assignment_description": assignment["description"],
                "assignment_due_date": assignment["due_at"],
                "points_possible": assignment["points_possible"]
            }

            if "omit_from_final_grade" in assignment:
                assignment_obj["omit_from_final_grade"] = assignment["omit_from_final_grade"]
            if "submission" in assignment and "score" in assignment["submission"]:
                assignment_obj["assignment_score"] = assignment["submission"]["score"]
            else:
                assignment_obj["assignment_score"] = None

            assignments.append(assignment_obj)

        if 'rel="next"' in api_res.headers["Link"]:
            return assignments + self.get_grade_data(session, course_id, page + 1)
        else:
            return assignments
