from flask import Blueprint

operations = Blueprint('operations', __name__)

from . import routes, events
print(routes)
print(events)