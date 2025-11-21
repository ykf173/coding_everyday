# attention
from torch import nn
import torch
import math

class Attention(nn.Module):
  def __init__(self, embed_size):
    self.embed_size = embed_size
    self.q_w = nn.Linear(embed_size, embed_size)
    self.k_w = nn.Linear(embed_size, embed_size)
    self.v_w = nn.Linear(embed_size, embed_size)

    self.scale = math.sqrt(embed_size)

  def forward(self, x):
    q = self.q_w(x)
    k = self.k_w(x)
    v = self.v_w(x)

    attention_weights = torch.softmax(torch.matmul(q, k.transpose(-2, -1)) / self.scale, dim=-1)
    attention_score = torch.matmul(attention_weights, v)

    return attention_score
    