from wallpaper.items import Wallpaper
import re
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor



class WallbaseSearch(CrawlSpider):
    name = "wallbase"
    allowed_domains = ["wallbase.cc"]
    start_urls = [
    #Improper women
##    "http://wallbase.cc/search?q=women&color=&section=wallpapers&q=women&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=010&board=21&aspect=0.00",
##    "http://wallbase.cc/search?q=butt&color=&section=wallpapers&q=butt&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=010&board=21&aspect=0.00",
##    "http://wallbase.cc/search?q=ass&color=&section=wallpapers&q=ass&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=010&board=21&aspect=0.00",
##    "http://wallbase.cc/search?q=boobs&color=&section=wallpapers&q=boobs&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=010&board=21&aspect=0.00"
##    "http://wallbase.cc/search?q=sexy%20women&color=&section=wallpapers&q=sexy%20women&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=010&board=21&aspect=0.00"    
    #Proper women
##    "http://wallbase.cc/search?q=actress&color=&section=wallpapers&q=actress&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
##    "http://wallbase.cc/search?q=model&color=&section=wallpapers&q=model&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
##    "http://wallbase.cc/search?q=butt&color=&section=wallpapers&q=butt&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
##    "http://wallbase.cc/search?q=sexy%20women&color=&section=wallpapers&q=sexy%20women&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
##    "http://wallbase.cc/search?q=women&color=&section=wallpapers&q=women&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00"
##    #Seed categories
    "http://wallbase.cc/search?q=abstract&color=&section=wallpapers&q=abstract&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=animal&color=&section=wallpapers&q=animal&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=anime&color=&section=wallpapers&q=anime&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=artistic&color=&section=wallpapers&q=artistic&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=cgi&color=&section=wallpapers&q=cgi&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=cartoon&color=&section=wallpapers&q=cartoon&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=celebrity&color=&section=wallpapers&q=celebrity&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=comics&color=&section=wallpapers&q=comics&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=dark&color=&section=wallpapers&q=dark&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=earth&color=&section=wallpapers&q=earth&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=fantasy&color=&section=wallpapers&q=fantasy&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=food&color=&section=wallpapers&q=food&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=game&color=&section=wallpapers&q=game&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=holiday&color=&section=wallpapers&q=holiday&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=humor&color=&section=wallpapers&q=humor&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=man&color=&section=wallpapers&q=man&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=military&color=&section=wallpapers&q=military&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=misc&color=&section=wallpapers&q=misc&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=movie&color=&section=wallpapers&q=movie&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=music&color=&section=wallpapers&q=music&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=pattern&color=&section=wallpapers&q=pattern&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=photography&color=&section=wallpapers&q=photography&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=products&color=&section=wallpapers&q=products&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=religious&color=&section=wallpapers&q=religious&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q==(science%20fiction)&color=&section=wallpapers&q==(science%20fiction)&res_opt=eqeq&res=0x0&order_mode=desc&thpp=32&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=sports&color=&section=wallpapers&q=sports&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=tv&color=&section=wallpapers&q=tv&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=technology&color=&section=wallpapers&q=technology&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=vehicles&color=&section=wallpapers&q=vehicles&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=video%20game&color=&section=wallpapers&q=video%20game&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00",
    "http://wallbase.cc/search?q=weapons&color=&section=wallpapers&q=weapons&res_opt=eqeq&res=0x0&order_mode=desc&thpp=60&purity=100&board=21&aspect=0.00"      
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
        wallpaper['origin'] = response.url
        wallpaper['favorites'] = int(response.xpath('//div[contains(@class, "favsrow")]/div[contains(@class, "title")]/span/text()').extract()[0])
        wallpaper['views'] = int("".join(response.xpath('//div[contains(@class, "centr")]/div[contains(@class, "l1")]//span[contains(@class, "highl")]/text()').extract()[0].split(",")))
        wallpaper['download_link'] = response.xpath('//div[contains(@class, "content")]/img[contains(@class, "wall")]/@src').extract()[0]
        colors = response.xpath('//div[contains(@class, "palette")]/a/@style').extract()
        wallpaper['filetype'] = wallpaper['download_link'].split('.')[-1] #get the last item
        wallpaper['colors'] = ["#" + hex[0:-1] for n, hex in [color.split('#') for color in colors]] #-1 removes semi-colon
        res = response.xpath('//a[contains(@class, "reso")]/div[contains(@class, "l1")]/text()').extract()[0]
        wallpaper['x_resolution'] = int(res.split('x')[0])
        wallpaper['y_resolution'] = int(res.split('x')[1])
        wallpaper['descriptors'] = response.xpath('//ul[contains(@class, "taglist")]/li[contains(@class, "item")]/a/text()').extract()
        wallpaper['comments'] = [""] 
        yield wallpaper  
 