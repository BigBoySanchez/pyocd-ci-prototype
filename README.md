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

    Follow these steps: 
    https://github.com/pyocd/pyOCD/blob/main/udev/README.md

    Replug the probe and re-run `pyocd list`.

----------------------------
🧪 Running the test script
----------------------------

This script flashes the ELF file and reads a memory address (e.g., an LED GPIO register):

    python flash_and_peek.py

Customize with environment variables:

    ELF=./blinky.elf ADDR=0x4001100C python flash_and_peek.py

----------------------------
🧰 Sample CI Workflow
----------------------------

Want to run real hardware tests from GitHub Actions?

This repo includes a **sample workflow file**:
📄 [sample-workflows/hardware.yml](sample-workflows/hardware.yml)

It demonstrates how to:

* Set up a **self-hosted GitHub runner** (on a PC or Pi connected to your board)
* Install `pyocd` in a virtual environment
* Use `flash_and_peek.py` to:

  * Flash a test ELF to the board
  * Reset and halt execution
  * Read a memory address (e.g. an LED state byte)

To set up the runner, follow GitHub’s official guide:
👉 [https://docs.github.com/en/actions/hosting-your-own-runners](https://docs.github.com/en/actions/hosting-your-own-runners)

Your self-hosted runner should have:

* Python 3.11 or newer
* `pyocd` installed (`pip install pyocd`)
* Access to the debug probe via proper **udev rules** (on Linux)

----------------------------
📎 Resources
----------------------------

- pyOCD: https://pyocd.io/docs/
- Self-hosted runners: https://docs.github.com/en/actions/hosting-your-own-runners
