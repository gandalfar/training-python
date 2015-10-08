# -*- coding: utf-8 -*-


class BicikeljParser:
	
	def __init__(self, filename):
		self.filename = filename

		self.data = []
		self.unique_station_names = []

		self._read_data()

	def _read_data(self):
		data = []
		unique_station_names = []

		f = open(self.filename)

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

		# remove 'ime' from station names
		unique_station_names.remove('ime')

		# remove headers
		self.data = data[1:]
		self.unique_station_names = unique_station_names

	def _station_average(self, station_name):
		bikes_count = 0
		count = 0
		for measurment in self.data:
			if measurment['station_name'] == station_name:
				bikes_count += int(measurment['bikes_count'])
				count += 1

		return bikes_count / count


	def get_stations_average(self):
		results = {}
		for station_name in self.unique_station_names:
			results[station_name] = self._station_average(station_name)

		return results


def main():
	bicikelj = BicikeljParser(filename='bicikelj.csv')
	station_averages = bicikelj.get_stations_average()

	for station in station_averages:
		print("{0} has {1} bikes on average".format(station, station_averages[station]))

if __name__ == '__main__':
	main()