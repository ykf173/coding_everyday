from torch.nn import functional as F
def dpo_loss(loggits_pi, loggits_ref, yw_idx, yl_idx, beta):
    loggits_yw_pi, loggits_yl_pi = loggits_pi[yw_idx], loggits_pi[yl_idx]
    loggits_yw_ref, loggits_yl_ref = loggits_ref[yw_idx], loggits_ref[yl_idx]

    pi_retio = loggits_yw_pi - loggits_yl_pi
    ref_retio = loggits_yw_ref - loggits_yl_ref

    retio_diff = pi_retio - ref_retio
    logits_losses = -F.logsigmoid(retio_diff * beta)
    reward = (beta * retio_diff).detach()

    return logits_losses.mean(), reward
