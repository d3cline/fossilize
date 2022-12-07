from minio import Minio
from minio.error import S3Error
from settings import OBJECT_STORAGE_ACCESS_KEY, OBJECT_STORAGE_SECRET_KEY, OBJECT_STORAGE_DOMAIN
import io 

def main():
    client = Minio(
        OBJECT_STORAGE_DOMAIN,
        access_key=OBJECT_STORAGE_ACCESS_KEY,
        secret_key=OBJECT_STORAGE_SECRET_KEY,
    )

    if not client.bucket_exists("fossilize"): client.make_bucket("fossilize")

    result = client.put_object(
        "fossilize", "ayy", io.BytesIO(b"hello"), length=-1, part_size=10*1024*1024,
    )


if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)
