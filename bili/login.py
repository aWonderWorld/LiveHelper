from bili.bilibili import Bilibili


def request_getKey():
    inst = Bilibili.instance

    temp_params = f'appkey={inst.dictAccount["appkey"]}'
    sign = inst.
