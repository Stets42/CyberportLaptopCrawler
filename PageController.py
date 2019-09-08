from urllib.parse import urljoin


class UrlProvider:
    def __init__(self):
        self.stock_url = "https://www.cyberport.de/notebook-und-tablet/notebooks.html?productsPerPage=24&sort=popularity&page=1"

    def create_start_url(self, sort_type):
        if sort_type == "ascending":
            return "https://www.cyberport.de/notebook-und-tablet/notebooks.html?productsPerPage=24&sort=price_asc&page="

        elif sort_type == "decending":
            return "https://www.cyberport.de/notebook-und-tablet/notebooks.html?productsPerPage=24&sort=price_desc&page="

        elif sort_type == "topseller":
            return "https://www.cyberport.de/notebook-und-tablet/notebooks.html?productsPerPage=24&sort=topseller&page="

        else:
            return "https://www.cyberport.de/notebook-und-tablet/notebooks.html?productsPerPage=24&sort=popularity&page="

    def url_all_pages(self, sort_type, start, stop):
        url_list = []
        for i in range(start, stop):
            url_list.append(urljoin(self.create_start_url(sort_type), str(range(start, stop))))
        return url_list