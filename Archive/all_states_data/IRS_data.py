import requests

BASE_URL = 'https://www.irs.gov/pub/irs-soi/eo_'
type = '.csv'

states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    # 'AS': 'American Samoa',
    # 'AZ': 'Arizona',
    # 'CA': 'California',
    # 'CO': 'Colorado',
    # 'CT': 'Connecticut',
    # 'DC': 'District of Columbia',
    # 'DE': 'Delaware',
    # 'FL': 'Florida',
    # 'GA': 'Georgia',
    # 'GU': 'Guam',
    # 'HI': 'Hawaii',
    # 'IA': 'Iowa',
    # 'ID': 'Idaho',
    # 'IL': 'Illinois',
    # 'IN': 'Indiana',
    # 'KS': 'Kansas',
    # 'KY': 'Kentucky',
    # 'LA': 'Louisiana',
    # 'MA': 'Massachusetts',
    # 'MD': 'Maryland',
    # 'ME': 'Maine',
    # 'MI': 'Michigan',
    # 'MN': 'Minnesota',
    # 'MO': 'Missouri',
    # 'MP': 'Northern Mariana Islands',
    # 'MS': 'Mississippi',
    # 'MT': 'Montana',
    # 'NA': 'National',
    # 'NC': 'North Carolina',
    # 'ND': 'North Dakota',
    # 'NE': 'Nebraska',
    # 'NH': 'New Hampshire',
    # 'NJ': 'New Jersey',
    # 'NM': 'New Mexico',
    # 'NV': 'Nevada',
    # 'NY': 'New York',
    # 'OH': 'Ohio',
    # 'OK': 'Oklahoma',
    # 'OR': 'Oregon',
    # 'PA': 'Pennsylvania',
    # 'PR': 'Puerto Rico',
    # 'RI': 'Rhode Island',
    # 'SC': 'South Carolina',
    # 'SD': 'South Dakota',
    # 'TN': 'Tennessee',
    # 'TX': 'Texas',
    # 'UT': 'Utah',
    # 'VA': 'Virginia',
    # 'VI': 'Virgin Islands',
    # 'VT': 'Vermont',
    # 'WA': 'Washington',
    # 'WI': 'Wisconsin',
    # 'WV': 'West Virginia',
    # 'WY': 'Wyoming'
}

def getStates(stateList):
    count = 0
    if stateList[0] == 'all':
        print 'Getting data for %d states...' % states.__len__()
        for state in states:
            request_url = BASE_URL + str.lower(state) + type
            response_obj = requests.get(request_url)

            # Iterate through all states, make request, save to directory
            with open((str.lower(state) + '_data.txt'), 'w') as file:
                for line in response_obj:
                    file.write(line)
                    file.write('\n')
                count =+1
    else:
        print 'Getting data for %d states...' % stateList.__len__()
        for state in stateList:
            request_url = BASE_URL + str.lower(state) + type
            response_obj = requests.get(request_url)

            # Iterate through stateList, make request, save to directory
            with open((str.lower(state) + '_data.txt'), 'w') as file:
                for line in response_obj:
                    file.write(line)
                    file.write('\n')

if __name__ == "__main__":
    getStates(stateList = ['wa','hi'])