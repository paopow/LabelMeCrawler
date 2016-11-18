# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy

ANNOTATION_URL = 'http://people.csail.mit.edu/brussell/research/LabelMe/Annotations/'
IMG_URL = 'http://people.csail.mit.edu/brussell/research/LabelMe/Images/'
ROOT_PATH = '/brussell/research/LabelMe/'

class AnnotationSpider(scrapy.Spider):
    name = 'annotations'
    start_urls = [ANNOTATION_URL]

    def parse_annotation(self, response):
        file_names = response.css('tr td:nth-child(2) a::attr(href)')
        for f in file_names:
            file_name = f.extract()
            file_path = response.urljoin(file_name)
            yield {
                'filename': file_name,
                'folder': response.meta['folder'],
                'file_urls': [file_path]
            }

    def parse(self, response):
        urls = response.css('tr td:nth-child(2) a::attr(href)')
        for u in urls:
            url = u.extract()

            if ROOT_PATH not in url:
                next_page = response.urljoin(url)
                request = scrapy.Request(next_page, callback=self.parse_annotation)
                request.meta['folder'] = url
                yield request


class ImageSpider(scrapy.Spider):
    name = 'images'
    start_urls = [IMG_URL]

    def parse_image(self, response):
        file_names = response.css('tr td:nth-child(2) a::attr(href)')
        for f in file_names:
            file_name = f.extract()
            file_path = response.urljoin(file_name)
            yield {
                'filename': file_name,
                'folder': response.meta['folder'],
                'image_urls': [file_path]
            }

    def parse(self, response):
        urls = response.css('tr td:nth-child(2) a::attr(href)')
        for u in urls:
            url = u.extract()

            if ROOT_PATH not in url:
                next_page = response.urljoin(url)
                request = scrapy.Request(next_page, callback=self.parse_image)
                request.meta['folder'] = url
                yield request
