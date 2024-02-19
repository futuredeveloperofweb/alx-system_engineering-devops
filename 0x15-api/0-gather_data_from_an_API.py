#!/usr/bin/python3
import requests
import sys
import re


REST_API = 'https://jsonplaceholder.typicode.com'


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            re = requests.get('{}/users/{}'.format(REST_API, id)).json()
            task_re = requests.get('{}/todos'.format(REST_API)).json()
            emp_nm = re.get('name')
            task = list(filter(lambda x: x.get('userId') == id, task_re))
            comp_task = list(filter(lambda x: x.get('completed'), task))
            print('Employee {} is done with tasks({}/{}):'.format(
                emp_nm, len(comp_task), len(task)))
            if len(comp_task) > 0:
                for tk in comp_task:
                    print('\t {}'.format(tk.get('title')))
