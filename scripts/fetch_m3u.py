import requests

# 目标m3u文件URL
url = 'https://yang-1989.eu.org/m3u/Gather'
# 定义user-agent
headers = {
    'User-Agent': 'Televizo'
}

# 发起请求获取m3u文件内容
response = requests.get(url, headers=headers)

if response.status_code == 200:
    with open('YanG.m3u', 'w', encoding='utf-8') as file:
        file.write(response.text)
    print("m3u file fetched and saved successfully.")
else:
    print(f"Failed to fetch m3u file. Status code: {response.status_code}")
