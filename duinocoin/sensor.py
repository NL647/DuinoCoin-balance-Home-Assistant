import requests
from datetime import timedelta
from requests.exceptions import HTTPError
import voluptuous as vol

from homeassistant.components.sensor import PLATFORM_SCHEMA, SensorEntity
from homeassistant.const import ATTR_ATTRIBUTION, CONF_USERNAME, CONF_NAME
import homeassistant.helpers.config_validation as cv

ATTRIBUTION = "Data provided by wallet.duinocoin.com"
CONF_USERNAME = "username"
SCAN_INTERVAL = timedelta(minutes=30)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
    
        vol.Optional(CONF_USERNAME): cv.string,
        vol.Optional(CONF_NAME): cv.string
        
    }
)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the DUCO sensors."""
    username = config.get(CONF_USERNAME)
    name = "DUCO Balance"
   

    add_entities([DuinocoinscanSensor(name, username)], True)


class DuinocoinscanSensor(SensorEntity):
    """Representation of an duino sensor."""

    def __init__(self, name,username):
        """Initialize the sensor."""
        self._name = name
        self.username =  username
        self._state = None
        self._unit_of_measurement = "DUCO"    

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement this sensor expresses itself in."""
        return self._unit_of_measurement

    @property
    def extra_state_attributes(self):
        """Return the state attributes of the sensor."""
        return {ATTR_ATTRIBUTION: ATTRIBUTION}

    def update(self):
        """Get the latest state of the sensor."""
            
        query = self.username           
        try:
            response = requests.get('https://server.duinocoin.com/balances/%s' %query)
            response.raise_for_status()
            # access JSOn content
            data = response.json()
            myBalance= str(round(data['result']['balance'], 2))
           #print("\n Duino Balance", myBalance)
            self._state = myBalance

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
