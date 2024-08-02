import os
import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


class GoogleSheetsClient:
    def __init__(self) -> None:
        """
        Initializes the Google Sheets client.
        """
        credentials = self._get_credentials()
        service = build("sheets", "v4", credentials=credentials)
        self.client = service.spreadsheets()

    def _get_credentials(self) -> Credentials:
        """
        Loads credentials from the JSON file.

        :return: Google API Credentials object.
        """
        CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

        if not CREDENTIALS:
            raise ValueError(
                "GOOGLE_APPLICATION_CREDENTIALS environment variable is not set."
            )

        if not os.path.exists(CREDENTIALS):
            raise FileNotFoundError(
                f"Credentials file not found: {CREDENTIALS}"
            )

        credentials = Credentials.from_service_account_file(
            CREDENTIALS,
            scopes=["https://www.googleapis.com/auth/spreadsheets"],
        )

        print

        return credentials

    def fetch_data(self, spreadsheet_id: str, range: str) -> pd.DataFrame:
        """
        Fetches data from Google Sheets and returns it as a Pandas DataFrame.

        :param sheet_id: The ID of the Google Sheet.
        :param range_name: The A1 notation of the range to fetch.
        :return: Pandas DataFrame containing the sheet data.
        """
        if not spreadsheet_id:
            raise ValueError("spreadsheet_id is required.")

        if not range:
            raise ValueError("range_name is required.")

        result = (
            self.client.values()
            .get(spreadsheetId=spreadsheet_id, range=range)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            raise ValueError("No data found.")

        headers = values[0]
        rows = values[1:]
        df = pd.DataFrame(rows, columns=headers)

        return df
