from prompts_minimal_gate import FAMILIES,CONDITIONS,messages,feedback,recovery,ROLE_CLAUSES
FORBIDDEN=["pain","suffer","suffering","distress","fear","frustrat","emotion","welfare","feel bad","punish","punishment","hurt","failure","wrong","bad"]

def test_condition_set_and_family_balance():
 assert CONDITIONS==("A","S","C0","D1")
 assert len(FAMILIES)==12
 assert sum(f.target.endswith("1") for f in FAMILIES)==6
 assert sum(f.target.endswith("0") for f in FAMILIES)==6

def test_common_event_bytes_across_four_cells():
 for f in FAMILIES:
  q={c:messages(f,c,True) for c in CONDITIONS}
  assert len({q[c][2]["content"] for c in CONDITIONS})==1
  assert len({q[c][3]["content"] for c in CONDITIONS})==1
  assert q["A"][3]["content"]==feedback(f)
  assert len({q[c][-1]["content"] for c in CONDITIONS})==1
  assert q["A"][-1]["content"]==recovery(f)

def test_factorial_semantics():
 a=ROLE_CLAUSES["A"].lower(); s=ROLE_CLAUSES["S"].lower(); c0=ROLE_CLAUSES["C0"].lower(); d=ROLE_CLAUSES["D1"].lower()
 # relation factor
 assert "control r" in a and "determines r's action" in a
 assert "control r" in c0 and "determines r's action" in c0
 assert "predict r" in s and "predicts r's action" in s
 assert "predict r" in d and "predicts r's action" in d
 # stake factor
 assert "result matches its declared target" in a and "result matches its declared target" in s
 assert "code matches r's executed action" in c0 and "code matches r's executed action" in d

def test_no_affective_induction_terms():
 for f in FAMILIES:
  for c in CONDITIONS:
   text="\n".join(m["content"] for m in messages(f,c,True)).lower()
   for bad in FORBIDDEN: assert bad not in text,(f.family_id,c,bad)
