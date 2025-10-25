"""
ApiApplication.py
Autor: Denilson Oliveira

Descrição:
Ponto de entrada da aplicação Flask.
Responsável por inicializar o servidor e registrar os blueprints (controllers).
"""
from flask import Flask
from controller.produto_controller import produto_api
from controller.produto_web import produto_web
from extensions import db, migrate

def create_app():
    app = Flask(__name__)

    # --- Config DB: arquivo SQLite na raiz do projeto ---
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///produtos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # --- Inicializa extensões ---
    db.init_app(app)
    migrate.init_app(app, db)

    # --- Registra blueprints ---
    app.register_blueprint(produto_api)
    app.register_blueprint(produto_web)

    return app

# Suporte a flask run e execução direta
app = create_app()

if __name__ == '__main__':
    print("Aplicação iniciada: http://127.0.0.1:5000")
    app.run(debug=True)
