import requests
import json
import datetime
import time

class Data(object):

    def __init__(self):
        self.terms = {}
        self.endpoints = {}
        self.time_instatiated = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        self.base_URL = 'https://swapi.co/api/'

    def getTerms(self):
        json_obj = json.loads(requests.get(self.base_URL).text)
        for resource in json_obj:
            self.terms[resource] = json_obj[resource]
        return self.terms

    def getEndpointData(self):
        self.content = {}
        self.terms = self.getTerms()
        for term in self.terms:
            next = True
            page = json.loads(requests.get('%s?page=1' % self.terms[term]).text)
            pages = []
            pages.append(page)
            while next:
                if bool(page['next']):
                    page = json.loads(requests.get(page['next']).text)
                    pages.append(page)
                else:
                    self.content[term] = pages
                    next = False
        return json.dumps(self.content)

if __name__ == '__main__':
    data_object = Data().getEndpointData()
    print data_object