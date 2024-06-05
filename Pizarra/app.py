from flask import Flask, render_template # Importa la clase Flask del módulo flask y la función render_template para manejar plantillas HTML
from flask_socketio import SocketIO # Importa la clase SocketIO del módulo flask_socketio para manejar comunicación en tiempo real mediante WebSockets

app = Flask(__name__)  # Crea una instancia de la clase Flask y la asigna a la variable 'app'
socketio = SocketIO(app) # Crea una instancia de la clase SocketIO pasando la aplicación Flask como argumento

@app.route('/') # Define una ruta para la URL raíz ('/') usando un decorador
def index(): 
 return render_template('Cindex.html')  # Renderiza la plantilla 'Cindex.html' y la devuelve como respuesta

@socketio.on('draw', namespace='/draw') # Define un manejador de eventos para el evento 'draw' en el espacio de nombres '/draw'
def draw(message):
 socketio.emit('draw', message, namespace='/draw')  # Emite el mensaje recibido a todos los clientes conectados en el espacio de nombres '/draw'

if __name__ == '__main__': # Comprueba si el script se está ejecutando directamente (no importado como módulo)
 socketio.run(app, host='0.0.0.0', port=5000)  # Ejecuta la aplicación Flask con soporte para SocketIO en la dirección '0.0.0.0' (todas las interfaces de red) y el puerto 5000