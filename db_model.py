import os
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import sessionmaker


if os.environ.get('DATABASE_URL') is None:
  print "using sqlite ~~~"
  SQLALCHEMY_DATABASE_URI = 'sqlite:///dinodb.db'
else:
  
  SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
  print "using post gres~~#("
  print os.environ['DATABASE_URL']


engine = sa.create_engine(SQLALCHEMY_DATABASE_URI)
Base = declarative_base()



class Link(Base):
  __tablename__ = 'Link'
  print "in constructor for database in dinodb\n"
  shortlink = Column(String, primary_key=True)
  url = Column(String)



#Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

def add_row(shortenedlink, url):
  print "in add row  in db model\n"
  l = Link()
  l.shortlink = shortenedlink
  l.url = url
  session.add(l)
  session.commit()

def get_url(shortenedlink):
  print "in get url in db model\n"
  # returns a list of the url(s) (should be 1 or 0) that correspond to that shortened link
  print 'link table is: ' + Link + '\n'
  print 'session is: ' + session + '\n'
  
  retrieved =  session.query(Link.url).filter(Link.shortlink == shortenedlink).first()
  print ' should have gotten retrieved \n'
  if retrieved is not None:
    return retrieved[0]
  else:
    return retrieved



