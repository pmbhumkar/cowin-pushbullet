import json
import time

from api import APIClient
from uri import URI

API_KEY = ""

def _get_today():
    today = time.time()
    timeformat = "%d-%m-%Y"
    return time.strftime(timeformat, time.gmtime(today))


class GetVaccine(object):
    def __init__(self):
        self.read_config()
        self.api = APIClient()
        self.api.session()
        self.pin_codes = self.config["pin_code"]
        self.today = _get_today()


    def read_config(self):
        with open("config.json", "r") as fd:
            self.config = json.load(fd)


    def get_vaccine_by_pin(self):
        self.vaccine_list = []
        for i in self.pin_codes:
            params = {
                "pincode": i,
                "date": self.today
            }
            response, ret_code = self.api.get(URI.calendar_by_pin, params=params)
            if response:
                self.vaccine_list.append(json.loads(response))

        
    def find_avail_vaccine(self):
        self.get_vaccine_by_pin()
        self.avail_data = []
        print(self.vaccine_list)
        for data in self.vaccine_list:
            for center in data["centers"]:
                center_data = {
                    "name": center["name"],
                    "fee": center["fee_type"],
                    "session": [],
                    "pincode": center["pincode"]
                }
                for session in center["sessions"]:
                    if session["available_capacity"] > 0:
                        center_data["session"].append({
                            "slot": session["slots"],
                            "avail": session["available_capacity"]
                        })
                if center_data["session"]:
                    self.avail_data.append(center_data)

    def print_slots(self):
        if self.avail_data:
            for data in self.avail_data:
                print(f"Center: {data['name']}")
                print(f"Fees: {data['fee']}")
                for session in data["session"]:
                    print(f"\tAvailable vaccine: {session['avail']}\tTime Slot: {session['slot']}")
        else:
            print(f"No vaccine available at {self.pin_codes}")


    def notify_to_my_phone(self):
        pincode_avail = []
        for data in self.avail_data:
            pincode_avail.append(data["pincode"])
        if pincode_avail:
            from pushbullet import Pushbullet
            pb = Pushbullet(API_KEY)
            push = pb.push_note("Vaccine available", f"{pincode_avail}")


if __name__ == "__main__":
    gv = GetVaccine()
    gv.find_avail_vaccine()
    gv.print_slots()
    gv.notify_to_my_phone()