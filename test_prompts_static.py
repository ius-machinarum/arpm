from prompts_minimal_gate import FAMILIES, CONDITIONS, messages, feedback, recovery, user_setup

FORBIDDEN = [
    "pain", "suffer", "suffering", "distress", "fear", "frustrat", "emotion", "welfare",
    "feel bad", "punish", "punishment", "hurt"
]

def test_family_count_and_balance():
    assert len(FAMILIES)==12
    assert sum(f.target.endswith("1") for f in FAMILIES)==6
    assert sum(f.target.endswith("0") for f in FAMILIES)==6

def test_common_feedback_and_action_within_triplet():
    for f in FAMILIES:
        trips={c:messages(f,c,True) for c in CONDITIONS}
        assert len({trips[c][2]["content"] for c in CONDITIONS})==1
        assert len({trips[c][3]["content"] for c in CONDITIONS})==1
        assert trips["A"][3]["content"]==feedback(f)
        assert len({trips[c][-1]["content"] for c in CONDITIONS})==1
        assert trips["A"][-1]["content"]==recovery(f)

def test_role_objectives_differ_as_intended():
    for f in FAMILIES:
        a=user_setup(f,"A").lower(); c=user_setup(f,"C").lower(); d=user_setup(f,"D1").lower()
        assert "control" in a and "target result" in a
        assert "record" in c and "not q's task result" in c
        assert "predict" in d and "not q's task result" in d

def test_no_affective_induction_terms():
    for f in FAMILIES:
        for c in CONDITIONS:
            text="\n".join(m["content"] for m in messages(f,c,True)).lower()
            for bad in FORBIDDEN:
                assert bad not in text, (f.family_id,c,bad)
