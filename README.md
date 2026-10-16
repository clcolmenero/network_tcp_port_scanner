```markdown
# Network TCP Port Scanner

A small TCP port scanner written in Python that lets you scan an IP address or domain using two scan modes: **fast** (the most common ports) and **well-known ports** (1–1023).

## Features

- Scans the **most common TCP ports** (fast mode).
- Scans **well-known ports** (range 1–1023).
- Detects open ports through TCP connections.
- Identifies the typical service associated with the 30 most-used ports (HTTP, SSH, RDP, etc.) in fast mode.
- Simple console interface.

## Requirements

- Python 3.x
- Python standard library (`socket`)

No external dependencies are required.

## Installation

1. Clone this repository or download the file:

```bash
git clone [https://github.com/your-username/network-tcp-port-scanner.git](https://github.com/your-username/network-tcp-port-scanner.git)
cd network-tcp-port-scanner
```

2. Make sure Python 3 is installed:

```bash
python --version
```

or

```bash
python3 --version
```

## Usage

Run the script from the terminal:

```bash
python scanner.py
```

or, on some systems:

```bash
python3 scanner.py
```

The program will ask you for:

1. **IP address or domain** to scan  
   - Valid examples:
     - `192.168.1.10`
     - `scanme.nmap.org`
     - `www.google.com`
   - Do not include `http://` or a trailing `/`.

2. **Scan type**:

- `Fast`  
  Scans only about 30 very common TCP ports (22, 80, 443, 3389, etc.) and also displays the name of the typical service.

- `Well-known`  
  Scans the well-known TCP ports from **1 to 1023**. This mode may take longer, depending on the configured timeout and your network.

### Example output (fast mode)

```text
Enter the IP address or domain you want to scan: scanme.nmap.org

If you want a fast scan (only the 30 most common TCP ports), type 'Fast'. If you want to scan well-known ports (range 1 to 1023), type 'Well-known': Fast
Port 22 (SSH) is OPEN.
Port 80 (HTTP) is OPEN.

Scan completed successfully.
```

## Code structure

- Uses `socket.socket(AF_INET, SOCK_STREAM)` to create TCP sockets.
- Uses `settimeout()` to limit the waiting time per port and avoid long blocks.
- Uses `connect_ex()` to check whether a port accepts connections (open port) or not.
- Includes a main `main()` function and an `if __name__ == "__main__":` block for a cleaner, reusable structure.

## Limitations and possible improvements

- It only scans **TCP ports** (not UDP).
- The scan is sequential, without parallelism.
- It does not detect services or versions, only open ports.

Possible future improvements:

- Add support for basic UDP scanning.
- Allow the user to specify a custom port range.
- Save the results to a file (for example, CSV or TXT).
- Add console colors to highlight open ports.

## Ethical use

This project is intended for educational purposes and for practicing programming and networking skills.  
Use it **only** against systems you own or for which you have explicit authorization. Unauthorized use of scanning tools may be illegal under the laws of your country.
