# -*- coding: utf-8 -*-

import boto3
import json
import logging
import pyupm_adxl345 as adxl345

from socket import gethostname
from sys import argv
from time import sleep

# logger for debugging
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

stream_name = argv[1]
logger.info("Stream Name: {0}".format(stream_name))

adxl = adxl345.Adxl345(6)  # Eaglet board Grove connector is connected to I2C_6
kinesis = boto3.client('kinesis')

while True:
    # get Acceleration
    adxl.update()
    force = adxl.getAcceleration()
    data = {'X': force[0], 'Y': force[1], 'Z': force[2]}
    logging.info("Data: {0}".format(data))

    # send to Kinesis
    res = kinesis.put_record(
        StreamName=stream_name,
        Data=json.dumps(data),
        PartitionKey=gethostname()  # as you like
    )
    logging.info("Response: {0}".format(res))

    sleep(0.1)
