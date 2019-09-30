from minio import Minio
from minio.error import ResponseError
import urllib3
import os

minioClient = Minio('localhost:9001',
                    access_key='minio',
                    secret_key='minio123',
                    secure=False)

try:
    print(minioClient.bucket_exists("images"))
except ResponseError as err:
    print(err)

# try:
#     minioClient.make_bucket("mynewbucket")
# except ResponseError as err:
#     print(err)


try:
    objects = minioClient.list_objects('jaggy', prefix='my-prefixname',
                              recursive=True)
    for obj in objects:
        print(obj.bucket_name, obj.object_name.encode('utf-8'), obj.last_modified,
            obj.etag, obj.size, obj.content_type)    
except ResponseError as err:
    print(err)

# buckets = minioClient.list_buckets()
# for bucket in buckets:
#     print(bucket.name, bucket.creation_date)


# # # adding a file
# # try:
# #     with open('testfile.csv', 'rb') as file_data:
# #         file_stat = os.stat('testfile.csv')
# #         minioClient.put_object('mynewbucket', 'testfile.csv', file_data,
# #                     file_stat.st_size, content_type='application/csv')

# # except ResponseError as err:
# #     print(err)


# try:
#     minioClient.fput_object('mynewbucket', 'testfile.csv', '/tmp/testfile.log')
# except ResponseError as err:
#     print(err)