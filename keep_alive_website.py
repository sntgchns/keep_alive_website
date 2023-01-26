import requests
import time

urls = ["https://web3.soñora.com", "https://nft.soñora.com", "https://santiago.soñora.com"]

while True:
    start_time = time.time()
    for url in urls:
        request_start_time = time.time()
        response = requests.get(url)
        request_time = time.time() - request_start_time
        print(url, '|', response.status_code, '|', round(request_time, 3))
    time_left = 12 * 60 - (time.time() - start_time)
    while time_left > 0:
        print("Next requests in {:03d} seconds\r".format(int(time_left)), end="")
        time_left -= 1
        time.sleep(1)
    print()
