# LabelMe Crawler
Last update: 17 November 2016

A crawler to download images and annotations from LabelMe.

Note:
The format of original LabelMe pages might change and affect the output of this code.

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

The annotations will be saved to ```annotations\```. The images will be saved to ```images\```
