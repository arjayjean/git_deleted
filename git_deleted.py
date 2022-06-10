import subprocess
import requests

subprocess.run('clear')

repo = input(f'What are you deleting: ').lower() 
directory = f'FILENAME/{repo}'

USERNAME = 'USERNAME'
URL = f'https://api.github.com/repos/{USERNAME}/{repo}'
TOKEN = 'YOUR_AUTHENTICATION'
AUTHENTICATION = f"token {TOKEN}"

# jsonPayload = {"owner": USERNAME, "name": repo}

headers = {     "Accept": "application/vnd.github.v3+json",
                "Authorization": AUTHENTICATION     }

response = requests.delete(URL, headers=headers)
subprocess.run('clear')

# print(response.json())

delete = ['rm', '-r', f'{directory}']

subprocess.run(delete)

if response.status_code == 204:
    print(f'"{repo}" has been deleted')
