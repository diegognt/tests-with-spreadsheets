# Python data-driven test using Google Spreadsheet

This is a POC project about how to perform tests using data from a Google spreadsheet, uses Python's built-in [unittest library](https://docs.python.org/3/library/unittest.html) for testing. This project includes a simple Python functions and a corresponding unit test to ensure its correctness.

## Setup and running

### 💿 Prerequisites

- [Docker](https://www.docker.com)
- [Docker compose](https://docs.docker.com/compose/)

### 🚀Building

1. Clone the repo
```sh
git clone https://github.com/diegognt/tests-with-spreadsheets.git
cd tests-with-spreadsheets
```

2. Build the Docker image using Docker Compose:
```sh
docker-compose up --build
```

The command will:

 - Build the Docker image based on the Dockerfile.
 - Run the unit tests inside the Docker container.

3. When you are done, you can stop and remove the Docker containers with:
```sh
docker-compose down
```

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
