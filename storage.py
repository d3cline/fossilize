from minio import Minio
from minio.error import S3Error
from settings import OBJECT_STORAGE_ACCESS_KEY, OBJECT_STORAGE_SECRET_KEY, OBJECT_STORAGE_DOMAIN
import io 

def put_object(path, data):
    client = Minio(
        OBJECT_STORAGE_DOMAIN,
        access_key=OBJECT_STORAGE_ACCESS_KEY,
        secret_key=OBJECT_STORAGE_SECRET_KEY,
    )
    if not client.bucket_exists("fossilize"): client.make_bucket("fossilize")
    result = client.put_object(
        "fossilize", path, io.BytesIO(data.encode('gbk')), length=-1, part_size=10*1024*1024,
    )
    print(f'Put: {path}')


