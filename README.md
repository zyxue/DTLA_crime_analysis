# Analysis of crime data in downtown Los Angeles

- data is collected from Los Angeles Times, http://maps.latimes.com/crime/
- data ranges from 2009 to early March of 2019

##### The distribution of crimes

![all](figs/all_crimes.png)

As seen, the [Skid Row](https://en.wikipedia.org/wiki/Skid_Row,_Los_Angeles)
(lower right) area is much worse than the other areas.

# Stats

### Crime by year

<img src="figs/crime_by_year.png" alt="by_year" width="500">

So the crime number is actually increasing in recent years, but it could be due to better way of reporting crimes.

### Crime by month

<img src="figs/crime_by_month.png" alt="by_month" width="500">

Not much difference from month to month

### Crime by day of the month

<img src="figs/crime_by_day.png" alt="by_day" width="500">

Not much difference from day to day

### Crime by day of the week

<img src="figs/crime_by_dayofweek.png" alt="by_day" width="500">

0 is Monday
([ref](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.dayofweek.html)),
so Friday and Saturday are slightly worse.

### Crime by hour

<img src="figs/crime_by_hour.png" alt="by_hour" width="500">

Crime number goes up quickly and remains high during the day
