import pandas as pd
import numpy as np

ACME_data = pd.read_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/test-data.csv')

def find_column_types(df):
    # identifies categorical, boolean and numerical values
    all_cols = list(df.columns)
    numerical_cols_temp = df._get_numeric_data().columns
    categorical_cols = list(set(all_cols) - set(numerical_cols_temp))
    bool_cols = [col for col in all_cols if np.isin(df[col].dropna().unique(), [0, 1, 0.0, 1.0]).all()]
    numerical_cols = list(set(numerical_cols_temp) - set(bool_cols))
    return categorical_cols, bool_cols, numerical_cols

cat_cols, bool_cols, num_cols = find_column_types(ACME_data)

ACME_data = ACME_data.dropna() #remove null rows to deal with potential future nulls

ACME_data['month'] = ACME_data['order_month'].str[:3]
ACME_data['year'] = '20' + ACME_data['order_month'].str[-2:]
ACME_data = ACME_data.drop(['order_month'], axis=1)
ACME_data['uk_region'] = ACME_data['uk_region'].str[3:]

ACME_data['age'] = abs(ACME_data['age']) #make all ages positive

#validation scripts to check. know what format needs to be, run a check against data to check this
#rest: check whether values are expected values- toothbrush, toys: value counts

ACME_data.info()
#print(ACME_data['product'].unique()) #check only toothbrush or toys
#print(ACME_data['uk_region'].unique()) #no South data
#print(ACME_data.dtypes) #one hot encode?
print(ACME_data.value_counts())

ACME_data.to_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/cleaned_ACME_data.csv', index=False)
