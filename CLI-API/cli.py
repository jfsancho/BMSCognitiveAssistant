import click

__author__ = "Javier Sancho"
g_username=''
def isSignIn():
    if(g_username==''):
        return False
    else:
        return True

@click.group()
def main():
    """
    CLI to test the API
    """
    C_API= ControllerAPI()

@main.command()
@click.argument('text')
def request(text):
    """To send a request to the API"""
    click.echo('La petición enviada es: %s ' % text)
    C_API.makeRequest(text)

@main.command()
@click.argument('username',nargs=1)
@click.argument('password',nargs=1)
def signIn(username,password):
    """To authenticate the user to use the API """
    aut=C_API.authenticateUser()
    if(aut):
        global g_username
        g_username=username
if __name__ == "__main__":
    main()
