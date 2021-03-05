#!/bin/python3

import os
import pandas as pd

from typing import List, Optional
from lxml import html

from course import Course

fall_path: str = "working/courses/courses-fall-2021.html"
spring_path: str = "working/courses/courses-spring-2021.html"
summer_path: str = "working/courses/courses-summer-2021.html"

courses: List[Course] = []

with open(file=summer_path, mode="r") as f:
    lines: List[str] = f.readlines()
    content: str = "\n".join(lines)
    f.close()

    page: html.HtmlElement = html.fromstring(content)
    tables: List[html.Element] = page.xpath("/html/body/div/form/table")
    table: html.HtmlElement = tables[0]
    rows: List[html.HtmlElement] = table.xpath('tr')
    subject_list: List[List[html.HtmlElement]] = []

    new_subject: bool = True
    first_loop: bool = True
    subject: List[html.HtmlElement]
    for row in rows:
        for cell in row.iter("th"):
            if cell.get("colspan") == "9":
                new_subject: bool = True

                if first_loop:
                    first_loop: bool = False
                else:
                    subject_list.append(subject)

        if new_subject:
            subject: List[html.HtmlElement] = [row]
            new_subject: bool = False
        else:
            subject.append(row)

    subject_list.append(subject)
    print(f"Found {len(subject_list)} Subject(s)")

    courses: dict = {}
    for subject in subject_list:
        if len(subject) > 0:
            headers: List[html.HtmlElement] = subject[0].xpath('th/small/strong')

            header: str
            for long_subject in headers:
                header = long_subject.text_content()

            # print(header)

        # print("--------------------------------------------------------")
        count: int = 0
        for row in subject:
            text: str = str.strip(row.text_content())

            if text != "" and "CRN" not in text and "START DATE" not in text and text != header:
                count += 1

                if count == 1:
                    course: List[html.HtmlElement] = []
                    # print("+++")

                # print(f"{count} - \"{text}\"")
                course.append(row)

                if count == 4:
                    if header not in courses:
                        courses[header] = []

                    courses[header].append(course)
                    # print("+++")
                    count = 0
        # print("--------------------------------------------------------")

    # Parse Out Data From Courses Itself
    # for subject_long in courses.keys():
    subject_long: str = "Accounting"
    print("Length: {length}".format(length=len(courses[subject_long])))
    for course in courses[subject_long]:
        count: int = 0

        crn: Optional[str] = None
        subject: Optional[str] = None
        crse: Optional[str] = None
        sec: Optional[str] = None
        credits: Optional[str] = None
        title: Optional[str] = None
        sub_college: Optional[str] = None
        start_date: Optional[str] = None
        end_date: Optional[str] = None
        days: Optional[str] = None
        times: Optional[str] = None
        building: Optional[str] = None
        room: Optional[str] = None
        instructor: Optional[str] = None
        enrolled: Optional[str] = None
        seats: Optional[str] = None
        waitlist_max: Optional[str] = None
        waitlist_available: Optional[str] = None

        for row in course:
            count += 1

            if count == 1:  # and len(p_crn) > 0
                values: List[html.HtmlElement] = row.xpath('td/small')

                crn = str.strip(values[0].text_content())
                subject = str.strip(values[1].text_content())
                crse = str.strip(values[2].text_content())
                sec = str.strip(values[3].text_content())
                credits = str.strip(values[4].text_content())
                title = str.strip(values[5].text_content())
                sub_college = str.strip(values[6].text_content())

                print(f"Course ID: {crn}")
                print(f"Subject: {subject}")
                print(f"Subject (Long): {subject_long}")
                print(f"CRSE: {crse}")
                print(f"SEC: {sec}")
                print(f"Credits: {credits}")
                print(f"Title: {title}")
                print(f"Sub-College: {sub_college}")
            elif count == 2:
                values: List[html.HtmlElement] = row.xpath('td')

                start_date = str.strip(values[1].text_content())
                end_date = str.strip(values[2].text_content())
                days = str.strip(values[3].text_content())
                times = str.strip(values[4].text_content())
                building = str.strip(values[5].text_content())
                room = str.strip(values[6].text_content())

                print(f"Start Date: {start_date}")
                print(f"End Date: {end_date}")
                print(f"Days: {days}")
                print(f"Times: {times}")
                print(f"Building: {building}")
                print(f"Room: {room}")
            elif count == 3:
                values: List[html.HtmlElement] = row.xpath('td')

                instructor = str.rsplit(str.strip(values[1].text_content()), sep=": ")[1]
                enrolled = str.rsplit(str.strip(values[2].text_content()), sep=": ")[1]
                seats = str.rsplit(str.strip(values[3].text_content()), sep=": ")[1]

                print(f"Instructor: {instructor}")
                print(f"Enrolled: {enrolled}")
                print(f"Seats: {seats}")
            elif count == 4:
                values: List[html.HtmlElement] = row.xpath('td')

                waitlist_max = str.rsplit(str.strip(values[2].text_content()), sep=": ")[1]
                # waitlist_available = str.rsplit(str.strip(values[3].text_content()), sep=": ")[1]

                print(f"Waitlist Maximum: {waitlist_max}")
                print(f"Waitlist Available: {waitlist_available}")

            if count == 4:
                course_class: Course = Course(name=title, course_id=int(crse), subject=subject, long_subject=subject_long,
                                              units=credits, term="GET ME FROM FILE NAME", instructors=instructor,
                                              sub_college=sub_college,
                                              section=sec, occupancy=enrolled, capacity=seats, waitlist=waitlist_max,
                                              start_date=start_date, end_date=end_date, meets=f"{days} {times}", location=building)

                print(course_class.to_string())
