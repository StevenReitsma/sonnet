![](https://utrechtinc.nl/wp-content/uploads/2018/05/Header_NL.png)

# Energy Hack NL 2018 - Team Granny Heckle
____

[![BCH compliance](https://bettercodehub.com/edge/badge/energyhacknl2018/grannyheckle?branch=master&token=910d4dde78889fe8a37607f7495a62ee3b6ffc0e)](https://bettercodehub.com/)

![](https://utrechtinc.nl/wp-content/uploads/2018/05/2018052133.jpg)

#### About the hackathon
How can we make sure that all of the energy that is used in the Netherlands is 100% sustainable?
Custom solutions, data and technology can be a solution here. Enpuls and Enexis Netbeheer cooperate with TU Eindhoven, Microsoft, TNO, FAN, UtrechtInc, 80 hackers and innovators to come with innovative solutions to three challenges: *Flexible Energy*, *Durable Urban Development* and *Durable Mobility*.

[More information on Energy Hack NL](https://utrechtinc.nl/sonnet-wint-energy-hack-nl-en-e4000/?lang=en)

___
#### Our idea: Sonnet
We developed a product called Sonnet, which is a solar panel prediction system that can help prevent and reduce station failure. We have built the following features:

*Solar panel database*<br>
We have built a big database containing solar panel data. We have enriched an existing registration of solar panels by detecting non-registered solar panels in aerial photography (Open Data NL) with a deep neural network.
![](https://i.imgur.com/Rkw49rD.png)

*Demographic database*<br>
We have also created a database with prognostic demographic data based on existing demographic data on a district level. We predicted the demographics per district for the upcoming 10 years. We also added the average roof quality per district by scraping the [ZonAtlas](http://www.zonatlas.nl/home/), which tells you whether your roof is suitable for solar panels.

*Solar panel forecast*<br>
We combine the two databases to predict solar panel growth on a district level.
![](https://media.giphy.com/media/g0vi8yyDDg7dsYvND8/giphy.gif)

*Station capacity forecast*<br>
Finally, we can combine all these effort into a product that shows if a station is prone to failure by comparing the predicted net capacity used by solar panels in a certain district and the available capacity in the district stations.

![](https://media.giphy.com/media/x6MVDLaMTiBTXM5dmO/giphy.gif)


___

#### Meet our team!

Robbert van der Gugten, data science consultant at Big Data Republic [![](https://i.imgur.com/Dm73sxB.png)](https://www.linkedin.com/in/robbert-van-der-gugten-80369270/)[![](https://i.imgur.com/O2DATTM.png)](https://github.com/robbertvdg)<br>
Steven Reitsma, data science consultant at Big Data Republic [![](https://i.imgur.com/Dm73sxB.png)](https://www.linkedin.com/in/steven-reitsma-b5229471/)[![](https://i.imgur.com/O2DATTM.png)](https://github.com/StevenReitsma)<br>
Joris van Vugt, data science student at the Radboud University Nijmegen [![](https://i.imgur.com/Dm73sxB.png)](https://www.linkedin.com/in/joris-van-vugt-506571109/)[![](https://i.imgur.com/O2DATTM.png)](https://github.com/jvanvugt)<br>
Tanja Crijns, data science student at the Radboud University Nijmegen [![](https://i.imgur.com/Dm73sxB.png)](https://www.linkedin.com/in/tanjacrijns/)[![](https://i.imgur.com/O2DATTM.png)](https://github.com/TanjaCrijns)<br>
Chris Kamphuis, data science student at the Radboud University Nijmegen [![](https://i.imgur.com/Dm73sxB.png)](https://www.linkedin.com/in/chris-kamphuis-985b3a52/)[![](https://i.imgur.com/O2DATTM.png)](https://github.com/Chriskamphuis)<br>

___

#### Overview of data sets used
- [Aerial imagery from Open Data NL](https://data.overheid.nl/data/dataset/luchtfoto-2016-25cm-rgb-open-data)
- Groningen solar panel data (to train our solar panel detector)
- [Amsterdam solar panel data](https://data.amsterdam.nl/#?dte=dcatd%2Fdatasets%2Fzonnepanelen&dtfs=T&mpb=topografie&mpz=11&mpv=52.3731081:4.8932945) (to train our solar panel detector)
- [Demographics data from CBS (2011-2017)](https://www.cbs.nl/nl-nl/dossier/nederland-regionaal/wijk-en-buurtstatistieken)
- [ZonAtlas](http://www.zonatlas.nl/home/)
- Maximum capacity of grid stations in Groningen (supplied by Enexis)
- [Average load of grid stations in Groningen](https://www.enexis.nl/over-ons/documenten-en-publicaties/open-data) (Open data Enexis)

___

![](https://media.giphy.com/media/3HHDlFmKwwWK4rKDoI/giphy.gif)

___

#### Extended version of our final presentation

![](https://i.imgur.com/JPCEhrV.png)
![](https://i.imgur.com/jJ5DwNR.png)
![](https://i.imgur.com/9lojuoN.png)
![](https://i.imgur.com/XNuT2SK.png)
![](https://i.imgur.com/kS8fm2A.png)
![](https://i.imgur.com/T8PW6xV.png)
![](https://i.imgur.com/GDGZWle.png)
![](https://i.imgur.com/NQ0iLVq.png)
![](https://media.giphy.com/media/g0vi8yyDDg7dsYvND8/giphy.gif)
![](https://i.imgur.com/v5qmYfT.png)
![](https://media.giphy.com/media/x6MVDLaMTiBTXM5dmO/giphy.gif)
![](https://i.imgur.com/GkygQd1.png)
![](https://i.imgur.com/iQcHXqb.png)
