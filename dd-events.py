#!/usr/bin/python3

import os
import sys
import time
import subprocess
import logging
from datadog import initialize, api

class DDAGGREGATOR(object):
    """This class is used to pull alerts from DataDog and push them into a Kafka topic.
    """
    def __init__(self):
        self.options = {"api_key" : 'XXXXXXXXXXXX', \
                    'app_key':'XXXXXXXXXXXXX'}
        initialize(**self.options)

    @staticmethod
    def prep_timing():
        """This function is used to set the time frame that events will be pulled from
        datadog. Returns an object with 2 KV pairs, start_time:int() and end_time:int()
        """
        end_time = time.time()
        start_time = end_time - (60 * 60 * 24) #86400 = 1day
        times = {"start_time": start_time, "end_time": end_time}
        return times

    def collect_events(self, times):
        """This function collects the datadog events for a time frame specified by the times
        object. We pull the full list from the API then format the pieces we want, returning
        a list.
        """
        all_events = api.Event.query(start=times["start_time"], end=times["end_time"])
        print(all_events)

DDA = DDAGGREGATOR()      
while True:
    TIMES = DDA.prep_timing()
    EVENT_ARRAY = DDA.collect_events(TIMES)
    print(EVENT_ARRAY)
    time.sleep(5)
