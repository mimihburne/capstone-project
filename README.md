# capstone-project
Capstone project from Xander Academy

In this project, insights have been produced to show the sales of toothbrushes and toys using sample data from ACME Corporation.
The data is a sample representing a larger set of data. The first steps, covered in main.py involve formatting the data so it is uniform.
Inspecting the value counts showed no nulls present in the dataset, however some provisions may be made to deal with these in a larger dataset.
Column types are found with the find_column_types function to allow for feature engineering in the future.
Once formatted, the file was outputted as a new, clean CSV file.

This dataset could then be used in MySQL Workbench to extract the required data. As required, sales information relating to different
user demographics was found, such as age range and region. When a larger dataset is used, this will help ascertain whether the allocated marketing spend is justifiable for each region.
The effect of seasons on sales was also highlighted. The relevant queries and tables obtained can be found within the repository under **SQL_results**.

The resulting tables were made into views and exported from MySQL back into python for visualisations.
The average cost per acquisition found in research was compared to the average CPA in the data.

**Results**

**Discussion**
