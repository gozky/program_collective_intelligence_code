#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt


## dataSet
# A dictionary of movie critics and their ratings of a small
# set of movies
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

def sim_distance(prefs, person1, person2):
	sim = {}
	for item in prefs[person1]:
		if item in prefs[person2]:
			sim[item] = 1
	
	if len(sim) == 0:
		return 0

	sum_of_square_diff = sum([ pow(prefs[person1][item] - prefs[person2][item], 2) for item in sim.keys()])


	return 1/(1 + sqrt(sum_of_square_diff))


def sim_pearson(prefs, person1, person2):
	commonList = []
	for item in prefs[person1]:
		if item in prefs[person2]:
			commonList.append(item)

	if len(commonList) == 0:
		return 0

	sum1 = sum([prefs[person1][item] for item in commonList])
	sum2 = sum([prefs[person2][item] for item in commonList])

	# sum of products
	pSum = sum([prefs[person1][item] * prefs[person2][item] for item in commonList])

	## 分子，协方差
	corr = pSum - (sum1 * sum2)/n 

	sum1Sq = sum([pow(prefs[person1][item], 2) for item in commonList])
	sum2Sq = sum([pow(prefs[person2][item], 2) for item in commonList])

	std1 = sum1Sq - pow(sum1, 2)/n
	std2 = sum1Sq - pow(sum2, 2)/n

	## 标准差乘积
	std = sqrt(std1 * std2)

	if std == 0:
		return 0

	return corr/(std)


	




