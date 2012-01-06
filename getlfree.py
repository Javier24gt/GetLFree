# -*- coding: utf-8 *-*
import sqlite3
connection = sqlite3.connect('db/freevana.db')
cursor = connection.cursor()
nombre = raw_input('Ingrese la nombre: ')
print nombre
query = 'SELECT * FROM series where name like "%s%s%s"' % ("%", nombre, "%")
cursor.execute(query)
i = 0
series = []
for row in cursor:
    print i, ' -> ', row[1]
    series.append(row)
    i = i + 1
id_nombre = int(raw_input('Seleccione la serie: '))
serie = series[id_nombre][0]
print series[id_nombre][1]


query = 'SELECT * FROM series_seasons where series_id=%s order by name' % serie
cursor.execute(query)
series_seas = []
for row in cursor:
    print ' -> ', row[3]
    series_seas.append(row)
season = int(raw_input('Seleccione la temporada: '))
print series_seas[season - 1][3]
print ""

query = 'SELECT * FROM series where id=%s' % serie
cursor.execute(query)
for row in cursor:
    print row
print ""

query = 'SELECT * FROM series_seasons WHERE series_id=%s and number=%s' % (serie, season)
cursor.execute(query)
for row in cursor:
    print row
print ""

query = 'SELECT id FROM series_seasons WHERE series_id=%s and number=%s' % (serie, season)
cursor.execute(query)
for row in cursor:
    temporada = row[0]

query = 'SELECT s.definition, s.url, e.url, e.id,se.number FROM series_episode_sources s inner join series_episodes e on e.id=s.series_episode_id inner join series_episodes se on se.id=s.series_episode_id WHERE e.season_id=%s and s.definition=360 order by se.number ASC' % temporada

subti = []
source_sub = 'http://sc.cuevana.tv/files/s/sub/%s_ES.srt'
cursor.execute(query)
for row in cursor:
    print row
    subti.append(source_sub % row[3])

for col in subti:
    print col
cursor.close()
connection.close()
