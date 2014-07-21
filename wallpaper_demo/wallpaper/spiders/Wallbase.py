from wallpaper.items import Wallpaper
import re
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor



class WallbaseSearch(CrawlSpider):
    name = "wallbase"
    allowed_domains = ["wallbase.cc"]
    start_urls = [
    "http://wallbase.cc/search?q=women&color=&section=wallpapers&q=women&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=actress&color=&section=wallpapers&q=actress&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=girl&color=&section=wallpapers&q=girl&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=waitress&color=&section=wallpapers&q=waitress&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00"
    "http://wallbase.cc/search?q=female%20singer&color=&section=wallpapers&q=female%20singer&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00"
    ]
    rules = (

    Rule(LinkExtractor(
            allow=('http://wallbase.cc/wallpaper/[0-9]*', )
        ), callback='parse_wallpaper'),

    )

    def parse_wallpaper(self, response):
        wallpaper = Wallpaper()
        wallpaper['uploader'] = response.xpath('//a[contains(@class, "user-link")]/text()').extract()[0]
        wallpaper['site'] = "wallbase.cc"
        wallpaper['favorites'] = int(response.xpath('//div[contains(@class, "favsrow")]/div[contains(@class, "title")]/span/text()').extract()[0])
        wallpaper['views'] = int(response.xpath('//div[contains(@class, "centr")]/div[contains(@class, "l1")]//span[contains(@class, "highl")]/text()').extract()[0])
        wallpaper['download_link'] = response.xpath('//div[contains(@class, "content")]/img[contains(@class, "wall")]/@src').extract()[0]
        colors = response.xpath('//div[contains(@class, "palette")]/a/@style').extract()
        wallpaper['colors'] = ["#" + hex for n, hex in [color.split('#') for color in colors]]
        res = response.xpath('//a[contains(@class, "reso")]/div[contains(@class, "l1")]/text()').extract()[0]
        wallpaper['x_resolution'] = int(res.split('x')[0])
        wallpaper['y_resolution'] = int(res.split('x')[1])
        wallpaper['descriptors'] = response.xpath('//ul[contains(@class, "taglist")]/li[contains(@class, "item")]/a/text()').extract()
        wallpaper['comments'] = [""] 
        yield wallpaper  
 
        #for sel in response.xpath('//img[contains(@data-original, ".jpg")]':
        #    id = re.findall('([0-9]*\.(?:jpg|jpeg|png))', sel)[0].split('.')[0]
        #    link = "http://wallbase.cc/wallpaper/"+ id
