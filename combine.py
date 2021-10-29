## this imports pandas, which is a data analysis python library
import pandas as pd

# step one: download the sheet you want to pull data from and save on your machine
# step two: save this CSV as variable 'pull_data1' (below command)
pull_data1 = pd.read_csv('/Users/nhusain/Desktop/muslim_ban/rowaida_muslim_ban - news_reports.csv')

# this was used as a test for pandas handling empty cells
pull_data2 = pd.read_csv('/Users/nhusain/Desktop/muslim_ban/data_combined.csv')

# this puts the columns we are interested in into dataframes called 'selected1', etc.
# important: the columns in this CSV have to be in the same order as the columns in 'data_combined'
selected1 = pull_data1.filter(['Name','Nationality','Residence'], axis=1)
selected2 = pull_data2.filter(['Name','Nationality','Residence'], axis=1)

# this is the step that appends the selected data in 'selected' to the 'data_combined' CSV
# data_combined.csv should be created beforehand with a header row and at least one empty row below that
selected1.to_csv('/Users/nhusain/Desktop/muslim_ban/data_combined_sample.csv', mode="a", header=False, index=False)
selected2.to_csv('/Users/nhusain/Desktop/muslim_ban/data_combined_sample.csv', mode="a", header=False, index=False)
print('APPENDED TO CSV')

## hypothetically we could add pull_data2, etc. for each tab downloaded
## and run one script to do everything at once

## might be safer to run this script for each tab downloaded, individually
## so we can check the data each time

## see data_combined_sample.csv in github repo for an example of what the output looks like
