
# Heroes Of Pymoli Data Analysis

<ul>
<li> Of the 573 active players, the vast majority are male (81.15%). There also exists, a smaller, but notable proportion of female players (17.45%).</li>
<li> Our peak age demographic falls between 20-24 (45.2%) with secondary groups falling between 15-19 (17.45%) and 25-29 (15.18%).
</li>
<li> Across all major age and gender demographics, the average purchase for a user is roughly $4.00 </li>   
</ul>


```python
import pandas as pd
```


```python
df_heroes = pd.read_json("purchase_data.json")
```

## Player Count:


```python
#calculate total number of unique players:
player_count = len(df_heroes['SN'].unique())

df_total_number_of_players=pd.DataFrame({
    "Total Players":[player_count ]
})

df_total_number_of_players.head()

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>



## Purchasing Analysis (Total):


```python
#calculate total number of unique items
unique_items=len(df_heroes["Item ID"].unique())

#calculate average  price 
average_price=df_heroes["Price"].mean()

#calculate total number of purchases
number_purchases=df_heroes["Item Name"].count()

#calculate total revenue
total_revenue=df_heroes["Price"].sum()

#create DataFrame and display results
df_purchasing_total=pd.DataFrame({
    "Number of Unique Items": [unique_items],
    "Average Price": [average_price],
    "Number of Purchases": [number_purchases],
    "Total Revenue": [total_revenue]
})
df_purchasing_total=df_purchasing_total[["Number of Unique Items","Average Price","Number of Purchases","Total Revenue"]]
df_purchasing_total["Average Price"]=df_purchasing_total["Average Price"].map('${:.2f}'.format)
df_purchasing_total["Total Revenue"]=df_purchasing_total["Total Revenue"].map('${:,.2f}'.format)
df_purchasing_total.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>183</td>
      <td>$2.93</td>
      <td>780</td>
      <td>$2,286.33</td>
    </tr>
  </tbody>
</table>
</div>



## Gender Demographics


```python
#create DataFrame with unique values
unique_players_df=df_heroes.drop_duplicates(subset=["SN"], keep='first', inplace=False)

#calculate count and percentage by gender
gender_counts=unique_players_df["Gender"].value_counts().rename("Total Count")

df_gender=pd.DataFrame(gender_counts)

df_gender["Percentage of Players"]=df_gender["Total Count"]*100/df_gender["Total Count"].sum()
df_gender["Percentage of Players"]=df_gender["Percentage of Players"].round(2)
df_gender=df_gender[["Percentage of Players", "Total Count"]]

df_gender.head()

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>81.15</td>
      <td>465</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.45</td>
      <td>100</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.40</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>



## Purchasing Analysis (Gender)


```python
#group data by gender
gender_group=df_heroes.groupby("Gender")
#calculate purchase count by gender
purchase=gender_group["Item Name"].count().rename("Purchase Count")

purchase_df=pd.DataFrame(purchase)
#calculate average purchase price by gender
purchase_df["Average Purchase Price"]=gender_group["Price"].mean().map('${:,.2f}'.format)

#calculate total purchase value by gender
purchase_df["Total Purchase Value"]=gender_group["Price"].sum().map('${:,.2f}'.format)

#calculate normalized totals by gender
purchase_df["Normalized Totals"]=gender_group["Price"].sum()/df_gender["Total Count"]
purchase_df["Normalized Totals"]=purchase_df["Normalized Totals"].map('${:,.2f}'.format)
purchase_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>$2.82</td>
      <td>$382.91</td>
      <td>$3.83</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>$2.95</td>
      <td>$1,867.68</td>
      <td>$4.02</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>$3.25</td>
      <td>$35.74</td>
      <td>$4.47</td>
    </tr>
  </tbody>
</table>
</div>



## Age Demographics


```python
#create labels and bins
group_names=["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
bins=[0,9,14,19,24,29,34,39,120]
#add categories and group Data Frame (with unique players) by categories ("Age Group")
unique_players_df["Age Group"]=pd.cut(unique_players_df["Age"],bins, labels=group_names)
group_age=unique_players_df.groupby("Age Group")

#calculate count and percentage by age category
age_total=group_age["SN"].count().rename("Total Count")

age_demographics_df=pd.DataFrame(age_total)
age_demographics_df["Percentage of Players"]=age_demographics_df["Total Count"]*100/age_demographics_df["Total Count"].sum()
age_demographics_df["Percentage of Players"]=age_demographics_df["Percentage of Players"].round(2)
age_demographics_df=age_demographics_df[["Percentage of Players", "Total Count"]]
age_demographics_df.head(10)
```

    /Applications/anaconda3/lib/python3.6/site-packages/ipykernel_launcher.py:5: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      """





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
    <tr>
      <th>Age Group</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>3.32</td>
      <td>19</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>4.01</td>
      <td>23</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>17.45</td>
      <td>100</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>45.20</td>
      <td>259</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>15.18</td>
      <td>87</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>8.20</td>
      <td>47</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>4.71</td>
      <td>27</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>1.92</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>



## Purchasing Analysis (Age)


```python
#add categories and group Data Frame  by categories ("Age Group")
df_heroes["Age Group"]=pd.cut(df_heroes["Age"],bins, labels=group_names)
p_group=df_heroes.groupby("Age Group")

#calculate purchase count by age group
p_group_count=p_group["Item Name"].count().rename("Purchase Count")
purchasing_age_group_df=pd.DataFrame(p_group_count)

#calculate average purchase price by age group
purchasing_age_group_df["Average Purchase Price"]=p_group["Price"].mean().map('${:.2f}'.format)

#calculate total purchase value by age group
purchasing_age_group_df["Total Purchase Value"]=p_group["Price"].sum().map('${:.2f}'.format)

#calculate normalized totals by age group
purchasing_age_group_df["Normalized Totals"]=p_group["Price"].sum()/group_age["SN"].count()
purchasing_age_group_df["Normalized Totals"]=purchasing_age_group_df["Normalized Totals"].map('${:.2f}'.format)
purchasing_age_group_df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Age Group</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>28</td>
      <td>$2.98</td>
      <td>$83.46</td>
      <td>$4.39</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>35</td>
      <td>$2.77</td>
      <td>$96.95</td>
      <td>$4.22</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>133</td>
      <td>$2.91</td>
      <td>$386.42</td>
      <td>$3.86</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>336</td>
      <td>$2.91</td>
      <td>$978.77</td>
      <td>$3.78</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>125</td>
      <td>$2.96</td>
      <td>$370.33</td>
      <td>$4.26</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>64</td>
      <td>$3.08</td>
      <td>$197.25</td>
      <td>$4.20</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>42</td>
      <td>$2.84</td>
      <td>$119.40</td>
      <td>$4.42</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>17</td>
      <td>$3.16</td>
      <td>$53.75</td>
      <td>$4.89</td>
    </tr>
  </tbody>
</table>
</div>



## Top Spenders


```python
#group data by players SN
spenders_group=df_heroes.groupby("SN")

#calculate total purchase value
spenders_sum=spenders_group["Price"].sum().rename("Total Purchase Value")
#identify the  top 5 spenders by total purchase value and create DataFrame
spenders_df=pd.DataFrame(spenders_sum.nlargest(5))

#calculate purchase count
spenders_df["Purchase Count"]=spenders_group["SN"].count()
#calculate average purchase price
spenders_df["Average Purchase Price"]=spenders_group["Price"].mean().map('${:.2f}'.format)

spenders_df=spenders_df[["Purchase Count","Average Purchase Price", "Total Purchase Value"]]
spenders_df["Total Purchase Value"]=spenders_df["Total Purchase Value"].map('${:.2f}'.format)
spenders_df.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>5</td>
      <td>$3.41</td>
      <td>$17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>4</td>
      <td>$3.39</td>
      <td>$13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>4</td>
      <td>$3.18</td>
      <td>$12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>3</td>
      <td>$4.24</td>
      <td>$12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3</td>
      <td>$3.86</td>
      <td>$11.58</td>
    </tr>
  </tbody>
</table>
</div>



## Most Popular Items


```python
#group data by items ID and name 
items_group=df_heroes.groupby(["Item ID","Item Name"])
#calculate purchase count
items_group_count=items_group["Item ID"].count().rename("Purchase Count")
#identify the 5 most popular items by purchase count  and create DataFrame
items_summary_df=pd.DataFrame (items_group_count.nlargest(5))
#add item price
items_summary_df["Item Price"]=items_group["Price"].max().map('${:.2f}'.format)
##calculate total purchase value
items_summary_df["Total Purchase Value"]=items_group["Price"].sum().map('${:.2f}'.format)
items_summary_df.head(5)


```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
      <td>$2.35</td>
      <td>$25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>11</td>
      <td>$2.23</td>
      <td>$24.53</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>9</td>
      <td>$1.49</td>
      <td>$13.41</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>9</td>
      <td>$2.07</td>
      <td>$18.63</td>
    </tr>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>9</td>
      <td>$4.14</td>
      <td>$37.26</td>
    </tr>
  </tbody>
</table>
</div>



## Most Profitable Items


```python
#group data by items ID and name 
items_group=df_heroes.groupby(["Item ID","Item Name"])
#calculate total purchase value
items_group_sum=items_group["Price"].sum().rename("Total Purchase Value")
#identify the 5 most profitable items by total purchase value and create DataFrame
items_profit_df=pd.DataFrame (items_group_sum.nlargest(5))

items_profit_df["Total Purchase Value"]=items_profit_df["Total Purchase Value"].map('${:.2f}'.format)
#add item price
items_profit_df["Item Price"]=items_group["Price"].max().map('${:.2f}'.format)
#calculate purchase count
items_profit_df["Purchase Count"]=items_group["Item ID"].count()
items_profit_df=items_profit_df[["Purchase Count","Item Price", "Total Purchase Value"]]
items_profit_df.head()

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>9</td>
      <td>$4.14</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>7</td>
      <td>$4.25</td>
      <td>$29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <td>6</td>
      <td>$4.95</td>
      <td>$29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>6</td>
      <td>$4.87</td>
      <td>$29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <td>8</td>
      <td>$3.61</td>
      <td>$28.88</td>
    </tr>
  </tbody>
</table>
</div>


