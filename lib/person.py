#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    # name = "Person"
    def __init__(self, name = "Person", job = APPROVED_JOBS):
        if ((isinstance(name, str)) and (1 <= len(name) <= 25)):
            self.name = name.title()
        elif name != "":
            print('Name must be string between 1 and 25 characters')
        else:
            print('Name must be string between 1 and 25 characters')

        self.job = job
        if job != APPROVED_JOBS:
            print('Job must be in list of approved jobs.')