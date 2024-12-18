from xmlrpc.client import DateTime

from sqlalchemy import Column,Integer,String, Float, ForeignKey
from sqlalchemy.orm import relationship
from postgres_sql import Base

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    eventid = Column(String, nullable=True)

    date = Column(DateTime, nullable=True)
    corp = Column(String)
    target = Column(String)
    natlty = Column(String)
    natlty_txt = Column(String)

    nkill = Column(Integer, nullable=True)
    nwound = Column(Integer, nullable=True)
    number_of_casualties_calc = Column(Integer, nullable=True)  # new

    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)


    attack_type1 = Column(Integer, ForeignKey('attack_type.id'))
    attack_type2 = Column(Integer, ForeignKey('attack_type.id'))
    attack_type3 = Column(Integer, ForeignKey('attack_type.id'))

    target_type1 = Column(Integer, ForeignKey('target_type.id'))
    target_type2 = Column(Integer, ForeignKey('target_type.id'))
    target_type3 = Column(Integer, ForeignKey('target_type.id'))
    


    country_id = Column(Integer, ForeignKey('countries.id'))
    region_id = Column(Integer, ForeignKey('regions.id'))
    city_id = Column(Integer, ForeignKey('cities.id'))


    location = relationship("Eventlocation", back_populates="event", uselist=False)
    attack_type = relationship("AttackDetails", back_populates="event", uselist=False)
    target_type = relationship("TargetType", back_populates="event", uselist=False)
    perpetrators = relationship("Perpetrators", back_populates="event", uselist=False)
    casualties = relationship("Casualties", back_populates="event", uselist=False)






class Region(Base):
    __tablename__ = 'regions'

    id = Column(Integer, primary_key=True)
    region = Column(String, nullable=True)
    latitude = Column(Float, nullable=True)  # from api
    longitude = Column(Float, nullable=True)  # from api


class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True, )
    country = Column(String, nullable=True)
    country_txt = Column(String, nullable=True)
    latitude = Column(Float, nullable=True) #from api
    longitude = Column(Float, nullable=True) #from api
    region_id = Column(Integer, ForeignKey('regions.id'))

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    city = Column(String, nullable=True)
    latitude = Column(Float, nullable=True) # from api
    longitude = Column(Float, nullable=True) # from api
    country_id = Column(Integer, ForeignKey('countries.id'))

class EventLatLon(Base):
    id = Column(Integer, primary_key=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    event_id = Column(Integer, ForeignKey('events.id'))




class AttackType(Base):
    __tablename__ = 'attack_type'

    id = Column(Integer, primary_key=True)
    attacktype = Column(String, nullable=True)
    attacktype_txt = Column(String, nullable=True)



class TargetType(Base):
    __tablename__ = 'target_type'

    id = Column(Integer, primary_key=True)

    # Primary target
    targtype1 = Column(String, nullable=True)
    targtype1_txt = Column(String, nullable=True)
    targsubtype1 = Column(String)
    targsubtype1_txt = Column(String)
    corp1 = Column(String, nullable=True)
    target1 = Column(String, nullable=True)
    natlty1 = Column(String, nullable=True)
    natlty1_txt = Column(String, nullable=True)

    # Secondary and tertiary targets
    targtype = Column(String)
    targtype_txt = Column(String)
    targsubtype = Column(String)
    targsubtype_txt = Column(String)


    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship("Event", back_populates="target_type")


class Perpetrators(Base):
    __tablename__ = 'perpetrators'

    id = Column(Integer, primary_key=True)
    gname = Column(String, nullable=True)
    gsubname = Column(String)
    gname2 = Column(String)
    gsubname2 = Column(String)
    gname3 = Column(String)
    gsubname3 = Column(String)
    nperps = Column(Integer, nullable=True)

    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship("Event", back_populates="perpetrators")


class Casualties(Base):
    __tablename__ = 'casualties'

    id = Column(Integer, primary_key=True)
    nkill = Column(Integer, nullable=True)
    nkillter = Column(Integer, nullable=True)
    nwound = Column(Integer, nullable=True)
    nwoundte = Column(Integer, nullable=True)

    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship("Event", back_populates="casualties")