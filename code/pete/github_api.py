import requests
from prettyprinter import pprint
from datetime import datetime, timedelta
import pytest
import pytest_repeat

students = [
    {'username': 'meganbradner', 'repo': 'capstone'},
    {'username': 'dbrunken', 'repo': 'Plan-Direct'},
    {'username': 'SC-Mack', 'repo': 'LFG'},
    {'username': 'mdziuban', 'repo': 'Sanctuary_Capstone'},
    {'username': 'mbKirby', 'repo': 'CharacterCreator'},
    {'username': 'demesimms', 'repo': 'GIState'},
    {'username': 'SwartyPDX', 'repo': 'PDXCodeGuild'},
]

get_student_info = lambda student: (student['username'], student['repo'])
# js arrow function:
# const getStudentInfo = student => [student.username, student.repo]
# [username, student] = getStudentInfo(student)

if __name__ == '__main__':
    for student in students:
        username, repo =  get_student_info(student)
        print(username, repo)
        url = f'https://api.github.com/repos/{username}/{repo}/commits'
        headers = {'Accept': 'application/vnd.github.v3+json'}
        response = requests.get(url, headers=headers)
        print(type(response.json()))
        pprint(response.json()[0]['commit']['author']['date'])
        commit_date = datetime.strptime(response.json()[0]['commit']['author']['date'], '%Y-%m-%dT%H:%M:%SZ')
        print(commit_date)
        yesterday = datetime.now() - timedelta(days=1)
        print(yesterday)
        print(commit_date > yesterday) # __gt__

index = -1

@pytest.mark.repeat(len(students))
def test_capstone_commits():
    global index
    index += 1
    username, repo =  get_student_info(students[index])
    url = f'https://api.github.com/repos/{username}/{repo}/commits'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(url, headers=headers)
    date_str = response.json()[0]['commit']['author']['date']
    commit_date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
    yesterday = datetime.now() - timedelta(days=1)
    assert commit_date > yesterday
