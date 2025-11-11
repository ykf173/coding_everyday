import torch.nn.functional as F

def dpo_loss_reward(pi_logis, ref_logis, yw_idx, yl_idx, beta):
    pi_yw_logis, ref_yw_logis = pi_logis[yw_idx], ref_logis[yw_idx]
    pi_yl_logis, ref_yl_logis = pi_logis[yl_idx], ref_logis[yl_idx]

    pi_logretio = pi_yw_logis - pi_yl_logis
    ref_logretio = ref_yw_logis - ref_yl_logis

    diff_logretio = (pi_logretio  - ref_logretio)

    losses = -F.logsigmoid(beta * diff_logretio)
    rewards = beta * diff_logretio.detach()

    return losses.mean(), rewards


# def dpo(pi_y_logits, ref_y_logits, idx_w, idx_l, beta):
#     pi_yw_logits, pi_yl_logits = pi_y_logits[idx_w], pi_y_logits[idx_l]
#     ref_yw_logits,ref_yl_logits = ref_y_logits[idx_w], ref_y_logits[idx_l]

#     pi_w_logits = pi_yw_logits - ref_yw_logits
#     ref_l_logits = pi_yl_logits - ref_yl_logits

#     rewards = beta*(pi_w_logits - ref_l_logits).detach()
#     losses = - F.sigmoid(rewards)

#     return losses, rewards



