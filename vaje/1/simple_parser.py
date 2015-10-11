# -*- coding: utf-8 -*-

def main():
	f = open('bicikelj.csv', 'U')
	data = []
	unique_station_names = []

	for line in f.readlines():
		# remove \n from the line ending
		line = line.strip()
		preneseno, stevilka, ime, timestamp, koles, prostih, skupno = line.split(',')

		single_measurement = {
			'synced': preneseno,
			'station_num': stevilka,
			'station_name': ime,
			'timestamp': timestamp,
			'bikes_count': koles,
			'spaces_count': prostih,
			'total_count': skupno		
		}

		data.append(single_measurement)

		if ime not in unique_station_names:
			unique_station_names.append(ime)

	# throw away first line
	all_data = data[1:]

	# remove 'ime' from station names
	unique_station_names.remove('ime')

	for station_name in unique_station_names:
		station_average = bikes_station_average(all_data, station_name)
		print("{0} has {1} bikes on average".format(station_name, station_average))

def bikes_station_average(all_data, station_name):
	bikes_count = 0
	count = 0
	for measurement in all_data:
		if measurement['station_name'] == station_name:
			bikes_count += int(measurement['bikes_count'])
			count += 1

	return bikes_count / count

if __name__ == '__main__':
	main()