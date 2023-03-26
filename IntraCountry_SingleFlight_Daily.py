import csv

from bs4 import BeautifulSoup
from IATA_Codes_Mapping import get_iata
from Scrape_Webpage import get_source

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

website = 'https://www.makemytrip.com/flight/search?itinerary={}-{}-{}&tripType=O&paxType=A-1_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng'

flight_dictionary = {}


def get_schedules(flight_name, departure_location, arrival_location, date_iteration, route_name, date_today):
    departure_iata_code = get_iata(departure_location)
    arrival_iata_code = get_iata(arrival_location)

    date_iteration_formatted = date_iteration.strftime("%d/%m/%Y")

    website_formatted_url = website.format(departure_iata_code, arrival_iata_code, date_iteration_formatted)

    try:
        page_source = get_source(website_formatted_url)
        soup = BeautifulSoup(page_source, 'lxml')

        flights = soup.findAll('div', class_='makeFlex simpleow')

        file_name = 'FlightData_{}_{}_{}_{}.csv'.format(flight_name, route_name, date_today,
                                                        date_iteration.strftime("%d-%m-%Y"));
        file_header = ['flight_name', 'job_date', 'flight_iteration_date', 'flight_number', 'flight_departure_time',
                       'flight_layover_info', 'flight_time', 'flight_price']
        file_path = 'D:\Web Scrapper\Python\WebScrapperProject\FlightDetails\{}'.format(file_name)

        file = open(file_path, 'w', encoding="utf-8", newline='')
        writer = csv.writer(file)
        writer.writerow(file_header)

        for flight in flights:
            flight_identity = flight.find('p', 'boldFont blackText airlineName').text.strip()
            flight_layover_info = flight.find('div', 'flexOne').find('p', 'flightsLayoverInfo').text.strip()

            if flight_identity == flight_name and flight_layover_info == 'Non stop':
                flight_departure_time = flight.find('div', 'timeInfoLeft').find('p', 'flightTimeInfo').text.strip()
                flight_total_time = flight.find('div', 'stop-info flexOne').p.text.strip()
                flight_arrival_time = flight.find('div', 'timeInfoRight').find('p', 'flightTimeInfo').span.text.strip()
                flight_price = flight.find('div', 'priceSection').p.text.strip()
                flight_number = flight.find('p', 'fliCode').text.strip()

                print(f"Flight Name: {flight_identity}")
                print(f"Flight Departure Time: {flight_departure_time}")
                print(f"Flight Arrival Time: {flight_arrival_time}")
                print(f"Flight Layover Info: {flight_layover_info}")
                print(f"Flight Price: {flight_price}")
                print(f"Flight Number: {flight_number}")
                print(f"Flight Total Time: {flight_total_time}")

                file_row = [
                    flight_name, date_today, date_iteration_formatted, flight_number,
                    flight_departure_time, flight_layover_info, flight_total_time, flight_price[2:].replace(",", "")
                ]

                writer.writerow(file_row)

                print()

        file.close()

    except Exception as e:
        print(str(e))
