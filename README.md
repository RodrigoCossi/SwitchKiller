# SwitchKiller - Hybrid MAC Flooding Tool

A powerful and flexible MAC flooding script built with [Scapy](https://scapy.net), designed for both stress testing and stealthy ARP-based simulations.
It floods switches on the same LAN with Ethernet frames from fake MACs. It causes switches to overflow their MAC table and revert to flooding mode.
This allows an attacker to sniff traffic they shouldn’t see.

> ⚠️ **Disclaimer:**  
> This tool is for **educational and authorized testing purposes only**.  
> The author is **not responsible** for any misuse or damage caused.  
> Use only on networks you **own** or have **explicit permission** to test.

---

## ✨ Features

- 🚀 **Stress Mode** — flood a switch with thousands of fake MACs rapidly  
- 🕵️ **Stealth Mode** — simulate realistic slow-paced attacks  
- 🎛️ Customizable interface, delay, and packet count  
- 🔁 Continuous sending or finite bursts  
- 🔧 Built with `scapy` and `argparse`

---

## 📦 Requirements

- Python 3.x  
- [Scapy](https://scapy.net)

Install dependencies:
```bash
pip install scapy
```

## 🚀 Usage

### Basic Syntax

```bash
python mac_flood.py [OPTIONS]
```

## 🔋 Options

| Option              | Description                                   | Default       |
| ------------------- | --------------------------------------------- | ------------- |
| `-i`, `--interface` | Network interface to use                      | Auto-detected |
| `-m`, `--mode`      | Mode: `stress` or `stealth`                   | `stress`      |
| `-d`, `--delay`     | Delay between packets (stealth mode only)     | `1.0` sec     |
| `-c`, `--count`     | Number of packets to send (stealth mode only) | `50`          |

## 📌 Examples

### 🢨 Stress Mode (default)

Flood the network rapidly with fake MACs:

```bash
python mac_flood.py -i eth0
```

### 🚐 Stealth Mode

Slow, targeted flooding to mimic more realistic attack patterns:

```bash
python mac_flood.py -i eth0 -m stealth -d 2 -c 100
```

## 🧠 How It Works

* Sends Ethernet frames with **random source MACs**
* Includes spoofed **ARP responses** with fake IP/MAC bindings
* Switches overwhelmed with these learn & fill their **MAC address tables**
* In stealth mode, sends gradually to **evade detection**

## 🚫 Important

* Run as **root or with sudo**:

  ```bash
  sudo python mac_flood.py -i eth0
  ```

* Avoid running this on production networks — use only in test environments.

> ⚠️ **Disclaimer:**
> This tool is for **educational and authorized testing purposes only**.
> The author is **not responsible** for any misuse or damage caused.
> Use only on networks you **own** or have **explicit permission** to test.
