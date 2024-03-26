from lxml import etree
from Orange.data import *
import os

# Get the home directory and specify the project path
home_directory = os.path.expanduser('~')
project_path = os.path.join(home_directory, 'Desktop', 'SenaNurBilgin_DataExp_FinalExam')

# Specify the relative path to the XML file within the project directory
xml_file = os.path.join(project_path, 'holidays.xml')

# Load the XML file
tree = etree.parse(xml_file)
root = tree.getroot()

# Initialize lists to store holiday dates and descriptions
dates = []
descriptions = []

# Iterate through each 'row' element in the XML
for row in root.findall('row'):
    dates.append(row.find('date').text)
    descriptions.append(row.find('description').text)

# Define variables for Orange data table
Date = StringVariable('Date')
Description = StringVariable('Description')

# Create domain for the extracted data
domain = Domain([], metas=[Date, Description])

# Create an Orange Table instance for the holiday data
out_data = Table.from_list(domain, list(zip(dates, descriptions)))

# Print the Orange Table
print(out_data)
