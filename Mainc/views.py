from django.shortcuts import render
from django.views import View
import requests
import lxml
from bs4 import BeautifulSoup
from xlwt import *
from woocommerce import API

class ImageView(View):
    template_name = "Image_page.html"
    def get(self, request, *args, **kwargs):
        context = {}
        context['urltag'] = 'Nothing to display'
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            passed_data = request.POST
            urltext = request.POST.get('urltext')
        if  len(urltext) > 5:
            url = urltext
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
            }
            f = requests.get(url, headers=headers)
            soup = BeautifulSoup(f.content, 'lxml')
            allv = ""
            items = {}
            counter = 0
            img = soup.find_all("img")
            for each in img:
                allv = allv + '-----' +each.get('src')
                items[counter] = each.get('src')
                counter= (counter + 1)

            resp = requests.get(url)
            print(resp.status_code)
            context['urltag'] = allv
            context['images'] = items
        else:
            context['urltag'] = ""
            context['images'] = ""
        return render(request, self.template_name, context)

class AhrefView(View):
    template_name = "Ahref_page.html"
    def get(self, request, *args, **kwargs):
        context = {}
        context['urltag'] = 'Nothing to display'
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            passed_data = request.POST
            urltext = request.POST.get('urltext')
        url = urltext
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }
        f = requests.get(url, headers=headers)
        soup = BeautifulSoup(f.content, 'lxml')
        allv = ""
        for title in soup.find_all('a'):
            try:
                allv = allv +  " - " + title.get('href')
            except:
                allv = allv + "-"

        resp = requests.get(url)
        print(resp.status_code)
        context['urltag'] = allv
        return render(request, self.template_name, context)

class HeadingView(View):
    template_name = "Heading_page.html"
    def get(self, request, *args, **kwargs):
        context = {}
        context['urltag'] = 'Nothing to display'
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            passed_data = request.POST
            urltext = request.POST.get('urltext')
        url = urltext
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }
        f = requests.get(url, headers=headers)
        soup = BeautifulSoup(f.content, 'lxml')
        allv = ""
        for title in soup.find_all('h1'):
            try:
                allv = allv +  " H1 - " + title.get_text() + " --- "
            except:
                allv = allv + "-"
        for title in soup.find_all('h2'):
            try:
                allv = allv +  " H2 - " + title.get_text() + "---"
            except:
                allv = allv + "-"
        for title in soup.find_all('h3'):
            try:
                allv = allv +  " H3 - " + title.get_text() + "---"
            except:
                allv = allv + "-"

        for title in soup.find_all('h4'):
            try:
                allv = allv +  " H4 - " + title.get_text() + "---"
            except:
                allv = allv + "-"

        resp = requests.get(url)
        print(resp.status_code)
        context['urltag'] = allv
        return render(request, self.template_name, context)

class ReadTagView(View):
    template_name = "Tag_page.html"
    def get(self, request, *args, **kwargs):
        context = {}
        context['urltag'] = 'Nothing to display'
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            passed_data = request.POST
            urltext = request.POST.get('urltext')
            urltag = request.POST['urltag']
        if  len(urltext) > 5:
            url = urltext
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
            }
            f = requests.get(url, headers=headers)
            soup = BeautifulSoup(f.content, 'lxml')
            allv = ""
            # for title in soup.find_all(urltag, class_=tagclass):
            for title in soup.find_all(urltag):
                allv = allv + title.get_text()

            resp = requests.get(url)
            print(resp.status_code)
            context['urltag'] = allv
        else:
            context['urltag'] = ""
        return render(request, self.template_name, context)

class TagAttributeView(View):
    template_name = "TagAttribute_page.html"
    def get(self, request, *args, **kwargs):
        context = {}
        context['urltag'] = 'Nothing to display'
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            passed_data = request.POST
            urltext = request.POST.get('urltext')
            urltag = request.POST['urltag']
            tagattribute = request.POST['tagattribute']
        url = urltext
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }
        f = requests.get(url, headers=headers)
        soup = BeautifulSoup(f.content, 'lxml')
        allv = ""
        for title in soup.find_all(urltag):
            try:
                allv = allv + title.get(tagattribute)
            except:
                allv = allv + "-"

        resp = requests.get(url)
        print(resp.status_code)
        context['urltag'] = allv
        return render(request, self.template_name, context)

class ReadWordPressPricesView(View):
    template_name = "ReadWordPressPrices_page.html"
    def get(self, request, *args, **kwargs):

        context = {}
        context['urltag'] = 'Nothing to display'
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            passed_data = request.POST
            urltext = request.POST.get('urltext')
        url = urltext
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }
        f = requests.get(url, headers=headers)
        soup = BeautifulSoup(f.content, 'lxml')
        allv = ""
        for title in soup.find_all('span', class_="woocommerce-Price-amount amount"):
            try:
                allv = allv + title.get_text()
            except:
                allv = allv + "-"

        resp = requests.get(url)
        print(resp.status_code)
        context['urltag'] = allv
        return render(request, self.template_name, context)


class MainView(View):
    template_name = "Link_Actions.html"
    def get(self, request, *args, **kwargs):
        context = {}
        context['urltag'] = 'Nothing to display'
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            passed_data = request.POST
            urltext = request.POST.get('urltext')
            urltag = request.POST['urltag']
            tagclass = request.POST['tagclass']
        url = urltext
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }
        f = requests.get(url, headers=headers)
        soup = BeautifulSoup(f.content, 'lxml')
        allv = ""
        #for title in soup.find_all(urltag, class_=tagclass):
        for title in soup.find_all(urltag):
            allv = allv + title.get_text()

        #img = soup.find_all(urltag)
        #for each in img:
        #    allv = allv + '-----' +each.get('src')

        resp = requests.get(url)
        print(resp.status_code)
        #print(resp.text)
        context['urltag'] = allv
        return render(request, self.template_name, context)

class ReadSitemapView(View):
    template_name = "ReadSitemap_page.html"
    def get(self, request, *args, **kwargs):
        context = {}
        context['urltag'] = 'Nothing to display'
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            passed_data = request.POST
            urltext = request.POST.get('urltext')
        url = urltext
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }
        xmlDict = {}
        r = requests.get(url)
        xml = r.text
        soup = BeautifulSoup(xml)
        sitemapTags = soup.find_all("sitemap")
        #sitemapTags = soup.find_all("url")

        print
        "The number of sitemaps are {0}".format(len(sitemapTags))

        for sitemap in sitemapTags:
            xmlDict[sitemap.findNext("loc").text] = sitemap.findNext("lastmod").text

        print(xmlDict)

        context['urltag'] = xmlDict
        return render(request, self.template_name, context)