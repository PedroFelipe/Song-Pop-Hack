# -*- encoding: utf-8 -*-

# Created by:	Pedro Felipe
#				Edekkun
#				Raphael Chaib
#				Mauricio Calligaris

import urllib

def songpop_hack(link = ""):
	if link == "": print "URL: ";
	else: 
		page = urllib.urlopen(link)
		page = page.read()
		search = page.split("\"genreName\":")
		sec = search[1]


		# First Song
		first_song = sec.split('{"itunesUrl":') [1]
		first = first_song.split('"id":') [0]

		title = first.split('"title": "')[1]
		title = title.split('",')[0]
		print "Song: " + title

		artist = first.split('"artist": "')[1]
		artist = artist.split('",')[0]
		print "Artist: " + artist

		itunes = first.split('"http://')[1]
		itunes = itunes.split('"},')[0]
		print "iTunes: http://" + itunes

		print " --------------- "


		# Second Song
		second_song  = sec.split('{"itunesUrl":') [2]
		second = second_song.split('"id":') [0]

		title = second.split('"title": "')[1]
		title = title.split('",')[0]
		print "Song: " + title

		artist = second.split('"artist": "')[1]
		artist = artist.split('",')[0]
		print "Artist: " + artist

		itunes = second.split('"http://')[1]
		itunes = itunes.split('"},')[0]
		print "iTunes: http://" + itunes

		print " --------------- "


		# Third Song
		third_song = sec.split('{"itunesUrl":') [3]
		third = third_song.split('"id":') [0]

		title = third.split('"title": "')[1]
		title = title.split('",')[0]
		print "Song: " + title

		artist = third.split('"artist": "')[1]
		artist = artist.split('",')[0]
		print "Artist: " + artist

		itunes = third.split('"http://')[1]
		itunes = itunes.split('"},')[0]
		print "iTunes: http://" + itunes

		print " --------------- "


		# Fourth Song
		fourth_song = sec.split('{"itunesUrl":') [4]
		fourth = fourth_song.split('"id":') [0]

		title = fourth.split('"title": "')[1]
		title = title.split('",')[0]
		print "Song: " + title

		artist = fourth.split('"artist": "')[1]
		artist = artist.split('",')[0]
		print "Artist: " + artist

		itunes = fourth.split('"http://')[1]
		itunes = itunes.split('"},')[0]
		print "iTunes: http://" + itunes

		print " --------------- "


		# Fifth Song
		fifth_song = sec.split('{"itunesUrl":') [5]
		fifth = fifth_song.split('"id":') [0]

		title = fifth.split('"title": "')[1]
		title = title.split('",')[0]
		print "Song: " + title

		artist = fifth.split('"artist": "')[1]
		artist = artist.split('",')[0]
		print "Artist: " + artist

		itunes = fifth.split('"http://')[1]
		itunes = itunes.split('"},')[0]
		print "iTunes: http://" + itunes


i = range(0,99)

for i in i:	
        link = raw_input("URL: ")
        if link.startswith('--'):
                link = link.replace('--\n', '');
                a = link.split(" ");
                link = a[2]
        else: 
                a = link.split(" ");
                link = a[2]

		try: songpop_hack(link);
		except: print "Error! Check the URL."