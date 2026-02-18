# Self Problem Statement

# Problem Statement: Network Logging

Below are the different scenarios under Network Logging.

---

## 1. Checking Latency

For example, we can consider Google DNS port number which is `8.8.8.8`.

We try to create some requests that connect to this host number.  
Later we fetch the latency which will be named as **average latency**.

```python
import subprocess

def check_latency(host_number):
    # Creating requests that will knock this port number
    subprocess.run(["ping", "-n", "4", host_number])

    # Searching for the average latency in output
    # If "Average" is found then print latency
```

---

## 2. Checking the Port Number

We can check if a particular port is available or not by creating a socket that will knock on the port number.

If the port is accessible and connected → **Port Open**  
Else → **Port Closed**

`s = socket.socket(AF_INET, SOCK_STREAM)` generates the knock to the port  
(Like knocking or using a calling bell to check if someone is home)

- `AF_INET` → Type of network address  
- `SOCK_STREAM` → Protocol (TCP)

We use try and except to check connectivity:

- If connection possible → Print port open  
- If not possible → Print connection not possible  

```python
import socket

def check_port(port_number):
    # Creating socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect(("localhost", port_number))
        print("Connection successful")
    except:
        print(f"{port_number} is closed")
```

---

## 3. Checking the Response Time

We input or use a default URL.  
We record start time and end time.

**Response Time = End Time - Start Time**

```python
import time
import urllib.request

def check_response(url):
    try:
        start = time.time()
        urllib.request.urlopen(url)
        end = time.time()

        response_time = end - start
        print(f"Response time of {url} is {response_time:.2f} ms")

    except:
        print("Response time failed")
```

---

## 4. Checking the Firewall

We provide a few website URLs.  
If the website opens → **Accessible**  
If not → **Blocked**

```python
import urllib.request

def firewall_check():
    test_sites = [
        "https://www.google.com",
        "https://www.netflix.com",
        "https://www.facebook.com"
    ]

    for site in test_sites:
        try:
            urllib.request.urlopen(site)
            print(f"{site} - Accessible")
        except:
            print(f"{site} - Blocked")
```
