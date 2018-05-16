#! /usr/bin/env python3
import sys
import requests
import json

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ENTER ACCOUNT ID HERE"
auth_token = "ENTER AUTH TOKEN HERE"

try:
    query = sys.argv[1]
except IndexError:
    print('\nError: no argument provided')
    print('Usage: lookup.py 123-456-7890\n')
    exit(1)

try:
    r = requests.get('https://lookups.twilio.com/v1/PhoneNumbers/' + query + '?Type=caller-name', auth=(account_sid, auth_token))
    r = json.loads(r.text)
except:
    print('\nError: unable to access twilio api endpoint\n')
    exit(1)

try:
    caller_name = (r['caller_name'])['caller_name']
    caller_type = (r['caller_name'])['caller_type']
    phone_number = (r['national_format'])
except:
    print('\nError: invalid API response\nensure that account id and auth token is set\n')
    exit(1)

print ()
try:
    print (' Caller Name:  ' + caller_name)
    print ('   Call Type:  ' + caller_type)
    print ('Phone Number:  ' + phone_number)
except TypeError:
    print ('Phone number not found!')
print ()
