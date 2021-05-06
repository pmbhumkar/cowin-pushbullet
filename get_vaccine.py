import json
import time
import datetime

from api import APIClient
from uri import URI


class GetVaccine(object):
    def __init__(self):
        self.read_config()
        self.api = APIClient()
        self.api.session()
        self.api_key = self.config["api_key"]
        self.pin_codes = self.config["pin_code"]
        self.time_delay = self.config["time_delay"]
        self.age = self.config["age"]
        print(self.pin_codes)


    def read_config(self):
        with open("config.json", "r") as fd:
            self.config = json.load(fd)


    def get_vaccine_by_pin(self):
        self.vaccine_list = []
        newdate = datetime.date.today()
        for days in range(4):
            str_date = newdate.strftime("%d-%m-%Y")
            for i in self.pin_codes:
                params = {
                    "pincode": i,
                    "date": str_date
                }
                response, ret_code = self.api.get(URI.calendar_by_pin, params=params)
                print(ret_code)
                if ret_code == 200:
                    self.vaccine_list.append(json.loads(response))
                newdate = newdate + datetime.timedelta(days=7)

        
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
                    if session["available_capacity"] > 0 and \
                    session["min_age_limit"] in self.age:
                        center_data["session"].append({
                            "slot": session["slots"],
                            "avail": session["available_capacity"],
                            "type": session["vaccine"]
                        })
                if center_data["session"]:
                    self.avail_data.append(center_data)

    def print_slots(self):
        if self.avail_data:
            for data in self.avail_data:
                print(f"Center: {data['name']}")
                print(f"Fees: {data['fee']}")
                for session in data["session"]:
                    print(f"\tAvailable vaccine: {session['type']}\t{session['avail']}\tTime Slot: {session['slot']}")
        else:
            print(f"No vaccine available at {self.pin_codes}")


    def notify_to_my_phone(self):
        data_to_notify = []
        for data in self.avail_data:
            vaccine_types = []
            for session in data["session"]:
                vaccine_types.append(session["type"])
            vaccine_types = set(vaccine_types)
            data_to_notify.append(f"{data['name']} - {','.join(vaccine_types)}")
        if data_to_notify:
            from pushbullet import Pushbullet
            pb = Pushbullet(self.api_key)
            info = "\n".join(set(data_to_notify))
            push = pb.push_note("Vaccine available", info)



if __name__ == "__main__":
    import sched
    import time

    event_schedule = sched.scheduler(time.time, time.sleep)
    gv = GetVaccine()

    def main():
        gv.find_avail_vaccine()
        gv.print_slots()
        gv.notify_to_my_phone()
        event_schedule.enter(gv.time_delay, 1, main)

    event_schedule.enter(2, 1, main)
    event_schedule.run()