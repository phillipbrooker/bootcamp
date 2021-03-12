"""
DATA MINING TEMPLATE:
Phillip Brooker

The following code provides the first element of a data mining script: the bit
that identifies a dataset, in .csv format, from a URL location, grabs it, and
writes it into a text file. If you run this code, you should see a new file
created in the same directory as the "DataMiningTemplate1" file, which will be
a .csv file containing the results of the 2008 Northern Ireland Deprivation
Index study.

There are LOTS of publically-available open-access datasets on the web, and this
is one of them. We can get a lot of social scientific use from these datasets,
so knowing a bit about how to grab them using Python can be really helpful.

The trick now is to use the template code here to grab a dataset of your own;
something that is relevant to your own research interests, and tweak the code
so that it works in the context of the dataset you've chosen. That might mean
tweaking how the Python csv module identifies a new line in the data, how it
reads in the data (i.e. is it broken up into lines already, or do we need to do
that with Python?), or even tweaking the whole format of the dataset altogether
(i.e. this code works for .csv format data, but what if you have your eye on a
.json or .xml dataset?). For now, the important thing is to identify a dataset
you'd like to use, then see if you can grab a copy and write it to a file on
your laptop using Python commands along the lines of those detailed below -
have fun!
"""
#The "requests" and "csv" modules are native to your Python installation
#already so you can just import them without installing them. However, if you
#want to work with other types of data format, you may need to install a library
#to handle that. If that's the case, give Phil a shout and he can help you.
import requests
import csv


#This is where you specify the URL location of the dataset you want to grab.
#Note that I've used a backslash to break up the URL across lines - this is just
#so the URL doesn't go too far off the page, so we can keep it all in view
#without scrolling back and forth too much. Backslashes are handy for
#readability of code.
url = "https://www.opendatani.gov.uk/dataset/e202fde9-7f0b-4d88-8711-\
e18a8817cff8/resource/887ad000-b6bf-4004-9ba8-3fb09372d432/download/nimdm2017\
---aa2008.csv"
#This bit reads the URL into Python, but we still need to break it down as
#specifically .csv data (see below)
response = requests.get(url)


#Line-by-line, this code uses a with stateament to create a new file
#("NIDeprivation.csv") in write mode ("w"), and calls that "csv_file". We then
#set where we want the Python csv module to write to ("csv_file") and where we
#want it to read from (the "response" variable which contains our URL
#information, but using the .splitlines() method to split that info into
#individual lines). The "text" bit just tells the csv module we want to treat
#this info as text/strings. Then there is a for loop to iterate through each
#line of csv data, and write it to the writer/the "NIDeprivation.csv" file.
with open("NIDeprivation.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    reader = csv.reader(response.text.splitlines())
    for row in reader:
        writer.writerow(row)
