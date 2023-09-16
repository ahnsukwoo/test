import argparse

parser = argparse.ArgumentParser(description='call my name')
parser.add_argument('name', type=str, help='your name')
args = parser.parse_args()

name = args.name


print(f'Hello, {name}!')