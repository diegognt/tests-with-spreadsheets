# Python data-driven test using Google Sheet

This is a POC project about how to perform unit tests using data from a Google spreadsheet, uses Python's built-in [unittest library](https://docs.python.org/3/library/unittest.html) for testing. This project includes a simple Python functions and a corresponding unit test to ensure its correctness.

## Setup and running

### 💿 Prerequisites

- [Docker](https://www.docker.com)
- [Docker compose](https://docs.docker.com/compose/)
- [Google Cloud setup](./docs/GOOGLE_CLOUD_SETUP.md)

## 🚀Running the tests

1. Clone the repo
```sh
git clone https://github.com/diegognt/tests-with-spreadsheets.git
cd tests-with-spreadsheets
```

2. Make sure to have the [Google Cloud](./docs/GOOGLE_CLOUD_SETUP.md) already setup

3. Running the tests,

All the tests
```sh
make all-tests
```

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
