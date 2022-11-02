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
  
## Alghorithm
  
We first get the logfile from the S3 bucket, as well as Time and DeltaTime from queries
  
https://<link>?T=<time>&dT=<time>
  
We start processing the logfile by calculating startTime and endTime based on deltaTime
  
Then we generate the array of times starting from startTime to endTime, so:
  
If endTime is "23:47:45" and startTime is "23:47:30" we will generate following array:

["23:47:30", "23:47:31", "23:47:32", ... , "23:47:45"]
  
You can always modify this by chaning timedelta parameters (e.g. seconds, minutes, hours)

Then we build a dictionary, e.g. :
  Key will be a time, for example: "23:47:30" and value would be rest of the line, e.g. : [scala-execution-context-global-73] WARN  HelperUtils.Parameters$ - s%]s,+2k|D}K7b/XCwG&@7HDPR8z
  
Please not that there can be a lot of logs on same file, so each time stores array of logs for that specific grouped time that we can access later
  
Finally we take array of generated times and for each value inside of this array we check if it exsists inside the dictionary and if it is, we hash the values and return statusCode 200
  
Access time is O(1) which satisfy the project requirment
  
 

## All repos:

https://github.com/exortme1ster/AkkaLogsHandler

https://github.com/exortme1ster/GRPCClientServer

https://github.com/exortme1ster/LogFileGenerator

https://github.com/exortme1ster/pythonLambda

## Video:
https://www.youtube.com/watch?v=fmeBeOcpBy0
