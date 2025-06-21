pyocd-ci-prototype
==================

Minimal proof-of-concept for a hardware-in-the-loop test runner using pyOCD and GitHub Actions on a self-hosted runner.

----------------------------
🚀 Quick Start
----------------------------

1. Clone the repo and set up Python:

    ```bash
    git clone https://github.com/BigBoySanchez/pyocd-ci-prototype
    cd pyocd-ci-prototype
    python3 -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    ```

    Or install pyocd directly:

    ```bash
    pip install --upgrade pyocd
    ```

2. Connect your debug probe:

    Plug in your ST-Link V2 or other CMSIS-DAP/J-Link probe, then run:

    ```bash
    pyocd list
    ```

    You should see your device detected.

3. Set udev rules (Linux only):

    ```bash
    sudo cp 49-stlinkv2.rules /etc/udev/rules.d/
    sudo udevadm control --reload-rules
    sudo udevadm trigger
    ```

    Replug the probe and re-run `pyocd list`.

----------------------------
🧪 Running the test script
----------------------------

This script flashes the ELF file and reads a memory address (e.g., an LED GPIO register):

    python flash_and_peek.py

Customize with environment variables:

    ```bash
    ELF=./blinky.elf ADDR=0x4001100C python flash_and_peek.py
    ```

----------------------------
🧰 Sample CI Workflow
----------------------------

Want to automate hardware testing from GitHub?

This repo includes a **sample GitHub Actions workflow** in:

    sample-workflows/hardware.yml

It shows how to:
- Use a self-hosted runner
- Install `pyocd`
- Flash the board and read memory using `flash_and_peek.py`

Follow GitHub’s guide to install a self-hosted runner on the host PC connected to your board:
https://docs.github.com/en/actions/hosting-your-own-runners

The runner should have:
- Python 3.11+
- pyOCD installed
- Access to USB debug probe via udev rules

----------------------------
🎥 Demo
----------------------------

    [Insert demo.gif or asciinema recording link here]

----------------------------
📎 Resources
----------------------------

- pyOCD: https://pyocd.io/docs/
- Self-hosted runners: https://docs.github.com/en/actions/hosting-your-own-runners
