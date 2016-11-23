#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 21:07:13 2016

@author: paopow
"""
import json

def load_images():
    with open('images.json') as f:
        images = json.load(f)
    return images
    
def load_annotations():
    with open('annotations.json') as f:
        annotations = json.load(f)
    return annotations
    
def get_tuple_id(obj):
    return obj['folder'] + obj['filename'].split('.')[0]
    
def create_dict(annotations, images):
    all_dict = {}
    for a in annotations:
        if len(a['files']) > 0:
            all_dict[get_tuple_id(a)] = {
                'annotation_path': 'annotations/' + a['files'][0]['path'],
                'image_path': None
            }
    for i in images:
        id = get_tuple_id(i)
        if len(i['images']) > 0 and id in all_dict:
            all_dict[id]['image_path'] = 'images/' + i['images'][0]['path']
            #do sth
    return all_dict
        
    
def clean_data():
    images = load_images()
    annotations = load_annotations()
    image_dict = create_dict(annotations, images)
    with open('images_annotations.json','w') as f:
        json.dump(image_dict, f)


if __name__ == '__main__':
    clean_data()