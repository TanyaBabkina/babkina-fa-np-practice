import socket
import threading
import concurrent.futures
import time
from tqdm import tqdm

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Порт {port} открыт")
        s.close()
    except:
        pass



def scan_ports_in_parallel_with_progress_bar(host, num_threads=10):
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(scan_port, host, port) for port in range(1, 1025)]
        for future in tqdm(concurrent.futures.as_completed(futures), total=1024):
            pass

def main():
    host = input("Введите имя хоста или IP-адрес: ")
    start_time = time.time()
    scan_ports_in_parallel_with_progress_bar(host)
    end_time = time.time()
    print(f"Сканирование завершено за {end_time - start_time} секунд")

if __name__ == "__main__":
    main()