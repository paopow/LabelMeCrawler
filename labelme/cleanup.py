#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 21:07:13 2016

@author: paopow
"""
import json
import os
import shutil

TARGET_FOLDER = 'results'

def load_images():
    with open('images.json') as f:
        images = json.load(f)
    return images
    
def load_annotations():
    with open('annotations.json') as f:
        annotations = json.load(f)
    return annotations
    
def get_tuple_id(obj):   
    return obj['folder'][:-1] + '-' + obj['filename'].split('.')[0]

def create_dict(annotations, images):
    results = {}
    for a in annotations:
        if len(a['files']) > 0 and '.xml' in a['files'][0]['path']:             
            results[get_tuple_id(a)] = {
                'annotation': get_tuple_id(a) + '.xml',
                'image': None
            }
            shutil.copy2('annotations/' +a['files'][0]['path'], 
                         'results/' + get_tuple_id(a) + '.xml' )
      
    for i in images:
        if len(i['images']) > 0 and '.jpg' in i['images'][0]['path']:
            if get_tuple_id(i) in results:
                results[get_tuple_id(i)]['image'] = get_tuple_id(i) + '.jpg'
            else:
                results[get_tuple_id(i)] = {
                    'annotation': None,
                    'image': get_tuple_id(i) + '.jpg'
                }
            shutil.copy2('images/' +i['images'][0]['path'], 
                         'results/' + get_tuple_id(i) + '.jpg' )
    return results
    
def clean_data():
    if not os.path.exists(TARGET_FOLDER):
        os.makedirs(TARGET_FOLDER)
    images = load_images()
    annotations = load_annotations()
    image_dict = create_dict(annotations, images)
    with open('images_annotations.json','w') as f:
        json.dump(image_dict, f)


if __name__ == '__main__':
    clean_data()