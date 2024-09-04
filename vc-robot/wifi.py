import network
import time

# 設定你的 Wi-Fi 名稱 (SSID) 和密碼
SSID = ''
PASSWORD = ''

# 初始化 WLAN (Wi-Fi)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)  # 啟用 Wi-Fi 模組

# 連接到指定的 Wi-Fi 網絡
print(f"Connecting to network '{SSID}'...")
wlan.connect(SSID, PASSWORD)

# 等待連接成功
while not wlan.isconnected():
    print("Waiting for connection...")
    time.sleep(1)

# 取得 IP 地址並顯示
ip = wlan.ifconfig()[0]
print(f"Connected, IP address: {ip}")
