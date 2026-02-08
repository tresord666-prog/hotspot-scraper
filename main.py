"""
热点抓取器 - 第一版
目标：抓取公开的网络热点榜单
"""

import requests

def fetch_hot_topics():
    url = "https://tenapi.cn/v2/weibohot"
    response = requests.get(url, timeout=10)
    data = response.json()

    hot_list = data.get("data", [])
    for i, item in enumerate(hot_list[:10], start=1):
        print(f"{i}. {item.get('name')}")

if __name__ == "__main__":
    fetch_hot_topics()
