import os
from datetime import datetime, timedelta
import json
import time
import requests
from urllib3.exceptions import InsecureRequestWarning

# 禁用 SSL 证书验证警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 使用环境变量获取 GitHub 令牌
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
USERNAME = 'BaiYin123-l'  # 替换为你想查询的用户名
CACHE_FILE = os.path.join(os.path.dirname(__file__), 'github_data.json')
CACHE_EXPIRATION = timedelta(hours=24)  # 缓存过期时间：24 小时

def get_github_data():
    """获取 GitHub 用户数据，优先从缓存文件读取"""
    # 检查缓存文件是否存在且未过期
    if os.path.exists(CACHE_FILE):
        # 获取文件修改时间
        file_mtime = datetime.fromtimestamp(os.path.getmtime(CACHE_FILE))
        # 检查文件是否在 24 小时内被修改过
        if datetime.now() - file_mtime < CACHE_EXPIRATION:
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
    
    # 如果缓存不存在或已过期，则从 GitHub API 获取数据
    with open(os.path.join(os.path.dirname(__file__), "..",'headers.json'), 'r', encoding='utf-8') as f:
        headers = json.load(f)
    # 获取用户信息
    try:
        user_response = requests.get(
            f'https://api.github.com/users/{USERNAME}',
            headers=headers,
            verify=False  # 禁用 SSL 证书验证
        )
        user_response.raise_for_status()  # 检查请求是否成功
        user_data = user_response.json()
    except requests.exceptions.RequestException as e:
        print(f"获取用户信息失败: {e}")
        user_data = {}
    
    # 获取用户仓库
    try:
        repos_response = requests.get(
            f'https://api.github.com/users/{USERNAME}/repos',
            headers=headers,
            verify=False  # 禁用 SSL 证书验证
        )
        repos_response.raise_for_status()  # 检查请求是否成功
        repos_data = repos_response.json()
    except requests.exceptions.RequestException as e:
        print(f"获取用户仓库失败: {e}")
        repos_data = []
    
    # 将数据存储到缓存文件
    github_data = {
        'user': user_data,
        'repos': repos_data,
        'timestamp': time.time()
    }
    
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(github_data, f, ensure_ascii=False, indent=4)
    
    return github_data

# 示例调用
if __name__ == "__main__":
    data = get_github_data()
    print(json.dumps(data, ensure_ascii=False, indent=4))