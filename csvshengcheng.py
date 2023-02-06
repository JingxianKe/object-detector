import csv
import os
import scipy.io as sio

anno_path = '/Users/mac/Downloads/caltech-101/Annotations/Airplanes_Side_2/'
annonames = os.listdir(anno_path)

with open('airplane.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for annoname in annonames:
        houzhui = annoname.split('_')[1]
        img_idx = houzhui.split('.')[0]
        imgname = 'image' + '_' + img_idx + '.jpg'

        new_path = anno_path + annoname
        mat_data = sio.loadmat(new_path)

        i = mat_data['box_coord'][0][0]
        j = mat_data['box_coord'][0][1]
        k = mat_data['box_coord'][0][2]
        l = mat_data['box_coord'][0][3]

        spamwriter.writerow([imgname] + [i] + [j] + [k] + [l] + ['airplane'])

