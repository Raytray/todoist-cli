import requests
import urllib
import argparse
import ConfigParser
import json
import os

config = ConfigParser.ConfigParser()
config.read([os.path.expanduser('~/.todoist.cfg')])

TOKEN = config.get('DEFAULT', 'TOKEN')
DEFAULT_PROJECT_NAME = config.get('DEFAULT', 'DEFAULT_PROJECT_NAME')
URL = 'https://api.todoist.com/API'


def get_projects():
    """Returns a dictionary of projects with key: value of
    project_name: project_id"""

    params = [('token', TOKEN)]
    res_url = "{}/getProjects?{}".format(URL, urllib.urlencode(params))

    response = requests.get(res_url)

    if response.status_code != 200:
        print response.reason
        exit()

    json_response = json.loads(response.text)

    projects = {}

    for project in json_response:
        projects[project['name']] = project['id']
        projects[project['id']] = project['name']

    return projects


def add_task(content, projects, project=None, due=None):
    """Adds a task. Returns resulting item json or error"""

    if due is not None:
        params.append(('date_string', due))

    if project in projects:
        project_id = projects[project]

    else:
        project_id = projects[DEFAULT_PROJECT_NAME]

    params = [('content', content), ('project_id', project_id), ('token', TOKEN), ('priority', 1)]

    res_url = "{}/addItem?{}".format(URL, urllib.urlencode(params))

    response = requests.get(res_url)

    if response.status_code != 200 or response.text.startswith('"ERROR'):
        print response.reason, response.text
        exit()

    json_response = json.loads(response.text)

    return json_response


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--project', help="project to add task to")
    parser.add_argument('content', help="desired task")
    parser.add_argument('-d', '--due', help="Due when?")

    args = parser.parse_args()

    projects = get_projects()

    json_response = add_task(args.content, projects, project=args.project, due=args.due)
    print "{} added to project {}, due {}".format(json_response['content'], projects[json_response['project_id']], json_response['due_date'])


if __name__ == "__main__":
    main()
