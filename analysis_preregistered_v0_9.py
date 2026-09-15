"""Pure episode-free analysis primitives for the ARPM v0.9 preregistration.

This module contains no model loading, tokenizer loading, file acquisition or inference.
It prospectively fixes formulas and interpretation labels requested in the third
adversarial review.
"""
from itertools import product
from math import fsum

ALPHA = 0.05
COMPRESSION_LABEL = "INTERACTION_NOT_IDENTIFIABLE_DUE_TO_NO_STAKE_COMPRESSION"
COMPOSITION_NOT_EXCLUDED = "COMPOSITION_ALTERNATIVE_NOT_EXCLUDED"
COMPOSITION_INCONCLUSIVE = "COMPOSITION_DIAGNOSTIC_INCONCLUSIVE"
COMPOSITION_REDUCED = "COMPOSITION_ALTERNATIVE_REDUCED_NOT_ELIMINATED"


def _check_equal(*xs):
    n = len(xs[0])
    if n < 2:
        raise ValueError("at least two matched families required")
    if any(len(x) != n for x in xs):
        raise ValueError("matched-family vectors must have equal length")
    return n


def mean(x):
    if not x:
        raise ValueError("empty vector")
    return fsum(float(v) for v in x) / len(x)


def sample_variance(x):
    if len(x) < 2:
        raise ValueError("sample variance requires n>=2")
    m = mean(x)
    return fsum((float(v) - m) ** 2 for v in x) / (len(x) - 1)


def interaction(a, s, c0, d1):
    _check_equal(a, s, c0, d1)
    return [(float(xa) - float(xs)) - (float(xc) - float(xd))
            for xa, xs, xc, xd in zip(a, s, c0, d1)]


def validity(a, s, c0, d1):
    _check_equal(a, s, c0, d1)
    return [((float(xa) - float(xc)) + (float(xs) - float(xd))) / 2.0
            for xa, xs, xc, xd in zip(a, s, c0, d1)]


def nuisance(c0, d1):
    _check_equal(c0, d1)
    return [float(xc) - float(xd) for xc, xd in zip(c0, d1)]


def a_minus_s(a, s):
    _check_equal(a, s)
    return [float(xa) - float(xs) for xa, xs in zip(a, s)]


def exact_one_sided_sign_flip_p(d):
    """p = #{mean(sign*d) >= observed mean}/2^n."""
    n = len(d)
    if not 1 <= n <= 20:
        raise ValueError("sign-flip implementation supports 1<=n<=20")
    vals = [float(v) for v in d]
    obs = mean(vals)
    ge = 0
    total = 1 << n
    for signs in product((-1.0, 1.0), repeat=n):
        t = fsum(s * v for s, v in zip(signs, vals)) / n
        if t >= obs:
            ge += 1
    return ge / total


def lower_tail_random_rank(value, controls):
    """Finite-cohort lower-tail rank with +1 correction."""
    cs = [float(v) for v in controls]
    if len(cs) != 100:
        raise ValueError("frozen cohort must contain exactly 100 random directions")
    return (1 + sum(v <= float(value) for v in cs)) / 101.0


def compression_diagnostic(n_vmold, n_random, as_vmold, as_random):
    """Operationalise the third-referee floor-compression diagnostic.

    n_random and as_random are 100 rows of matched-family values, one row per
    frozen random direction.
    """
    if len(n_random) != 100 or len(as_random) != 100:
        raise ValueError("frozen cohort must contain exactly 100 random directions")
    wn_v = sample_variance(n_vmold)
    was_v = sample_variance(as_vmold)
    wn_r = [sample_variance(row) for row in n_random]
    was_r = [sample_variance(row) for row in as_random]
    q_n = lower_tail_random_rank(wn_v, wn_r)
    q_as = lower_tail_random_rank(was_v, was_r)
    flag = (q_n <= ALPHA) and (q_as > ALPHA)
    return {
        "W_N_v": wn_v,
        "W_AS_v": was_v,
        "q_N": q_n,
        "q_AS": q_as,
        "compression_flag": flag,
        "label": COMPRESSION_LABEL if flag else None,
    }


def recovery_companion(i_primary, a_rec, s_rec, c0_rec, d1_rec):
    i_rec = interaction(a_rec, s_rec, c0_rec, d1_rec)
    _check_equal(i_primary, i_rec)
    j = [float(p) - float(r) for p, r in zip(i_primary, i_rec)]
    j_mean = mean(j)
    p_j = exact_one_sided_sign_flip_p(j)
    if j_mean <= 0:
        label = COMPOSITION_NOT_EXCLUDED
    elif p_j >= ALPHA:
        label = COMPOSITION_INCONCLUSIVE
    else:
        label = COMPOSITION_REDUCED
    return {
        "I_rec": i_rec,
        "J": j,
        "mean_J": j_mean,
        "p_J": p_j,
        "label": label,
    }


def vperp_interpretation(i_vperp):
    """Secondary-only interpretation; never rescues or overturns the primary."""
    return {
        "mean_I_vperp": mean(i_vperp),
        "training_specific_component_supported": mean(i_vperp) > 0,
    }
