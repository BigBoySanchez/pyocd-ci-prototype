pyocd-ci-prototype
==================

Minimal proof-of-concept for a hardware-in-the-loop test runner using pyOCD and GitHub Actions on a self-hosted runner.

This setup:
- Flashes a Cortex-M board over SWD
- Halts execution
- Reads a memory address to confirm debugger control

Target: STM32F103 (via ST-Link V2)  
Host: Self-hosted Linux runner with USB connection to board

----------------------------
🚀 Quick Start
----------------------------

1. Clone the repo and set up Python:

    git clone https://github.com/BigBoySanchez/pyocd-ci-prototype
    cd pyocd-ci-prototype
    python3 -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt

    Or install pyocd directly:

    pip install --upgrade pyocd

2. Connect your debug probe:

    Plug in your ST-Link V2 or other CMSIS-DAP/J-Link probe, then run:

    pyocd list

    You should see your STM32F103 device detected.

3. Set udev rules (Linux only):

    sudo cp 49-stlinkv2.rules /etc/udev/rules.d/
    sudo udevadm control --reload-rules
    sudo udevadm trigger

    Replug the probe and re-run `pyocd list`.

----------------------------
🧪 Running the test script
----------------------------

This script flashes the ELF file and reads a memory address (e.g., an LED GPIO register):

    python flash_and_peek.py

Expected output:

    Probe: ST-Link/V2, Target: stm32f103xb
    Flashing test.elf...
    Reading address 0x4001100C: value = 0x00000020

Customize with environment variables:

    ELF_PATH=./blinky.elf READ_ADDR=0x4001100C python flash_and_peek.py

----------------------------
🧰 CI Workflow
----------------------------

1. Self-hosted GitHub runner setup:

    Follow GitHub’s guide to install a self-hosted runner on the host PC connected to your board:
    https://docs.github.com/en/actions/hosting-your-own-runners

    The runner should have:
    - Python 3.11+
    - pyOCD installed
    - Access to USB debug probe via udev rules

2. GitHub Actions file:

    The `.github/workflows/hardware.yml` job will:
    - Checkout the repo
    - Install Python and pyOCD
    - Run `flash_and_peek.py`

----------------------------
🎥 Demo
----------------------------

    [Insert demo.gif or asciinema recording link here]

----------------------------
🧼 Repo Status
----------------------------

| Item      | Status/Value |
|-----------|--------------|
| Build     | [![Build Status](https://github.com/YOUR_USERNAME/pyocd-ci-prototype/actions/workflows/hardware.yml/badge.svg)] |
| Target    | STM32F103 via ST-Link |
| pyOCD     | v0.35.3 |

----------------------------
📎 Resources
----------------------------

- pyOCD: https://pyocd.io/docs/
- STM32F103 RM: https://www.st.com/resource/en/reference_manual/CD00171190.pdf
- Self-hosted runners: https://docs.github.com/en/actions/hosting-your-own-runners

----------------------------
🙋 Maintainers
----------------------------

Feel free to open issues or PRs. For feedback on this prototype, contact Khalil (libhal).
