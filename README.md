# capstone-project
Capstone project from Xander Academy

In this project, insights have been produced to show the sales of toothbrushes and toys using sample data from ACME Corporation.
The data is a sample representing a larger set of data. The first steps, covered in main.py involve formatting the data so it is uniform.
Inspecting the value counts showed no nulls present in the dataset, however some provisions may be made to deal with these in a larger dataset.
Column types are found with the find_column_types function to allow for feature engineering in the future.
Once formatted, the file was outputted as a new, clean CSV file.

This dataset could then be used in MySQL Workbench to extract the required data. As required, sales information relating to different
user demographics was found, such as age range and region. When a larger dataset is used, this will help ascertain whether the allocated marketing spend is justifiable for each region. The effect of seasons on sales was also highlighted. The resulting tables were made into views and exported from MySQL back into python for visualisations. The average cost per acquisition found in research was compared to the average CPA in the data.

**Results**

The SQL script contains queries used to make the tables located in SQL_results. Views were created of these tables so they could be exported to csv files, to be imported to the python script for visualization. The resulting graphs are located in the figures folder. 

It is difficult to draw reliable conclusions from the given data due to the size of the dataset. For example, there were zero sales in the Southern region. With a larger dataset, the relative proportions of regional sales may change to such an extent that any conclusions drawn from this small dataset may turn out to be inaccurate. This must be kept in mind when extracting insights from this data. 

First, an overall comparison of the quantity of toothbrushes and toys sold showed that more toothbrushes than toys were purchased in the dataset. In turn this provides us with more information about toothbrush sales than toy sales, but also shows that it appears toothbrush sales have been more successful. The difference between number of sales and quantities of items sold must be understood; here, the data displayed is showing the number of items bought, however some sales involved more than one item. This is why there were 50 rows in the dataset, but 66 items in total displayed on the pie chart.

The bar chart comparing sales of toothbrushes and toys across different age ranges shows significant differences between the two products, with toothbrush sales only occurring in age ranges 18-24 and 40-60, whereas all toy sales were by individuals aged 25-40. No sales were made to under 18s and over 60s, suggesting marketing towards these age groups has not been so successful. Regional comparison of sales between toothbrushes and toys shows that there was much success in sales of toys in the North East, but no success anywhere else, with 100% of toy sales happening here. The North East was also a good region for toothbrush sales, with 51% of overall sales, and some other sales in the North and South East. Neither product was sold in the South region. Similarly, no sales were made in the summer season, with the majority of sales occurring in the winter time, suggesting a seasonal trend. 

Comparing the CPA values from the research to the actual average CPA values from the table, it can clearly be seen that the data consistently showed lower CPA values. This graph could have shown further insight using error bars to show the variation in obtained data surrounding the average values. It must be considered that the average CPA values from the research only corresponded to the month of October 2021, so may vary with time therefore not provide an accurate comparison to the data, which spans many months.

**Discussion**

It was imperative to allow the code to handle larger datasets to allow for scaling up. For this reason, loops were avoided where possible. Loops were included only in ordering some of the bar chart x axes, to allow the values to be sorted into the desired order without duplicates. Since the loops would go through the rows in SQL views, which never have many rows, even with lots of data, the efficiency would not suffer. It would be advantageous to add more data formatting and cleaning as with larger datasets, there could be more variation in the inputs of various columns. In the original dataset, some of the ages were added with negative numbers, so the absolute values were added to the clean dataset. However, it is difficult to pre-empt what types erroneous entries will arise and how to mitigate against these without knowing exactly what they will be.

Further automation would significantly increase efficiency with larger datasets. This could be done by connecting MySQL and python, rather than having to export the clean csv, import it to SQL Workbench for querying, then exporting the resulting views and reading them back into the python script. This connection would allow programmatic access to the MySQL database, allowing querying within the python script which could immediately result in visualizations.

