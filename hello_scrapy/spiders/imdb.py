import scrapy
from hello_scrapy.items import MovieItem

class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = [
            'http://www.imdb.com/chart/top',
            'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'
        ]


    def parse(self, response):
        columns = response.css('table tbody tr')

        for col in columns:
            url = col.css(".titleColumn a::attr(href)").get()
            yield response.follow(url, callback = self.parse_movie)

    def parse_movie(self, response): 
        movie = MovieItem()
        movie['title'] = response.css('h1[data-testid=hero-title-block__title]::text').get()
        movie['rating'] = response.css('.sc-7ab21ed2-1::text').get()
        movie['summary'] = response.css('.sc-16ede01-2::text').get().strip()
        movie['genres'] = response.css('.sc-16ede01-3 ::text').getall()
        cast_crew = response.css('li[data-testid=title-pc-principal-credit]')
        movie['director'] = cast_crew[0].css('a::text').getall()
        movie['writers'] = cast_crew[1].css('a::text').getall()
        movie['cast'] = cast_crew[2].css('a.ipc-metadata-list-item__list-content-item::text').getall()
        yield movie
