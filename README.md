
# pyocd-ci-prototype

A minimal proof-of-concept for a hardware-in-the-loop (HIL) continuous integration (CI) runner using [pyOCD](https://github.com/pyocd/pyOCD) and GitHub Actions on a self-hosted runner.

## Features

* **Firmware Flashing**: Automatically flash firmware onto target devices using pyOCD.
* **Execution Control**: Halt execution at specified breakpoints or times to facilitate testing.
* **Memory Inspection**: Read and verify RAM contents to ensure correct execution.
* **GitHub Actions Integration**: Automate testing workflows with GitHub Actions on self-hosted runners.

## Getting Started

### Prerequisites

* Python 3.7 or higher
* A supported debug probe (e.g., ST-Link V2, CMSIS-DAP, J-Link)
* Target device with Arm Cortex-M microcontroller

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/BigBoySanchez/pyocd-ci-prototype
   cd pyocd-ci-prototype
   ```



2. **Set Up Python Environment**:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```



*Alternatively, install pyOCD directly:*

```bash
pip install --upgrade pyocd
```



3. **Connect Your Debug Probe**:

   Plug in your debug probe and verify connection:

   ```bash
   pyocd list
   ```



You should see your device listed.

4. **Set Up udev Rules (Linux Only)**:

   Follow the instructions in the [pyOCD udev README](https://github.com/pyocd/pyOCD/blob/main/udev/README.md) to configure udev rules.

   After setting up, replug the probe and rerun `pyocd list` to confirm detection.

## Usage

The repository includes example scripts and GitHub Actions workflows to demonstrate the following:

* **Flashing Firmware**: Automatically program the target device with the desired firmware.
* **Halting Execution**: Pause execution at specific points to facilitate debugging and testing.
* **Memory Inspection**: Read and verify RAM contents to ensure the program is executing as expected.

These workflows are designed to run on self-hosted GitHub Actions runners connected to the target hardware.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for enhancements or bug fixes.