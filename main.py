import json
import multiprocessing
import os
import socket
from urllib.parse import urlsplit

import httpx
from colorama import Fore, init

init(autoreset=True)

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


class Worker(multiprocessing.Process):

    def __init__(self, job_queue, worker_num):
        super().__init__()
        self._job_queue = job_queue
        self.worker_num = worker_num
        self.valid_domains = []

    def run(self):
        while True:
            url = self._job_queue.get()
            if url is None:
                break
            fqdn = urlsplit(url).netloc
            try:
                httpx.get(url, headers=HEADERS, follow_redirects=True)
                ip = socket.gethostbyname(fqdn)
                print(f"{Fore.GREEN} {url} ({ip}) - Found!")
                self.valid_domains.append({"url": url, "ip": ip})
            except (
                httpx.ConnectError,
                httpx.ConnectTimeout,
                httpx.ReadTimeout,
                httpx.InvalidURL,
                httpx.ReadError,
            ):
                if url.startswith("https://"):
                    self._job_queue.put(f"http://{fqdn}")
            except httpx.UnsupportedProtocol:
                print(f"{Fore.RED} {url} - UnsupportedProtocol!")
            except socket.gaierror:
                print(f"{Fore.RED} {url} - getaddrinfo failed!")

        print(f"{Fore.BLUE} Worker {self.worker_num} - {len(self.valid_domains) = }.")
        with open(f"tmp/{self.worker_num}.json", "w") as f:
            json.dump(self.valid_domains, f)
        


if __name__ == '__main__':
    jobs = []
    job_queue = multiprocessing.Queue()
    unique_domains = set()

    for i in range(10):
        p = Worker(job_queue, i)
        jobs.append(p)
        p.start()

    # This is the master code that feeds URLs into queue.
    with httpx.stream("GET", "https://raw.githubusercontent.com/mickeydarrenlau/Discord-scam-links/main/nitroscamlinks.txt") as r:
        for line in r.iter_lines():
            unique_domains.add(f"https://{line.strip()}")
    print(f"{Fore.BLUE} {len(unique_domains) = }.")

    os.makedirs("tmp", exist_ok=True)

    for domain in unique_domains:
        job_queue.put(domain)

    # Send None for each worker to check and quit.
    for j in jobs:
        job_queue.put(None)

    for j in jobs:
        j.join()
