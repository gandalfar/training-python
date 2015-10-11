# -*- coding: utf-8 -*-
import csv
from measurelib.measure import AverageMeasure, OccupancyMeasure

def main(input_filename):
	input_file = open(input_filename)
	bicikelj_reader = csv.DictReader(input_file, delimiter=',')

	station_bikes = {}
	station_occupancy = {}

	for line in bicikelj_reader:
		station_name = line['ime']
		bikes = int(line['koles'])
		total_spaces = int(line['skupno'])

		if station_name not in station_bikes:
			station_bikes[station_name] = AverageMeasure()
			station_occupancy[station_name] = OccupancyMeasure()

		station_bikes[station_name].update(bikes)
		station_occupancy[station_name].update(bikes, total_spaces)

	for station_name, station_average in station_bikes.items():
		print("{0} has {1} bikes on average".format(station_name, station_average.average))

	for station_name, station_average in station_occupancy.items():
		print("{0} has {1} occupancy on average".format(station_name, station_average))

if __name__ == '__main__':
	main(input_filename='bicikelj.csv')
