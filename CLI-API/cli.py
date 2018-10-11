import click
from ControllerAPI import ControllerAPI
__author__ = "Javier Sancho"
g_username=''
C_API=ControllerAPI()
def isLogIn():
    if(g_username==''):
        return False
    else:
        return True

@click.group()
def main():
    """CLI to test the API"""

@main.command()
@click.argument('text')
def request(text):
    """To send a request to the API"""
    print(C_API.makeRequest(text))

@main.command()
@click.argument('username',nargs=1)
@click.argument('password',nargs=1)
def login(username,password):
    """To authenticate the user to use the API """
    aut=C_API.authenticateUser(username,password)
    if(aut):
        global g_username
        g_username=username

if __name__ == "__main__":
    main()
