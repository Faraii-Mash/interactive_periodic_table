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
import re
import sys

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

    # Some of the data has bracketed text from Wikipedia that we want to
    # remove, such as the atomic weight of Boron:
    # "10.81[III][IV][V][VI]" should be "10.81"

    for key, value in element.items():
        element[key] = re.sub(r'\[(I|V|X)+\]', '', value)

    elements_structure[line[0]] = element  # Map the atomic number to the element.
    elements_structure[line[1]] = element  # Map the symbol to the element.

print('Periodic Table of Elements')
print('By FB Mashiri')
print('Designed for Dr ZLKM')
print()

# Start main program loop
while True:
    # Show table and let the user select an element:
    print('''           Periodic Table of Elements
      1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
    1 H                                                  He
    2 Li Be                               B  C  N  O  F  Ne
    3 Na Mg                               Al Si P  S  Cl Ar
    4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
    5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
    6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
    7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og
    
            Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
            Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr''')
    print('Enter a symbol or atomic number to examine, or QUIT to stop the program')
    user_input = input('> ').title()

    if user_input == 'QUIT':
        sys.exit()

    # Display the selected element's data:
    if user_input in elements_structure:
        for key in all_columns:
            keyJustified = key.rjust(longest_column)
            print(keyJustified + ': ' + elements_structure[user_input][key])
        input('Please press Enter to continue...')