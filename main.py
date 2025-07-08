from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    sid = request.sid
    print(f'Cliente conectado. URL-SID: {sid}')
    emit('set_sid', {'sid': sid})

@socketio.on('message')
def handleMessage(msg):
    sid = request.sid
    print(f'Mensaje de cliente {sid}: {msg}')
    send(f'Echo del servidor {sid}: {msg}', broadcast=True, include_self=False)

if __name__ == '__main__':
    socketio.run(app, debug=True)