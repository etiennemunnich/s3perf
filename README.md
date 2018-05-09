# s3perf
Some performance ideas for S3:

The plan here is to create a copy ideas for writing to S3 to include the much needed random hash in the prefix to allow for higher request rates 
  - https://docs.aws.amazon.com/AmazonS3/latest/.../request-rate-perf-considerations.html
  
Example 1:
s3hcp.py - This is an simple example of adding the MD5 hash of a file infront of object name and then writing an index file that contains the object name and the location (hashed) in a csv.

example use for copying files in the current folder (doesn't recursively copy folders just yet) : 
 > python3 s3hcp.py * --bucket mybucket
 
more to follow.
