import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#style & font
plt.style.use(['ggplot'])
plt.rcParams['font.family'] = 'serif'

#import SQL views- would be better to connect to server instead of having to import
overall = pd.read_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/overall_performance.csv')
toys_region = pd.read_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/toys_region.csv')
toothbrush_region = pd.read_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/toothbrush_region.csv')
toys_agegroup = pd.read_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/toys_agegroup.csv')
toothbrush_agegroup = pd.read_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/toothbrush_agegroup.csv')
toys_season = pd.read_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/toys_season.csv')
toothbrush_season = pd.read_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/toothbrush_season.csv')
CPA = pd.read_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/CPA.csv')
actual_CPA = pd.read_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/CPA_actual.csv')
df = pd.read_csv('C:/Users/MimiHoulihan-Burne/OneDrive - JCW Resourcing/Data engineering/Capstone/cleaned_ACME_data.csv')

def overall_comparison_pie():
    #pie chart displaying overall comparison of Toys and Toothbrushes bought
    explode = (0.2, 0)
    plt.pie(overall['Total_quantity'], labels=overall['Total_quantity'], explode=explode,  autopct='%.0f%%', shadow=True)
    plt.title('Total Sales of Toys and Toothbrushes')
    plt.legend(labels=overall['product'], loc=1)
    plt.savefig('overall_comparison_pie')
    plt.show()

def region_comparison_pies():
    #pie chart displaying variation in sales of toothbrushes and toys across different regions
    fig, axs = plt.subplots(2)
    fig.suptitle('Region Comparisons for Toys and Toothbrush Sales')
    axs[0].pie(toothbrush_region['Total_quantity'], labels=toothbrush_region['Total_quantity'],  autopct='%.0f%%', shadow=True)
    axs[1].pie(toys_region['Total_quantity'], labels=toys_region['Total_quantity'], autopct='%.0f%%', shadow=True)
    fig.legend(labels=toothbrush_region['uk_region'], loc = 'right')
    fig.savefig('region_comparison_pies')
    plt.show()

def age_group_bar(): #axes, ordered
    #combining both product types for plotting, with grouped ages
    toothbrush_agegroup['product'] = pd.Series(['toothbrush' for x in range(len(toothbrush_agegroup.index))])
    toys_agegroup['product'] = pd.Series(['toys' for x in range(len(toys_agegroup.index))])
    toys_toothbrush_agegroup = pd.concat([toothbrush_agegroup, toys_agegroup], axis=0)

    #bar chart displaying difference in sales of toothbrushes and toys across different age groups
    plotdata = toys_toothbrush_agegroup.pivot_table('Total_quantity', ['age_group'], 'product')
    plotdata.plot(kind='bar')
    plt.title('Sales of Toys and Toothbrushes by Age Group')
    plt.ylabel('Sales')
    plt.xlabel('Age Groups')
    plt.savefig('age_group_bar')
    plt.show()

def season_bar():
    #combining both product types for plotting, with grouped seasons
    toothbrush_season['product'] = pd.Series(['toothbrush' for x in range(len(toothbrush_season.index))])
    toys_season['product'] = pd.Series(['toys' for x in range(len(toys_season.index))])
    toys_toothbrush_season = pd.concat([toothbrush_season, toys_season], axis=0)

    #bar chart displaying difference in sales of toothbrushes and toys across different seasons
    plotdata = toys_toothbrush_season.pivot_table('Total_quantity', ['season'], 'product')
    plotdata.plot(kind='bar')
    plt.title('Sales of Toys and Toothbrushes by Season')
    plt.ylabel('Sales')
    plt.xlabel('Season')
    plt.savefig('season_bar')
    plt.show()
    #order in certain order?
def CPA_bar():
    # CPA comparison
    combined_CPA = pd.concat([CPA, actual_CPA], axis=1)
    del combined_CPA['uk_region']
    combined_CPA = combined_CPA.fillna(0)  # do something with null values that come from insufficient data
    print(combined_CPA.head())

    plotdata = combined_CPA.pivot_table('Total_quantity', ['region'], 'product')
    plotdata.plot(kind='bar')
    #want: region as x axis
    #average and expected as 2 bars
    #cpa values as y axis

#overall_comparison_pie()
#region_comparison_pies()
#age_group_bar()
#season_bar()
CPA_bar()
