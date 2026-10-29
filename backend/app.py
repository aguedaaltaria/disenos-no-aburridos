import os
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder='../frontend')

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:nombre_archivo>')
def servir_archivos(nombre_archivo):
    return send_from_directory(app.static_folder, nombre_archivo)

@app.route('/api/estilos')
def listar_estilos():
    # Carpeta frontend donde están guardados los HTMLs
    frontend_dir = os.path.join(app.root_path, '../frontend')
    
    estilos = []
    if os.path.exists(frontend_dir):
        for archivo in os.listdir(frontend_dir):
            if archivo.endswith('.html') and archivo != 'index.html':
                # Limpiamos el nombre para mostrarlo bonito (ej: 'neobrutalism.html' -> 'Neobrutalism')
                nombre_limpio = archivo.replace('.html', '').replace('-', ' ').title()
                estilos.append({
                    "nombre": nombre_limpio,
                    "archivo": archivo
                })
    
    return jsonify(estilos)

if __name__ == '__main__':
    app.run(debug=True, port=5002)