from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///db_sqlite3"

engine = create_engine(
    # connect_args={"check_same_thread" só é necessário quando se usa SQLite
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Classe que representa uma sessão do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe que será usada para criação do modelo do banco de dados
Base_db = declarative_base()

# Função para gerar uma instância da SessionLocal (cria as novas sessões)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()