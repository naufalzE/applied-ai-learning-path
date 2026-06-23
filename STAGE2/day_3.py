import sys

def is_virtual_environment():
    return sys.prefix != sys.base_prefix


if is_virtual_environment():
    print("Virtual Environment Aktif")
else:
    print("Menggunakan System Python")