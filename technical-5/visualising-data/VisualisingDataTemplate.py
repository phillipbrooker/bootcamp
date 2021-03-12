"""
DATA VISUALISATION TEMPLATE
Phillip Brooker

The following code provides the building blocks for visualising data in Python.
Though the stuff you do here is not necessarily anything you can't already do
in other bits of software (Excel, SPSS, etc), the point is to see this as the
very basics of visualising stuff in Python, so that you can then go on to dig
into more sophisticated and funkier forms of visualising the social world. So,
with that in mind, the code below takes some data - flu and pneumonia death
rates by US state for the year 2016 (as a kind of proxy for thinking about
inequality in healthcare) - and produces a super simple bar chart of them.

The trick now is to use the template here to do something that you find useful.
That's almost certainly going to involve finding some different data to look at,
as well as potentially also finding some different methods of visualising them
(e.g. bar charts are pretty staid - what if you have location data and want to
map it out? Or what if you want to do a violin plot of something?). This is not
just about quantitative research either; think about how you could visualise
and display various types of qualitative data too! Having these skills opens up
all sorts of potential paths to take - have fun!
"""

#You will need to install matplotlib before running this code - give Phil a
#shout and he can help. Also note that we're importing the visualisation
#library "matplotlib.pyplot" AS "plt" - that just means we can write "plt"
#rather than "matplotlib.pyplot" every time, which is a handy timesaver.
import matplotlib.pyplot as plt

#Here's the data, in a list-of-tuples format.
flu_death_rates = [('Alabama', 17.1),('Alaska', 12.5),('Arizona', 10.4),
                   ('Arkansas', 17.1),('Cali.', 14.0),('Colorado', 9.6),
                   ('Conn.', 11.7),('Delaware', 10.7),('Florida', 9.3),
                   ('Georgia', 14.3),('Hawaii', 24.4),('Idaho', 11.3),
                   ('Illinois', 14.5),('Indiana', 12.6),('Iowa', 11.6),
                   ('Kansas', 14.4),('Kentucky', 17.3),('Louisiana', 14.3),
                   ('Maine', 12.0),('Maryland', 15.1),('Mass.', 14.1),
                   ('Michigan', 13.7),('Minnesota', 7.8),
                   ('Miss.', 23.4),('Missouri', 15.1),('Montana', 11.1),
                   ('Nebraska', 14.3),('Nevada', 18.1),
                   ('New Hamp.', 11.8),('New Jer.', 10.7),
                   ('New Mex.', 14.6),('New York', 18.3),
                   ('N. Carolina', 16.5),('N. Dakota', 14.5),
                   ('Ohio', 15.0),('Oklahoma', 12.4),('Oregon', 8.9),
                   ('Penn.', 13.9),('Rhode Isl.', 11.0),
                   ('S. Carolina', 12.0),('S. Dakota', 16.7),
                   ('Tennessee', 20.1),('Texas', 11.1),('Utah', 15.5),
                   ('Vermont', 7.0),('Virginia', 12.7),('Washington', 10.0),
                   ('W. Virginia', 17.3),('Wisconsin', 11.9),('Wyoming', 15.0)]


#These two lines use a list comprehension to go through each item in the data
#above, and separate them into datapoints/values and labels.
values = [item[1] for item in flu_death_rates] 
labels = [item[0] for item in flu_death_rates]

#This code tells Python we want to plot a bar chart, using "labels" as labels
#and "values" as values/datapoints, as you might have guessed from above.
plt.bar(labels, values)

#These lines of code are hopefully kind of intuitive as to what they do - as a
#collection they're about formatting the visualisation to make it a bit more
#explicit as to what it is about. NOTE: the "plt.xticks(rotation=90)" command
#means we're setting the data labels on the x axis at a 90 degree angle - this
#is so the words (the titles of US states) don't overlap with one another. NOTE:
#the "plt.tight_layout()" command is something we need to use in pretty much
#any matplotlib visualisation, since it just makes sure everything we've
#included - all the titles and ticks and that - are shown on screen.
plt.title("Bar chart to show US 2016 flu/pneumonia death rates by state")
plt.xlabel("States")
plt.ylabel("Deaths per 100,000")
plt.xticks(rotation=90)

plt.tight_layout()

#And finally, this command just gets Python to print out (show) the plot we've
#designed. Run the code and see how it looks!
plt.show()

"""
NOTE: there are MANY other visualisation libraries for Python other than
matplotlib. And in fact, matplotlib is about the most basic one - that's why
we've used it here. It's easy to use, but, as you'll see, it doesn't necessarily
produce the bonniest visualisations. HOWEVER, now that you know the basic
principles behind getting Python to visualise stuff, you're well equipped to go
on to look at better and more powerful visualisation libraries, such as Seaborn,
ggplot or geoplotlib - these offer better-looking visualisations, but also offer
different TYPES of visualisations that maybe help us get more creative in
thinking about how we want to display the social world from the data at hand.
"""
