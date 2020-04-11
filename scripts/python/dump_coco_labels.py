# Copyright 2018-202 Amikelive. All rights reserved
#
# Licensed under the MIT License found in the LICENSE file in the root directory of this source tree
'''
This script downloads COCO dataset annotations archive file and will dump the labels to stdout
'''

import os
import sys
import getopt
import ijson
import wget

from zipfile import ZipFile


def download_url(year):
    '''
    Obtain the download URL for the annotations based on the dataset release year
    '''
    if year == '2014':
        url = 'http://images.cocodataset.org/annotations/annotations_trainval2014.zip'
    elif year == '2017':
        url = 'http://images.cocodataset.org/annotations/annotations_trainval2017.zip'
    else:
        raise ValueError('Invalid argument for year')
    return url


def json_file_path(year, basedir='/tmp'):
    '''
    Check if the JSON file exists in the designated directory
    '''
    if year == '2014':
        return os.path.join(basedir,'annotations','instances_val2014.json')
    elif year == '2017':
        return os.path.join(basedir,'annotations','instances_val2017.json')
    else:
        return None


def extract_annotations(year, target_dir='/tmp'):
    '''
    Extract the annotation zip file based on the dataset release year
    '''
    print('Downloading and extracting COCO annotations file')

    try:
        url = download_url(year)
        dest_zip_file = os.path.join(target_dir, year + '.zip')
        wget.download(url,dest_zip_file)

        with ZipFile(dest_zip_file, 'r') as zip_archive:
            zip_archive.extractall(target_dir)

    except ValueError:
        print('Invalid value supplied to argument')

    except:
        print('Failed to extract zipped annotations')
        raise


def show_help():
    print('python dump_coco_labels.py -y <year>')


def main(argv):
    json_file = None
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hy:",["help","year="])
    except getopt.GetoptError:
        show_help()
        sys.exit(1)

    year = None

    for opt, arg in opts:
        if opt == '-h':
            show_help()
            sys.exit()

        elif opt == '-y':
            if arg == '2014':
                year = arg
            elif arg == '2017':
                year = arg

    if year is not None:
        json_file = json_file_path(year)
    else:
        print('Invalid release year. Only 2014 and 2017 are supported')
        sys.exit(1)

    if json_file is not None:
        if not os.path.isfile(json_file):
            extract_annotations(year)

        fd = open(json_file,'r')
        objs = ijson.items(fd, 'categories.item')
        labels = (o for o in objs)
        count = 0
        for label in labels:
            print('id:{}, category:{}, super category:{}'.format(label['id'], label['name'], label['supercategory']))
            count += 1
        print('Total categories/labels: ', count)


if __name__ == "__main__":
    main(sys.argv[1:])