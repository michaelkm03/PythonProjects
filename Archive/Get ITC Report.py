import subprocess
import os

# THIS REPORT IS FOR SALES AND TRENDS IN ITUNES CONNECT ONLY

# Change to directory of 'Reporter' files
os.chdir('/Users/michaelmontgomery/Desktop/Reporter')

# Set all variables to desired report type and date range
cred_file = 'Reporter.jar'
properties_file ='Reporter.properties'
GET_cmd = 'Sales.getReport'
vendor_num = '86755230'  # Jenn Im, Fashion Forward
account_id = 'a='+str(117858295)   # Fashion Forward account id

# For daily and weekly reports, use format YYYYMMDD. For monthly, use YYYYMM. For yearly, use YYYY
subtype = {
    0:'Daily',
    1:'Weekly',
    2:'Monthly',
    3:'Yearly'
}
# Start date of Report (End date will always be Current date)
date ='20160825'

# Gather set variables, use subprocess to run in command line
GETreport = subprocess.call(
    ['java','-jar',cred_file,'p='+properties_file,account_id,GET_cmd,vendor_num,
     ',',
     'Sales',',',
     'Summary',',',
     subtype[0],',',
     date]
)
