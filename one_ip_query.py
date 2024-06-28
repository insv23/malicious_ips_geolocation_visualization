import requests
from ratelimit import sleep_and_retry, limits
from loguru import logger
from tqdm import tqdm


# 获取 IP 对应经纬度
def get_geolocations(ips):
    """
    获取多个 IP 地址对应的地理位置。

    Args:
        ips (list[str]): 要查询的 IP 地址列表

    Returns:
        list[tuple[float, float]]: 返回每个 IP 对应的 (纬度, 经度) 的元组列表
    """
    locations = []
    for ip in tqdm(ips, desc='查询 IP 地理位置'):
        location = get_lat_lon(ip)
        if location:
            lat, lon = location
            locations.append((lat, lon))
    return locations


@sleep_and_retry
@limits(calls=30, period=60)  # 每分钟限制 45 个
def get_lat_lon(ip):
    """
    获取给定 IP 地址的地理位置。

    Args:
        ip (str): 要查询的 IP 地址

    Returns:
        tuple[float, float] | None: 如果成功，返回 (纬度, 经度) 的元组；如果失败，返回 None
    """
    url = f"http://ip-api.com/json/{ip}?fields=status,lat,lon"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 如果 status_code 不是 2xx, 则抛出异常
        data = response.json()

        if data['status'] == 'success':
            return data['lat'], data['lon']
        else:
            logger.error(f"{ip} 地理位置获取失败: API 返回状态 {data['status']}")
            return None

    except requests.exceptions.RequestException as e:
        logger.error(f"{ip} 地理位置获取失败")
        return None
