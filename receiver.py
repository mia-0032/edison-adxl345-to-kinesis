# -*- coding: utf-8 -*-

import boto3
import logging

from sys import argv
from time import sleep

# logger
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

stream_name = argv[1]
logger.info("Stream Name: {0}".format(stream_name))

kinesis = boto3.client('kinesis')

# get shard id
stream = kinesis.describe_stream(
    StreamName=stream_name
)

# streame has only 1 shard
shard_id = stream['StreamDescription']['Shards'][0]['ShardId']

shard_iterator = kinesis.get_shard_iterator(
    StreamName=stream_name,
    ShardId=shard_id,
    ShardIteratorType='TRIM_HORIZON'
)['ShardIterator']

while True:
    res = kinesis.get_records(
        ShardIterator=shard_iterator,
        Limit=100
    )
    for r in res['Records']:
        logger.info(
            'Time: {0}, Data: {1}'.format(
                r['ApproximateArrivalTimestamp'],
                r['Data']
            )
        )
    shard_iterator = res['NextShardIterator']
    sleep(1)
