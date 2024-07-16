
from typing import List, Dict
from flask_login import UserMixin

class StudProjectGraded:
    def __init__(
            self,
            id: int,
            name_ru: str,
            leader: str,
            tags: List[str],
            grade: int,
            start_date: str,
            finish_date: str,
            project_link: str,
            vacancy_name: str
        ):
        
        self.id = id
        self.name_ru = name_ru
        self.leader = leader
        self.tags = tags
        self.grade = grade
        self.start_date = start_date
        self.finish_date = finish_date
        self.project_link = project_link

        self.vacancy_name = vacancy_name


class Card(StudProjectGraded):
    def __init__(
            self,
            project: StudProjectGraded,
            description: str,
            files: List[str],
            outer_link: str
        ):

        super().__init__(project.id, project.name_ru, project.leader, project.tags, project.grade,
                        project.start_date, project.finish_date, project.project_link, project.vacancy_name)
        self.description = description
        self.files = files
        self.outer_link = outer_link
        

class User(UserMixin):
    def __init__(
            self,
            id,
            login,
            password,
            edu_info,
            projects
            ):
        
        self.id = id
        self.login = login
        self.password = password
        self.edu_info = edu_info
        self.projects = projects

class Student():
    def __init__(
            self,
            id,
            login: str,
            password: str,
            edu_info: Dict,
            projects: Dict[int, StudProjectGraded]
            ):
        
        self.id = id
        self.login = login
        self.password = password
        self.edu_info = edu_info
        self.projects = projects

        self.available_projects = projects.copy()
        self.cards = {}

