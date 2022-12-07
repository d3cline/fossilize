from minio import Minio
from minio.error import S3Error
from config import OBJECT_STORAGE_ACCESS_KEY, OBJECT_STORAGE_SECRET_KEY, OBJECT_STORAGE_DOMAIN

def main():
    client = Minio(
        OBJECT_STORAGE_DOMAIN,
        access_key=OBJECT_STORAGE_ACCESS_KEY,
        secret_key=OBJECT_STORAGE_SECRET_KEY,
    )

    if not client.bucket_exists("fossilize"): client.make_bucket("fossilize")

    client.fput_object(
        "fossilize", "asiaphotos-2015.zip", "/home/user/Photos/asiaphotos.zip",
    )

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)
