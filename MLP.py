import torch
from torch import nn

class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(6, 32),  # Input layer
            nn.ReLU(),
            nn.Linear(32, 16),  # Hidden layer
            nn.ReLU(),
            nn.Linear(16, 2),  # Output layer
        )

    def forward(self, x):
        return self.layers(x)

model = MLP()