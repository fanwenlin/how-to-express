import json
import os

from util import cached_data, is_running
   
def handle():
    # print(sys.argv)
    resp = {
        'items': [],
    }
    term = os.environ.get('input')

    taskname = f'fetch_response {term}'
    if (not is_running(taskname)) and (not cached_data(taskname)):
        # start_generate(taskname, term)
        resp['rerun'] = 0.5
        resp['items'].append({
            'title': 'Please wait...',
            'subtitle': f'querying {taskname}',
        })
    else:
        if is_running(taskname):
            resp['rerun'] = 0.1
        content = cached_data(taskname)
        if content:
            content = content.split('\n')
            for i, line in enumerate(content):
                parts = content[i].split('|')
                title, subtitle = parts[0], ''
                if len(parts) > 1:
                    subtitle = parts[1]
                resp['items'].append({
                    'title': title,
                    'subtitle': subtitle,
                    'valid': True,
                    'arg': title,
                })
        if len(resp['items']) == 0:
            resp['items'].append({
                'title': 'Please wait...',
                'subtitle': f'querying {taskname}',
            }) 
    print(json.dumps(resp))



if __name__ == '__main__': 
    handle()
