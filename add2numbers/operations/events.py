from flask_socketio import emit, join_room, leave_room
from flask import request
from .. import socketio

clients = []

def send_message(client_id, msg):
    socketio.emit('output', msg, client_id)
    print('sending message "{}" to client "{}".'.format(msg, client_id))

@socketio.on('connect')
def test_connect():
    print("Han conectado")
    clients.append(request.sid)
    print('-------')
    print(clients) 
    print('---X---')

    emit('identified', {'id': request.sid})

@socketio.on('message')
def test_message(message):
    print("Y han dialogado")
    print('WS:', request.sid)

    emit('response', {'data': 'Y esto me han respondido: "{}"'.format(message['data'])})


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')
    clients.remove(request.sid)
    print('---X---')
    print(clients) 
    print('---·---')
