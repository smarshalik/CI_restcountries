# 1- load countries-input.json
# 2- crawl,parse and update population
# 3- crawl,parse and update gini
# 4- save json string in new file

import json
import collections

import sys
sys.path.append('crawlers')
import population
import gini


def getCountriesJSON():
    inputJsonFile = open('countries-input.json')
    inputJsonString = json.load(inputJsonFile,
                                object_pairs_hook=collections.OrderedDict)
    inputJsonFile.close()
    return inputJsonString


def saveCountriesJSON(countriesJSON):
    outputJsonFile = open('countries-output.json', 'w')
    with open('countries-output.json', 'w') as outputJsonFile:
        json.dump(countriesJSON, outputJsonFile)

countriesJSON = getCountriesJSON()
countriesJSON = population.update(countriesJSON)
countriesJSON = gini.update(countriesJSON)
saveCountriesJSON(countriesJSON)
