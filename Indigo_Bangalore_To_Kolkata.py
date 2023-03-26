from IntraCountry_SingleFlight_Daily import get_schedules
import datetime
from dateutil.relativedelta import relativedelta

departure_location = 'Bangalore'
arrival_location = 'Kolkata'
flight_name = 'IndiGo'
route_name = 'BLR-CCU'

if __name__ == '__main__':

    date_today = datetime.datetime.now()
    for i in range(0, 3):
        date = date_today + relativedelta(days=i)

        print(f'Flight details for {date}\n')
        get_schedules(flight_name, departure_location, arrival_location, date, route_name, date_today.strftime("%d-%m-%Y"))
