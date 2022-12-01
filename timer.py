# Make sure you call the following commands in your Bash Terminal prior to running this Python file:
#   pip install schedule
#   pip install requests

# Imports
import schedule
import time
import json
import time
import requests
import os

_CWD = os.path.dirname(os.path.abspath(__file__))
_CITIZEN_RESPONSE_OUTPUT_FOLDER = os.path.normpath(_CWD+"/citizenData/")
_CITIZEN_REQUEST_HEADERS = {
    "Host":"citizen.com",
    #User-Agent Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0
    "Accept":"application/json",
    "Accept-Language":"en-US,en;q=0.5",
    "Accept-Encoding":"gzip, deflate, br",
    "Referer":"https://citizen.com/explore",
    "DNT":1,
    "Alt-Used":"citizen.com",
    "Connection":"keep-alive",
    "Cookie client":"Country=US",
    "Sec-Fetch-Dest":"empty",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"same-origin",
    "Sec-GPC":1
}
_CITIZEN_REQUEST_URL = 'https://citizen.com/api/incident/trending?lowerLatitude=40.448434320616485&lowerLongitude=-74.76447397469826&upperLatitude=41.00440450208279&upperLongitude=-73.16752602529988&fullResponse=true&limit=30'
_TIME_DELAY = 60    # Seconds delay between timer

# Main function - called upon file being run
def main():

    # First check if an output folder exists. If it doesn't create it
    isExist = os.path.exists(_CITIZEN_RESPONSE_OUTPUT_FOLDER)
    if not isExist:
        os.makedirs(_CITIZEN_RESPONSE_OUTPUT_FOLDER)
        print("[TIMER] Path to output folder has been created!")
    else:
        print("[TIMER] Path to output folder already exists!")

    # The timer function that runs every `_TIME_DELAY` seconds
    def timer():
        # Get current time for the filename
        timestr = time.strftime("%Y-%m-%d_%H-%M-%S")
        # Make the request to Citizen
        r = requests.get(\
            _CITIZEN_REQUEST_URL,\
            _CITIZEN_REQUEST_HEADERS\
        )
        # Convert response into serialized string
        json_object = json.dumps(r.json(), indent=2)
        # Create a new file, write to file, and then close file
        json_file = os.path.normpath(_CITIZEN_RESPONSE_OUTPUT_FOLDER+"/"+timestr+".json")
        outfile = open(json_file, "w")
        outfile.write(json_object)
        outfile.close()
        print("[TIMER] Printing record: {}".format(json_file))

    # This is the schedule that runes `timer()` everu `_TIME_DELAY` seconds
    schedule.every(_TIME_DELAY).seconds.do(timer)

    # Infinite loop to run the scheduler
    while True:
        schedule.run_pending()
        time.sleep(1)

# This ensures that this python code will run if you call it from a Bash Terminal
if __name__ == "__main__":
    main()