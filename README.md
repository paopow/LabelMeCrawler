# LabelMe Crawler
Last update: 23 November 2016

A crawler to download images and annotations from [LabelMe](http://labelme.csail.mit.edu/).


## Running the crawlers
1. Install required packages
    ```
    pip install -r requirements.txt
    ```
2. In ```\labelme```, run the crawler for annotations
    ```
    scrapy crawl annotations -o annotations.json
    ```
3. Run the crawler for images
    ```
    scrapy crawl images -o images.json
    ```
## Output
1. ```annotations.json``` lists all downloaded files. The filename on LabelMe is
in the 'filename' field and the corresponding local file path is in 'files'->'path'.
The field 'folder' states from which folder the original file is from.
2. Annotation files (.xml) are in ```annotations\```
3. ```images.json``` lists all downloaded files. The filename on LabelMe is
in the 'filename' field and the corresponding local file path is in 'images'->'path'.
The field 'folder' states from which folder the original file is from.
4. Image files are in ```images\```.


## Post-processing
To generate a mapping between images and annotations, run ```python cleanup.py```.
"Valid" annotation files and image files will be copied to ```labelme\results\```
and renamed to reflect the original files folder structure.
The mapping will be generated and saved as ```images_annotations.json```.

## Note
- The format of original LabelMe pages might change and affect the output of this code.
- The crawler only download images of width >= 500px and height >= 500px. To change this setting,
change the field ```IMAGES_MIN_HEIGHT``` and ```IMAGES_MIN_WIDTH``` in ```labelme\settings.py```.



