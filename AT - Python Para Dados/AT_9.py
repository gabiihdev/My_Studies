from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
import pathlib
from AT_8 import filmes, series

Base = declarative_base()  
DIR_CUR = pathlib.Path(__file__).parent.resolve()

    
class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
     
class Series(Base):
    __tablename__ = 'series'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    seasons = Column(Integer, nullable=False)
    episodes = Column(Integer, nullable=False)

def criar_conexao_bd():
    engine = create_engine(f"sqlite:///{DIR_CUR}/imdb.db")
    Base.metadata.create_all(engine)
    Session =  sessionmaker(bind=engine)
    return Session()

session = criar_conexao_bd()

for filme in filmes:
    try:
        filme_existente = session.query(Movie).filter_by(title=filme.title, year=filme.year).first()
        if not filme_existente:
            novo_filme = Movie(title=filme.title, year=filme.year, rating=filme.rating)
            session.add(novo_filme)
    except Exception as e:
        print(f">> ERRO: inserção do filme no BD - {e}")

for serie in series:
    try:
        serie_existente = session.query(Series).filter_by(title=serie.title, year=serie.year).first()
        if not serie_existente:
            nova_serie = Series(title=serie.title, year=serie.year, seasons=serie.seasons, episodes=serie.episodes)
            session.add(nova_serie)
    except Exception as e:
        print(f">> ERRO: inserção da série no BD - {e}")

session.commit()
session.close()