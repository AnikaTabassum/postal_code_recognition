# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
class findWhiteImage:
	def get_image_no(self, csvFilename):
		# csvFilename
		data = pd.read_csv(csvFilename)
		# input data
		df = data[["imageNo", "value"]]
		# scatterplot of inputs data
		# plt.scatter(df["imageNo"], df["value"])
		# plt.show()
		# new_df=df["Contribution"].copy()
		# create arrays
		X = df.values
		cutOffVal=4.0/len(X)
		cutOffVal=cutOffVal*100
		print(cutOffVal)
		# instantiate model
		nbrs = NearestNeighbors(n_neighbors = 5)
		# fit model
		nbrs.fit(X)
		# distances and indexes of k-neaighbors from model outputs
		distances, indexes = nbrs.kneighbors(X)
		# print("distances" , distances, indexes)
		# plot mean of k-distances of each observation
		mean_dist=[]
		for dist in distances:
			print("dist ", dist.mean())
			mean_dist.append(dist.mean())
		# print("mean_dist",mean_dist, distances.mean())
		# plt.plot(distances.mean(axis =1))
		# plt.show()
		dsds=distances.mean()
		# print("dsds", distances.mean())
		perc=np.percentile(mean_dist, cutOffVal)
		print(perc)
		# visually determine cutoff values > 0.9
		outlier_index = np.where(distances.mean(axis = 1) >perc)
		# print("outlier_index",outlier_index)
		# filter outlier values
		outlier_values = df.iloc[outlier_index]
		print("outlier_values",outlier_values['imageNo'].values)
		return outlier_values['imageNo'].values

# findWhiteImage().get_image_no('dataset/csv/2_b.jpg.csv')
