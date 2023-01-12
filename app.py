import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import datetime as dt
from datetime import datetime
from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(autoload_with = engine)

measurement = Base.classes.measurement
station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def home():
    print("List all the available routes.")
    return (
        "Welcome to the Climate page!<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/start/<start><br/>"
        "/api/v1.0/start_end/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Convert the last 12 months of precipitation data to a dictionary.")
    session = Session(engine)

    data = engine.execute('select * from measurement').fetchall()

    recent_date = []
    for list in data:  
        recent_date.append(list[2])

    most_recent_date = max(recent_date)
    datetime_most_recent_date = dt.datetime.strptime(most_recent_date, '%Y-%m-%d')
    datetime_one_year_ago = datetime_most_recent_date - dt.timedelta(days=365)
    one_year_ago = datetime_one_year_ago.strftime('%Y-%m-%d')
    scores = session.query(measurement.date, measurement.prcp).\
        filter((measurement.date <= most_recent_date) & (measurement.date >= one_year_ago)).all()

    session.close()

    dictionary_precipitation = []
    for date, precip in scores:
        precipitation_dic = {}
        precipitation_dic[date] = precip
        dictionary_precipitation.append(precipitation_dic)
         
    return jsonify(dictionary_precipitation)

@app.route("/api/v1.0/stations")
def stations():
    print("Return jasonified data of all the stations in the database.")
    session = Session(engine)

    all_stations = session.query(station.station, station.name).\
        all()
    session.close()

    list_station = []
    for query in all_stations:
        json_stations = {}
        json_stations["station"] = query[0]
        json_stations["name"] = query[1]
        list_station.append(json_stations)

    return jsonify(list_station)


@app.route("/api/v1.0/tobs")
def tobs():
    print("Query the dates and temperatures of the most active station for the past year")
    session = Session(engine)

    active_stations = session.query(measurement.station, func.count(measurement.date)).\
    group_by(measurement.station).order_by(func.count(measurement.date).desc()).all()

    active_recent = session.query(func.max(measurement.date)).\
    filter(measurement.station == active_stations[0][0]).first()

    active_recent_date = active_recent[0]

    dt_active_recent = dt.datetime.strptime(active_recent_date, '%Y-%m-%d')
    dt_active_past = dt_active_recent - dt.timedelta(days = 365)

    active_past_date = dt.datetime.strftime(dt_active_past, '%Y-%m-%d')

    past_year = session.query(measurement.date, measurement.tobs).\
        filter(measurement.station == active_stations[0][0]).\
        filter((measurement.date >= active_past_date) & (measurement.date <= active_recent_date)).all()

    session.close()

    new_list = []
    for date, temperature in past_year:
        dict_past_year = {}
        dict_past_year[date] = temperature
        new_list.append(dict_past_year)

    return jsonify(new_list)


@app.route("/api/v1.0/start/<start>")
def start(start):
    print("Returns a list of min, avg, and max temperatures for a specified start date to the end of the dataset inclusive")
    session = Session(engine)

    start_datetime = dt.datetime.strptime(start, "%Y-%m-%d")

    start_query = session.query(measurement.date, func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
        filter(measurement.date >= start_datetime).all()

    session.close()

    start_list = []
    for query in start_query:
        start_dict = {}
        start_dict["Date"] = query[0]
        start_dict["Temp_Min"] = query[1]
        start_dict["Temp_Avg"] = query[2]
        start_dict["Temp_Max"] = query[3]
        start_list.append(start_dict)

    return jsonify(start_list)


@app.route("/api/v1.0/start_end/<start>/<end>")
def start_end(start, end):
    print("Returns the min, avg, and max temperatures for a specified start date to a specified end date inclusive")
    session = Session(engine)

    start_datetime = dt.datetime.strptime(start, '%Y-%m-%d')
    end_datetime = dt.datetime.strptime(end, '%Y-%m-%d')

    start_end_query = session.query(measurement.date, func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
        filter((measurement.date >= start_datetime) & (measurement.date <= end_datetime)).all()

    session.close()

    start_end_list = []
    for query in start_end_query:
        start_end_dict = {}
        start_end_dict["Date"] = query[0]
        start_end_dict["Temp_Min"] = query[1]
        start_end_dict["Temp_Avg"] = query[2]
        start_end_dict["Temp_Max"] = query[3]
        start_end_list.append(start_end_dict)

    return jsonify(start_end_list)


if __name__ == "__main__":
    app.run
