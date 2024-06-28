import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap


def plot_world(coordinates, title='Malicious IP Geo Locations on World Map',
               save_path='Malicious IP Geo Locations on World Map.png'):
    """
    绘制世界地图并标记给定坐标位置的函数。

    参数：
        coordinates (list): 坐标列表，每个元素为一个元组 (纬度, 经度)。
        title (str): 地图标题，默认为 'Malicious IP Geo Locations on World Map'。
        save_path (str): 保存地图的路径，默认为 'Malicious IP Geo Locations on World Map.png'。
    """

    plt.figure(figsize=(16, 12))
    m = Basemap(projection='mill', llcrnrlat=-60, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180)

    m.drawcoastlines()
    m.drawcountries()

    for lat, lon in coordinates:
        x, y = m(lon, lat)
        m.plot(x, y, 'bo', markersize=4)

    plt.title(title)
    plt.savefig(save_path)
    plt.show()
    plt.close()


def plot_china(coordinates, title='Malicious IP Geo Locations on China Map',
               save_path='Malicious IP Geo Locations on China Map.png'):
    """
    绘制中国地图并标记给定坐标位置的函数。

    参数：
        coordinates (list): 坐标列表，每个元素为一个元组 (纬度, 经度)。
        title (str): 地图标题，默认为 'Malicious IP Geo Locations on China Map'。
        save_path (str): 保存地图的路径，默认为 'Malicious IP Geo Locations on China Map.png'。
    """

    plt.figure(figsize=(12, 8))
    m = Basemap(projection='merc', llcrnrlat=16, urcrnrlat=54, llcrnrlon=72, urcrnrlon=136, resolution='l')

    # 加载中国省份边界数据
    shp_info = m.readshapefile('gadm41_CHN_shp/gadm41_CHN_1', 'states', drawbounds=True)

    # 绘制省份界线
    for shape_dict, seg in zip(m.states_info, m.states):
        seg = np.array(seg)
        m.plot(seg[:, 0], seg[:, 1], 'k-', linewidth=0.5)

    # 绘制海岸线和国家边界
    m.drawcoastlines()
    m.drawcountries()

    # 绘制位置点
    for lat, lon in coordinates:
        x, y = m(lon, lat)
        m.plot(x, y, 'bo', markersize=5)

    plt.title(title)
    plt.savefig(save_path)
    plt.show()
    plt.close()
