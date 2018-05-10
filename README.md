# s3perf
Some performance ideas for S3 - make the most of request rates to S3:

The plan here is to create some proof of concept ideas for writing/reading to/from S3 to allow for higher request rates 
  - https://docs.aws.amazon.com/AmazonS3/latest/.../request-rate-perf-considerations.html
  
Random Hash implementations:
 - Using a random hash prefix to the object name will allow for higher request rates.  Here are some example
   s3://mybucket/[random hex hash]/objectname.txt
   s3://mybucket/a/objectname.txt
   s3://mybucket/b/objectname.txt
   ....
   s3://mybucket/z/objectname.txt
  
Example 1:
s3hcp.py - This is an simple example of adding the MD5 hash of a file infront of object name and then writing an index file that contains the object name and the location (hashed) in a csv.

Use: 
 > python3 s3hcp.py [localfile(s)] --bucket [bucketname]

Example use for copying files in the current folder (doesn't recursively copy folders just yet): 
 > python3 s3hcp.py * --bucket mybucket
 or
 > python3 s3hcp.py *.csv --bucket mybucket
 
Some further ideas:
 - async implementation or look at threading for higher through-puts
 - need to put more exception checking in:
    * check the bucket exists
 - allow for writing ACLs, encryption, tags and meta-data
 - allow for an input file list to process for upload to S3
 - allow for retry logic and debug log files
