import argparse
import sys
from pyocd.core.helpers import ConnectHelper

def main():
    parser = argparse.ArgumentParser(description="Verify contents of RAM of a target device.")
    parser.add_argument('--addr', required=True, help='Memory address to read')
    parser.add_argument('--expected', required=True, help='Expected value at the memory address')

    args = parser.parse_args()

    # Connect to the target device
    session = ConnectHelper.session_with_chosen_probe()
    with session:
        session.open()
        contents = session.target.read_memory(args.addr)

        expected_value = int(args.expected, 0)  # Convert expected value to integer
        if contents != expected_value:
            print(f"Verification failed: Expected {expected_value}, but got {contents} at address {args.addr}")
            sys.exit(1)


