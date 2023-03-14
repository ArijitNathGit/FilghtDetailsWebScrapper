from bs4 import BeautifulSoup
from IATA_Codes_Mapping import get_iata
from Scrape_Webpage import get_source

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

website = 'https://www.makemytrip.com/flight/search?itinerary={}-{}-{}&tripType=O&paxType=A-1_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng'


def get_schedules(flight_name, departure_location, arrival_location, date_today):
    departure_iata_code = get_iata(departure_location)
    arrival_iata_code = get_iata(arrival_location)

    website_formatted_url = website.format(departure_iata_code, arrival_iata_code, date_today)

    try:
        page_source = get_source(website_formatted_url)
        soup = BeautifulSoup(page_source, 'lxml')

        flights = soup.findAll('div', class_='makeFlex simpleow')

        for flight in flights:
            flight_identity = flight.find('p', 'boldFont blackText airlineName').text.strip()
            flight_layover_info = flight.find('div', 'flexOne').find('p', 'flightsLayoverInfo').text.strip()

            if flight_identity == flight_name and flight_layover_info == 'Non stop':
                flight_departure_time = flight.find('div', 'timeInfoLeft').find('p', 'flightTimeInfo').text.strip()
                flight_arrival_time = flight.find('div', 'timeInfoRight').find('p', 'flightTimeInfo').span.text.strip()

                flight_price = flight.find('div', 'priceSection').p.text.strip()

                print(f"Flight Name: {flight_identity}")
                print(f"Flight Departure Time: {flight_departure_time}")
                print(f"Flight Arrival Time: {flight_arrival_time}")
                print(f"Flight Layover Info: {flight_layover_info}")
                print(f"Flight Price: {flight_price}")
                print()

    except Exception as e:
        print(str(e))


