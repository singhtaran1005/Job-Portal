import scrapy
# xyz=[]
# ur='https://in.linkedin.com/jobs/search?keywords=&location=India&locationId=&geoId=102713980&sortBy=R&f_TPR=&f_JT=I&f_E=1%2C2&position=1&pageNum='
# counter=0
# for counter in range(0,10):
#     url=ur+str(counter)
#     counter=counter+1
#     xyz.append(url)
class tryer(scrapy.Spider):

    name='quoutes'
    # start_urls=xyz
    start_urls=['https://in.linkedin.com/jobs/search?keywords=&location=India&locationId=&geoId=102713980&sortBy=R&f_TPR=&f_JT=I&f_E=1%2C2&position=1&pageNum=0']
    def parse(self,response):
        job_title=response.css("span.screen-reader-text")[0].extract()
        yield{'Title is ':job_title}
