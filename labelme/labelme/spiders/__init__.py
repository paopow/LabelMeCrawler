# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy

ANNOTATION_URL = 'http://people.csail.mit.edu/brussell/research/LabelMe/Annotations/'
IMG_URL = 'http://people.csail.mit.edu/brussell/research/LabelMe/Images/'


class AnnotationSpider(scrapy.Spider):
    name = 'annotations'
    start_urls = [ANNOTATION_URL]

    def parse_annotation(self, response):
        pass

    def parse(self, response):
        pass


class ImageSpider(scrapy.Spider):
    name = 'images'
    start_urls = [IMG_URL]

    def parse_image(self, response):
        pass

    def parse(self, response):
        pass
