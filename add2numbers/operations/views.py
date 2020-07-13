from flask import request
from flask.views import MethodView
from http import HTTPStatus
from .events import send_message


class Index(MethodView):
    def post(self):
        sid = request.json.get('iid')
        op1 = request.json.get('op1')
        op2 = request.json.get('op2')
        if not op1:
            send_message(sid, {'msg': "Introduce op1", 'param': "op1"})
            result = "waiting op1"
        elif not op2:
            send_message(sid, {'msg': "Introduce op2", 'param': "op2"})
            result = "waiting op2"
        else:
            result = float(op1) + float(op2)

        return dict(
            status="success",
            result=result
        )

