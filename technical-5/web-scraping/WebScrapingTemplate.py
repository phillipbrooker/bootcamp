"""
WEB-SCRAPING TEMPLATE
Phillip Brooker

The following code provides the building blocks on which you can put together a script for
scraping content from a website you specify. The code below imports in various relevant
libraries and modules (notably, the "requests" module for grabbing content from a URL, and
BeautifulSoup as a module for reading, or "parsing", HTML code into Python). This code then
extracts out all of the HTML information given as "paragraphs" on the webpage - if you visit
the URL in a web-browser, you'll see that the text on this page is primarily a transcription
of a speech of former PM Theresa May's on the NHS - the kind of thing you could use to explore
Tory rhetoric around issues that matter to the public but which the Tories do not necessarily
share an appreciation of.

There is also some code to "clean up" the text given - if you call the variable "text" in the
shell you'll see that the raw data from the webpage contains various bits and bobs of junk,
which we don't necessarily want to see. So, using techniques already covered in the bootcamp,
we can get rid of those and be left with the "gold-dust" (such that it is) of a Tory then-PM's
asinine commentary on the NHS.

The trick now is to scrape something from the web that YOU'RE interested in and helps you do
YOUR work. This will mean learning something about how HTML information is tagged and
formatted (using the hopefully-handy guide in the TECHNICAL5/WebScraping folder), and applying
these techniques to a differently-structured place on the web. It would also be worth thinking
about how you might want to use Python to assist in the analysis of these data - how might
you dig into large-corpus text datasets such as those gathered through web-scraping? To get
ahead here, you will almost certainly need to explore the Python and BeautifulSoup
documentation online to learn extra techniques, as well as get familiar with HTML (if you are
not already). Have fun!
"""

#You will need to install the "BeautifulSoup" library before running the code - the "requests"
#library is native to Python, so you should already have this just by virtue of having
#nstalled Python. Give Phil a shout and he can help with BeautifulSoup.
from requests import get
from bs4 import BeautifulSoup

#This is where you specify which URL you want to scrape information from. You should identify
#a page relevant to your research interests/needs in a web browser, then copy that info
#across to here. The "response" variable just sorts out information grabbed from that URL.
url = "https://www.gov.uk/government/speeches/pm-speech-on-the-nhs-18-june-2018"
response = get(url)

#Given you know the source data is a webpage (and is therefore written in HTML), we can use
#BeautifulSoup to unravel HTML code into something readable in Python. This is called
#"parsing", and here we're parsing the HTML code for the entire webpage.
html_soup = BeautifulSoup(response.text, "html.parser")

#Now we need to search within that entire HTML code to find just the bits we need - having
#done the detective work to identify that Theresa May's speech is contained in paragraphs that
#are marked with the HTML tag-pairing <p></p>, we can now search within that tag soup for
#bits of information tagged with a "p". If you call the "text" variable in the shell, you'll
#see the results.
text = html_soup.find_all("p")

"""
CLEANUP TIME!
If you called "text" in the shell, you can maybe identify that some bits of info are still
kind of junk-y. We can get rid of those with list and string methods, as in the code below.
"""
#Calling "text" shows us the first and last five paragraphs tagged with <p></p> are junk.
#Let's delete those.
del(text[0:5])
del(text[-1:-5:-1])

#We still have those weird "<p>" and "</p>" HTML bits included in our text and that's kind of
#annoying and would get in the way of any kind of Python-based word analysis. So let's get
#rid of them. Here we establish a "clean_text" variable to put the end result in, then use a
#for loop to iterate through each item in "text", turn it into a string, replace the "<p>" and
#"</p> characters with empty strings (i.e. replace them with nothing - delete them) and append
#the remaining text to the "clean_text" list. Hey presto - just the text of the speech!
clean_text = []
for item in text:
    item = str(item)
    item = item.replace("<p>", "")
    item = item.replace("</p>", "")
    clean_text.append(item)
