
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

The `verify.yml` workflow is designed to run on a self-hosted GitHub Actions runner connected to your target hardware. It performs the following steps:

1. **Checkout Repository**: Clones the repository containing the firmware and scripts.
2. **Set Up Python Environment**: Installs Python and necessary dependencies.
3. **Flash Firmware**: Uses pyOCD to flash the firmware onto the target device.
4. **Halt Execution**: Halts the device execution at a specified breakpoint or time.
5. **Verify RAM Contents**: Reads and verifies RAM contents to ensure correct execution.

Here's a simplified version of the `verify.yml` workflow:

```yaml
name: Verify Firmware

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  verify:
    runs-on: self-hosted

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Flash firmware
        run: |
          pyocd flash path/to/firmware.elf

      - name: Halt execution
        run: |
          pyocd cmd "halt"

      - name: Verify RAM contents
        run: |
          pyocd cmd "read32 0x20000000 4"
```

**Note**: Replace `path/to/firmware.elf` with the actual path to your firmware file.

## 🛠️ Setting Up the Self-Hosted Runner

To use this workflow, you'll need to set up a self-hosted GitHub Actions runner connected to your target hardware:

1. **Set Up the Runner**:

   * Follow GitHub's [official guide](https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners) to add a self-hosted runner to your repository.

2. **Install pyOCD**:

   * Ensure `pyocd` is installed on the runner machine:

     ```bash
     pip install --upgrade pyocd
     ```

3. **Connect Debug Probe**:

   * Connect your supported debug probe (e.g., ST-Link, CMSIS-DAP) to the runner machine and the target device.

4. **Configure udev Rules (Linux Only)**:

   * Set up udev rules to allow non-root access to the debug probe.

## ✅ Verifying the Setup

After setting up the self-hosted runner and connecting your hardware:

1. **Start the Runner**:

   * Run the self-hosted runner application on your machine.

2. **Push Changes**:

   * Push changes to the `main` branch or open a pull request targeting `main`.

3. **Monitor Workflow**:

   * Navigate to the "Actions" tab in your GitHub repository to monitor the workflow execution.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for enhancements or bug fixes.