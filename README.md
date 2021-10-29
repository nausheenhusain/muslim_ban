# muslim_ban

Currently, these files are to determine if there are duplicates in this data, and to combine several datasets into one longer CSV. This longer CSV will eventually be used for data analysis for this story.

**> muslim_ban.csv**
This is a file downloaded from data collected in Google Sheets: https://docs.google.com/spreadsheets/d/1pwgCCllPxyA60Y-tOzuiV-06PYoXfzohqSpL4cYm4xE/edit#gid=0.

**> muslim_ban.py**
This checks for duplicates in muslim_ban.csv using Pandas.

**> combine.py**
This sets up a structure for choosing certain columns from the variety of datasets Rowaida has compiled, and appending to one CSV.

**> data_combined_sample.csv**
This is a sample output file of 'combine.py'. It has name, nationality and residence data from the 'news_reports' tab in Google Sheets.

**> muslim_ban.Rproj**
These are any R files for the Muslim Ban project.

**> find_duplicates.Rhistory**
This finds duplicates in muslim_ban.csv using R's dplyr.
