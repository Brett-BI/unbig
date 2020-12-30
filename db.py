from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class SQLAlchemy():
    def __init__(self):
        self.db_uri = None
        self.engine = None
        self.session = None
        self.Base = declarative_base()
    
    def initialize(self, db_uri):
        self.db_uri = db_uri
        self.engine = self.create_engine()
        self.session = self.create_session()

    def create_engine(self):
        engine = create_engine(self.db_uri, echo=False)
        return engine
    
    def create_session(self):
        # sessionmaker returns a class
        session = sessionmaker(self.engine)
        
        return session()
    
    def setup_db(self):

        print('Dropping all tables...')
        self.Base.metadata.drop_all(self.engine)

        print('Creating new tables...')
        self.Base.metadata.create_all(self.engine)

    

