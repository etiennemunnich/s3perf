import argparse
import os
import glob
import hashlib
import boto3

def main():

    parser = argparse.ArgumentParser(description='Read in a file or set of files, and return the result.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('path', nargs='+', help='Path of a file or a folder of files')
    parser.add_argument('-e', '--extension', default='', help='File extension to filter by')
    parser.add_argument('-b', '--bucket', default='', help='Destination Bucket, eg. -b mybucket')

    args = parser.parse_args()

    path = args.path
    if path == '':
        print ('No bucket specified.')
        exit(1)
    else:
        bucket = args.bucket
        print ('Destination bucket: ',bucket)


esp.cars@yahoo.com.au


    s3 = boto3.resource( 's3' )

    indexfile = open('index.csv', 'w')
    indexfile.write('FileName, HFLocation')
    files = set()
    for f in path:
        
        if os.path.isdir(f):
            print (f, ' is a folder, skipped.')
        else:
            try:
                hash_prefix = hashlib.md5(open(f, 'rb').read()).hexdigest()
            except IOError as e:
                errno, strerror = e.args
                print("I/O error({0}): {1}".format(errno,strerror))
                # e can be printed directly without using .args:
                # print(e)
            filehash = "/".join([hash_prefix + '/' + f])
            print(f)
            s3.Object(bucket, filehash).put(Body=open(f, 'rb'))
            ContentsIndex = f + ',' + filehash + '\n'
            indexfile.write(ContentsIndex)

    print('Writing index file.')
    s3.Object(bucket, 'index.csv').put(Body=open('index.csv', 'rb'))


if __name__ == '__main__':
    main()
