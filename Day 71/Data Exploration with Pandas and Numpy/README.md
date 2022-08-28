


# Exploring Data with Pandas


1. First go to google collab and then explore the following command

        import pandas as pd
        import numpy as np
        df = pd.read_csv("file Path")


2. Explore your DataFrame and find out the number of rows and columns as well as the column names.

        df.head()       # Shows top rows and columns
        df.tails()      # for last rows and columns
        df.shape        # Show number of rows and columns

3. For cleaning the data
 
        df.dropna()     # for droping or deleting enteries which are empty.

4. Access Entire Columns

        df['column name']            #for accessing single column
        df[['column name 1', 'column name 2', 'column name 3']] # For multiple Columns

5. Access individual cells in a DataFrame 

        df['column name'][index]        #via index it give single entry
        df['column name'].loc["column name]    # Via label
        df.iloc[index]                  #Access group of rows and columns by integer position(s).

6. The largest and smallest values, as well as their positions, can be found with methods like 
        
        df['Column name'].max()             # Give maximum entry of column.
        df['Column name'].min()             # Give minimum entry of column.
        df['Column name'].idxmax()          # Give maximum entry index in column.
        df['Column name'].idxmin()          # Give maximum entry index in column.

7. Sorting 

        df['Column name'].sort_values()     # For sorting

8. grouping entries that belong to a particular category.

        
        df.groupby('Column name').count()


### Documentation
https://pandas.pydata.org/docs/reference/frame.html