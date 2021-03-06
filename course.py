from typing import Optional


class Course:
    def __init__(self, name: str, course_id: str, subject: str, units: str, term: str, instructors: str, section: str, occupancy: str, capacity: str, start_date: str, end_date: str, meets: str, location: str, waitlist: Optional[str] = None, college: str = "UNIVERSITY OF NORTH GEORGIA", long_subject: Optional[str] = None, sub_college: Optional[str] = None, career: Optional[str] = None, description: Optional[str] = None, prerequisites: Optional[str] = None, corequisites: Optional[str] = None, equivalent_courses: Optional[str] = None, components: Optional[str] = None, class_attributes: Optional[str] = None, notes: Optional[str] = None, grading_basis: Optional[str] = None, instruction_mode: Optional[str] = None, textbooks: Optional[str] = None, room: Optional[str] = None, crn: Optional[str] = None):
        self.name = name
        self.capacity = capacity

        if capacity == "**CLOSED**":
            self.capacity = None

        self.course_id = course_id
        self.subject = subject
        self.long_subject = long_subject
        self.units = units
        self.term = term
        self.instructors = instructors
        self.college = college

        self.section = section
        self.occupancy = occupancy
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.meets = meets
        self.waitlist = waitlist

        self.room = room
        self.crn = crn
        self.sub_college = sub_college
        self.career = career
        self.description = description
        self.prerequisites = prerequisites
        self.corequisites = corequisites
        self.equivalent_courses = equivalent_courses
        self.components = components
        self.class_attributes = class_attributes
        self.notes = notes
        self.grading_basis = grading_basis
        self.instruction_mode = instruction_mode
        self.textbooks = textbooks

    def to_string(self) -> str:
        return f"{self.name} - {self.long_subject} ({self.subject}) {self.course_id}"

    def sections_dict(self) -> dict:
        results: dict = {
            "section": self.section,  # Required
            "course": self.name,  # Required
            "course_id": self.course_id,  # Required
            "college": self.college,  # Required
            "description": self.description,
            "component": self.components,
            "notes": self.notes,
            "occupancy": self.occupancy,  # Integer
            "capacity": self.capacity,  # Integer
            "waitlist": self.waitlist,  # Integer
            "start_date": self.start_date,  # Date
            "end_date": self.end_date,  # Date
            "meets": self.meets,
            "location": self.location,
            "final_deadline": None,  # Date
            "units": self.units,
            "grading_basis": self.grading_basis,
            "instruction_mode": self.instruction_mode,
            "term": self.term,  # Required
            "instructors": self.instructors,
            "textbooks": self.textbooks
        }

        return results

    def sections_dtype(self) -> dict:
        dtype: dict = {
            "section": "str",
            "course": "str",
            "course_id": "str",
            "college": "str",
            "description": "str",
            "component": "str",
            "notes": "str",
            "occupancy": "int",
            "capacity": "int",
            "waitlist": "int",
            "start_date": "str",  # Date
            "end_date": "str",  # Date
            "meets": "str",
            "location": "str",
            "final_deadline": "str",  # Date
            "units": "str",
            "grading_basis": "str",
            "instruction_mode": "str",
            "term": "str",
            "instructors": "str",
            "textbooks": "str"
        }

    def courses_dict(self) -> dict:
        results: dict = {
            "course": self.name,  # Required
            "course_id": self.course_id,  # Required
            "college": self.college,  # Required
            "sub_college": self.sub_college,
            "subject": self.subject,
            "career": self.career,
            "description": self.description,
            "prerequisites": self.prerequisites,
            "corequisites": self.waitlist,
            "equivalent_course": self.start_date,
            "components": self.end_date,
            "class_attributes": self.meets,
            "notes": self.location,
            "units": self.units,
            "grading_basis": self.grading_basis,
            "instruction_mode": self.instruction_mode,
            "term": self.term,
            "instructors": self.instructors,
            "textbooks": self.textbooks
        }

        return results

    def subjects_dict(self) -> dict:
        results: dict = {
            "subject": self.subject,  # Required
            "college": self.college,  # Required
            "equivalence_class": None # self.equivalent_courses
        }

        return results