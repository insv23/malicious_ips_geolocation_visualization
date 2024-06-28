import requests
from loguru import logger
from ratelimit import sleep_and_retry, limits
from tqdm import tqdm

from files import save_list_to_json


def process_ips(ips, batch_size=90):
    """
    将 ips 列表切成一批(不超过100个), 并使用 batch_ip_query 函数进行查询
    """
    successful_all, failed_all = [], []

    for i in tqdm(range(0, len(ips), batch_size)):
        ip_list = ips[i:i + batch_size]
        successful, failed = batch_ip_query(ip_list)

        successful_all.extend(successful)
        failed_all.extend(failed)

        # 每一批处理完后，保存到 JSON 文件
        save_list_to_json(successful_all, "successful_ips.json")
        save_list_to_json(failed_all, "failed_ips.json")

    return successful_all, failed_all


@sleep_and_retry
@limits(calls=40, period=60)  # 每分钟限制 45 个
def batch_ip_query(ip_list):
    """
    批量查询 IP 地址信息。

    Args:
        ip_list: 要查询的 IP 地址列表。(最多一百个)

    Returns:
        tuple: 包含两个列表的元组，第一个列表包含成功查询的 IP 地址和其经纬度，格式为 (query, lat, lon)，第二个列表包含失败查询的 IP 地址。
    """
    url = 'http://ip-api.com/batch?fields=57536'

    response = requests.post(url, json=ip_list, timeout=10)
    datas = response.json()

    successful = []
    failed = []

    for data in datas:
        if data['status'] == 'success':
            successful.append((data['query'], data['lat'], data['lon']))
            logger.info(f"IP {data['query'], data['lat'], data['lon']}")
        else:
            failed.append((data['query']))
            logger.warning(f"Query IP {data['query']} failed")

    return successful, failed
