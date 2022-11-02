# LambdaFunction in python

## A distributed program for parsing logfiles to return result back

## Name: Nikita Mashchenko

### Development Environment

- Windows 10
- Python 3.9.0
- Visual Studio Code

## Entire Setup of the Project:


## Overview

This project describes behaviour of Lambda Function.<br/>
The Lambda function checks with the help of dict if timestamp is present inside<br/>

If the logs are present, the response returned is the md5 hash of logs with a statusCode of 200.<br/>
If no logs were present in the timerange, the response is a 400-level message with a message that logs were not present in the time range.


## Running

To run this, you can either use local file and do python <filename>.py or copy and paste this code directly to the lambda function

## Tests

I have two implementations : binary search and this one, after doing heavy tests (with 5000+ lines) and using both codes, runtime for this one is less for 10/12 tests. I can also show the binary search code on request later. I can explain it happens because python dict elements access has O(1) access time which is a lot faster than O(logn) for binary search

## All repos:

https://github.com/exortme1ster/AkkaLogsHandler

https://github.com/exortme1ster/GRPCClientServer

https://github.com/exortme1ster/LogFileGenerator

https://github.com/exortme1ster/pythonLambda

## Video:
https://www.youtube.com/watch?v=fmeBeOcpBy0
