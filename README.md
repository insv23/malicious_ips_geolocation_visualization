# Malicious IPs Geolocation Visualization | 恶意 IP 地理位置可视化

## 介绍

我的服务器每天都会被其他人尝试登录几百次,
受到这篇 [博客](https://romeov.github.io/malicious_ip_addresses/malicious_ip_analysis.html) 的启发, 我决定用 Python
可视化所有尝试登录我服务器的用户的 IP

思路很简单:

1. 通过 sshd 和 grep 获取所有登录服务器的 IP
2. 查询 IP 对应的地理位置(使用 API: https://ip-api.com/)
3. 将地理位置坐标画到地图中

## 使用

1. 克隆或下载到本地
2. 安装依赖包
    ```bash
   pip install requests folium tqdm ratelimit loguru matplotlib basemap numpy
   ```
3. 运行
    ```bash
    python main.py
    ```
   生成两张地图, 分别是世界和中国

   ![Malicious IP Geo Locations on World Map.png](Malicious%20IP%20Geo%20Locations%20on%20World%20Map.png)

   ![Malicious IP Geo Locations on China Map.png](Malicious%20IP%20Geo%20Locations%20on%20China%20Map.png)

## 把玩

推荐使用 Jupyter Notebook 把玩, 详见 main.ipynb