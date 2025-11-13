import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import time, random

def start_phone_tracker(target):
    print(f"PhoneTracer - OSINT")
    time.sleep(2)
    print(f"Target = {target}")
    p = phonenumbers.parse(target, None)
    r = geocoder.description_for_number(p, "en")
    timezones = timezone.time_zones_for_number(p)

    print(f"Location: {r}")
    print(f"TimeZone: {', '.join(timezones)}")

number = input("Enter Phone Number: EX (+1(719)299-2167)", )
start_phone_tracker(number)