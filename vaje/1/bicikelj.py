# -*- coding: utf-8 -*-
import csv

# class BicikeljCsvReader(object):
# 	def __init__(self, filename):
# 		self.file = open(filename, 'r')
# 		self.csvreader = csv.DictReader(self.file, delimiter=',')

# 	def __iter__(self):
# 		return self

# 	def next(self):
# 		return self.csvreader.next()

class AverageMeasure(object):
	def __init__(self):
		self.count = 0
		self.sum = 0

	def update(self, value):
		self.count += 1
		self.sum += value

	@property
	def average(self):
		return self.sum / self.count

	def __repr__(self):
		return self.average
		# return "Average: {0} over {1} values".format(self.average, self.count)

class OccupancyMeasure(AverageMeasure):
	def update(self, value, total):
		occupancy_value = value / float(total)
		super(OccupancyMeasure, self).update(occupancy_value)

	def __repr__(self):
		average_percent = self.average * 100
		return "{0:.1f}%".format(average_percent)

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
	main(input_filename='../data/bicikelj.csv')