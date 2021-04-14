import pandas as pd

# import the data from the .csv file as a DataFrame: pd.read_csv('<filename/url>', index_col = <column number>)
reviews = pd.read_csv("ign.csv", index_col = 2)

#print(reviews)
# print all the row names using .index Attribute

# print all the column names using .columns attribute
#print(reviews.columns)

# helpful methods: .max(), .min(), .mean(), .median(), .std()

# Boolean indexing: <df>[<conditional involving dataframe column>]


# print all the unique values in column using .unique()

#using .describe() for summary statistics

# other methods: .value_counts(), .sort_index(), .sort_values(by=[<'column'>], ascending = <bool, default True>, .head(), .head(<int default 5>), .tail(<int default 5>). .to_csv(<'filename'>) )


# checking if string contains a specific string (<df>[<dfcolumn>.str.contains(<string>)])


# Using Python, identify which what is is the most common month for games to be released


# Have Python identify all the games released in 2008 and sort them in descending score. Save the results in a .csv file named '2008.csv'


# Have Python identify all the games on Game Boy Advance that were labeled masterpieces. Save the results in a .csv file name 'GBA.csv'