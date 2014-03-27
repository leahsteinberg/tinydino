import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import sessionmaker


engine = sa.create_engine("sqlite:///dinodb.db")
Base = declarative_base()



class Link(Base):
  __tablename__ = 'Link'

  shortlink = Column(String, primary_key=True)
  url = Column(String)



Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

def add_row(shortenedlink, url):
  l = Link()
  l.shortlink = shortenedlink
  l.url = url
  session.add(l)
  session.commit()

def get_url(shortenedlink):
  # returns a list of the url(s) (should be 1 or 0) that correspond to that shortened link
  retrieved =  session.query(Link.url).filter(Link.shortlink == shortenedlink).first()
  if retrieved is not None:
    return retrieved[0]
  else:
    return retrieved



