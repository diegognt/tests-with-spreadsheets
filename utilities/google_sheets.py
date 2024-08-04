import os
import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


class GoogleSheetsClient:
    """
    A client to interact with Google Sheets Python API.
    """

    def __init__(self) -> None:
        """
        Initializes the Google Sheets client.
        """
        credentials = self._get_credentials()
        service = build("sheets", "v4", credentials=credentials)
        self.client = service.spreadsheets()

    def set_spreadsheet_id(self, spreadsheet_id: str) -> None:
        """
        Sets the spreadsheet ID.

        :param spreadsheet_id: The ID of the spreadsheet.
        :raises ValueError: If the spreadsheet_id is not set.
        """
        if not spreadsheet_id:
            raise ValueError("spreadsheet_id is required.")

        self.spreadsheet_id = spreadsheet_id

    def _get_credentials(self) -> Credentials:
        """
        Loads credentials from the JSON file.

        :returns: Google API Credentials object.
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

    def fetch_data(self, range: str) -> pd.DataFrame:
        """
        Fetches data from Google Sheets and returns it as a Pandas DataFrame.

        :param sheet_id: The ID of the Google Sheet.
        :param range_name: The A1 notation of the range to fetch.
        :return: Pandas DataFrame containing the sheet data.
        :raises ValueError: If the spreadsheet_id or range is not set.
        """
        if not self.spreadsheet_id:
            raise ValueError("spreadsheet_id has not been set.")

        if not range:
            raise ValueError("range is required.")

        result = (
            self.client.values()
            .get(spreadsheetId=self.spreadsheet_id, range=range)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            raise ValueError("No data found.")

        headers = values[0]
        rows = values[1:]
        df = pd.DataFrame(rows, columns=headers)

        return df

    def add_new_sheet(self, sheet_name: str) -> None:
        """
        Adds a new sheet to an existing spreadsheet.

        :param new_sheet_name: The name of the new sheet.
        :raises ValueError: If the sheet_name or the spreadsheet id is not set.
        """
        if not self.spreadsheet_id:
            raise ValueError("spreadsheet_id has not been set.")

        if not sheet_name:
            raise ValueError("new_sheet_name is required.")

        requests = [{"addSheet": {"properties": {"title": sheet_name}}}]

        body = {"requests": requests}
        result = self.client.batchUpdate(
            spreadsheetId=self.spreadsheet_id, body=body
        ).execute()

        if not result:
            raise ValueError("Failed to add sheet.")

        print(f"Added sheet: {sheet_name}")

    def update_sheet(self, sheet_name: str, data: list) -> None:
        """
        Updates a sheet from the A1 cell of.

        :param sheet_name: The sheet's name to update.
        :param data: The data to write to the cells.
        :raises ValueError: If the spreadsheet_id, sheet_name, or data is not set.
        """
        if not self.spreadsheet_id:
            raise ValueError("spreadsheet_id has not been set.")

        if not self.spreadsheet_id:
            raise ValueError("spreadsheet_id has not been set.")

        if not sheet_name:
            raise ValueError("sheet_name is required.")

        if not data:
            raise ValueError("data is required.")

        body = {"values": data}
        result = (
            self.client.values()
            .update(
                spreadsheetId=self.spreadsheet_id,
                range=f"{sheet_name}!A1",
                valueInputOption="RAW",
                body=body,
            )
            .execute()
        )

        if not result:
            raise ValueError("Failed to update sheet.")

        print(f"Sheet {sheet_name} updated successfully.")
