#! /usr/bin/env python3
import sys
import requests
import json

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ENTER ACCOUNT ID HERE"
auth_token = "ENTER AUTH TOKEN HERE"

r = requests.get('https://lookups.twilio.com/v1/PhoneNumbers/' + sys.argv[1] + '?Type=caller-name', auth=(account_sid, auth_token))
r = json.loads(r.text)

caller_name = (r['caller_name'])['caller_name']
caller_type = (r['caller_name'])['caller_type']
phone_number = (r['national_format'])

print ()
try:
    print (' Caller Name:  ' + caller_name)
    print ('   Call Type:  ' + caller_type)
    print ('Phone Number:  ' + phone_number)
except TypeError:
    print ('Phone number not found!')
print ()
