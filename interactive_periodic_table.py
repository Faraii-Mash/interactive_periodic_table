"""This is a sample Python script. A Small interactive periodic table program in python
This project is adapted from a project by Al Sweigart
This project uses a csv file in order to manipulate data and sort it as a visual periodic table"""

# Data from https://en.wikipedia.org/wiki/List_of_chemical_elements
# Highlight the table, copy it, then paste it into a spreadsheet program
# like Excel or Google Sheets like in https://invpy.com/elements
# Then save this file as periodictable.csv.
# Or download this csv file from https://invpy.com/periodictable.csv

# Read csv file (periodictable.csv)
import csv

elements_file = open('periodictable.csv', encoding='utf8')
elements_csv_reader = csv.reader(elements_file)
elements = list(elements_csv_reader)
elements_file.close()

# Create ..... to store the information locally

all_columns = ['Atomic Number', 'Symbol', 'Element', 'Origin of name', 'Group', 'Period', 'Atomic weight', 'Density',
               'Melting Point', 'Boiling Point', 'Specific heat capacity', 'Electronegativity',
               'Abundance in earth\'s crust']

# Text justification using longest string in all_columns
longest_column = 0
for key in all_columns:
    if len(key) > longest_column:
        longest_column = len(key)

# place all elements into the data structure
elements_structure = {}
for line in elements:
    element = {'Atomic Number': line[0],
               'Symbol': line[1],
               'Element': line[2],
               'Origin of name': line[3],
               'Group': line[4],
               'Period': line[5],
               'Atomic weight': line[6] + ' u',  # Add atomic mass unit
               'Density': line[7] + ' g/cm^3',  # Add grams per cubic cm
               'Melting Point': line[8] + ' K',  # Add Kelvin unit measurement
               'Boiling Point': line[9] + ' K',  # Add Kelvin unit measurement
               'Specific heat capacity': line[10] + ' J/(g*K)',  # Add Joule Per gram Per Kelvin
               'Electronegativity': line[11],
               'Abundance in earth\'s crust': line[12] + ' mg/kg'}
