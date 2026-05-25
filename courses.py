from fastapi import APIRouter,Path
from model import Course
import json

course_router = APIRouter()

coursesList = "courses.json"

@course_router.get("/courses")
async def get_courses() -> list:
    with open(coursesList, "r", encoding="utf-8") as f:
        return json.load(f)

@course_router.post("/courses")
async def add_course(course: Course) -> dict:
    with open(coursesList, "r", encoding="utf-8") as f:
        courses = json.load(f)
    courses.append(course.dict())
    with open(coursesList, "w", encoding="utf-8") as f:
        json.dump(courses, f)
    return {
        "msg": "Course added successfully"
    }
@course_router.get("/course/{course_id}")
async def get_single_course(course_id: int = Path(..., description="The ID of the course to retrieve")) -> dict:
    for course in courses_list:
        if course.id == course_id:
            return {
                "course": course
            }
    return {
        "msg": "Course with the given ID not found"
    }