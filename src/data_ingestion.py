import requests, os, pandas as pd
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")
events_url = f'https://app.ticketmaster.com/discovery/v2/events.json?apikey={API_KEY}'
events_params_action_api = {
    'startDateTime': '2025-05-01T18:00:00-05:00',
    'endDateTime': '2027-12-31T17:00:00-05:00',
    'classificationName': 'music',
    'dmaId': '345', 
    'city': 'New York',
    'size': '20', 
    'page': '5'
}
r = requests.get(events_url, params=events_params_action_api)
print(r.status_code)
data=r.json()

def getAllPages(pages=10, per_page=100):
    # url = f'https://app.ticketmaster.com/discovery/v2/events.json?apikey={API_KEY}'
    
    events_params_action_api = {
    'startDateTime': '2025-05-01T18:00:00-05:00',
    'endDateTime': '2027-12-31T17:00:00-05:00',
    'classificationName': 'music',
    # 'dmaId': '345', 
    'city': 'New York',
    'size': '200', 
    'page': '100'
    }
    
    all_records = []

    url = f'https://app.ticketmaster.com/discovery/v2/events.json?apikey={API_KEY}'

    for page in range(1, pages + 1):         
        response = requests.get(
            url,
            params={**events_params_action_api, 'page': page, 'size': per_page}
        )
        response.raise_for_status()
        records = response.json()
        all_records.extend(records['_embedded']['events'])
        
    return pd.DataFrame(all_records) 

more_events= getAllPages()

renamed_more_events = more_events.rename(columns= {
    'name':'NAME', 
    'type': 'TYPE', 
    'id': 'ID',
    'classifications': 'GENRE', 
    'accessibility': 'ACCESSIBILITY', 
    'ticketLimit': 'TICKET_LIMIT', 
    '_embedded': 'VENUE_NAME',
    'products': 'PRODUCTS'
}
)
data_ex = renamed_more_events.loc[:, ~renamed_more_events.columns.isin(['images','doorsTimes', '_links', 'linkMoreInfo', 'outlets', 'images', 'test','pleaseNote', 'seatmap','nameOrigin', 'promoters', 'url', 'priceRanges', 'locale', 'sales', 'dates','ageRestrictions'])]

data_ex.rename(columns= {
    'name':'NAME', 
    'type': 'TYPE', 
    'id': 'ID',
    'classifications': 'GENRE', 
    'promoter': 'PROMOTER',
    'accessibility': 'ACCESSIBILITY', 
    'ticketLimit': 'TICKET_LIMIT', 
    '_embedded': 'VENUE_NAME',
    'products': 'PRODUCTS',
    'ticketLimit': 'TICKET_LIMIT',
    'info': 'INFO',
    'ticketing': 'TICKETING'


}, inplace=True
)


product_name = data_ex['PRODUCTS']
data_clean = data_ex.dropna(subset = ['PRODUCTS', 'ACCESSIBILITY']).copy()
data_clean.rename(columns= {
    'name':'NAME', 
    'type': 'TYPE', 
    'id': 'ID',
    'classifications': 'GENRE', 
    'promoter': 'PROMOTER',
    'ticketLimit': 'TICKET_LIMIT', 
    '_embedded': 'VENUE_NAME',
    'ticketLimit': 'TICKET_LIMIT',
    'info': 'INFO',
    'products': 'PRODUCTS',
    'accessibility': 'ACCESSIBILITY',
    'ticketing': 'TICKETING' ,
    'Accessibility_Filtered': 'ACCESSIBILITY_Filtered'
    


}, inplace=True
)

data_clean['PRODUCTS_Filtered'] = [
    ', '.join([n['name'] for n in item]) for item in data_clean['PRODUCTS']
]
data_clean['VENUE_NAME_Filtered'] = [
    name['venues'][0]['name']
    for name in data_clean['VENUE_NAME']
    
    
]
data_clean['Accessibility_Filtered'] = [
    f"Ticket Limit: {item.get('ticketLimit', 'N/A')}" for item in data_clean['ACCESSIBILITY']
]


data_clean['Genre_Filtered'] = [item['genre']['name']
                                for x in data_clean['GENRE']
                                for item in x
    ]


move_col1=data_clean.pop('Accessibility_Filtered')
data_clean.insert(9, column='Accessibility_Filtered', value=move_col1)

move_col2 = data_clean.pop('Genre_Filtered')
data_clean.insert(4, column='Genre_Filtered', value=move_col2)

move_col3 = data_clean.pop('PROMOTER')
data_clean.insert(10, column='PROMOTER',value=move_col3 )

move_col4 = data_clean.pop('VENUE_NAME_Filtered')
data_clean.insert(6, column='VENUE_NAME_Filtered', value=move_col4)

move_col5 = data_clean.pop('INFO')
data_clean.insert(11, column='INFO', value=move_col5)

move_col6 = data_clean.pop('VENUE_NAME')
data_clean.insert(5, column='VENUE_NAME', value=move_col6)

move_col7 = data_clean.pop('PRODUCTS')
data_clean.insert(7, column='PRODUCTS', value=move_col7)

move_col8 = data_clean.pop('PRODUCTS_Filtered') #Not sure why 'Products_Filtered' appears two times. 
data_clean.insert(8, column='PRODUCTS_Filtered', value=move_col8)
data_clean.to_csv('data/processed/TicketMaster.csv')
