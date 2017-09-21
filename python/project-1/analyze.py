# Import your extra libraries/modules
import agate, os 

# Call the data
storm_events = agate.Table.from_csv('./data/StormEvents_details-ftp_v1.0_d2017_c20170918.csv')

# Do stuff to the data

# First, let's take a look at the data
# This print function lets me see the structure of the data
#print storm_events

# And this different print function lets me see the first few lines of the data
#storm_events.print_table()

# Now that we know which columns we've got and what stuff looks like, let's pull
# out only Kentucky storms
ky_storms = storm_events.where(lambda row: row['STATE_FIPS'] == 21)

# I like to test my code to see if it did anything, so let's see how many rows
# we've got in our original file, and how many we've got in our KY-specific file
print len(storm_events)
print len(ky_storms)

# Why not do this with excel?
