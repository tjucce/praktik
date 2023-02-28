import requests
from csv import writer, reader
from turfpy.random import random_points
from images import get_images_csv


def get_coordinates(count, points):  # left: lng, bottom: lat, right: lng, top: lat

    points = random_points(count=count, bbox=points)

    for i in range(count):
        coordinates = points['features'][i]['geometry']['coordinates']
        print(coordinates[1], coordinates[0])
        write_to_csv(coordinates[1], coordinates[0])
    # get_images_csv()


def write_to_csv(lat, lng):
    with open('coordinates.csv', 'a', newline='') as coo:
        writer_object = writer(coo)
        print(lat, lng)
        if street_view(lat, lng):
            lat, lng = get_valid_coordinates(lat, lng)
            print(lat, lng)
            writer_object.writerow([f'{lat}, {lng}'])
            # get_images(lat, lng)
            print('Written to csv and downloaded street view image')
        else:
            print('No image for that point')


def read_from_csv():
    with open('coordinates.csv', 'r') as coo:
        csvreader = reader(coo)
        for row in csvreader:
            if not row:
                pass
            else:
                print(row)
                print(row[0], row[1])


def street_view(lat, lng):
    meta_base = 'https://maps.googleapis.com/maps/api/streetview/metadata?'
    api_key = 'AIzaSyALl6syoF6aqdiA1p5QOeLoE7ERAXT5zjA'
    location = f'{lat},{lng}'
    meta_params = {'key': api_key,
                   'location': location}
    meta_response = requests.get(meta_base, params=meta_params)
    status = meta_response.json()['status']
    if status == 'OK':
        print('status:', status)
        return True
    else:
        print(status)
        return False


def get_valid_coordinates(lat, lng):
    meta_base = 'https://maps.googleapis.com/maps/api/streetview/metadata?'
    api_key = 'AIzaSyALl6syoF6aqdiA1p5QOeLoE7ERAXT5zjA'
    location = f'{lat},{lng}'
    meta_params = {'key': api_key,
                   'location': location}
    meta_response = requests.get(meta_base, params=meta_params)
    lat = meta_response.json()['location']['lat']
    lng = meta_response.json()['location']['lng']
    return lat, lng


if __name__ == '__main__':
    get_coordinates(100, [10.332824, 60.248179, 10.429307, 60.529599])
    # read_from_csv()
    # street_view(57.637573, 12.251197)
    # write_to_csv(57.635874, 12.252072)
