import os
from typing import Any, Dict
import pandas as pd
import unittest
from utilities.google_sheets import GoogleSheetsClient
from app.arithmetic import add, subtract, multiply, divide


class ArithmeticTest(unittest.TestCase):
    sheets_client = GoogleSheetsClient()
    spreadsheet_id: str | None = ""
    data: pd.DataFrame = []
    results: list[Dict[str, Any]] = []

    @classmethod
    def setUp(cls) -> None:
        cls.spreadsheet_id = os.environ.get("SPREADSHEET_ID")

        if not cls.spreadsheet_id:
            raise ValueError(
                "SPREADSHEET_ID is not set in the environment variables."
            )

        data_range = "arithmetic_test_cases!A1:D"
        cls.data = cls.sheets_client.fetch_data(
            spreadsheet_id=cls.spreadsheet_id, range=data_range
        )

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


if __name__ == "__main__":
    unittest.main()
