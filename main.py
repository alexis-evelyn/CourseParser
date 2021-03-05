#!/bin/python3

import os
import pandas as pd

from typing import List
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

    for subject in subject_list:
        if len(subject) > 0:
            headers: List[html.HtmlElement] = subject[0].xpath('th/small/strong')

            header: str
            for long_subject in headers:
                header = long_subject.text_content()

            print(header)

        print("--------------------------------------------------------")
        count: int = 0
        for row in subject:
            text: str = str.strip(row.text_content())

            if text != "" and "CRN" not in text and "START DATE" not in text and "Fully at a Distance" not in text and text != header:
                count += 1

                if count == 1:
                    print("+++")

                print(f"{count} - \"{text}\"")

                if count == 3:
                    print("+++")
                    count = 0
        print("--------------------------------------------------------")
