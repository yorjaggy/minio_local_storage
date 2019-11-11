from minio import Minio
from minio.error import ResponseError
import urllib3
import os

minio_access_key = '<access_key_val>'
minio_secret_key = '<secret_key_val>'

minioClient = Minio('i2thub.icesi.edu.co:9992',
                    access_key=minio_access_key,
                    secret_key=minio_secret_key)

# try:
#     print(minioClient.bucket_exists("guaralst"))
# except ResponseError as err:
#     print(err)

# try:
#     minioClient.make_bucket("otroguaral")
# except ResponseError as err:
#     print(err)

#adding a file
# try:
#     with open('test2.csv', 'rb') as file_data:
#         file_stat = os.stat('test2.csv')
#         minioClient.put_object('guaralst', 'test2.csv', file_data, file_stat.st_size, content_type='application/csv')
# except ResponseError as err:
#     print(err)


# try:
#     minioClient.fput_object('guaralst', 'test2_copy.csv', 'test2_copy.csv')
# except ResponseError as err:
#     print(err)

# # Get a full object.
# try:
#     data = minioClient.get_object('guaralst', 'test2_copy.csv')
#     with open('my-testfile.csv', 'wb') as file_data:
#         for d in data.stream(32*1024):
#             file_data.write(d)
# except ResponseError as err:
#     print(err)

# List objects
try:
    objects = minioClient.list_objects('guaralst', recursive=True)
    for obj in objects:
        print(obj.bucket_name, obj.object_name.encode('utf-8'), obj.last_modified,
            obj.etag, obj.size, obj.content_type)    
except ResponseError as err:
    print(err)

# List objects
try:
    objects = minioClient.list_objects('guaralrpc', recursive=True)
    for obj in objects:
        print(obj.bucket_name, obj.object_name.encode('utf-8'), obj.last_modified,
            obj.etag, obj.size, obj.content_type)    
except ResponseError as err:
    print(err)

# # List objects
# buckets = minioClient.list_buckets()
# for bucket in buckets:
#     print(bucket.name, bucket.creation_date)

# Remove Bucket
try:
    minioClient.remove_bucket("guaralst")
except ResponseError as err:
    print(err)

# Remove an object.
# try:
#     minioClient.remove_object('guaralst', 'emotionv2.jpeg')
#     minioClient.remove_object('guaralrpc', '55.jpg')
# except ResponseError as err:
#     print(err)