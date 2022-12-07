from minio import Minio
from minio.error import S3Error
from config import OBJECT_STORAGE_ACCESS_KEY, OBJECT_STORAGE_SECRET_KEY, OBJECT_STORAGE_DOMAIN

def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        OBJECT_STORAGE_DOMAIN,
        access_key=OBJECT_STORAGE_ACCESS_KEY,
        secret_key=OBJECT_STORAGE_SECRET_KEY,
    )

    # Make 'asiatrip' bucket if not exist.
    found = client.bucket_exists("asiatrip")
    if not found:
        client.make_bucket("asiatrip")
    else:
        print("Bucket 'asiatrip' already exists")

    # Upload '/home/user/Photos/asiaphotos.zip' as object name
    # 'asiaphotos-2015.zip' to bucket 'asiatrip'.
    client.fput_object(
        "asiatrip", "asiaphotos-2015.zip", "/home/user/Photos/asiaphotos.zip",
    )


if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)
