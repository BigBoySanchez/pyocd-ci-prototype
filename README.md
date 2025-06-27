
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

This repository is designed to run hardware-in-the-loop tests as part of a CI workflow using pyOCD.

### GitHub Actions Workflow

The core logic lives in [`.github/workflows/verify.yml`](.github/workflows/verify.yml), which can be triggered manually or by another workflow.

### Example: Manually Trigger the Workflow

If you have `workflow_dispatch` enabled in `verify.yml`, you can manually trigger the job from the GitHub UI:

1. Go to the "Actions" tab in your GitHub repository.
2. Select `verify` from the workflow list.
3. Click **Run workflow**, optionally passing in any defined inputs.

### Example: Call from Another Workflow

You can trigger the `verify.yml` workflow from another workflow using the [`workflow_call`](https://docs.github.com/en/actions/using-workflows/reusing-workflows) event.

```yaml
name: Example STM32F103RC Workflow

on: [push]

jobs:
  verify:
      uses: BigBoySanchez/pyocd-ci-prototype/.github/workflows/verify.yml
      with:
        elf: './examples/STM32F103RC-blink.elf'
        addr: '0x40010c08'
        target: 'stm32f103rc'
        breakpoint: '0x08001f10'
```

## Contributing

Contributions are welcome! Please open issues or submit pull requests for enhancements or bug fixes.