# src/database.py
from sqlalchemy import create_engine, Column, String, Float, Boolean, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = "postgresql://user:password@postgres:5432/case_study"  # Docker içinden erişim için

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class CampgroundDB(Base):
    __tablename__ = "campgrounds"

    id = Column(String, primary_key=True)
    type = Column(String)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    region_name = Column(String)
    administrative_area = Column(String)
    nearest_city_name = Column(String)
    accommodation_type_names = Column(String)  # JSON olarak kaydedilecek
    bookable = Column(Boolean)
    camper_types = Column(String)  # JSON
    operator = Column(String)
    photo_url = Column(String)
    photo_urls = Column(String)  # JSON
    photos_count = Column(Integer)
    rating = Column(Float)
    reviews_count = Column(Integer)
    slug = Column(String)
    price_low = Column(Float)
    price_high = Column(Float)
    availability_updated_at = Column(DateTime)

Base.metadata.create_all(bind=engine)