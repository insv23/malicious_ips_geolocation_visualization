import json


# 读取 txt 文件并将每一行存储为一个列表
def read_ips(file_path):
    with open(file_path, 'r') as file:
        ips = [line.strip() for line in file]
    return ips


def save_list_to_json(data_list, file_path, mode="w"):
    """
    将列表数据保存到 JSON 文件中

    Args:
        data_list: 要保存的列表数据
        file_path: JSON 文件路径
        mode: 文件打开模式，默认为 "w" (覆盖写入)，也可以使用 "a" (追加写入)
    """
    with open(file_path, mode) as f:
        json.dump(data_list, f, indent=4)


def load_list_from_json(file_path):
    """
    从 JSON 文件中读取列表数据

    Args:
        file_path: JSON 文件路径

    Returns:
        读取到的列表数据
    """
    with open(file_path, "r") as f:
        return json.load(f)
