#!/usr/bin/env python
# coding: utf-8

# ## Birth Dates in the United States
#
# Some people are too supersititious to have a baby on Friday the 13th, which you can read about [here.](https://fivethirtyeight.com/features/some-people-are-too-superstitious-to-have-a-baby-on-friday-the-13th/)
#
# We'll be working with a data set from the Centers for Disease Control and Prevention's National Center for Health Statistics. The data set has the following structure
#
# * `year` - Year
# * `month` - Month
# * `date_of_month` - Day number of the month
# * `day_of_week` - Day of week, where 1 is Monday and 7 is Sunday
# * `births` - Number of births


# read in CSV file
f = open("births.csv",'r')
text = f.read()
print(text)


# split file into new lines
new_data = text.split('\r')
print(new_data)
#create a dictionary containing
#total number of births for each unique day of the week

data_no_header = new_data[1:len(new_data)]
days_counts = dict()
for line in data_no_header:
    split_line = line.split(",")
    day_of_week = split_line[3]
    num_births = int(split_line[4])
    if day_of_week in days_counts:
        days_counts[day_of_week] = days_counts[day_of_week] + num_births
    else:
        days_counts[day_of_week] = num_births
print(days_counts)
