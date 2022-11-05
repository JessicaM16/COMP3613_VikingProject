import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import create_db, get_migrate
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users )
from App.controllers import ( create_recommendation_cli, get_all_recommendation, get_all_recommendation_json )
from App.controllers import ( create_notification_cli, get_all_notification_json )

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    create_db(app)
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands')

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("role", default="teacher")
@click.argument("password", default="robpass")
@click.argument("email", default="rob@mail.com")
def create_user_command(username, role, password, email):
    create_user(username, password, email, role)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

##############

recommendation_cli = AppGroup('recommendation', help='recommendation object commands') 


@recommendation_cli.command("create",help="Creates a recommendation")
@click.argument("letter", default="This is a recommendation for bob")
@click.argument("recipient_id", default="2")
@click.argument("sender", default="2")
def create_recommendation_command(letter, recipient_id, sender):
    create_recommendation_cli(letter, recipient_id, sender)
    print(f'{letter} created!')

@recommendation_cli.command("list", help="list recommendations")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_recommendation())
    else:
        print(get_all_recommendation_json())

app.cli.add_command(recommendation_cli)

###############

notification_cli = AppGroup('notification', help='notification object commands') 


@notification_cli.command("create",help="Creates a notification")
@click.argument("message", default="This is a request for a recommendation from ms jade")
@click.argument("recipient_id", default="2")
@click.argument("sender", default="2")
def create_notification_command(message, recipient_id, sender):
    create_notification_cli(message, recipient_id, sender)
    print(f'{message} created!')

@notification_cli.command("list", help="list notification")
def list_notification_command():
        print(get_all_notification_json())

app.cli.add_command(notification_cli)

##################

'''
Generic Commands
'''

@app.cli.command("init")
def initialize():
    create_db(app)
    print('database intialized')

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)