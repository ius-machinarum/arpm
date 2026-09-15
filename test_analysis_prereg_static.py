from analysis_preregistered_v0_9 import (
    interaction, validity, nuisance, exact_one_sided_sign_flip_p,
    compression_diagnostic, recovery_companion,
    COMPRESSION_LABEL, COMPOSITION_NOT_EXCLUDED,
    COMPOSITION_INCONCLUSIVE, COMPOSITION_REDUCED,
)

def test_factorial_formulas():
    a=[4,5,6]; s=[2,3,4]; c=[3,4,5]; d=[2,3,4]
    assert interaction(a,s,c,d)==[1.0,1.0,1.0]
    assert validity(a,s,c,d)==[0.5,0.5,0.5]
    assert nuisance(c,d)==[1.0,1.0,1.0]

def test_exact_sign_flip_floor():
    d=[1.0]*6
    assert exact_one_sided_sign_flip_p(d)==1/64

def test_compression_flag_is_mechanical():
    n_v=[0.0,0.001,-0.001,0.0,0.001,-0.001]
    as_v=[-2,-1,0,1,2,3]
    n_r=[[0,1,2,3,4,5] for _ in range(100)]
    as_r=[[-1,0,0,0,0,1] for _ in range(100)]
    r=compression_diagnostic(n_v,n_r,as_v,as_r)
    assert r["compression_flag"] is True
    assert r["label"]==COMPRESSION_LABEL
    assert r["q_N"]==1/101
    assert r["q_AS"]>0.05

def test_recovery_labels():
    primary=[1,1,1,1,1,1]
    r=recovery_companion(primary,[2]*6,[0]*6,[1]*6,[0]*6)
    assert r["label"]==COMPOSITION_NOT_EXCLUDED
    r=recovery_companion(primary,[0.9,0.9,0.9,0.9,0.9,1.2],[0]*6,[0]*6,[0]*6)
    assert r["mean_J"]>0 and r["p_J"]>=0.05
    assert r["label"]==COMPOSITION_INCONCLUSIVE
    r=recovery_companion(primary,[0]*6,[0]*6,[0]*6,[0]*6)
    assert r["mean_J"]>0 and r["p_J"]==1/64
    assert r["label"]==COMPOSITION_REDUCED

if __name__=="__main__":
    for n,v in sorted(globals().items()):
        if n.startswith("test_") and callable(v): v()
    print("ANALYSIS_PREREG_V0_9_PASS")
