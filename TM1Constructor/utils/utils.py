import json
import sys
import os


CONFIG_PATH = r'\..\config\database_parameters.json'


def getConnection():
    with open(set_current_directory() + CONFIG_PATH) as op:
        config = json.load(op)
    connection = config['database_connection']
    return connection


def set_current_directory():
    # determine if application is a script file or frozen exe
    if getattr(sys, 'frozen', False):
        application_path = os.path.abspath(sys.executable)
    elif __file__:
        application_path = os.path.abspath(__file__)
    directory = os.path.dirname(application_path)
    # set current directory
    os.chdir(directory)
    return directory
