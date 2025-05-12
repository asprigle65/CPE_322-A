# Lab 7 - ThingSpeak and Google Sheets
---

-Continued to use Git Bash
-I had to work around certain steps for this lab. Please especially refer to the original instructions and supplementary files from lesson7 for more on this.

## ThingSpeak

Signed up for MathWorks ThingSpeak\
![tsup](SourceFolder/tssup.png)

Created new channel\
![nc](SourceFolder/newchannel.png)\

Copying .py files to ~/demo\
-psutil was already installed, so the first command was unnecessary
```
$ pip install -U psutil
$ cd ~/demo
$ cp ~/iot/lesson7/thingspeak_cpu_loop.py .
$ cp ~/iot/lesson7/thingspeak_feed.py .
```

Cat-ing thingspeak_cpu_loop.py and thingspeak_feed.py\
![tsclpy](SourceFolder/tsclpy.png)\
![tsfpy](SourceFolder/tsfpy.png)

Inserting Write API key from ThingSpeak\
![pytsfpy](SourceFolder/pytsfpy.png)

ThingSpeak channel stats\
![tscs](SourceFolder/tscs.png)

## Google Sheets

Creating a new project in Google IAM\
![np](SourceFolder/newproj.png)

Enabling Drive and Sheets API\
![drive](SourceFolder/drive.png)
![sheets](SourceFolder/sheets.png)

Creating credentials (service account)\
-A slightly different and updated method than the one listed on the lesson7 page was needed\
![sacc](SourceFolder/saccount.png)

Installing gspread and oauth2client
```
$ pip install -U gspread oauth2client
```
![gs](SourceFolder/gspread.png)

Copying .py files to ~/demo
```
$ cd demo
$ cp ~/iot/lesson3/system_info.py .
$ cp ~/iot/lesson7/rpi_spreadsheet.py .
```

Manually moving .json file to 'demo' folder\
-Due to the lab normally being done on a Raspberry Pi, I had to improvise a bit for this step\
![copy](SourceFolder/copy.png)

Sharing spreadsheet with client_email\
![share](SourceFolder/share.png)

Editing rpi_spreadsheet.py\
![edit](SourceFolder/edit.png)

Running rpi_spreadsheet.py (attempt 1 - error)\
-Once again, not having the proper Pi hardware caused some roadblocks. I ended up having to edit the code in system_info.py originally from lesson7 to account for this.\
see new code [here](SourceFolder/system_info.py) \
![error](SourceFolder/error.png)

Running rpi_spreadsheet.py (attempt 2 - success)\
Running python file\
![rpspy](SourceFolder/rpspy.png)\
Live update to Google sheets\
![ss](SourceFolder/sheetshow.png)


