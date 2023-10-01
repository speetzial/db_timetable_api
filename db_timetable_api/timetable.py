import requests
import xml.etree.ElementTree as ET
from datetime import datetime

class timetable_api:
    
    def __init__(self, clientid: str, clientsecret: str):
        """
        The function initializes the headers and payload for making API requests with a client ID and client
        secret.
        
        :param clientid: The `clientid` parameter is the ID of the client that is making the API request. It
        is typically a unique identifier assigned to each client by the API provider
        :param clientsecret: The `clientsecret` parameter is a secret key or password that is used for
        authentication and authorization purposes. It is typically provided by the service or API that you
        are interacting with. In this case, it is used as the value for the `'DB-Api-Key'` header in the
        `self
        """
        self.headers = {
        'DB-Client-Id': clientid,
        'DB-Api-Key': clientsecret
        }
        self.payload = {}


    def get_station(self, stationame: str):
        """
        The `get_station` function sends a GET request to the Deutsche Bahn API to retrieve information
        about a specific train station and returns the response as a dictionary.
        
        :param stationame: The `stationame` parameter is the name of the station for which you want to
        retrieve information
        :return: The function `get_station` returns a dictionary `dct` containing information about a train
        station. Each key in the dictionary represents a tag in the XML response, and the corresponding
        value is a dictionary containing the attributes of that tag.
        """
        url = f"https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/station/{stationame}"
        response = requests.request("GET", url, headers=self.headers, data=self.payload)
        root = ET.fromstring(response.text)
        dct = {}
        for child in root:
            child_dct = {}
            for key, value in child.attrib.items():
                child_dct[key] = value
            dct[child.tag] = child_dct
        return dct
    
    def get_timetable(self, eva: str, date: str, hour: str):
        """
        The `get_timetable` function retrieves train timetable information for a specific station, date, and
        hour using the Deutsche Bahn API.
        
        :param eva: The parameter "eva" is a code that represents a specific train station. It is used to
        identify the station for which you want to retrieve the timetable
        :param date: The date parameter is a string representing a date in the format 'YYYY-MM-DD'
        :param hour: The `hour` parameter is a string representing the hour of the day in 24-hour format.
        For example, if you want to get the timetable for 9 AM, you would pass "09" as the `hour` parameter
        :return: The function `get_timetable` returns a dictionary containing the station name and a list of
        train information. Each train information is represented as a dictionary with keys "id", "tl", "ar",
        and "dp". The values for "id", "tl", "ar", and "dp" are obtained from the XML response.
        """
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        dbdate = str(date_obj.strftime('%y%m%d'))
        dbhour = str(hour.zfill(2))
        url = f"https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/plan/{eva}/{dbdate}/{dbhour}"
        response = requests.request("GET", url, headers=self.headers, data=self.payload)
        root = ET.fromstring(response.text)
        data = {"station": root.attrib["station"], "trains": []}
        for s in root.findall('s'):
            train = {"id": s.attrib["id"]}
            tl = s.find('tl')
            train["tl"] = tl.attrib
            ar = s.find('ar')
            if ar is not None:
                train["ar"] = ar.attrib
            dp = s.find('dp')
            if dp is not None:
                train["dp"] = dp.attrib
            data["trains"].append(train)
        return data
    

    def get_changes(self, eva: str):
        """
        The `get_changes` function retrieves timetable changes for a given train station using the Deutsche
        Bahn API and returns the changes in a dictionary format.
        
        :param eva: The parameter "eva" is a code that represents a specific train station. It is used to
        retrieve timetable information for that particular station
        :return: a dictionary that represents the XML response from the API.
        """
        def xml_to_dict(element):
            dictionary = {}
            for key in element.attrib:
                dictionary[key] = element.attrib[key]
            for child in element:
                dictionary[child.tag] = dictionary.get(child.tag, [])
                dictionary[child.tag].append(xml_to_dict(child))
            if not dictionary:
                return element.text or None
            return dictionary
        url = f"https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/fchg/{eva}"
        response = requests.request("GET", url, headers=self.headers, data=self.payload)
        root = ET.fromstring(response.text)
        result_dict = xml_to_dict(root)
        return result_dict
    

    def get_recent_changes(self, eva: str):
        """
        The `get_recent_changes` function retrieves recent changes for a given EVA
        (Eisenbahn-Verkehrsunternehmen) code from the Deutsche Bahn API and returns the result as a
        dictionary.
        
        :param eva: The parameter "eva" is a code that represents a specific train station. It is used to
        retrieve recent changes or updates related to the train timetable for that particular station
        :return: a dictionary that represents the recent changes for a given EVA
        (Eisenbahn-Verkehrsunternehmen) code.
        """
        def xml_to_dict(element):
            dictionary = {}
            for key in element.attrib:
                dictionary[key] = element.attrib[key]
            for child in element:
                dictionary[child.tag] = dictionary.get(child.tag, [])
                dictionary[child.tag].append(xml_to_dict(child))
            if not dictionary:
                return element.text or None
            return dictionary
        url = f"https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/rchg/{eva}"
        response = requests.request("GET", url, headers=self.headers, data=self.payload)
        root = ET.fromstring(response.text)
        result_dict = xml_to_dict(root)
        return result_dict