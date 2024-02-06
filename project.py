import requests
class Irctc:
    def __init__(self) -> None:
        user_input = input("""
        How would you like to procees?
        1. Enter 1 to check live train status
        2. Enter 2 to check PNR
        3. Enter 3 to check train schedule
""")
        
        if user_input == "1":
            print("Live train status")
        elif user_input == "2":
            print("Check PNR")
        else:
            self.train_schedule()

    def train_schedule(self):
        train_num = input("Enter the train number ")
        self.fetch_data(train_num)

    def fetch_data(self, train_num):
        data = requests.get("https://indianrailapi.com/api/v2/TrainSchedule/apikey/30c382602bfa67c8a7c580e6cfe2becb/TrainNumber/{}".format(train_num))
        data = data.json()
        # print(data)

        for i in data['Route']:
            print(i['StationName'], "|", i['ArrivalTime'], "|", i['DepartureTime'], "|", i["Distance"], "km")


obj = Irctc()