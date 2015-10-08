# -*- coding: utf-8 -*-

def main():
	f = open('bicikelj.csv')
	data = []
	unique_station_names = []

	for line in f.readlines():
		preneseno, stevilka, ime, timestamp, koles, prostih, skupno = line.split(',')
		skupno.strip()

		data.append({
			'synced': preneseno,
			'station_num': stevilka,
			'station_name': ime,
			'timestamp': timestamp,
			'bikes_count': koles,
			'spaces_count': prostih,
			'total_count': skupno
		})

		if ime not in unique_station_names:
			unique_station_names.append(ime)

	f.close()

	# throw away first line
	all_data = data[1:]

	# remove 'ime' from station names
	unique_station_names.remove('ime')

	# print(bikes_station_average(all_data, 'BARJANSKA C.-CENTER STAREJ\xc5\xa0IH TRNOVO'))

	for station_name in unique_station_names:
		print("{0} has {1} bikes on average".format(station_name, bikes_station_average(all_data, station_name)))

def bikes_station_average(all_data, station_name):
	bikes_count = 0
	count = 0
	for measurment in all_data:
		if measurment['station_name'] == station_name:
			bikes_count += int(measurment['bikes_count'])
			count += 1

	return bikes_count / count


if __name__ == '__main__':
	main()