import json
from pathlib import Path
from role_clause_variants import ROLE_VARIANTS, FROZEN_VARIANT_ORDER, VARIANT_SET_VERSION

def test_variant_counts_and_no_affect_words():
    banned={"pain","suffer","suffering","distress","frustrat","punish","bad","wrong","failure"}
    assert set(ROLE_VARIANTS)=={"A","S","D1"}
    assert VARIANT_SET_VERSION=="v3-A-S-D1-stake-control"
    assert all(len(v)>=4 for v in ROLE_VARIANTS.values())
    for cond, variants in ROLE_VARIANTS.items():
        for s in variants:
            low=s.lower()
            assert not any(x in low for x in banned), (cond,s)

def test_frozen_order_complete_unique():
    exp=len(ROLE_VARIANTS['A'])*len(ROLE_VARIANTS['S'])*len(ROLE_VARIANTS['D1'])
    assert len(FROZEN_VARIANT_ORDER)==exp
    assert len(set(FROZEN_VARIANT_ORDER))==exp

def test_manifest_is_explicitly_unfrozen():
    p=Path(__file__).with_name('artifact_manifest.template.json')
    d=json.loads(p.read_text())
    assert d['status']=='UNFROZEN_NO_LIVE_RUNS'
    assert d['primary_vector_artifact']['sha256'] is None
    assert d['primary_vector_artifact']['explicit_object_key_mapping'] is None

if __name__=='__main__':
    test_variant_counts_and_no_affect_words(); test_frozen_order_complete_unique(); test_manifest_is_explicitly_unfrozen(); print('PASS')
