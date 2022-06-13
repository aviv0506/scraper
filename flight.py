
class Flight:
    """This class represent flight. """

    company_name: str
    terminal: int

    def __init__(self, company_name, flight_number, from_country, terminal,
                               expected_time, updated_time, status):
        self._company_name = company_name
        self._flight_number = flight_number
        self._from_country = from_country
        self._expected_time = expected_time
        self._updated_time = updated_time
        self._status = status
        self._terminal = terminal

    @classmethod
    def from_dict(cls, dict):
        return cls(dict["company_name"],
                   dict["flight_number"],
                   dict["from_country"],
                   dict["terminal"],
                   dict["expected_time"],
                   dict["updated_time"],
                   dict["status"])

    def to_dict(self):
        return {"company_name": self._company_name,
                "flight_number": self._flight_number,
                "from_country": self._from_country,
                "terminal": self._terminal,
                "expected_time": self._expected_time,
                "updated_time": self._updated_time,
                "status": self._status
                }

    def __str__(self):
        return str(self.to_dict())