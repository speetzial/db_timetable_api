
# DB Timetable API

Simple access to the Deutsche Bahn timetable API
## Installation

Windows:
```bash
  pip install db-timetable-api
```

Unix:
```bash
  pip3 install db-timetable-api
```
## Usage/Examples

### Load package and enter API key
```python
from db_timetable_api import timetable

db = timetable.timetable_api(clientid=<YOUR_CLIENT_ID>, clientsecret=<YOUR_CLIENT_SECRET>)
```
To get an API key you have to register at https://developers.deutschebahn.com/, create an application and subscribe to the free Timetables API in the API catalog

### Get information about the station using the station name
```python
db.get_station(<STATION_NAME>)

### EXAMPLE ###
db.get_station("Berlin Hbf")
```
This public interface allows access to information about a station.



### Returns planned data for a specified station within an hourly time slice
```python
db.get_timetable(<STATIONS EVA ID>, <DATE YYYY-MM-DD>, <HOUR HH>)

### EXAMPLE ###
db.get_timetable("8011160", "2023-10-31", "12")
```
Returns a Timetable object (see Timetable) that contains planned data for the specified station (evaNo) within the hourly time slice given by date and hour. The data includes stops for all trips that arrive or depart within that slice. There is a small overlap between slices since some trips arrive in one slice and depart in another.

Planned data does never contain messages. On event level, planned data contains the 'plannned' attributes pt, pp, ps and ppth while the 'changed' attributes ct, cp, cs and cpth are absent.

Planned data is generated many hours in advance and is static, i.e. it does never change. It should be cached by web caches.public interface allows access to information about a station.

### Returns all known changes for a station
```python
db.get_changes(<STATIONS EVA ID>)

### EXAMPLE ###
db.get_changes("8011160")
```
Returns a Timetable object (see Timetable) that contains all known changes for the station given by evaNo.

The data includes all known changes from now on until ndefinitely into the future. Once changes become obsolete (because their trip departs from the station) they are removed from this resource.

Changes may include messages. On event level, they usually contain one or more of the 'changed' attributes ct, cp, cs or cpth. Changes may also include 'planned' attributes if there is no associated planned data for the change (e.g. an unplanned stop or trip).


### Returns all recent changes for a station
```python
db.get_recent_changes(<STATIONS EVA ID>)

### EXAMPLE ###
db.get_recent_changes("8011160")
```
Returns a Timetable object (see Timetable) that contains all recent changes for the station given by evaNo. Recent changes are always a subset of the full changes. They may equal full changes but are typically much smaller. Data includes only those changes that became known within the last 2 minutes.

A client that updates its state in intervals of less than 2 minutes should load full changes initially and then proceed to periodically load only the recent changes in order to save bandwidth.