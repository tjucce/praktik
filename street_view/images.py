import requests
import csv
import os


def get_coordinates():  # format. 57.65813,12.88897
    with open("./books.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)
            print(row[1], row[0])
            get_images(row[0], row[1])


def _get_coordinates():  # format. 12.88897,57.65813,0
    with open("./books.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)
            print(row[1], row[0])
            get_images(row[1], row[0])


def get_images(lat, lng):
    # Define the API endpoint and API key
    endpoint = 'https://maps.googleapis.com/maps/api/streetview?'
    api_key = 'AIzaSyALl6syoF6aqdiA1p5QOeLoE7ERAXT5zjA'

    # Define the latitude, longitude coordinates and image size
    lat = lat
    lng = lng
    heading = 0
    size = '456x456'

    # Do a for loop 4 times to get a picture from every direction, heading=0,90,180,270
    for i in range(4):
        image_name = f'{lat},{lng}hd={heading}.jpg'
        # Send a request to the API endpoint with the given parameters
        response = requests.get(f'{endpoint}location={lat},{lng}&size={size}&heading={heading}&key={api_key}')
        # Check the response status code
        if response.status_code == 200:
            # Save the image to a file
            with open(os.path.join('C:/projekt/praktik/street_view/', image_name), 'wb') as f:
                f.write(response.content)
                print('Street View image saved')
        else:
            # Print an error message if the request failed
            print(f'Error: {response.status_code}')

        heading += 90


def get_images_csv():
    with open('coordinates.csv') as coo:
        csvreader = csv.reader(coo, delimiter=',')
        for row in csvreader:
            print(row)
            try:
                print(row[0], row[1])
                get_images(row[0], row[1])
            except IndexError:
                pass


if __name__ == '__main__':
    # get_coordinates()
    # get_images(57.6375709, 12.2518)
    get_images_csv()
