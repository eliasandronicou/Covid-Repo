import pandas as pd
import requests
import io
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.mode.chained_assignment = None  # default='warn'

#%matplotlib inline # uncommend for Jupyter IPython notebook το εργαλείο που χρησιμοποίησα
url = "https://www.stats.govt.nz/assets/Uploads/Effects-of-COVID-19-on-trade/Effects-of-COVID-19-on-trade-At-15-December-2021-provisional/Download-data/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"
response = requests.get(url)
csv_data = response.content
df = pd.read_csv(io.BytesIO(csv_data))

# από το αρχικό αφήνει μόνο τις στήλες με δολάριο και τόνους αντίστοιχα
def filter_dollar(df):
    dollar = df[df['Measure'] == '$']
    return dollar


def filter_tonnes(df):
    dollar = df[df['Measure'] == 'Tonnes']
    return dollar


#δημιουργεί 2 γραφηκές με τα αντίστοιχα dataframe
def plot_two_graphs(df_1, df_2, x_value):
    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Plot the first graph on the left subplot
    df_1.plot(x=x_value, y='Value', kind='bar', color='blue', label='$', ax=ax1)
    ax1.set_xlabel(x_value)
    ax1.set_ylabel('Value')
    ax1.set_title('Value by dollar per '+x_value)

    # Plot the second graph on the right subplot
    df_2.plot(x=x_value, y='Value', kind='bar', color='red', label='T', ax=ax2)
    ax2.set_xlabel(x_value)
    ax2.set_ylabel('Value')
    ax2.set_title('Value by Tonnes per '+x_value)

    # Adjust spacing between subplots
    plt.tight_layout()

    # Display the plots
    plt.show()

#Προσθέτει τις γραμμές με ίδια στήλη sort_by
def calculate_monthly_sums(dataframe,sort_by):
    monthly_sum = dataframe.groupby(sort_by)['Value'].sum().reset_index()
    return monthly_sum

#βρίσκει τα 5 με το μεγαλύτερο άθροισμα
def top5_df(df):
    sorted_sums = df.sort_values('Value', ascending=False)
    top_5_sums = sorted_sums.head(5)
    return top_5_sums



# γράφημα για το 7 ερώτημα
def plot_top_5_per_country(df1,df2):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    sns.barplot(x='Country', y='Value', hue='Commodity', data=df1, ax=ax1)
    ax1.set_xlabel('Country')
    ax1.set_ylabel('Value')
    ax1.set_title('Value by dollar for Each Commodity per Country')
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=90)
    ax1.legend(bbox_to_anchor=(1, 1))

    sns.barplot(x='Country', y='Value', hue='Commodity', data=df2, ax=ax2)
    ax2.set_xlabel('Country')
    ax2.set_ylabel('Value')
    ax2.set_title('Value by Tonnes for Each Commodity per Country')
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=90)
    ax2.legend(bbox_to_anchor=(1, 1))

    plt.tight_layout()
    plt.show()

# γράφημα για το 8 ερώτημα
def plot_best_day_commodity(df1,df2):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    sns.barplot(x='Weekday', y='Value', hue='Commodity', data=df1, ax=ax1)
    ax1.set_xlabel('Day')
    ax1.set_ylabel('Value')
    ax1.set_title('Top day by dollar for Each Commodity')
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=90)
    ax1.legend(bbox_to_anchor=(1, 1))

    sns.barplot(x='Weekday', y='Value', hue='Commodity', data=df2, ax=ax2)
    ax2.set_xlabel('Day')
    ax2.set_ylabel('Value')
    ax2.set_title('Top day by Tonnes for Each Commodity')
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=90)
    ax2.legend(bbox_to_anchor=(1, 1))

    plt.tight_layout()
    plt.show()

#Οι συναρτήσεις που είναι σε σχόλια χρησιμοποιήθηκαν για debuging

# bullet 1
er_1=df.drop(columns=['Direction','Year','Weekday','Country','Commodity','Transport_Mode','Cumulative'])


er_1a=er_1[er_1['Measure'] == 'Tonnes']


er_1b=er_1[er_1['Measure'] == '$']


er_1a['Date'] = pd.to_datetime(er_1['Date'], format='%d/%m/%Y')

monthly_sum_a = er_1a.groupby(er_1a['Date'].dt.month)['Value'].sum().reset_index()
monthly_sum_a.rename(columns={'Date': 'Month'}, inplace=True)
monthly_sum_a['Measure'] = 'T'



er_1b['Date'] = pd.to_datetime(er_1b['Date'], format='%d/%m/%Y')

monthly_sum_b = er_1b.groupby(er_1b['Date'].dt.month)['Value'].sum().reset_index()
monthly_sum_b.rename(columns={'Date': 'Month'}, inplace=True)
monthly_sum_b['Measure'] = '$'



#plot_two_graphs(monthly_sum_b, monthly_sum_a, 'Month')

tonnes=filter_tonnes(df)

dollar=filter_dollar(df)


# bullet 2
er_2_a=tonnes.drop(columns=['Direction','Year','Weekday','Date','Commodity','Transport_Mode','Cumulative'])


er_2_b=dollar.drop(columns=['Direction','Year','Weekday','Date','Commodity','Transport_Mode','Cumulative'])




country_sum_a = calculate_monthly_sums(er_2_a,'Country')
country_sum_a['Measure'] = 'T'


country_sum_b = calculate_monthly_sums(er_2_b,'Country')
country_sum_b['Measure'] = '$'


#plot_two_graphs(country_sum_b, country_sum_a, 'Country')

# bullet3
er_3_a=tonnes.drop(columns=['Direction','Year','Country','Date','Commodity','Weekday','Cumulative'])


er_3_b=dollar.drop(columns=['Direction','Year','Country','Date','Commodity','Weekday','Cumulative'])


transport_sum_a = calculate_monthly_sums(er_3_a,'Transport_Mode')
transport_sum_a['Measure'] = 'T'


transport_sum_b = calculate_monthly_sums(er_3_b,'Transport_Mode')
transport_sum_b['Measure'] = '$'


#plot_two_graphs(transport_sum_b, transport_sum_a, 'Transport_Mode')

# bullet 4
er_4_a=tonnes.drop(columns=['Direction','Year','Country','Date','Commodity','Transport_Mode','Cumulative'])


er_4_b=dollar.drop(columns=['Direction','Year','Country','Date','Commodity','Transport_Mode','Cumulative'])


weekday_sum_a = calculate_monthly_sums(er_4_a,'Weekday')
weekday_sum_a['Measure'] = 'T'


weekday_sum_b = calculate_monthly_sums(er_4_b,'Weekday')
weekday_sum_b['Measure'] = '$'


#plot_two_graphs(weekday_sum_b, weekday_sum_a, 'Weekday')

# bullet 5
er_5_a=tonnes.drop(columns=['Direction','Year','Country','Date','Weekday','Transport_Mode','Cumulative'])


er_5_b=dollar.drop(columns=['Direction','Year','Country','Date','Weekday','Transport_Mode','Cumulative'])


commodity_sum_a = calculate_monthly_sums(er_5_a,'Commodity')
commodity_sum_a['Measure'] = 'T'


commodity_sum_b = calculate_monthly_sums(er_5_b,'Commodity')
commodity_sum_b['Measure'] = '$'


#plot_two_graphs(commodity_sum_b, commodity_sum_a, 'Commodity')

#bullet 6
er_6_a=top5_df(monthly_sum_a)


er_6_b=top5_df(monthly_sum_b)


#plot_two_graphs(er_6_b, er_6_a, 'Month')

# bullet 7
er_7_a=tonnes.drop(columns=['Direction','Year','Weekday','Date','Transport_Mode','Cumulative'])
top_5_per_country_a = er_7_a.groupby(['Country', 'Commodity'])['Value'].sum().reset_index()
top_5_per_country_a['Measure'] = 'T'


er_7_b=dollar.drop(columns=['Direction','Year','Weekday','Date','Transport_Mode','Cumulative'])
countries_com = er_7_b.groupby(['Country', 'Commodity'])['Value'].sum().reset_index()

top_5_per_country_b = countries_com.groupby('Country').head(5)
top_5_per_country_b['Measure'] = '$'


#plot_top_5_per_country(top_5_per_country_b,top_5_per_country_a):


# bullet 8
er_8_a=tonnes.drop(columns=['Direction','Year','Country','Date','Transport_Mode','Cumulative'])
day_com_a = er_8_a.groupby(['Weekday', 'Commodity'])['Value'].sum().reset_index()


best_day_a = day_com_a.groupby('Commodity').head(1)
best_day_a['Measure'] = 'T'



er_8_b=dollar.drop(columns=['Direction','Year','Country','Date','Transport_Mode','Cumulative'])
day_com_b = er_8_b.groupby(['Weekday', 'Commodity'])['Value'].sum().reset_index()
best_day_b = day_com_b.groupby('Commodity').head(1)
best_day_b['Measure'] = '$'


#plot_two_graphs(best_day_b, best_day_a, 'Commodity')