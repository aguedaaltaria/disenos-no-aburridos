from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='../frontend')

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:nombre_archivo>')
def servir_archivos(nombre_archivo):
    return send_from_directory(app.static_folder, nombre_archivo)

if __name__ == '__main__':
    app.run(debug=True, port=5002)