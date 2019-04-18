import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import Config

lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))
