import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#connect to server instead of having to import
toys_region = pd.read_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/toys_region.csv')
toothbrush_region = pd.read_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/toothbrush_region.csv')
toys_agegroup = pd.read_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/toys_agegroup.csv')
toothbrush_agegroup = pd.read_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/toothbrush_agegroup.csv')
toys_season = pd.read_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/toys_season.csv')
toothbrush_season = pd.read_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/toothbrush_season.csv')
overall = pd.read_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/overall_performance.csv')
CPA = pd.read_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/CPA.csv')
actual_CPA = pd.read_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/CPA_actual.csv')
df = pd.read_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/cleaned_ACME_data.csv')

#CPA comparison
combined_CPA = pd.concat([CPA, actual_CPA], axis=1)
del combined_CPA['uk_region']
combined_CPA = combined_CPA.fillna(0) #do something with null values that come from insufficient data
#print(combined_CPA.head())

def overall_comparison_pie():
    explode = (0.2, 0)
    plt.pie(overall['Total_quantity'], labels=overall['Total_quantity'], explode=explode,  autopct='%.0f%%', shadow=True)
    plt.title('Total Sales of Toys and Toothbrushes')
    plt.legend(labels=overall['product'], loc=1)
    plt.savefig('overall_comparison_pie')
    plt.show()

def region_comparison_pies():
    fig, axs = plt.subplots(2)
    fig.suptitle('Region Comparisons for Toys and Toothbrush Sales')
    axs[0].pie(toothbrush_region['Total_quantity'], labels=toothbrush_region['Total_quantity'],  autopct='%.0f%%', shadow=True)
    axs[1].pie(toys_region['Total_quantity'], labels=toys_region['Total_quantity'], autopct='%.0f%%', shadow=True)
    fig.legend(labels=toothbrush_region['uk_region'], loc = 'right')
    fig.savefig('region_comparison_pies')
    plt.show()

def age_group_bar(): #axes, ordered
    age_groups = ['18 and Under', '18-24', '25-40', '40-60', '60 and Over']
    plt.bar(toys_agegroup['age_group'], toys_agegroup['Total_quantity'])
    plt.bar(toothbrush_agegroup['age_group'], toothbrush_agegroup['Total_quantity'])
    plt.savefig('age_group_bar')
    plt.show()
    #reorder

def season_bar():
    plt.bar(toys_season['season'], toys_season['Total_quantity'])
    plt.bar(toothbrush_season['season'], toothbrush_season['Total_quantity'])
    plt.savefig('season_bar')
    plt.show()

def countplots():
    #combining both product types for plotting, with grouped ages/seasons
    toothbrush_season['product'] = pd.Series(['toothbrush' for x in range(len(toothbrush_season.index))])
    toys_season['product'] = pd.Series(['toys' for x in range(len(toys_season.index))])
    toys_toothbrush_season = pd.concat([toothbrush_season, toys_season], axis=0)

    toothbrush_agegroup['product'] = pd.Series(['toothbrush' for x in range(len(toothbrush_agegroup.index))])
    toys_agegroup['product'] = pd.Series(['toys' for x in range(len(toys_agegroup.index))])
    toys_toothbrush_agegroup = pd.concat([toothbrush_agegroup, toys_agegroup], axis=0)

    #still not working as returning 1's for the y axis instead of 'total quantity'
    age_groups = ['18 and Under', '18-24', '25-40', '40-60', '60 and Over']
    sns.countplot(x='age_group', y='Total_quantity', hue='product', data = toys_toothbrush_agegroup, order=age_groups)
    plt.show()

# overall_comparison_pie()
# region_comparison_pies()
# age_group_bar()
# season_bar()
