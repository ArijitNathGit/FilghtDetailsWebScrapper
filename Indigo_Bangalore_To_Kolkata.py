from IntraCountry_SingleFlight_Daily import get_schedules
import datetime
from dateutil.relativedelta import relativedelta



departure_location = 'Bangalore'
arrival_location = 'Kolkata'
flight_name = 'IndiGo'


if __name__ == '__main__':

    for i in range(0, 3):
        day = datetime.datetime.now() + relativedelta(days=i)
        date = day.strftime("%d/%m/%Y")

        print(f'Flight details for {date}\n')
        get_schedules(flight_name, departure_location, arrival_location, date)