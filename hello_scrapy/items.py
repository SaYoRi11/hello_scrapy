import scrapy

class MovieItem(scrapy.Item):
    title = scrapy.Field()
    summary = scrapy.Field()
    genres = scrapy.Field()
    rating = scrapy.Field()
    director = scrapy.Field()
    writers = scrapy.Field()
    cast = scrapy.Field()
