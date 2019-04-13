from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


def get_service():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('sheets', 'v4', credentials=creds)
    return service


def get_spreadsheet(service, spreadsheet_id, ranges):
    request = service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=ranges)
    return request.execute()


def get_cell(service, spreadsheet_id, range_):
    request = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_)
    value = request.execute()
    return value


def send_cell(service, spreadsheet_id, range_, body_):
    service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_, body=body_, valueInputOption='USER_ENTERED').execute()

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    service = get_service()
    spreadsheet_id = "14WKX_tnQboiw9-plw2W2euThCyfEdZTNU76m-146R6Q"
    # Call the Sheets API
    spreadsheet = get_spreadsheet(service, spreadsheet_id, [])
    # print(spreadsheet)
    body = {'values': [[25, 26, 27]]}
    send_cell(service, spreadsheet_id, 'Sheet1!A3:C3', body)
    print(get_cell(service, spreadsheet_id, 'Sheet1!A1:C4'))

if __name__ == '__main__':
    main()
