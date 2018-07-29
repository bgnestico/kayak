# -*- coding: utf-8 -*-
from qa_automation.tools import steps_helper


PICKUP_LOCATION = 'SFO'

DROPOFF_LOCATION = 'LAX'

PICKUP_DATE = [
    generate_pickup_date(1),
    generate_pickup_date(4),
    generate_pickup_date(7),
    generate_pickup_date(10),
    generate_pickup_date(13),
]

DROPOFF_DATE = [
    generate_dropoff_date(1),
    generate_dropoff_date(4),
    generate_dropoff_date(7),
    generate_dropoff_date(10),
    generate_dropoff_date(13),
]
