import argparse

parser1 = argparse.ArgumentParser(description='Get the Arguments')
parser1.add_argument('initial_dir', type=str, help='Initial Directory')
parser1.add_argument('final_dir', type=str, help='Final Directory')

output1 = parser1.parse_args()

print(output1.initial_dir)
print(output1.final_dir)

# input('sdsd')