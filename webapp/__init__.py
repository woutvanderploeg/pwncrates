from flask import Flask
app = Flask(__name__)
from webapp import views, api, auth, template_preprocessor, database