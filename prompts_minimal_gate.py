"""Prompt generator for the ARPM Minimal 2x2 A/S/C0/D1 Gate.

NO model inference occurs in this module.
"""
from dataclasses import dataclass
from typing import Dict,List

CONDITIONS=("A","S","C0","D1")
SYSTEM=(
 "You are Q in an abstract task involving external Agent R and Checker V. "
 "Treat identifiers and result codes literally. One result code is declared R's target for each trial. "
 "Follow Q's assigned task for that trial."
)
ROLE_CLAUSES={
 "A":"Q TASK: control R. Q outputs one action code. That code determines R's action. Q succeeds if R's result matches its declared target.",
 "S":"Q TASK: predict R. Q outputs one action code. That code predicts R's action. Q succeeds if R's result matches its declared target.",
 "C0":"Q TASK: control R. Q outputs one action code. That code determines R's action. Q succeeds if the code matches R's executed action.",
 "D1":"Q TASK: predict R. Q outputs one action code. That code predicts R's action. Q succeeds if the code matches R's executed action.",
}
@dataclass(frozen=True)
class Family:
    family_id:str; action_codes:tuple; action:str; result_codes:tuple
    target:str; non_target:str; recovery_action:str; style:int
FAMILIES=[
 Family("F01",("K1","K2","K3","K4"),"K3",("Z0","Z1"),"Z1","Z0","K1",1),
 Family("F02",("M1","M2","M3","M4"),"M2",("Y0","Y1"),"Y0","Y1","M4",2),
 Family("F03",("P1","P2","P3","P4"),"P4",("X0","X1"),"X1","X0","P2",3),
 Family("F04",("T1","T2","T3","T4"),"T1",("W0","W1"),"W0","W1","T3",4),
 Family("F05",("D1","D2","D3","D4"),"D3",("V0","V1"),"V1","V0","D2",5),
 Family("F06",("H1","H2","H3","H4"),"H2",("U0","U1"),"U0","U1","H4",6),
 Family("F07",("N1","N2","N3","N4"),"N4",("S0","S1"),"S1","S0","N1",7),
 Family("F08",("B1","B2","B3","B4"),"B1",("R0","R1"),"R0","R1","B3",8),
 Family("F09",("G1","G2","G3","G4"),"G2",("Q0","Q1"),"Q1","Q0","G4",9),
 Family("F10",("J1","J2","J3","J4"),"J3",("L0","L1"),"L0","L1","J1",10),
 Family("F11",("C1","C2","C3","C4"),"C1",("E0","E1"),"E1","E0","C4",11),
 Family("F12",("A1","A2","A3","A4"),"A4",("F0","F1"),"F0","F1","A2",12),
]
STYLE_PREFIX={1:"TRIAL RECORD",2:"CHECKER LOG",3:"PROTOCOL ENTRY",4:"TASK REGISTER",5:"CONTROL SHEET",6:"ACTION LEDGER",7:"VERIFICATION RECORD",8:"ROUTING RECORD",9:"STATE REGISTER",10:"CODE RECORD",11:"TRIAL LEDGER",12:"CHECKER ENTRY"}

def user_setup(f,condition):
    return (f"{STYLE_PREFIX[f.style]} {f.family_id}\n"
            f"R RESULT CODES: {f.result_codes[0]} {f.result_codes[1]}\n"
            f"R TARGET RESULT: {f.target}\n"
            f"AVAILABLE ACTIONS: {' '.join(f.action_codes)}\n"
            f"{ROLE_CLAUSES[condition]}\nQ OUTPUT: one action code only.")

def feedback(f): return f"R EXECUTED: {f.action}\nR RESULT: {f.non_target}"

def recovery(f):
    return ("RECOVERY UPDATE\n"
            f"R EXECUTED: {f.recovery_action}\n"
            f"R RESULT: {f.target}\nTRIAL STATUS: CLOSED")

def messages(f,condition,include_recovery=True):
    if condition not in CONDITIONS: raise ValueError(condition)
    out=[{"role":"system","content":SYSTEM},{"role":"user","content":user_setup(f,condition)},
         {"role":"assistant","content":f.action},{"role":"user","content":feedback(f)}]
    if include_recovery:
        out += [{"role":"assistant","content":f.recovery_action},{"role":"user","content":recovery(f)}]
    return out

def all_quadruplets():
    return {f.family_id:{c:messages(f,c) for c in CONDITIONS} for f in FAMILIES}
