#!/usr/bin/env python3
"""
Author: Mbcrump's Twitch Stream
Purpose: Help folks learn about argument parsing in Python
"""

import argparse

# --------------------------------------------------
def get_args():
    """Get specified arguements from CLI"""
    parser = argparse.ArgumentParser(description="Hello, Twitch Stream")
    parser.add_argument('-n', '--name', metavar='{Enter name}',
                        default='World', help="Name to greet")

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Starting entry point"""
    args = get_args()
    print('Hello, ' + args.name + '!')

# --------------------------------------------------
main()
