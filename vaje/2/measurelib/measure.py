# -*- coding: utf-8 -*-
import unittest

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

class TestMeasureClasses(unittest.TestCase):
	def test_average(self):
		avg = AverageMeasure()
		avg.update(3)
		avg.update(4)
		avg.update(5)

		self.assertEqual(avg.average, 4)

	def test_occupancy(self):
		occupancy = OccupancyMeasure()
		occupancy.update(3, 10)
		occupancy.update(4, 10)
		occupancy.update(5, 10)

		self.assertAlmostEqual(occupancy.average, 0.4)


if __name__ == '__main__':
	## Without unit tests

	#Simple test of Average Measure
	avg = AverageMeasure()
	avg.update(3)
	avg.update(4)
	avg.update(5)

	assert avg.average == 4


	#Simple test of Occupancy Measure
	occupancy = OccupancyMeasure()
	occupancy.update(3, 10)
	occupancy.update(4, 10)
	occupancy.update(5, 10)

	assert occupancy.average - 0.4 < 0.000001


	# With unit tests
	unittest.main()