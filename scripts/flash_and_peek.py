import logging
import argparse
from pyocd.core.helpers import ConnectHelper
import os
from pyocd.flash.file_programmer import FileProgrammer
import time
import sys

# Configure logging to display output to stdout
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def resolve_arg(key, cli_value, default=None):
    return cli_value or os.environ.get(key) or default

def arg_error(arg_name):
    messages = {
        'ELF': "ELF path invalid. Please provide a valid ELF file.",
        'ADDR': "Memory address is required. Please provide a valid address.",
        'TARGET': "Target device is required. Please provide a valid target.",
        'BREAKPOINT': "Breakpoint address is required. Please provide a valid breakpoint address."
    }

    if arg_name in messages:
        logger.error(messages[arg_name])
        sys.exit(1)



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', help='Target device to connect to')
    parser.add_argument('--elf', help='Path to ELF file')
    parser.add_argument('--addr', help='Memory address to read')
    parser.add_argument('--breakpoint', help='Breakpoint address')
    args = parser.parse_args()

    
    # Get parameters from command line arguments or environment variables
    # no elf = skip flash, path has to be valid
    args.elf = resolve_arg('ELF', args.elf)
    if args.elf and not os.path.isfile(args.elf):
        arg_error('ELF')

    args.addr = resolve_arg('ADDR', args.addr)
    try:
        args.addr = int(args.addr, 0)  # Convert address to integer, supports hex and decimal formats
    except ValueError:
        arg_error('ADDR')

    args.target = resolve_arg('TARGET', args.target)
    if not args.target:
        arg_error('TARGET')

    args.break_addr = resolve_arg('BREAKPOINT', args.breakpoint)
    try:
        args.break_addr = int(args.break_addr, 0)  # Convert breakpoint address to integer
    except ValueError:
        arg_error('BREAKPOINT')

    return args


def poll_for_breakpoint(target, timeout=10, rate_s=0.05):
    """Polls the target for a breakpoint hit within a specified timeout."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        if target.is_halted():
            return True
        time.sleep(rate_s)
    return False


def main():
    # Parse command line arguments
    args = get_args()

    # Check if probe is connected    
    if not ConnectHelper.get_all_connected_probes(blocking=False):
        logger.error("No debug probe found. Please check USB connection.")
        sys.exit(1)

    with ConnectHelper.session_with_chosen_probe(target_override=args.target) as session:
        target = session.target

        # Flash the ELF file if provided
        if args.elf:
            programmer = FileProgrammer(session)
            programmer.program(args.elf)
        else:
            logger.info("No ELF file provided — skipping flashing.")

        # Wait for breakpoint to be reached
        logger.info("Running the target...")
        target.reset_and_halt()
        target.set_breakpoint(args.break_addr)
        target.resume()
        if not poll_for_breakpoint(target):
            logger.error("Breakpoint not hit within timeout period.")
            sys.exit(1)
        target.halt()

        logger.info(f"Reading value at address {hex(args.addr)}...")
        led_state = target.read32(args.addr)

        logger.info(f"LED state value: {hex(led_state)}")

if __name__ == "__main__":
    main()