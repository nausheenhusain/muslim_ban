## this imports pandas, which is a data analysis python library
import pandas as pd

# step one: download the sheet you want to pull data from and save on your machine
# step two: save this CSV as variable 'pull_data1' (below command)
pull_data1 = pd.read_csv('/Users/nhusain/Desktop/muslim_ban/combine_script/yama.csv')
print(pull_data1)

# this puts the columns we are interested in into dataframes called 'selected1', etc.
# important: the columns in this CSV have to be in the same order as the columns in 'compiled_sheet'
selected1 = pull_data1.filter(['Name','Nationality','Residence','Date Applied for Visa', 'Date of Visa Interview','Parent/Child Separation','Partner Separation','Sibling Separation','Grandparent/Grandchild Separation','Babies Born Waiting','Death','Medical/Health Needs','Financial Loss','Other Loss','Wait Time','Source','Link','from_sheet'], axis=1)
print(selected1)

# this is the step that appends the selected data in 'selected' to the 'data_combined' CSV
# data_combined.csv should be created beforehand with a header row and at least one empty row below that
selected1.to_csv('/Users/nhusain/Desktop/muslim_ban/combine_script/compiled_sheet.csv', mode="a", header=False, index=False)
print('APPENDED TO CSV')

## see data_combined_sample.csv in github repo for an example of what the output looks like