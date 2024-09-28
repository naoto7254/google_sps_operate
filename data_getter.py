import gspread
from oauth2client.service_account import ServiceAccountCredentials

class DataGetter:
    def __init__(self, credentials_file, spreadsheet_id):
        self.credentials_file = credentials_file
        self.spreadsheet_id = spreadsheet_id
        self.client = self.authenticate()
        self.sheet = self.client.open_by_key(self.spreadsheet_id).worksheet("input")
        
    def authenticate(self):
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = ServiceAccountCredentials.from_json_keyfile_name(self.credentials_file, scope)
        client = gspread.authorize(creds)
        return client

    def get_data(self):
        return self.sheet.get_all_records()