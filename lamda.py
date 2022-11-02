import json
import boto3

from datetime import datetime
from datetime import timedelta

from collections import defaultdict

import configparser
import hashlib


def lambda_handler(event, context):
    config = configparser.ConfigParser()
    config.read('config.ini')
    bucket = config['DEFAULT']['S3_BUCKET']
    key = config['DEFAULT']['S3_KEY']
    s3 = boto3.client("s3")
    response = s3.get_object(Bucket=bucket, Key=key)
    data = response['Body'].read().decode('utf-8')
    logs = data.split('\n')
    # f = open("logs.log", "r").read()
    # logs = f.split('\n')

    # get the input parameters
    inputT = event['queryStringParameters']['T']
    inputDeltaT = event['queryStringParameters']['dT']

    # inputT = "23:47:00"
    # inputDeltaT = "00:00:05"

    # getting initial times
    initialTime = datetime.strptime(inputT, "%H:%M:%S")
    inputDeltaTimeArray = inputDeltaT.split(':')

    startDateTime = initialTime - timedelta(hours=int(inputDeltaTimeArray[0])) - timedelta(
        minutes=int(inputDeltaTimeArray[1])) - timedelta(seconds=int(inputDeltaTimeArray[2]))

    endDateTime = initialTime + timedelta(hours=int(inputDeltaTimeArray[0])) + timedelta(
        minutes=int(inputDeltaTimeArray[1])) + timedelta(seconds=int(inputDeltaTimeArray[2]))

    # gettin edge start and end times
    startTime = startDateTime.strftime("%H:%M:%S")
    endTime = endDateTime.strftime("%H:%M:%S")

    times = []

    # filling times array with values from start to end time

    while (startDateTime.strftime("%H:%M:%S") <= endTime):
        times.append(startDateTime.strftime("%H:%M:%S"))

        startDateTime = startDateTime + \
            timedelta(hours=0, minutes=0, seconds=1)

    print(times)

    response = {}
    transaction = {}

    # perform calculations

    found = False
    Dict = {}

    # separate values to build time -> value dict
    for i in range(0, len(logs)):
        if (logs[i] != ''):
            arrayOfTests = logs[i].split(" ")

            string = arrayOfTests.pop(0)

            splitted1 = string.split(":")

            splitted2 = splitted1[2].split(".")

            finalTime = splitted1[0] + ":" + splitted1[1] + ":" + splitted2[0]

            concat = ' '.join(arrayOfTests)
            if finalTime in Dict:
                Dict[finalTime].append(concat)
            else:
                Dict[finalTime] = [concat]

    # hash values
    hashed = []
    transaction['content'] = hashed
    for i in range(0, len(times)):
        if times[i] in Dict:
            hashed.extend(Dict[times[i]])
            found = True

    for i in range(0, len(hashed)):
        hashed[i] = str(hashlib.md5(hashed[i].encode()))

    if found == True:
        transaction['content'] = hashed
        response['statusCode'] = 200
    else:
        response['statusCode'] = 404

    transaction['isFound'] = str(found)

    response['headers'] = {}
    response['headers']['Content-Type'] = 'application/json'
    response['body'] = json.dumps(transaction)

    print(response)

    # return
    return response


# lambda_handler(1, 1)
