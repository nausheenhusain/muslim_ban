## this imports pandas, which is a data analysis python library
import pandas as pd

# step one: create 'data_combined.csv': should have a header row with the columns you want to include
# step two: save it as dataframe 'data_combined' (below)
# when we run the script, print() helps us see if this looks right
data_combined = pd.read_csv('/Users/nhusain/Desktop/muslim_ban/data_combined.csv')
print('LANDING CSV:', data_combined)

# step one: download the sheet you want to pull data from and save on your machine
# step two: save this CSV as variable 'pull_data1'
pull_data1 = pd.read_csv('/Users/nhusain/Desktop/muslim_ban/rowaida_muslim_ban - news_reports.csv')
print('NEWS REPORTS', pull_data)

# this puts the columns we are interested in into a dataframe called 'selected'
# important: the columns in this CSV have to be in the same order as the columns in 'data_combined'
selected = pull_data1.filter(['Name','Nationality','Residence'], axis=1)
print('SELECTED COLUMNS', selected)

# this is the step that appends the selected data in 'selected' to the 'data_combined' CSV
selected.to_csv('/Users/nhusain/Desktop/muslim_ban/data_combined.csv', index=False)
print('APPENDED CSV', data_combined)

## hypothetically we could add pull_data2, etc. for each tab downloaded
## and run one script to do everything at once

## might be safer to run this script for each tab downloaded, individually
## so we can check the data each time

## see data_combined_sample.csv in github repo for an example of what this looks like