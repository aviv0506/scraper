import os
from datetime import datetime
from save_flight import SaveFlight

class FlightManager:
    """
    This class is saving a new flight to Excel file.
    """
    DATA_PATH = "flight_data"

    def create_new_flights_table(self, flights):
        now = datetime.now()
        # dd/mm/YY H:M:S
        filename = now.strftime("%d%m%Y%H%M%S") + ".json"
        SaveFlight.save_flights(flights, os.path.join(FlightManager.DATA_PATH, filename))

    def get_flight_tables_files(self):
        table_files = [f for f in os.listdir(FlightManager.DATA_PATH) if
                       os.path.isfile(os.path.join(FlightManager.DATA_PATH, f))]

        return table_files

    def get_flight_table_count(self):
        return len(self.get_flight_tables_files())

    def search_flight_by_company(self, company_name):
        table_files = self.get_flight_tables_files()

        results = []
        for file in table_files:
            flight_list = SaveFlight.load_flights(os.path.join(FlightManager.DATA_PATH, file))
            results += [f for f in flight_list if f._company_name == company_name]

        return results
