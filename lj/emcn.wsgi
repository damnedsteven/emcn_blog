# import os	
# import sys
# import logging

# os.environ['DATABASE_URL'] = 'mssql+pyodbc://sa:support@MSSQL-PYTHON-TEST'

# logging.basicConfig(stream=sys.stderr)
# sys.path.insert(0,"/srv/proj/flask/emcn/")


# application.secret_key = 'Add your secret key'


import os
import sys


sys.path.insert(0, '/srv/proj/flask/emcn')
os.chdir("/srv/proj/flask/emcn")
from app import app as application

activate_this = '/srv/proj/flask/emcn/env/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))



