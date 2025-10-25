"""

Módulo: extensions.py
Autor: Denilson Oliveira
Descrição:
    Módulo responsável pela inicialização das extensões do Flask
    utilizadas no projeto. Centraliza a criação de objetos globais
    que são compartilhados entre os diferentes módulos da aplicação.

Camada: Infraestrutura (suporte à arquitetura MVC)
Relacionamentos:
    - Banco de Dados: SQLAlchemy (ORM)
    - Migrações: Flask-Migrate (integração com Alembic)
    - Aplicação: ApiApplication.py (registra e inicializa as extensões)

Responsabilidades:
    - Criar instâncias globais de SQLAlchemy e Flask-Migrate;
    - Permitir que outros módulos importem essas instâncias
      sem precisar criar dependências circulares;
    - Ser inicializado dentro da factory function (create_app)
      em ApiApplication.py via:
          db.init_app(app)
          migrate.init_app(app, db)

Benefícios:
    - Evita importações circulares entre módulos;
    - Garante separação entre configuração e uso das extensões;
    - Facilita testes, migrações e manutenção da aplicação.
"""

# extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
