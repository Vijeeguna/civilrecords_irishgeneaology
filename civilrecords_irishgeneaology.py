# @Author: Vijayalakshmi Gunasekarapandian

# The raw data is from the website civilrecords.irishgenealogy.ie
# that holds Irish marriage records from the nineteenth century.
# The original records are basedon dusty handwritten ledgers but there is an online
# index, searchable by name etc.
# Unfortunately, while each record does enumerate various details of an individual’s
# marriage, it omits one crucial detail:  the name of the spouse!
# I have used Python to identify a couple based on partial information about them:
# the woman’s name (Mary Roche), the man’s firstname (Nicholas) and an approximate
# date of their marriage (1870 to 1885).

# This Python program  prints all pairs of matching records
# (records of two individuals,one from each list,
# that match up in terms of district, year, quarter, volume and page number)

import re

#Function to read details from raw text file 
def readfile(fname):
    count = 0 
    with open(fname, "r", encoding="utf8") as textfile:
        name_list = {}
        name_list[count] = {}
        regexp1 = re.compile(r'\b(\w*Marriage of\w*)\b')
        regexp2 = re.compile(r'\b(\w*in\w*)\b')
        regexp3 = re.compile(r'\b(\w*Group Registration ID\w*)\b')
        regexp4 = re.compile(r'\b(\w*SR District/Reg Area*)\b')
        regexp5 = re.compile(r'\b(\w*Returns Year*)\b')
        regexp6 = re.compile(r'\b(\w*Returns Quarter*)\b')
        regexp7 = re.compile(r'\b(\w*Returns Volume No*)\b')
        regexp8 = re.compile(r'\b(\w*Returns Page No*)\b')
        for line in textfile:
            if regexp1.search(line):
                count = count+ 1
                name = line.split("of")[1]
            if regexp2.search(line):
                year = line.split()[1]
            if regexp3.search(line):
                reg_id = line.split("ID")[1]
            if regexp4.search(line):
                area = line.split("Area")[1]
            if regexp5.search(line):
                ret_year = line.split("Year")[1]
            if regexp6.search(line):
                quarter = line.split("Quarter")[1]
            if regexp7.search(line):
                volume = line.split("Volume No")[1]
            if regexp8.search(line):
                page = line.split("Page No")[1]
                name_list[count]= name_list[count]= \
                {'Name' : name.strip(), 'Year' : year.strip(), \
                 'ID' : reg_id.strip(), 'Area' : area.strip(), \
                 'Return Year' : ret_year.strip(), \
                 'Quarter' :quarter.strip(), \
                 'Volume' : volume.strip(), 'Page' : page.strip()}
    del name_list[0]
    return name_list
    
#Function to print details of potential spouses  
def print_matches(spouse_one, spouse_two, area, year, quarter, volume, page):
    print("Possible match!")
    print(spouse_one, " and ", spouse_two, " in ", area, " in ", year)
    print("Quarter = ",quarter, ", Volume =", volume, ", Page = ", page)
    
#Function to compare details and find potential spouses 
def find_matches(spouse_one_details, spouse_two_details):
    potential_spouses = {}
    matches = 0
    spouses = []
    spouse_one, spouse_two, area, year, quarter, volume, page = \
                '', '', '', '',  '', '', ''
    for p_id in spouse_one_details:
        for q_id  in spouse_two_details:
            count = 0
            if(spouse_one_details.get(p_id,{}).get('Name')!='' \
               and spouse_two_details.get(q_id,{}).get('Name')!=''):
                spouse_one = spouse_one_details[p_id]['Name']
                spouse_two = spouse_two_details[q_id]['Name']
                if(spouse_one_details[p_id]['Area'] == \
                   spouse_two_details[q_id]['Area']):
                    area = spouse_one_details[p_id]['Area']
                    count = count+1
                if(spouse_one_details[p_id]['Year'] == \
                   spouse_two_details[q_id]['Year']):
                    year = spouse_one_details[p_id]['Year']
                    count = count+1
                if(spouse_one_details[p_id]['Quarter'] == \
                   spouse_two_details[q_id]['Quarter']):
                    quarter = spouse_one_details[p_id]['Quarter']
                    count = count+1
                if(spouse_one_details[p_id]['Volume'] == \
                   spouse_two_details[q_id]['Volume']):
                    volume = spouse_one_details[p_id]['Volume']
                    count = count+1
                if(spouse_one_details[p_id]['Page'] == \
                   spouse_two_details[q_id]['Page']):
                    page = spouse_one_details[p_id]['Page']
                    count = count+1
                if(count == 5):
                    print_matches(spouse_one, spouse_two, area, \
                                  year, quarter, volume, page)
    
#Main Program
spouse_one_details = readfile("spouse_one.txt")
spouse_two_details = readfile("spouse_two.txt")
find_matches(spouse_one_details, spouse_two_details)
                

