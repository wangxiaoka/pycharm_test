# -*- coding: utf-8 -*-
import math

def cos_dist(a, b):
	if len(a) != len(b):
		return None
	part_up = 0.0
	a_sq = 0.0
	b_sq = 0.0
	for a1, b1 in zip(a, b):
		part_up += a1 * b1
		a_sq += a1 ** 2
		b_sq += b1 ** 2
	part_down = math.sqrt(a_sq * b_sq)
	if part_down == 0.0:
		return None
	else:
		return part_up / part_down


if __name__ == "__main__":
	# d1 = (0.5, 0.8, 0.3)
	# d2 = (0.9, 0.4, 0.2)
	# q = (1.5, 1.0, 0)
	d1 = (0, 1, 2)
	d2 = (1, 4, 6)
	q = (0, 2, 4)
	print cos_dist(d1, q)
	print cos_dist(d2, q)