# Import Dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func

from flask import Flask, jsonify
import datetime as dt 
import pandas as pd 

# Database Setup
engine=create_engine('sqlite:///hawaii.sqlite')

# declare a Base using 'automap_base()'
Base=automap_base()

#use the Base class to reflect the database tables
Base.prepare(engine, reflect=True)

# Assign the station class to a variable called 'Station'
Station=Base.classes.station

#Assign the measurement class to a variable called 'Measurement'
Measurement=Base.classes.measurement

#Create a session
session=Session(engine)

#Flask Setup
app=Flask(__name__)

#add Flask Routes
## http://localhost:5000/
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )
 


#http://localhost:5000/api/v1.0/precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Query for the dates and temperature observations from the last year.
    Convert the query results to a Dictionary using date as the key and tobs as the value.
    Return the JSON representation of your dictionary."""

    query_date=dt.date.today()-dt.timedelta(days=365)
    #if we need the whole year of observation (starting from the latest date in our db)
    #uncomment the block of the code below:
    
    #ldate=session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    #l=ldate[0]
    #latest_date=pd.to_datetime(l).date()
    #query_date =latest_date-dt.timedelta(days=365)

    date_prcp=(session.query(Measurement.date,Measurement.prcp)
        .filter(Measurement.date>=query_date).all())
    dict_prcp=dict(date_prcp)
    return jsonify(dict_prcp)
    
#http://localhost:5000/api/v1.0/stations
@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations from the dataset."""
    station_list=session.query(Station.station).all()
    # Convert list of tuples into normal list
    new_station = [row[0] for row in station_list]
    return jsonify(new_station)

#http://localhost:5000/api/v1.0/tobs
@app.route("/api/v1.0/tobs")
def tobs():
    """Return a JSON list of Temperature Observations (tobs) for the previous year
    for station with the highest number of observations, 'USC00519281'."""
    query_date=dt.date.today()-dt.timedelta(days=365) 
    #if we need the whole year of observation (starting from the latest date in our db)
    #uncomment the block of the code below:
    
    #ldate=session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    #l=ldate[0]
    #latest_date=pd.to_datetime(l).date()
    #query_date =latest_date-dt.timedelta(days=365)

    tobs_list=(session.query(Measurement.tobs).filter(Measurement.station=='USC00519281')
    .filter(Measurement.date>=query_date).all())                 
    new_tobs= [row[0] for row in tobs_list]
    return jsonify(new_tobs)


if __name__=='main':
    app.run(debug=True)