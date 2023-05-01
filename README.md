# Surfs Up!
<p align="center">
  <img src="https://github.com/ericyang91/SQLAlchemy_Challenge/blob/main/Resources/main.jpg" alt="main"/>
</p>

## About:

  The purpose of this project is to do a climate analysis on Honolulu, Hawaii. Variables that are observed include but are not limited to "date", "precipitation", "station", and "temperatures." The first part of the project analyzes the precipitation amount by date as well as the lowest, highest, and average temperatures in Hawaii measured for 12 months by the most active climate station. The second part of the project designs a Flask API based on the observations from the first part of the project.

## Precipitation Analysis:

The previous 12 months of precipitation data from the most recent date in the dataset:
</br></br>
<p align="center">
  <img src="https://github.com/ericyang91/SQLAlchemy_Challenge/blob/main/Resources/precip.jpg" alt="precip"/>
</p>
</br>

## Station Analysis:
</br>
- The most active station based on the number of observations: USC00519281</br>
- Lowest, highest, and average temperatures that filters on the most active station: 54.0, 85.0, 71.7</br>
- Histogram showing the most active station's number of observations for a range of temperatures for a 12-month period.
</br>
</br>
<p align="center">
  <img src="https://github.com/ericyang91/SQLAlchemy_Challenge/blob/main/Resources/obs.jpg" alt="obs"/>
</p>
</br>

## How to Use the Climate App:
</br>
1) Run app.py and enter the command "python -m flask run" inside the correct directory.</br></br>
2) Choose from the different routes:</br></br>
-  "/api/v1.0/precipitation": Returns jsonified precipitation data for the final year in the database<br/> 
-  "/api/v1.0/stations": Returns jsonified data of all the stations in the database<br/>
-  "/api/v1.0/tobs": Returns the jsonified data of the past year from the most active station<br/>
-  "/api/v1.0/start/<start>": Enter a start date YYYY-MM-DD. Returns the date, min, avg, and max temperatures calculated from the given date to the end of the dataset<br/>
-  "/api/v1.0/start_end/<start>/<end>": Enter a start and an end date YYYY-MM-DD. Returns the date, min, avg, and max temperatures calculated from the given start date to the given end date<br/></br>
3) Enjoy!


</br>
</br>

## Languages and Libraries:
[![Python](https://img.shields.io/badge/python-v3.10-blue)](https://www.python.org/downloads/release/python-310/)
[![Pandas](https://img.shields.io/badge/pandas-v1.3.3-blue)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/numpy-v1.21.4-blue)](https://numpy.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-v1.4.25-blue)](https://www.sqlalchemy.org/)
[![datetime](https://img.shields.io/badge/datetime-library-green)](https://docs.python.org/3/library/datetime.html)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-v3.5.1-red)](https://matplotlib.org/)
[![SQLite](https://img.shields.io/badge/SQLite-v3.36.0-blue)](https://www.sqlite.org/index.html)
