# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.

import pandas as pd
import argparse
import os

print("In train.py")
print("As a data scientist, this is where I use my training code.")

parser = argparse.ArgumentParser("train")

parser.add_argument("--input_data", type=str, help="input data")
parser.add_argument("--output_train", type=str, help="output_train directory")

args = parser.parse_args()

print("Argument 1: %s" % args.input_data)
print("Argument 2: %s" % args.output_train)

if not (args.output_train is None):
    os.makedirs(args.output_train, exist_ok=True)
    print("%s created" % args.output_train)

# +
print("read data from the given input_data, %s" % args.input_data)
input_path = os.path.join(args.input_data)

df = pd.read_csv(input_path)
df["num"] += 1

# +
# output_path = os.path.join(args.output_train,"amlpipedata.csv")
# # output_path = os.path.join(args.output_train)
# print("write data to the output_data, %s" % args.output_train)
# df.to_csv(output_path)
# -

output_path = os.path.join(args.input_data)
# output_path = os.path.join(args.output_train)
print("write data to the output_data, %s" % output_path)
df.to_csv(output_path, index=False)

print("training is done")
