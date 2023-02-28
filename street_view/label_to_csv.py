from PIL import Image
import os
from csv import writer, reader


def label_images():
    with open('coordinates.csv', 'r') as coo:
        csvreader = reader(coo)
        for row in csvreader:
            lat = row[0]
            lng = row[1]
            lng = lng.replace(';', '')
            image = f'{lat},{lng}'
            print(image)
            path = 'C:/projekt/praktik/street_view/'
            north = f'{image}hd=0.jpg'
            if os.path.exists(f'{path}{north}'):
                img = Image.open(north)
                img.show()
                print('North')
                move_image(north)
            east = f'{image}hd=90.jpg'
            if os.path.exists(f'{path}{east}'):
                img = Image.open(east)
                img.show()
                print('East')
                move_image(east)
            south = f'{image}hd=180.jpg'
            if os.path.exists(f'{path}{south}'):
                img = Image.open(south)
                img.show()
                print('South')
                move_image(south)
            west = f'{image}hd=270.jpg'
            if os.path.exists(f'{path}{west}'):
                img = Image.open(west)
                img.show()
                print('West')
                move_image(west)
            os.system("taskkill /f /im  Microsoft.Photos.exe")


def tag_coordinate(lat, lng):
    pass
    with open('image_tags.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        img_label = []
        # tag = prediction
        img_label.append(f'{lat},{lng},{tag}')
        writer_object.writerows([img_label])


def move_image(image):
    running = True
    while running:
        label = input('Label: ')
        if label == 'fo':
            label = 'forest'
        elif label == 'fi':
            label = 'field'
        elif label == 'co':
            label = 'coast'
        elif label == 'ci':
            label = 'city'
        elif label == 'm':
            label = 'mountain'
        old_path = f'C:/projekt/praktik/street_view/{image}'
        new_path = f'C:/projekt/praktik/street_view/train_data/{label}/{image}'
        if os.path.exists(f'C:/projekt/praktik/street_view/train_data/{label}'):
            os.replace(old_path, new_path)
            print('File moved')
            running = False
        else:
            print('No such directory')


if __name__ == '__main__':
    label_images()
    # move_image('57.6375709!12.2518hd=90.jpg', 'field')
    # move_image('59.4981150038661, 8.619506661063017hd=0.jpg')
