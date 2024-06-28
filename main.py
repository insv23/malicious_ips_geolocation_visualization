from loguru import logger

import draw_map
from batch_ips_query import process_ips
from files import read_ips

# 禁止向控制台输出日志
logger.remove()
logger.add('run.log')


def main():
    # 从 txt 文件中读取 IP
    ips = read_ips('malicious_ips.txt')

    # 查询 IP 对应经纬度
    successful_all, _failed_all = process_ips(ips)

    # 转化为 (纬度, 经度) list
    coordinates = [(lat, lon) for _, lat, lon in successful_all]

    # 在世界地图中显示 IP 地理位置
    draw_map.plot_world(coordinates)

    # 在中国地图中显示 IP 地理位置
    draw_map.plot_china(coordinates)


if __name__ == '__main__':
    main()
