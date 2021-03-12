"""
DATA MINING TEMPLATE 2:
Phillip Brooker

If you've run the previous data mining template file first, you'll have a file
in your folder called "NIDeprivation.csv" - this script opens that file and
prints out some potentially interesting information from it, so that we can
start to work with these data. Specifically, the code below prints out the
names of the political constituencies of Northern Ireland, and the numbers of
recorded incidents of violence per 1000 people in them.

Though this is potentially useful in itself (inasmuch as we can start to
understand things about crime and inequality across different areas of Northern
Ireland), we can maybe also see how the idea of grabbing, storing-as-text, and
then working with data further is relevant to our needs in a more general
sense. The trick now is to apply these techniques to a dataset you're interested
in working with yourself. That may mean doing something more sophisticated than
just printing out those results in the Python shell (e.g. visualising them -
see other template scripts associated with the bootcamp), or pulling out a range
of different data to use as a piece. It may also mean relying on different
techniques than those shown here - for instance, if your dataset is in a format
other than .csv, then you will need to find out about and apply different Python
libraries/modules to unravel it. But while you may find yourself needing to
consult other documentation to learn the commands for doing those things, the
broad idea of creating/working with datasets and files will apply across all
of that. Have fun!
"""

#The csv module is native to Python, but not all modules relevant to data mining
#are like this - some you need to install prior to importing. If this is the
#case for you (e.g. if you are working with a data format other than csv), give
#Phil a shout and he can help you.
import csv

#In the previous template we saw a file being created/used with a "with"
#statement. That would apply here too, but just for completeness I've used
#different methods for working with files (e.g. "file = open(FILENAME, MODE)"
#and "file.close()").

#This code opens our csv datafile in read mode (i.e. so we can't overwrite any
#information in there), uses the csv module to read in that data to Python, then
#for each row in the dataset, we print certain elements of it - the elements
#at index position 1 (i.e. the constituency name) and the element at index
#position 32 (i.e. the "violent_rate") - see below for further detail. Then
#we close the file. So, when you run this code, you should see the results!
file = open("NIDeprivation.csv", "r")
reader = csv.reader(file)
for row in reader:
    print(row[1] + "    " + row[32])
file.close()

"""
If you open the .csv file in something like Microsoft Excel you can see the
various bits of information and work out the index positions of different fields
within each row of data. Hence, we can see in that file that "#AA2008name"
refers to the parliamentary constitutency name, and this is stored at at row[1]
for each row of data. We can also see that "Violent_rate" gives the rate of
violent offences per 1000 population, and this is stored at row[32]. We can also
play around in Python to identify these things - once you've read in the csv
file, try calling things like row[0][32] in the shell to see what results you
get.
"""
