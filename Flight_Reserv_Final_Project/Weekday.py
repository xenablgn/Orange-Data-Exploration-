import Orange
import numpy
from datetime import datetime

# Function to get weekday name from a date string
def get_weekday(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.strftime('%A')

if in_data is not None:
    # Check if 'Date' column exists
    if 'DateOfDeparture' in in_data.domain:
     # Extract the 'DateOfDeparture' and convert it to the corresponding weekday
        weekdays = [get_weekday(str(row['DateOfDeparture'])) for row in in_data]
        
        # Create a new StringVariable for the weekdays
        weekday_var = Orange.data.StringVariable('Weekday')
        
        # Extend the domain with the new 'Weekday' meta attribute
        new_attributes = in_data.domain.attributes
        new_classes = in_data.domain.class_vars
        new_metas = in_data.domain.metas + (weekday_var,)
        
        # Create a new domain with the added 'Weekday' meta attribute
        new_domain = Orange.data.Domain(new_attributes, new_classes, metas=new_metas)
        
        # Create a new Table with the same data but with the updated domain
        new_data = in_data.transform(new_domain)
        
        # Add the weekdays data to the new_data metas
        new_weekday_column = numpy.array(weekdays)  
        for i in range(len(new_data)):
            new_data.metas[i, -1] = new_weekday_column[i]
        
        # Set the modified table as the output
        out_data = new_data
