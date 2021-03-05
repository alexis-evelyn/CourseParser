from typing import Optional


class Course:
    def __init__(self, name: str, course_id: int, subject: str, units: str, term: str, instructors: str, college: str = "UNIVERSITY OF NORTH GEORGIA", long_subject: Optional[str] = None, sub_college: Optional[str] = None, career: Optional[str] = None, description: Optional[str] = None, prerequisites: Optional[str] = None, corequisites: Optional[str] = None, equivalent_courses: Optional[str] = None, components: Optional[str] = None, class_attributes: Optional[str] = None, notes: Optional[str] = None, grading_basis: Optional[str] = None, instruction_mode: Optional[str] = None, textbooks: Optional[str] = None):
        self.name = name
        self.course_id = course_id
        self.subject = subject
        self.long_subject = long_subject
        self.units = units
        self.term = term
        self.instructors = instructors
        self.college = college

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