from .base import *
import os

if os.environ.get('mysite') == 'prod':
   from .prod import *
else:
   from .dev import *