from datetime import datetime

import matplotlib.pyplot as plt
import pandas

# headers
# Date,Publisher,Billing Type,Filled Rate,Unfilled Rate,Total Auctions,Successful,Unfilled,Completed Auctions Rate,Publisher Revenue,Nimbus Revenue

# define python style constants
DATE_COLUMN = "Date"
PUBLISHER_COLUMN = "Publisher"
REVENUE_COLUMN = "Publisher Revenue"

# load in the CSV data
df = pandas.read_csv("revenue-1647449358.csv", parse_dates=True)
# isolate the CSV to just the 3 below columns
df = df.loc[:, [DATE_COLUMN, PUBLISHER_COLUMN, REVENUE_COLUMN]]
# group the data so that it's organized by cumulative sums by publisher and date
grouped = df.groupby([PUBLISHER_COLUMN, DATE_COLUMN])

# get the first publisher in the data set
publisher_name = grouped[PUBLISHER_COLUMN].first()[0]
# create an empty slice to hold graph data
dates_revenue = []
for name, group in grouped:
    if publisher_name != name[0]:

        # configure the graph size and quality settings
        fig, ax = plt.subplots(figsize=(17, 15))
        plt.figure(dpi=300)
        plt.rcParams.update({'font.size': 5})

        # plot the data

        dates_revenue.sort(key=lambda x: x[0])
        dates, revenue = zip(*dates_revenue)
        dates = [i.strftime("%m/%d/%y") for i in dates]

        plt.plot(dates, revenue)
        # use the publisher name as the graph's title
        plt.title(publisher_name)
        # label the axis's
        plt.xlabel('Dates')
        plt.ylabel('Revenue')

        # rotate the dates to avoid overlaps
        plt.xticks(rotation=90)

        # format the numbers on the y axis
        current_values = plt.gca().get_yticks()
        plt.gca().set_yticklabels(['${:,.2f}'.format(x) for x in current_values])
        # save data graph as a file

        plt.savefig(f'/Users/marcsantiago/Desktop/pub_revenue_report/revenue_plots/{publisher_name}.png')
        # plt.show()
        # break
        # reset the list
        dates_revenue = []
        # assign the new name
        publisher_name = name[0]
    for row_index, row in group.iterrows():
        # convert string version to date to a datetime data object
        date_time_obj = datetime.strptime(row[DATE_COLUMN], '%m/%d/%y')
        dates_revenue.append((date_time_obj, row[REVENUE_COLUMN]))
