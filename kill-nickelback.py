#Define a set that contains tuples. Each tuple should contain two strings:
#The name of an artist and a song by that artist
#Example set

songs = {
    ('Nickelback', 'How You Remind Me'), 
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals')
}

#Using a set comprehension, 
#create a new set that contains all songs that were not performed by Nickelback.

no_nickelback = [ song for song in songs if song[0] != 'Nickelback' ]
print(no_nickelback)