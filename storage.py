from minio import Minio
from minio.error import S3Error
from settings import OBJECT_STORAGE_ACCESS_KEY, OBJECT_STORAGE_SECRET_KEY, OBJECT_STORAGE_DOMAIN
import io 

client = Minio(
    OBJECT_STORAGE_DOMAIN,
    access_key=OBJECT_STORAGE_ACCESS_KEY,
    secret_key=OBJECT_STORAGE_SECRET_KEY,
)

def put_object(path, data):
    if not client.bucket_exists("fossilize"): client.make_bucket("fossilize")
    result = client.put_object("fossilize", path, io.BytesIO(data.encode('gbk')), length=-1, part_size=10*1024*1024)
    print(f'Put: {path}')

def list_rdap():
    cached_rdaps = []
    for obj in client.list_objects("fossilize", prefix="rdap/"): cached_rdaps.append(obj.object_name.split('/')[1].encode().decode("idna"))
    return cached_rdaps