# edsion-adxl345-to-kinesis
Send ADXL345 sensor values to Amazon Kinesis from Intel Edison.

## Setup

```shell
$ pip install -r requirements.txt
```

## Execute

Send sensor data to Kinesis.

```
$ python sender.py <your_stream_name>
```

## Check Stream Data

Get data fron Kinesis.

```
$ python receiver.py <your_stream_name>
```
