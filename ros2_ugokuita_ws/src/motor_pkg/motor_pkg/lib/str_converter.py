def to_str(byte_str):
    str = byte_str.decode('utf-8')
    return str

def to_dict(str):
    # strを辞書に変換する
    dict = {}
    for key_value in str.split(','):
        key, value = key_value.split(':')
        dict[key] = value
    return dict