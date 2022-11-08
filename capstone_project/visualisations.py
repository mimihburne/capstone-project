import pandas as pd
import matplotlib.pyplot as plt

#style & font
plt.style.use(['ggplot'])
plt.rcParams['font.family'] = 'serif'

#import SQL views
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
    #pie chart displaying overall comparison of toys and toothbrushes bought
    explode = (0.2, 0)
    plt.pie(overall['Total_quantity'], labels=overall['Total_quantity'], explode=explode,  autopct='%.0f%%', shadow=True)
    plt.title('Total Sales of Toys and Toothbrushes')
    plt.legend(labels=overall['product'], loc=1)
    plt.savefig('Figures/overall_comparison_pie')
    plt.show()

def region_comparison_pies():
    #pie chart displaying variation in sales of toothbrushes and toys across different regions
    fig, axs = plt.subplots(2)
    fig.suptitle('Region Comparisons for Toys and Toothbrush Sales')
    axs[0].pie(toothbrush_region['Total_quantity'], labels=toothbrush_region['Total_quantity'],  autopct='%.0f%%', shadow=True)
    axs[0].set_title('Toothbrush')
    axs[1].pie(toys_region['Total_quantity'], labels=toys_region['Total_quantity'], autopct='%.0f%%', shadow=True)
    axs[1].set_title('Toys')
    fig.legend(labels=toothbrush_region['uk_region'], loc = 'right')
    fig.savefig('Figures/region_comparison_pies')
    plt.show()

def age_group_bar(): #axes, ordered
    #combining both product types for plotting, with grouped ages
    toothbrush_agegroup['product'] = pd.Series(['toothbrush' for x in range(len(toothbrush_agegroup.index))])
    toys_agegroup['product'] = pd.Series(['toys' for x in range(len(toys_agegroup.index))])
    toys_toothbrush_agegroup = pd.concat([toothbrush_agegroup, toys_agegroup], axis=0)

    #bar chart displaying difference in sales of toothbrushes and toys across different age groups
    #sort age groups into order, removing duplicates
    age_order = ['Under 18', '18-24', '25-40', '40-60', 'Over 60']
    sort_agegroups = sorted(toys_toothbrush_agegroup['age_group'], key=age_order.index)
    agegroups_ordered = []
    [agegroups_ordered.append(item) for item in sort_agegroups if item not in agegroups_ordered]

    plotdata = toys_toothbrush_agegroup.pivot_table('Total_quantity', ['age_group'], 'product')
    plotdata.loc[agegroups_ordered].plot(kind='bar')
    plt.title('Sales of Toys and Toothbrushes by Age Group')
    plt.ylabel('Sales')
    plt.xlabel('Age Groups')
    plt.savefig('Figures/age_group_bar')
    plt.show()

def season_bar():
    #combining both product types for plotting, with grouped seasons
    toothbrush_season['product'] = pd.Series(['toothbrush' for x in range(len(toothbrush_season.index))])
    toys_season['product'] = pd.Series(['toys' for x in range(len(toys_season.index))])
    toys_toothbrush_season = pd.concat([toothbrush_season, toys_season], axis=0)

    #bar chart displaying difference in sales of toothbrushes and toys across different seasons
    #sort seasons into order, removing duplicates
    season_order = ["Spring", "Summer", "Autumn", "Winter"]
    sort_seasons = sorted(toys_toothbrush_season['season'], key=season_order.index)
    seasons_ordered = []
    [seasons_ordered.append(item) for item in sort_seasons if item not in seasons_ordered]

    plotdata = toys_toothbrush_season.pivot_table('Total_quantity', ['season'], 'product')
    plotdata.loc[seasons_ordered].plot(kind='bar')
    plt.title('Sales of Toys and Toothbrushes by Season')
    plt.ylabel('Sales')
    plt.xlabel('Season')
    plt.savefig('Figures/season_bar')
    plt.show()

def CPA_bar():
    #CPA comparison
    combined_CPA = pd.concat([CPA, actual_CPA], axis=1)
    del combined_CPA['uk_region']
    combined_CPA = combined_CPA.fillna(0)  #do something with null values that come from insufficient data

    combined_CPA.plot(kind='bar')
    plt.xticks([0, 1, 2, 3], ['South East', 'North East', 'North', 'South']) #note- done manually. This will not correspond if row order changes
    plt.title('CPA Comparison by Region')
    plt.ylabel('CPA')
    plt.xlabel('Region')
    plt.savefig('Figures/CPA_bar')
    plt.show()

overall_comparison_pie()
region_comparison_pies()
age_group_bar()
season_bar()
CPA_bar()
