import os
from google.oauth2 import service_account
from googleapiclient.discovery import build


class GoogleSheetsApi:
	def __init__(self):
		self.creds = service_account.Credentials.from_service_account_file(
			'credentials.json',
			scopes=['https://www.googleapis.com/auth/spreadsheets']
		)
	
	def saveCSVtoSheets(self, csvText, spreadsheetId):
		service = build('sheets', 'v4', credentials=self.creds)

		height = len(csvText.splitlines())
		if height <= 0:
			return

		width = len(csvText.splitlines()[0].split(','))
		if width <= 0: 
			return

		range_name = f"Sheet1!A1:{chr(64+width)}{height}"
		csv_values = []
		for row in csvText.splitlines():
			csv_values.append(row.split(','))

		request = service.spreadsheets().values().update(
			spreadsheetId=spreadsheetId,
			range=range_name,
			valueInputOption='RAW',
			body={'values': csv_values}
		)

		response = request.execute()