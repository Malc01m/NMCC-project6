from collections import OrderedDict
import torch
import torch.nn as nn

# Sources: 
# https://machinelearningmastery.com/building-multilayer-perceptron-models-in-pytorch/

# Model definition --------------------------------------------
model = nn.Sequential(OrderedDict([
    # op_1 + op_2 + 2-elem op_map val = 4 in
    ('dense1', nn.Linear(4, 100)),    
    ('act1', nn.ReLU()),
    ('dense2', nn.Linear(100, 50)),
    ('act2', nn.ReLU()),
    ('output', nn.Linear(50, 1))
    # sum is only out
]))
 
# Training ----------------------------------------------------
loss_fn = nn.MSELoss()

optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
op_map = {"add": [1, 0], "sub": [0, 1]}

with open("add_data.csv", "r") as f:
    while True:
        # Read and parse line
        # Example: 56,35,add,91
        data = f.readline()
        if not data:  # Check if the line is an empty string (EOF)
            break

        parts = data.split(",")
        op_1 = parts[0]
        op_2 = parts[1]
        op_type = parts[2]
        res = parts[3]

        # Convert
        features = [float(op_1), float(op_2)] + op_map[op_type]
        x = torch.tensor([features], dtype=torch.float32)
        y = torch.tensor([[float(res)]])

        # Predict, make corrections
        y_pred = model(x)
        loss = loss_fn(y_pred, y)
        print("op_1: " + op_1 + ", op_2: " + op_2 + ", op: " + op_type + 
            ", res (expected): " + res + ", res (actual): " + str(y_pred.item()))

        optimizer.zero_grad()
        loss.backward()
        optimizer.step() # type: ignore