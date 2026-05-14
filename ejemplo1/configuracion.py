from sqlalchemy import create_engine
# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

engine = create_engine('sqlite:///demobase.db', echo=True)# echo=true muestra lo que esta pasando detras.

# mysql
# pip install mysql-connector-python
# engine = create_engine("mysql+mysqlconnector://user:pass@localhost:3306/demo100", echo=True)

# postgres
# sudo apt install libpq-dev
# pip install psycopg2
#engine = create_engine("postgresql+psycopg2://usuario:secreto@0.0.0.0:5432/mibase", echo=True)
