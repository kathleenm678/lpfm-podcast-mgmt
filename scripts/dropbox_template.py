# Show Name: Dropbox Template
# Show Type: Dropbox Local Show

import re
import urllib.request
import shutil
import os
import ssl
import logging

# Set local show specific variables
# Dropbox Folder
dropboxfolder = "C:\\Users\\Test\\Dropbox\\Ancient and Modern"
# Destination Folder
localshowfolder = "C:\\WNHN\\LOCAL_SHOWS\\Ancient_and_Modern"

# Set up logging
logging.basicConfig(filename="C:\\FeedProcessing\\feedprocessing.log", encoding="utf-8", level=logging.DEBUG, format="%(asctime)s %(levelname)-8s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
logging.info("Processing dropboxfolder: " + dropboxfolder + " and localshowfolder: " + localshowfolder)

# Check correct folders exist
if not os.path.exists(dropboxfolder):
	logging.error(dropboxfolder + " does not exist. Exiting script.")
	exit()
if not os.path.exists(localshowfolder):
	logging.error(localshowfolder + " does not exist. Exiting script.")
	exit()
if not os.path.exists(localshowfolder + "\\Incoming"):
	logging.error(localshowfolder + "\\Incoming" + " does not exist. Exiting script.")
	exit()
if not os.path.exists(localshowfolder + "\\Newest"):
	logging.error(localshowfolder + "\\Newest" + " does not exist. Exiting script.")
	exit()

# Find episode name
if len(os.listdir(dropboxfolder)) == 0:
	logging.error(dropboxfolder + " is empty. Exiting script.")
	exit()
episodeName = os.listdir(dropboxfolder)[0]
if episodeName == "desktop.ini":
	if len(os.listdir(dropboxfolder)) == 1:
		logging.error(dropboxfolder + " is empty. Exiting script.")
		exit()
	episodeName = os.listdir(dropboxfolder)[1]
logging.info("episodeName: " + episodeName)
dropboxPath = dropboxfolder + "\\" + episodeName
incomingPath = localshowfolder + "\\Incoming\\" + episodeName
newestPath = localshowfolder + "\\Newest\\" + episodeName

# Copy episode from Dropbox to Incoming
shutil.copyfile(dropboxPath, incomingPath)
if os.path.isfile(incomingPath):
	logging.info("Episode " + episodeName + " successfully moved to Incoming")
else:
	logging.error("Episode " + episodeName+ " not moved to Incoming correctly. Exiting script.")
	exit()

# Delete contents of Newest
for f in os.listdir(localshowfolder + "\\Newest\\"):
    os.remove(os.path.join(localshowfolder + "\\Newest\\", f))

# Copy latest episode to Newest
shutil.copyfile(incomingPath, newestPath)
if os.path.isfile(newestPath):
	logging.info("Episode " + episodeName + " successfully moved to Newest")
else:
	logging.error("Episode " + episodeName+ " not moved to Newest correctly. Exiting script.")
	exit()
