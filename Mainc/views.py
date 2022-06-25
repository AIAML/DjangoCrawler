from django.shortcuts import render
from django.views import View
import requests
import lxml
from bs4 import BeautifulSoup
from xlwt import *

class MainView(View):
    template_name = "Main_page.html"
    def get(self, request, *args, **kwargs):
        context = {}

        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        context = {}
        urltext = request.POST.get('urltext')
        #urltext = request.POST['urltext']
        urltag = request.POST['urltag']

        url = urltext
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }
        f = requests.get(url, headers=headers)
        soup = BeautifulSoup(f.content, 'lxml')
        for title in soup.find_all(urltag):
            print(title.get_text())
        return render(request, self.template_name, context)