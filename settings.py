PODUP_API_URL = "https://api.fediverse.observer/"
INSTANCE_URL = "https://opalstack.social/"
OBJECT_STORAGE_ACCESS_KEY = ''
OBJECT_STORAGE_SECRET_KEY = ''
OBJECT_STORAGE_DOMAIN = ''

try:
    from .local_settings import *
except ImportError:
    pass