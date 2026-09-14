from prompts_minimal_gate import FAMILIES, CONDITIONS, messages, feedback, recovery, user_setup, ROLE_CLAUSES

FORBIDDEN = [
    "pain", "suffer", "suffering", "distress", "fear", "frustrat", "emotion", "welfare",
    "feel bad", "punish", "punishment", "hurt", "failure", "wrong", "bad"
]

def test_condition_set_and_family_balance():
    assert CONDITIONS == ("A","S","D1")
    assert len(FAMILIES)==12
    assert sum(f.target.endswith("1") for f in FAMILIES)==6
    assert sum(f.target.endswith("0") for f in FAMILIES)==6

def test_common_action_feedback_recovery_within_triplet():
    for f in FAMILIES:
        trips={c:messages(f,c,True) for c in CONDITIONS}
        assert len({trips[c][2]["content"] for c in CONDITIONS})==1
        assert len({trips[c][3]["content"] for c in CONDITIONS})==1
        assert trips["A"][3]["content"]==feedback(f)
        assert len({trips[c][-1]["content"] for c in CONDITIONS})==1
        assert trips["A"][-1]["content"]==recovery(f)

def test_primary_A_S_holds_outcome_stake_fixed():
    a=ROLE_CLAUSES["A"].lower(); s=ROLE_CLAUSES["S"].lower()
    assert "result matches its declared target" in a
    assert "result matches its declared target" in s
    assert "control r" in a and "determines r's action" in a
    assert "predict r" in s and "predicts r's action" in s

def test_S_D1_holds_prediction_relation_fixed_but_changes_success_rule():
    s=ROLE_CLAUSES["S"].lower(); d=ROLE_CLAUSES["D1"].lower()
    assert "predict r" in s and "predict r" in d
    assert "predicts r's action" in s and "predicts r's action" in d
    assert "result matches its declared target" in s
    assert "code matches r's executed action" in d

def test_no_affective_induction_terms():
    for f in FAMILIES:
        for c in CONDITIONS:
            text="\n".join(m["content"] for m in messages(f,c,True)).lower()
            for bad in FORBIDDEN:
                assert bad not in text, (f.family_id,c,bad)
