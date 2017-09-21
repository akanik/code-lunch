# Import your extra libraries/modules
import agate, os 

# Call the data
storm_events = agate.Table.from_csv('./data/StormEvents_details-ftp_v1.0_d2017_c20170918.csv')

# Do stuff to the data

# First, let's take a look at the data
# This print function lets me see the structure of the data
print storm_events

# And this different print function lets me see the first few lines of the data
storm_events.print_table()

# Now that we know which columns we've got and what stuff looks like, let's pull
# out only Kentucky storms.
ky_storms = storm_events.where(lambda row: row['STATE_FIPS'] == 21)

# I like to test my code to see if it did anything, so let's see how many rows
# we've got in our original file, and how many we've got in our KY-specific file
print len(storm_events)
print len(ky_storms)

# Did you notice how long that took. Let's export our ky_storms data as a csv file
# and then we can just call that instead of filtering a 35,530 row spreadsheet each
# time
ky_storms.to_csv('./data/20170921_KY_StormEvents_NOAA.csv')


#########################################################################


ky_storms = agate.Table.from_csv('./data/20170921_KY_StormEvents_NOAA.csv')

# Let's find the deadliest KY storms
deadliest_ky_storms = ky_storms.order_by('DEATHS_DIRECT')

# But wait, there's another column called DEATHS_INDIRECT. What if I want to add those
# deaths in as well? We can create a new row and then order_by that!
def add_deaths(row):
    return row['DEATHS_DIRECT'] + row['DEATHS_INDIRECT']

num_type = agate.Number()

ky_storms_all_deaths = ky_storms.compute([
    ('total_deaths', agate.Formula(num_type, add_deaths))
])

print ky_storms_all_deaths

# Why not do this with excel?
