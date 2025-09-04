from torch import nn
import torch
import math

class MultiAttention(nn.modules):
    def __init__(self, n_heads, h_dims, mask):
        assert h_dims % n_heads == 0
        self.w_q = nn.Linear(h_dims, h_dims)
        self.w_k = nn.Linear(h_dims, h_dims)
        self.w_v = nn.Linear(h_dims, h_dims)

        self.attention = self.w_q * torch.permute(self.w_k)/ math.sqrt(h_dims)
        if mask is not None:
            self.attention = torch.masked_fill(0, 1e-10)
        
    def forward(self, q, dropout):
        q
