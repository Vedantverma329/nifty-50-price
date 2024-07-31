# Nifty Scheduler

This Python script fetches and displays real-time NIFTY 50 stock data using the `jugaad-data` library. It can be scheduled to run at specific intervals using the `schedule` library. Additionally, it creates a DataFrame from the fetched data and allows for further data manipulation.

## Features

- **Real-time Stock Data**: Fetches the latest NIFTY 50 data using the `jugaad-data` library.
- **Scheduling**: Uses the `schedule` library to run the data retrieval function at specified intervals.
- **Data Export**: Converts the fetched data into a pandas DataFrame for easy data manipulation and potential export.
- **Error Handling**: Includes error handling for data fetching and DataFrame creation.

## Project Structure

- **`nifty_scheduler.py`**: Main script that contains the logic for fetching stock data, scheduling the retrieval process, and converting the data to a DataFrame.

## Requirements

- Python 3.x
- `jugaad-data` library
- `numpy` library
- `pandas` library
- `schedule` library

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/nifty_scheduler.git
   cd nifty_scheduler

## pip install jugaad-data numpy pandas schedule
