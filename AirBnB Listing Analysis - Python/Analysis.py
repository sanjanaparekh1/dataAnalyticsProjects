import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

listings = pd.read_csv("Listings.csv",low_memory=False,encoding="ISO-8859-1",
parse_dates=["host_since"])

#Columns required - "host_since","neighbourhood","city","accommodates","price" with city = Paris
paris_listings = listings.query("city == 'Paris'").loc[:,["host_since","neighbourhood","city","accommodates","price"]]
paris_listings.info()

#Check for missing values
missing_values = paris_listings.isna().sum()

#Get minimum, maximum and average of each numeric field
paris_listings.describe()
print(paris_listings.describe())

countMin = paris_listings.query("price == 0 and accommodates == 0").count()
print("Minimum count: \n",countMin)


#Group by neighbourhood, find average price and sort by price
paris_listings_neighbourhood = paris_listings.groupby("neighbourhood").agg({"price":"mean"}).sort_values("price")
print(paris_listings_neighbourhood.head())

#Group by accommodates for the highest accomodation, find average price and sort by price
paris_listings_accomodations = paris_listings.query("neighbourhood == 'Elysee'").groupby("accommodates").agg({"price":"mean"}).sort_values("price")
print(paris_listings_accomodations.tail())

#Grouped by year of the 'host_since' column. Calculate a count of rows representing the number of new hosts and the average price for each year.
paris_listings_over_time = paris_listings.set_index('host_since').resample('Y').agg({'neighbourhood':'count','price':'mean'})
print(paris_listings_over_time.head())

#Bar chart of average price by neighbourhood in Paris
paris_listings_neighbourhood.plot.barh(
    title = 'Average Listing Price in Paris by Neighbourhood',
    xlabel = 'Price per night (Euros)',
    ylabel = 'Neighbourhood',
    figsize = (15,10)
    )
sns.despine()
plt.show()

#Bar chart of average price by accomodations in Paris - most expensive neighbourhood
paris_listings_accomodations.plot.barh(
    title = 'Average Listing Price in Paris by Accomodations for Elysee',
    xlabel = 'Price per night (Euros)',
    ylabel = 'Neighbourhood',
    figsize = (15,10)
    )
sns.despine()
plt.show()

#Two line charts, one for the number of new hosts and one for the average price of listings in Paris over time
paris_listings_over_time['neighbourhood'].plot(
    xlabel='Hosts Since (Year)',
    ylabel = "New Hosts",
    title = "New Airbnb hosts in Paris Over Time"
)
sns.despine()
plt.show()

paris_listings_over_time['price'].plot(
    xlabel='Hosts Since (Year)',
    ylabel = "Average Price (Euros)",
    title = "New Airbnb price in Paris Over Time"
)
sns.despine()
plt.show()

#Dual axis plots
fig, ax = plt.subplots()
ax.plot(paris_listings_over_time.index, 
        paris_listings_over_time['neighbourhood'], 
        label='New Hosts',
        color='tab:blue'
        )

ax.set_ylabel('New Hosts')

ax2 = ax.twinx()
ax2.plot(paris_listings_over_time.index, 
        paris_listings_over_time['price'], 
        label='Average Price',
        color='tab:pink'
        )

ax2.set_ylabel('Average Price')
ax.set_title("2015 Regulations Lead to Fewer New Hosts and Higher Prices")
plt.show()