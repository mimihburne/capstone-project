import pandas as pd
import numpy as np

#read data file
ACME_data = pd.read_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/test-data.csv')

def find_column_types(df):
    #identify categorical, boolean and numerical values
    all_cols = list(df.columns)
    numerical_cols_temp = df._get_numeric_data().columns
    categorical_cols = list(set(all_cols) - set(numerical_cols_temp))
    bool_cols = [col for col in all_cols if np.isin(df[col].dropna().unique(), [0, 1, 0.0, 1.0]).all()]
    numerical_cols = list(set(numerical_cols_temp) - set(bool_cols))
    return categorical_cols, bool_cols, numerical_cols

cat_cols, bool_cols, num_cols = find_column_types(ACME_data)

ACME_data = ACME_data.dropna() #remove null rows to deal with potential future nulls

#formatting data
ACME_data['month'] = ACME_data['order_month'].str[:3]
ACME_data['year'] = '20' + ACME_data['order_month'].str[-2:]
ACME_data = ACME_data.drop(['order_month'], axis=1)
ACME_data['uk_region'] = ACME_data['uk_region'].str[3:]
ACME_data['age'] = abs(ACME_data['age']) #make all ages positive

#use validation scripts to check required format is followed
#check whether values are as expected, eg. sum of value counts of toothbrush, toys = total no.rows

ACME_data.info()
#print(ACME_data['product'].unique()) ##check whether values are as expected; sum of value counts of toothbrush, toys = total no.rows
#print(ACME_data['uk_region'].unique()) #shows no South data in current dataset, will skew findings
#print(ACME_data.dtypes) #potential for one hot encoding
print(ACME_data.value_counts())

#save to a new file for analysis/visualisation
ACME_data.to_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/cleaned_ACME_data.csv', index=False)