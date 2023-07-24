# Show Name: RSS Template
# Show Type: RSS Podcast

import re
import urllib.request
import shutil
import os
import ssl
import logging

# Set podcast specific variables
# RSS link
rssurl = "http://feeds.feedburner.com/civillibertiesminute"
# Destination Folder
podfolder = "C:\\WNHN\\PODCASTS\\The_Civil_Liberties_Minute"

# Set up logging
logging.basicConfig(filename="C:\\FeedProcessing\\feedprocessing.log", encoding="utf-8", level=logging.DEBUG, format="%(asctime)s %(levelname)-8s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
logging.info("Processing podfolder: " + podfolder + " and rssurl: " + rssurl)

# Check correct folders exist
if not os.path.exists(podfolder):
	logging.error(podfolder + " does not exist. Exiting script.")
	exit()
if not os.path.exists(podfolder + "\\Incoming"):
	logging.error(podfolder + "\\Incoming" + " does not exist. Exiting script.")
	exit()
if not os.path.exists(podfolder + "\\Newest"):
	logging.error(podfolder + "\\Newest" + " does not exist. Exiting script.")
	exit()

# Get latest XML episode List
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
html = urllib.request.urlopen(rssurl, context=ctx).read()
xmlContents = html.decode('utf-8')

# Find URL of episode
hit = re.search('http.*mp3', xmlContents)
episodeURL = hit.group(0)
logging.info(episodeURL)

# Find episode name
episodeName = episodeURL[episodeURL.rfind('/')+1:]
logging.info("episodeName: " + episodeName)
incomingPath = podfolder + "\\Incoming\\" + episodeName
newestPath = podfolder + "\\Newest\\" + episodeName

# Get latest episode and put in Incoming
filedata = urllib.request.urlopen(episodeURL, context=ctx).read()
with open(incomingPath, 'b+w') as f:
	f.write(filedata)
if os.path.isfile(incomingPath):
	logging.info("Episode " + episodeName + " successfully moved to Incoming")
else:
	logging.error("Episode " + episodeName+ " not moved to Incoming correctly. Exiting script.")
	exit()

# Delete contents of Newest
for f in os.listdir(podfolder + "\\Newest\\"):
    os.remove(os.path.join(podfolder + "\\Newest\\", f))

# Copy latest episode to Newest
shutil.copyfile(incomingPath, newestPath)
if os.path.isfile(newestPath):
	logging.info("Episode " + episodeName + " successfully moved to Newest")
else:
	logging.error("Episode " + episodeName+ " not moved to Newest correctly. Exiting script.")
	exit()
