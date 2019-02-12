"""run.py"""

import os
from api.v1 import create_app

app = create_app('testing')

if __name__ == '__main__':
    app.run()
