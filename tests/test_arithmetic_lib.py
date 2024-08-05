"""
Arithmetic Test Suite.

This module contains the test cases for the arithmetic library.

This Test Suite uses Google Sheets to fetch the test cases and store the results, to
run the test cases, you need to set the following:
- Make sure you completed the `../docs/GOOGLE_CLOUD_SETUP.md` guide and have all functional.
- A Google spreadsheet where test cases will be stored.
- Set the `SPREADSHEET_ID` in the environment variables, uses the `.env` file for that.

The spreadsheet should have a sheet named `arithmetic_test_cases` with the following columns:
    - operation: The operation to perform, it can be:
        - addition
        - subtraction
        - multiplication
        - division
    - a: The first number.
    - b: The second number.
    - expected: The expected result of the operation.

The test cases will be executed and the results will be stored in a new sheet in the same
spreadsheet with the name `arithmetic_test_results_{timestamp}`.

To run this test suite, you can use the following command:
    $ make arithmetic-test
"""

import os
from datetime import datetime
from typing import Any, Dict
import pandas as pd
import unittest
from utilities.google_sheets import GoogleSheetsClient
from app.arithmetic import add, subtract, multiply, divide


class ArithmeticTest(unittest.TestCase):
    sheets_client = GoogleSheetsClient()
    data: pd.DataFrame = []
    spreadsheet_id = os.getenv("SPREADSHEET_ID")
    results: list[Dict[str, Any]] = []

    @classmethod
    def setUp(cls) -> None:
        if not cls.spreadsheet_id:
            raise ValueError(
                "SPREADSHEET_ID is not set in the environment variables."
            )

        data_range = "arithmetic_test_cases!A1:D"
        cls.sheets_client.set_spreadsheet_id(cls.spreadsheet_id)
        cls.data = cls.sheets_client.fetch_data(range=data_range)

    def tests_arithmetic(self) -> None:
        for index, row in self.data.iterrows():
            with self.subTest(
                f"Test case {index}, with operation {row['operation']}"
            ):
                try:
                    operation = row["operation"]
                    a = int(row["a"])
                    b = int(row["b"])
                    expected = row["expected"]
                    result: int | float = 0

                    if operation == "addition":
                        result = add(a, b)
                    elif operation == "subtraction":
                        result = subtract(a, b)
                    elif operation == "multiplication":
                        result = multiply(a, b)
                    elif operation == "division":
                        result = divide(a, b)

                    self.assertEqual(result, int(expected))
                    self.results.append(
                        {
                            "operation": operation,
                            "a": a,
                            "b": b,
                            "expected": expected,
                            "result": result,
                            "status": "PASS",
                        }
                    )
                except Exception as e:
                    self.results.append(
                        {
                            "operation": operation,
                            "a": a,
                            "b": b,
                            "expected": expected,
                            "result": str(e),
                            "status": "FAIL",
                        }
                    )

                    if expected == "error":
                        self.assertRaises(ValueError, divide, a, b)
                    else:
                        self.fail(f"Unexpected error: {e}")

    @classmethod
    def tearDown(cls) -> None:
        df = pd.DataFrame(cls.results)

        print(df)

        now = datetime.now().strftime("%Y%m%dT%H%M%S")
        result_sheet_name = f"arithmetic_test_results_{now}"

        cls.sheets_client.add_new_sheet(sheet_name=result_sheet_name)
        cls.sheets_client.update_sheet(
            sheet_name=result_sheet_name,
            data=[df.columns.tolist()] + df.values.tolist(),
        )


if __name__ == "__main__":
    unittest.main()
