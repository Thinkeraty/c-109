import pandas as pd
import statistics
import csv

df = pd.read_csv('height-weight.csv')
height_list = df['Height(Inches)'].tolist()
weight_list = df['Weight(Pounds)'].tolist()

mean_height = statistics.mean(height_list)
mean_weight = statistics.mean(weight_list)

mode_height = statistics.mode(height_list)
mode_weight = statistics.mode(weight_list)

median_height = statistics.median(height_list)
median_weight = statistics.median(weight_list)

# print("Height: Mean = {}, Median = {} Mode = {}".format(mean_height, median_height, mode_height))
# print("Weight: Mean = {}, Median = {} Mode = {}".format(mean_weight, median_weight, mode_weight))

height_std_deviation = statistics.stdev(height_list)

weight_std_deviation = statistics.stdev(weight_list)

# one, two and three std deviations for height.
height_first_std_deviation_start, height_first_std_deviation_end   = mean_height - height_std_deviation, mean_height + height_std_deviation
height_second_std_deviation_start, height_second_std_deviation_end = mean_height - (2*height_std_deviation), mean_height + (2*height_std_deviation)
height_third_std_deviation_start, height_third_std_deviation_end   = mean_height - (3*height_std_deviation), mean_height + (3*height_std_deviation)

# one, two and three std deviations for weight.
weight_first_std_deviation_start, weight_first_std_deviation_end   = mean_weight - weight_std_deviation, mean_weight + weight_std_deviation
weight_second_std_deviation_start, weight_second_std_deviation_end = mean_weight - (2*weight_std_deviation), mean_weight + (2*weight_std_deviation)
weight_third_std_deviation_start, weight_third_std_deviation_end   = mean_weight - (3*weight_std_deviation), mean_weight + (3*weight_std_deviation)

#percentage of data within one, two and three std deviations for height.
height_list_of_data_within_one_std_deviation   = [result for result in height_list if result > height_first_std_deviation_start  and result < height_first_std_deviation_end]
height_list_of_data_within_two_std_deviation   = [result for result in height_list if result > height_second_std_deviation_start and result < height_second_std_deviation_end]
height_list_of_data_within_three_std_deviation = [result for result in height_list if result > height_third_std_deviation_start  and result < height_third_std_deviation_end]

#percentage of data within one, two and three std deviations for height.
weight_list_of_data_within_one_std_deviation   = [result for result in weight_list if result > weight_first_std_deviation_start  and result < weight_first_std_deviation_end]
weight_list_of_data_within_two_std_deviation   = [result for result in weight_list if result > weight_second_std_deviation_start and result < weight_second_std_deviation_end]
weight_list_of_data_within_three_std_deviation = [result for result in weight_list if result > weight_third_std_deviation_start  and result < weight_third_std_deviation_end]

print("{}% of data for height lies within one standard deviation".format(len(height_list_of_data_within_one_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within two standard deviation".format(len(height_list_of_data_within_two_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within third standard deviation".format(len(height_list_of_data_within_three_std_deviation)*100.0/len(height_list)))
print(".")
print(".")
print(".")
print("{}% of data for weight lies within one standard deviation".format(len(weight_list_of_data_within_one_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within two standard deviation".format(len(weight_list_of_data_within_two_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within third standard deviation".format(len(weight_list_of_data_within_three_std_deviation)*100.0/len(weight_list)))