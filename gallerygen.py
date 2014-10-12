# This script generates the HTML for the gallery page.
# Adding new games to the list only requires adding another entry to the `games` list below.

# Title shown at the top of the page.
title = "UVic GameDev Gallery"

# Introduction text below the title.
intro =  \
"Games made by the UVic Game Development club, collected in one place for your viewing pleasure."

# Put in this list all the games you want to be on the list.
# This is a list of 3-tuples of strings: (header, body, footer).
# Embedded HTML is allowed inside the body and the footer, but not the header.
games = [

("Friday Night Bullet Arena",
"""<img src=\"fnbapreview.gif\"><br/>
A 4-player party game where you need to shoot down all the other players.
You only have one bullet, but you can catch it and shoot it again. Bullets also wrap around the screen.
Developed by Brandon Duncan.""",
"<a href=\"http://brandond.itch.io/friday-night-bullet-arena\">itch.io page</a>"),

("Auction Boxing",
"""<img src=\"abpreview.png\"><br/>
A smash bros-like fighting game with unique characters and abilities.
Before each fight, you participate in an auction where you are able to buy items for your fight.
Developed by Nick Pettyjohn and others (who?)""",
"<a href=\"https://github.com/NarPar/AuctionBoxing\">github repository</a>"),

("TODO: Good hydrations",
"""TODO: Description.
Developed by Nick Pettyjohn and others(who?)""",
"<a href=\"https://github.com/NarPar/Good-Hydrations\">github repository</a>"),

("TODO: Puppet master",
"""TODO: Description.
Developed by Nick Pettyjohn and others(who?)""",
"<a href=\"https://github.com/NarPar/PuppetMaster\">github repository</a>"),

("Rock n' Roll Soul",
"""<img src=\"rnrspreview.png\"><br/>
A mix of platforming and physics based puzzle themed about love and rock and roll.
Developed by Brandon Duncan and Nicolas Guillemot (more credits on the github page.)""",
"<a href=\"https://github.com/nguillemot/rock-n-roll-soul\">github repository</a>"),

("Alone",
"""<img src=\"alonepreview.jpg\"><br/>
An artsie game with the theme \"Alone\".
Developed by Nicolas Guillemot.""",
"<a href=\"https://github.com/nguillemot/LD22-Alone\">github repository</a>")

("Credens Divinitatis",
"""<img src=\"credenspreview.gif\"><br/>
An scrolling shooter made in 72 hours for the 2013 Tsukino-Con Game Jam. The theme for the jam was Magical Girls.<br/>
Developed by Jason Lim.""", "")

("Slimageddon",
"""<img src=\"slimageddonpreview.png\"><br/>
A Katamari style game made in 72 hours during the UVIC GameDev Spring 2014 Game Jam. Players control a small slime that absorbs objects in the world around it to get bigger. Getting bigger allows the slime to absorb bigger objects and even buildings!<br/>
Developed by Jason Lim.""", "")

] # End of games list

# =================================================
# =================================================
# From here on is the code that generates the HTML
# -------------------------------------------------

from datetime import datetime

print("<!--DO NOT EDIT THIS FILE BY HAND. THIS FILE IS AUTOMATICALLY GENERATED BY " + __file__ + "-->")
print("<html>")

print("<head>")
print("<title>")
print(title)
print("</title>")
print("</head>")

print("<body>")

print("<h1>" + title + "</h1>")
print("<p>")
print(intro)
print("</p>")

print("<i>Last updated %s</i>" %
    datetime.now().strftime("%B %d %Y"))

for game in games:
    gameHeader = game[0]
    gameBody   = game[1]
    gameFooter = game[2]

    print("<hr/>")
    escapedHeader = gameHeader.replace(' ', '_')
    print("<h2 id=\"#%s\">%s</h2>" %
        (escapedHeader, gameHeader))

    print("<p>")
    print(gameBody)
    print("</p>")

    print("<i>" + gameFooter + "</i>")
    print("</br>")

print("</body>")
print("</html>")
