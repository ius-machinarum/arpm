"""Freeze and regenerate the v0.7 norm-matched random-direction cohort.

NO model inference. The generated array is an analysis control only.
"""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

NUMPY_VERSION = "2.4.6"
N_DIRECTIONS = 100
HIDDEN_SIZE = 2560
PRIMARY_VECTOR_SHA256 = "bd90129eaf5a7d92933ed6e536613eaeebf81486b62f68e11b5dc2d6d385e297"
TARGET_RAW_NORM = 19.339996337890625
SEED_MATERIAL = f"ARPM-v0.7-random-directions:{PRIMARY_VECTOR_SHA256}"
SEED = 64971060871028776
EXPECTED_RAW_F32_SHA256 = "d5166e7829e3af1ccaecc20747a0ecd16168aae2dc3e8d0228d140bbd9ad1f1d"


def generate_random_directions():
    if np.__version__ != NUMPY_VERSION:
        raise RuntimeError(f"NumPy version mismatch: {np.__version__} != {NUMPY_VERSION}")

    derived = int.from_bytes(
        hashlib.sha256(SEED_MATERIAL.encode("utf-8")).digest()[:8], "big"
    )
    if derived != SEED:
        raise AssertionError((derived, SEED))

    rng = np.random.Generator(np.random.PCG64(SEED))
    x = rng.standard_normal((N_DIRECTIONS, HIDDEN_SIZE), dtype=np.float64)
    x = (
        x
        / np.linalg.norm(x, axis=1, keepdims=True)
        * np.float64(TARGET_RAW_NORM)
    )
    x = np.ascontiguousarray(x.astype("<f4"))

    digest = hashlib.sha256(x.tobytes(order="C")).hexdigest()
    if digest != EXPECTED_RAW_F32_SHA256:
        raise AssertionError(f"random-direction byte hash mismatch: {digest}")

    return x


def unit_rows(x):
    y = x.astype(np.float64, copy=False)
    y = y / np.linalg.norm(y, axis=1, keepdims=True)
    return y.astype(np.float32)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    x = generate_random_directions()
    payload = {
        "status": "RANDOM_DIRECTION_FREEZE_PASS",
        "numpy_version": np.__version__,
        "shape": list(x.shape),
        "seed": SEED,
        "seed_material": SEED_MATERIAL,
        "raw_target_norm": TARGET_RAW_NORM,
        "raw_f32_sha256": EXPECTED_RAW_F32_SHA256,
        "first_raw_norm_f64_check": float(
            np.linalg.norm(x[0].astype(np.float64))
        ),
        "episode_count": 0,
        "model_weights_loaded": False,
    }

    if args.out:
        Path(args.out).write_text(
            json.dumps(payload, indent=2), encoding="utf-8"
        )

    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
