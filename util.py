import os

def write_status(taskname:str, status:str):
    with open(f'cache/{taskname}_status.txt', 'w') as f:
        f.write(status)
def is_running(taskname :str) -> bool:
    # check if status file exists
    if not os.path.exists(f'cache/{taskname}_status.txt'):
        return False
    with open(f'cache/{taskname}_status.txt') as f:
        s = f.read()
        if s == 'running':
            return True
    return False

def cached_data(key: str):
    if not os.path.exists(f'cache/{key}_cached.txt'):
        return None
    with open(f'cache/{key}_cached.txt') as f:
        content = f.read()
        return content

def cache_data(key:str, content:str):
    with open(f'cache/{key}_cached.txt', 'wb') as f:
        f.write(content.encode('utf-8'))