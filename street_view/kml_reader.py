# from bs4 import BeautifulSoup
#
# # Reading the data inside the xml
# # file to a variable under the name
# # data
# with open('test_route.kml', 'r') as f:
#     data = f.read()
#
# # Passing the stored data inside
# # the beautifulsoup parser, storing
# # the returned object
# Bs_data = BeautifulSoup(data, "kml")
#
# # Finding all instances of tag
# # `unique`
# b_unique = Bs_data.find_all('coordinates')
#
# print(b_unique)
import csv
from pykml import parser


def reading_kml_from_google():
    kml_file = 'test_route.kml'
    with open(kml_file) as f:
        doc = parser.parse(f)
        root = doc.getroot()
        coords = root.Document.Placemark.LineString.coordinates.text
        # print(coords)
        coords = coords.replace(' ', '')
        print(type(coords))
        coords = coords.split(',')
        print(coords)
        coords = [s.strip('\n') for s in coords]
        coords = [s.strip('0\n') for s in coords]
        print(coords)
        lat = coords[1::2]
        lng = coords[::2]

        print(lat)
        print(lng)
        print(lat[0])
        lng = lng[:-1]
        result = [None] * (len(lat) + len(lng))
        result[::2] = lat
        result[1::2] = lng
        _result = zip(lat, lng)

        print(result)
        print(_result)
        test = []
        for i in _result:
            test.append('{},{}'.format(i[0], i[1]))
        print('working', test)
        with open('books.csv', mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in test:
                csv_writer.writerow([row])
        #     for row in lng:
        #         csv_writer.writerow([row])
        #     print('hello')
    # print(root.Document.Placemark.Point.coordinates)


def write_to_csv():
    data_to_save = ['57.66577', '57.66549', '57.66519']
    _data_to_save = ['12.89214', '12.89188', '12.89166']
    # with open('test.csv', mode='w', newline='') as csv_file:
    #     csv_writer = csv.writer(csv_file)
    #     for row in data_to_save:
    #         for rows in _data_to_save:
    #             test = row + ',' + rows
    #             print(test)
                # csv_writer.writerow([row])
                # csv_writer.writerow(row)
    c = zip(data_to_save, _data_to_save)
    with open('devicelist.txt', 'w') as out_file:
        for i in c:
            out_file.write('{},{} \n'.format(i[0], i[1]))


if __name__ == '__main__':
    # write_to_csv()
    reading_kml_from_google()
