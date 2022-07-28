import time
import hmac
import hashlib
import math

key = bytes([142, 167, 155, 206, 195, 213, 69, 151, 239, 225, 134, 120, 10, 131, 92, 7, 84, 0, 98, 58, 17, 72, 29, 61, 23, 221, 146, 233, 5, 219, 182, 21])

timeInMs = time.time() * 1000

startTime = math.floor((timeInMs - 300000) / 1000)
endTime = math.floor((timeInMs + 1800000) / 1000)

data = f'st={startTime}~exp={endTime}~acl=*'
hmac_token = hmac.new(key, bytes(data, 'utf-8'), digestmod=hashlib.sha256).hexdigest()

print(f'Your LVR Token is: {data}~hmac={hmac_token}')
