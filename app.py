from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'clave_secreta')

CORS(app)

# Importar rutas
from routes.auth import auth_bp
from routes.productos import productos_bp
from routes.usuarios import usuarios_bp

# Registrar rutas
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(productos_bp, url_prefix='/api')
app.register_blueprint(usuarios_bp, url_prefix='/api')

@app.route('/')
def home():
    return jsonify({
        'success': True,
        'message': '🚀 Backend Jugueteria funcionando!',
        'database': 'Jugueteria',
        'endpoints': {
            'auth': '/api/auth/*',
            'productos': '/api/productos/*',
            'usuarios': '/api/usuarios/*'
        }
    })

@app.route('/api/health')
def health():
    return jsonify({
        'success': True,
        'message': '✅ Servidor y base de datos activos',
        'status': 'running'
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'True').lower() == 'true'
    print(f"🚀 Servidor Flask en http://localhost:{port}")
    print("📊 Base de datos: Jugueteria")
    app.run(host='0.0.0.0', port=port, debug=debug)