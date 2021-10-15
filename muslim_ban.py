## this imports pandas, which is a data analysis python library
import pandas as pd

## this creates a dataframe out of the muslim ban csv
df = pd.read_csv('path_to_muslim_ban.csv')

## this uses the duplicated function in pandas to check for duplicates
## using the below three columns
show_duplicates = df[df.duplicated(['name','nationality/country','current_city'])]

## this prints the output of show_duplicates to the terminal
print(show_duplicates)



# for nausheen's machine:
# import pandas as pd

# df = pd.read_csv('/Users/nhusain/Desktop/muslim_ban/muslim_ban.csv')

# show_duplicates = df[df.duplicated(['name','nationality/country','current_city'])]
# print(show_duplicates)