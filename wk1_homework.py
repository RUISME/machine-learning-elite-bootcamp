# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import time

homework_datafile = input("input homework csv file address")
homework = pd.read_csv(homework_datafile)

#homework 1

pd_start = time.time()
pd_mean = homework.mean(axis="rows")
pd_median = homework.median(axis="rows")
pd_max = homework.max(axis="rows")
pd_min = homework.min(axis="rows")
pd_end = time.time()

np_start = time.time()
np_mean = np.mean(homework, axis='rows')
np_median = np.median(homework, axis=0)
np_max = np.max(homework, axis='rows')
np_min = np.min(homework, axis='rows')
np_end = time.time()

pd_time_spend = pd_end-pd_start
np_time_spend = np_end-np_start

print ("Pandas spend time:", pd_time_spend, "; Numpy spend time:", np_time_spend)


#homework 2

mean_vector = np_mean
distance = abs(homework-np_mean)
avg_distance_each_sample = np.mean(distance,axis=1)
avg_distance = np.mean(avg_distance_each_sample)
std_avg_distance = np.std(avg_distance_each_sample)
drop = avg_distance_each_sample.between(avg_distance-3*std_avg_distance,avg_distance+3*std_avg_distance,inclusive=True)
outlier_cleaned_hw = homework.loc[drop,:]

#outlier_cleaned_hw is the answer
