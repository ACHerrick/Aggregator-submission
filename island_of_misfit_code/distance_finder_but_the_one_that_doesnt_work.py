'''
This file was a first pass at developing an algorithm for calculating minimum
Starbucks distance with better than n^2 efficiency. 

The idea was to use the concept of quadtrees (see here: https://en.wikipedia.org/wiki/Quadtree).
The original plan was as follows:

-- Create a lat/long grid by using the min/max lat/long among a set of points
to find boundary conditions. 
-- Split the grid into 4 equal sections by dividing along midpoints
-- Assign all lat/long pairs into buckets based on their location
-- Count the number of nodes in each bucket - if it exceeds a threshold of 
algorithmic complexity (say 5-10 restaurants), return to step 2.
-- Once all locations are broken into smaller buckets, compute distances between
nodes within the same bucket, or (if a bucket has only a single node) between
neighboring nodes.

This approach would dramatically reduce computation time for large numbers of nodes,
since distances would never need to be calculated for more than a fairly small number
of nodes.

The problem with this algorithm is that fails to account for points that are closer 
to each other than points within their own boxes (because they are close to a 
shared edge, for example). This problem is necessarilly amplifield for points 
that are alone in their boxes. While expanding the search range could plausbily
help mitigate this problem, at some point it seemed likely too much of the algorithmic
efficiency was being lost along the way.

The BallTree method was instead used, and can be seen in detail in find_distances.py

Not pictured: hours spent installing Anaconda and setting up a server in order to
install SciPy, in order to install BallTree and NodeTree classes. (Ultimately I
couldn't get the server to work, and so SciPy was used through the VM instead)
'''


import csv
import sqlite3
import random

def generate_points(i):
    # Generates random numbers, and truncates them.
    points = []

    for entry in range(i):
        a = random.uniform(0, 10)
        a = int(a*10000 + 0.5)/10000
        b = random.uniform(0, 10)
        b = int(b*10000 + 0.5)/10000
        points.append((a,b))
    return points

def find_initial_boundaries(points):
	'''
	Given a set of points, determines an initial boundary set based
	on min/max of lat/long pairs
	'''

	# Find outer boxes
	min_x = points[0][0]
	max_x = points[0][0]
	min_y = points[0][1]
	max_y = points[0][1]
	for entry in points:
		if entry[0] < min_x:
			min_x = entry[0]
		if entry[0] > max_x:
			max_x = entry[0]
		if entry[1] < min_y:
			min_y = entry[1]
		if entry[1] > max_y:
			max_y = entry[1]

	boundaries = (min_x, max_x, min_y, max_y)

	return boundaries



def make_partition(point_bucket, boundaries):
	'''
	This was the first pass at a function which iteratively created smaller
	and smaller sub-buckets. It is not fully functional here, but it does succeed
	in partitioning smaller and smaller buckets until a sufficiently small number
	of points are contained (has not been implemented for all points).

	When writing this function, I realized the problems with the algorithm and
	renewed my search for a more efficient method.
	'''

	x_divider = (boundaries[0] + boundaries[1])/2
	y_divider = (boundaries[2] + boundaries[3])/2

	upleft_bucket = []
	upright_bucket = []
	downleft_bucket = []
	downright_bucket = []

	upleft_boundary = (boundaries[0], x_divider, y_divider, boundaries[3])
	upright_boundary = (x_divider, boundaries[1], y_divider, boundaries[3])
	downleft_boundary = (boundaries[0], x_divider, boundaries[2], y_divider)
	downright_boundary = (x_divider, boundaries[1], boundaries[2], y_divider)

	for point in point_bucket:
		if point[0] <= x_divider:
			if point[1] <= y_divider:
				downleft_bucket.append(point)
			else:
				upleft_bucket.append(point)
		else:
			if point[1] <= y_divider:
				downright_bucket.append(point)
			else:
				upright_bucket.append(point)

	if len(upleft_bucket) > 5:
		print("Up Left:", len(upleft_bucket))
		return make_partition(upleft_bucket, upleft_boundary)

	if len(upright_bucket) > 5:
		print("Up Right:", len(upright_bucket))
		return make_partition(upright_bucket, upright_boundary)

	if len(downleft_bucket) > 5:
		print("Down Left:", len(downleft_bucket))
		return make_partition(downleft_bucket, downleft_boundary)

	if len(downright_bucket) > 5:
		print("Down Right:", len(downright_bucket))
		return make_partition(downright_bucket, downright_boundary)

	#return upleft_bucket
