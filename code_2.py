import pandas as pd
import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

dice_result = []
for i in range(0, 100):
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_result.append(dice_1 + dice_2)

dice_mean = statistics.mean(dice_result)
print(dice_mean)

dice_median = statistics.median(dice_result)
print(dice_median)

dice_mode = statistics.mode(dice_result)
print(dice_mode)

dice_std_deviation = statistics.stdev(dice_result)

first_std_deviation_start, first_std_deviation_end = dice_mean - dice_std_deviation, dice_mean + dice_std_deviation
second_std_deviation_start, second_std_deviation_end = dice_mean - (2*dice_std_deviation), dice_mean + (2*dice_std_deviation)
third_std_deviation_start, third_std_deviation_end = dice_mean - (3*dice_std_deviation), dice_mean + (3*dice_std_deviation)

list_of_data_within_one_std_deviation = [result for result in dice_result if result > first_std_deviation_start and result < first_std_deviation_end ]
list_of_data_within_two_std_deviation = [result for result in dice_result if result > second_std_deviation_start and result < second_std_deviation_end ]
list_of_data_within_three_std_deviation = [result for result in dice_result if result > third_std_deviation_start and result < third_std_deviation_end ]

print("{}% is the data percentage within one std deviation".format(len(list_of_data_within_one_std_deviation)*100/len(dice_result)))
print("{}% is the data percentage within two std deviation".format(len(list_of_data_within_two_std_deviation)*100/len(dice_result)))
print("{}% is the data percentage within three std deviation".format(len(list_of_data_within_three_std_deviation)*100/len(dice_result)))

fig = ff.create_distplot([dice_result], ["Result"], show_hist=False)
fig.add_trace(go.Scatter(x=[dice_mean, dice_mean], y=[0, 0.17], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.17], mode="lines", name="Mean"))
fig.show()
