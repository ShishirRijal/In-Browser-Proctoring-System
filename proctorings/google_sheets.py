import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to your service account JSON key file
SERVICE_ACCOUNT_FILE = os.path.join('C:/Users/Angel/OneDrive/Desktop/InBrowserProctoring/proctoring_systems/proctorings/decent-envoy-436203-c9-ab5ba84d0fcb.json')

# Google Sheets API Scopes
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# ID of the Google Sheet (get it from the URL of your sheet)
SPREADSHEET_ID = '1SDLbzbMcBhkELizRKoQNaOPYJF_eR4mu3eHnC0QVi70'

# Range of the data you want to read from the sheet (e.g., 'Sheet1!A1:F100')
RANGE_NAME = 'formresponse!A1:F100'

def get_sheet_data():
    # Authenticate using the service account credentials
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # Build the Sheets API client
    service = build('sheets', 'v4', credentials=credentials)

    # Call the Sheets API to get data
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
        return None
    return values
