from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# URL de la base de donnée SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./budget.db"

# Créer le moteur de la BDD(base de données)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# Créer la session 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Créer la base pour le modèle
BASE = declarative_base()

# Dépendance pour obtenir une session DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

