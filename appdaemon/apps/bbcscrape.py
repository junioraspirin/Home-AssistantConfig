######## BBC Radio 6 Music Media Scraper ########

# This script scrapes the bbc mosuc website every 20 seconds to pull the latest track information
# Uses beautiful soup to extract the relevant info

import appdaemon.plugins.hass.hassapi as hass
import requests
import urllib.request
import datetime
# import time
from bs4 import BeautifulSoup

class BbcScrape(hass.Hass):
    def initialize(self):
        self.log("BBC Radio 6 Track Scraper Started")
        time = self.datetime() + datetime.timedelta(seconds=5)
        self.run_every(self.scrape, time, 20)
        
    def scrape(self, kwargs):
        url = 'https://www.bbc.co.uk/sounds/play/live:bbc_6music'
        response = requests.get(url)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        try:
            count = 0
            artist = soup.find(class_='sc-c-track__artist').get_text()
            title = soup.find(class_='sc-c-track__title').get_text()
            
            #artist = soup.find(class_='on-air__track-now-playing__artist').get_text()
            #title = soup.find(class_='on-air__track-now-playing__title').get_text()

            self.set_state("sensor.sixmusicartistpy", state = artist)
            self.set_state("sensor.sixmusictitlepy", state = title)
            
            self.log(artist + " - " + title)
        except Exception as error:
            count = count + 1
            
            self.log("Track info not found" + " (" + str(count) + ")")
            
            if count > 15:
                self.set_state("sensor.sixmusicartistpy", state = "Track info not avaliable")
                self.set_state("sensor.sixmusictitlepy", state = "Radio 6 Music")                

