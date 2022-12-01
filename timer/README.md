# bdf22-final [_Group Name Pending_]

## Group Members:
- Aditya Ramesh Chavan
- Bhavish Yalamanchi
- Dipak Patel
- Ryan Kim

## Data Sources:

## Current Setup:

### Timer: Pulling data from Citizen:

_Provided via `timer.py`_

**How to run:**
1. Open `timer.py` in an IDE (recommended: Visual Studio Code or IntelliJ)
2. Run `timer.py` via either IDE UI or via command prompt in a Bash Terminal window
The code will automatically  create a folder to save the outputted JSON files into.

**How it works:**
1. Upon startup, the program will automatically create an output folder `citizenData` in the same directory as `timer.py`.
2. The program has a variable `_TIME_DELAY` that will act as the time gap (in seconds) between pulling data from Citizen
3. Every `_TIME_DELAY` seconds, the program will make a `GET` request to the Citizen API. The response will be in JSON format.
4. This received data will be saved as `<CURRENT TIME>.json` inside of `citizenData` directory.
5. The program will repeat steps 3-4 until you tell the program to stop via command prompt:
    * `ctrl+C` in Windows
    * `cmd+C` in Mac

### Data Processing
TBD
