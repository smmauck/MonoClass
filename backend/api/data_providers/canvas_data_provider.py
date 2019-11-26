import json

import requests

from .data_provider import DataProvider


class CanvasDataProvider(DataProvider):

    def get_overview(self, session: requests.Session):
        api_res = json.loads(
            session.get(
                "https://canvas.colorado.edu/api/v1/courses?include[]=total_scores"
            ).content[9:].decode("utf-8")
        )

        overview = []
        for course in api_res:
            if "name" in course:
                course_obj = {
                    "course_number": course["course_code"],
                    "course_name": course["name"].split(":")[1].lstrip(),
                    "course_score": course["enrollments"][0]["computed_current_score"],
                    "course_grade": course["enrollments"][0]["computed_current_grade"],

                }
                overview.append(course_obj)

        return overview

    def get_grade_data(self):
        pass
