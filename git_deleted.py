import subprocess
import requests
import typer

subprocess.run('clear')

app = typer.Typer()

def repo(name):
    return name

def github(repo):
    directory = f'FILENAME/{repo}'

    USERNAME = 'USERNAME'
    URL = f'https://api.github.com/repos/{USERNAME}/{repo}'
    TOKEN = 'YOUR_AUTHENTICATION'
    AUTHENTICATION = f"token {TOKEN}"

    headers = {     "Accept": "application/vnd.github.v3+json",
                    "Authorization": AUTHENTICATION     }

    response = requests.delete(URL, headers=headers)
    subprocess.run('clear')

    # print(response.json())

    delete = ['rm', '-rf', f'{directory}']

    subprocess.Popen(delete)

    if response.status_code == 204:
        print(f'"{repo}" has been deleted')
    else:
        print(f'\n{response.status_code}')
        print(response.content)   

@app.command()
def delete(name: str):
    github(repo(name))

if __name__ == "__main__":
    app()