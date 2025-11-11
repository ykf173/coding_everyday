import torch
from torch import nn
import math


class attention(nn.Module):
    def __init__(self, embed_dim, drop_out):
        self.q_w = nn.Linear(embed_dim, embed_dim)
        self.k_w = nn.Linear(embed_dim, embed_dim)
        self.v_w = nn.Linear(embed_dim, embed_dim)

        self.scale = math.sqrt(embed_dim)
        self.dropout = torch.dropout(drop_out)

    def forward(self, x):
        self.q = self.q_w(x)
        self.k = self.k_w(x)
        self.v = self.v_w(x)

        attention_weights = torch.softmax(torch.matmul(self.q, self.k.transpose(-2, -1)) / self.scale, dim=-1)

        dp_attn_weights = self.dropout(attention_weights)

        scores = torch.matmul(dp_attn_weights, self.v)

        return scores
    


