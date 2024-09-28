from data_getter import DataGetter
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == '__main__':
    SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
    CREDENTIALS_FILE = 'credentials.json'

    getter = DataGetter(CREDENTIALS_FILE, SPREADSHEET_ID)
    data = getter.get_data()
    
    print(data)