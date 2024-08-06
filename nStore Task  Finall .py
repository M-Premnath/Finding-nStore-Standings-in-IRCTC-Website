import csv
import json
import os
import requests

#station code JSON data

station_data = """
{
  "stations": [
    {
      "code": "AGC",
      "name": "Agra Cantonment"
    },
    {
      "code": "JTJ",
      "name": "Jolarpettai"
    },
    {
      "code": "CNB",
      "name": "Kanpur Central"
    },
    {
      "code": "TN",
      "name": "Tuticuorin"
    },
    {
      "code": "MAS",
      "name": "Chennai Central"
    },
    {
      "code": "ED",
      "name": "Eroad JN"
    },
    {
      "code": "TJ",
      "name": "Thanjavur JN"
    },
    {
      "code": "CBE",
      "name": "Coimbatore"
    },
    {
      "code": "TUP",
      "name": "Tirupur"
    },
    {
      "code": "TPTY",
      "name": "Tirupati"
    },
    {
      "code": "TPJ",
      "name": "Tiruchchirappalli JN"
    }
  ]
}
"""

# URL template with placeholders for station code
url_template = "https://www.ecatering.irctc.co.in/api/v2/station/outlets?stationCode={}&time=&date=&token=03AFcWeA533OG2vPylwP6I8uVNWB6NKKhqgaWjDRm48MrZKK_GkSIeAqvqJSvbIKzRuSAPTl19ffPpySu-5VKbh3P_V8B2UfvqQTW7jjEtRAW7DPT0wKTy5577R7hSKkU27N51khDek36O3PeBdaykBf0lhe7LlniiNL7WbS1qtoT9jH4R5L2_CrCjCJQN2bo_YJ2JPsCUjI4-2YFcmpWB28yV-crh1TMKdu1dnRrHxIXYeC6w0gYC_HQrhiAb3eQLBELK8HOUErJ2XdR2p-MfpDnmdLDdiPbcsFdr3cwEzzQFHYVRixy9djb4Ns_pnc5KZSsUxa9Qy-q3kSu-ghftu0jNZE0HoOZMASfW1HqSJOdUV5n_MpoZKx71dnZE2Hp2DwM7BIDu-fA2oUTtty9scJ2SHoX3iXiHkFrFoK8jNPWZdcGtbdGlloGY0KIwkhEi4UPP9MT4QrRGVVMMVUknQmnGc--y6Uc-_yAyQP_efPhNtXvYwqt2-_NMIBQnrFRvjId7deJ6LCQc1_I3MLrhxNKzLM93yLVdhi34fWuZ-6O9OaD9wIINscRY8AUboit3ZmuJtEF_ORHF2RanxgfODJNlwQ8KDQVdZQmV9lU2BLch0if_a5o0iAEj3YPNw6JgKorLD5y9ae4gnyYJgcbEXoszYf_7WBXUCOkGV9P0P9W7wmads80yxN2xbjkPHPwyvrFvJ6F-Z6JY&_=1715842759032"


# Parse station data
station_data_json = json.loads(station_data)

# Clear the CSV file
if os.path.exists('nStore position.csv'):
    os.remove('nStore position.csv')


# Open (or create) a CSV file with append mode
with open('nStore position data.csv', 'a', newline='') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)

    # Check if the CSV file is empty
    if csvfile.tell() == 0:
        # Write the header row
        writer.writerow(["S.No","Station Name", "Station Code", "Total Outlets", "nStore Index"])
         
        # Initialize a serial number variable
        s_no = 1

    # Iterate over each station
    for station in station_data_json["stations"]:
        # Extract station code and name
        station_code = station["code"]
        station_name = station["name"]

        # Construct URL with station code
        url = url_template.format(station_code) # type: ignore

        # Send request
        response = requests.get(url)

        # Check if request was successful
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()

            # Find the index of the "nStore Technologies Pvt Ltd" vendor
            nstore_index = None
            total_outlets = data["result"]["totalOutlets"]
            for index, vendor in enumerate(data["result"]["vendors"]):
                if vendor["name"] == "nStore Technologies Pvt Ltd":
                    nstore_position = index + 1
                    break

            # Write the station data to the CSV file
            writer.writerow([s_no, station_name, station_code, total_outlets, nstore_position])
                    
            # Increment the serial number
            s_no += 1

        else:
            writer.writerow([station_name, station_code, "Failed to fetch data", ""])

