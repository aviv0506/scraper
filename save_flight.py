import json
from flight import Flight

class SaveFlight:
    """
    This class is saving a new flight to Json file.
    """

    @staticmethod
    def save_flights(flights, filename):
        data = [f.to_dict() for f in flights]
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)

    @staticmethod
    def load_flights(filename):
        with open(filename) as outfile:
            data = json.load(outfile)
        data = [Flight.from_dict(f) for f in data]

        return data


