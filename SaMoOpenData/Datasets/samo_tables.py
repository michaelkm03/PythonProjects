import json
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import os

class Datasets(object):

    def __init__(self):
        self.driver = webdriver.Chrome('/Users/victorious/Desktop/Projects/Python Projects/PublicProjects/chromedriver')

        self.TOTALdatasetsCount = 0
        self.TOTALcolumnCount = 0
        self.TOTALrowCount = 0
        self.ListOfDatasetsId = 'en4k-pem5'

    def scrape(self, id):
        # Construct/request url, return page source and url
        api_url = 'https://data.smgov.net/api/views/%s' % id
        self.driver.get(api_url)
        return self.driver.page_source, self.driver.current_url
        driver.quit()

    def getIDs(self):
        map = {}
        list = []
        with open('datasets.txt') as data_file:
            datasets = json.load(data_file)
            for dataset in datasets:
                name = dataset['name']
                id = dataset['identifier']
                map[name] = id
                list.append(id)
            return map, list

    def downloadAllDatasets(self):
        id_map, id_list = self.getIDs()
        for id in list:
            try:
                download_url = 'https://data.smgov.net/api/views/%s/rows.csv?accessType=DOWNLOAD' % id
                driver = webdriver.Chrome('/Users/victorious/Desktop/Projects/Python Projects/PublicProjects/chromedriver')
                driver.get(download_url)
            except:
                print 'missed id %s' % id
                pass

    def getRowCount(self):
        path = '/Users/victorious/Desktop/datasets/'
        dataset_rowcount_map = {}
        for filename in os.listdir(path):
            if (filename != '.DS_Store'):
                with open(path + filename, 'r') as file:
                    row_count = sum(1 for row in file)
                    dataset_rowcount_map[filename] = row_count
        return dataset_rowcount_map

    def getDatasetInfo(self):
        dataset_rowcount_map = self.getRowCount()
        for count in dataset_rowcount_map.values():
            self.TOTALrowCount+=count

        # Get dataset ids list and iterate.  Returns json for each id
        dataset_id_map, datasets_id = self.getIDs()
        for dataset in datasets_id:
            data, url = self.scrape(dataset)
            soup = bs(data, "html.parser")
            json_obj = json.loads(soup.find("body").text)
            self.TOTALdatasetsCount += 1
            self.TOTALcolumnCount+=len(json_obj['columns'])

            # Get and Display Columns
            name             = json_obj['name']
            columns          = json_obj['columns']
            epoch            = json_obj['indexUpdatedAt']
            index_updated    = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch))
            epoch            = json_obj['viewLastModified']
            last_modified    = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch))
            if dataset != 'cr94-dauy':
                display_type = json_obj['displayType']

            print '# [ ' + str(self.TOTALdatasetsCount) + ' ]'
            print '  Dataset:                  ' + str(name)
            print '  Columns:                  ' + str(len(columns))
            print '  Index Updated:            ' + str(index_updated)
            print '  Data Updated:             ' + str(last_modified)
            print '  URL:                      ' + str(url)
            print '  Type:                     ' + str(display_type)
            print '|-------------------------------------------------------------|'
        print 'TOTAL DATASET COUNT:     ' + str(self.TOTALdatasetsCount)
        print 'TOTAL COLUMN COUNT:      ' + str(self.TOTALcolumnCount)
        print 'TOTAL ROW COUNT:         ' + str(self.TOTALrowCount)
        print ''
        print '==========================================================='
        for dataset in dataset_rowcount_map:
            print dataset
            print 'TOTAL ROWS:  ' + str(map[dataset])
            print ''
        print '==========================================================='

if __name__ == '__main__':
    data_obj = Datasets()
    data_obj.getDatasetInfo()