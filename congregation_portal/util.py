# -*- coding: utf-8 -*-
import datetime


def clean_phone(phone):
    return phone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')

states = [('AL', 'Alabama'),
          ('AK', 'Alaska'),
          ('AZ', 'Arizona'),
          ('AR', 'Arkansas'),
          ('CA', 'California'),
          ('CO', 'Colorado'),
          ('CT', 'Connecticut'),
          ('DE', 'Delaware'),
          ('FL', 'Florida'),
          ('GA', 'Georgia'),
          ('HI', 'Hawaii'),
          ('ID', 'Idaho'),
          ('IL', 'Illinois'),
          ('IN', 'Indiana'),
          ('IA', 'Iowa'),
          ('KS', 'Kansas'),
          ('KY', 'Kentucky'),
          ('LA', 'Louisiana'),
          ('ME', 'Maine'),
          ('MD', 'Maryland'),
          ('MA', 'Massachusetts'),
          ('MI', 'Michigan'),
          ('MN', 'Minnesota'),
          ('MS', 'Mississippi'),
          ('MO', 'Missouri'),
          ('MT', 'Montana'),
          ('NE', 'Nebraska'),
          ('NV', 'Nevada'),
          ('NH', 'New Hampshire'),
          ('NJ', 'New Jersey'),
          ('NM', 'New Mexico'),
          ('NY', 'New York'),
          ('NC', 'North Carolina'),
          ('ND', 'North Dakota'),
          ('OH', 'Ohio'),
          ('OK', 'Oklahoma'),
          ('OR', 'Oregon'),
          ('PA', 'Pennsylvania'),
          ('RI', 'Rhode Island'),
          ('SC', 'South Carolina'),
          ('SD', 'South Dakota'),
          ('TN', 'Tennessee'),
          ('TX', 'Texas'),
          ('UT', 'Utah'),
          ('VT', 'Vermont'),
          ('VA', 'Virginia'),
          ('WA', 'Washington'),
          ('WV', 'West Virginia'),
          ('WI', 'Wisconsin'),
          ('WY', 'Wyoming')]

years = tuple((str(n)) for n in range(1995, datetime.datetime.now().year + 1))

msgs = {'msg_login': u'User does not exist or password was incorrect.'}

dthandler = lambda obj: (obj.isoformat() if isinstance(obj, (datetime.datetime, datetime.date)) else None)
