# Banach–Tarski claim ledger

| ID | Claim | Status | Dependency |
|---|---|---|---|
| BT-001 | TIR tetrahedral frame has off-diagonal Gram value `-1/3` | EXACT / SOURCE_DERIVED | pinned TIR commit |
| BT-002 | `T_+ ∪ (-T_+)` is the stella-octangula/cube vertex set | EXACT / DEFINITIONAL CONSTRUCTION | BT-001 |
| BT-003 | Stella dot spectrum is `{1,-1,-1/3,+1/3}` | EXACT | BT-001, BT-002 |
| BT-004 | Bloch relation alphabet is `{1,0,1/3,2/3}` | EXACT | BT-003 + standard Bloch overlap |
| BT-005 | Unmatched cross-sector pairs obey `cos(theta)=1/3` | EXACT | BT-003 |
| BT-006 | Disjoint-pair minimal-rotation axes are orthogonal | EXACT | vector product identity + BT-001 |
| BT-007 | Explicit matrices `A,B` are in `SO(3)` and have `cos(theta)=1/3` | EXACT | direct algebra |
| BT-008 | `A,B` are conjugate to the standard orthogonal-axis pair | EXACT | `SO(3)` transitivity on oriented orthonormal frames |
| BT-009 | `<A,B> ≅ F_2` | STANDARD_THEOREM | classical free-rotation theorem + BT-008 |
| BT-010 | Reduced words through length 12 produce no identity | NUMERICAL_WITNESS | validator |
| BT-011 | `F_2` has a paradoxical decomposition | STANDARD_THEOREM | group theory |
| BT-012 | Free rotational action transfers the paradoxical decomposition to `S^2 \ D` | STANDARD_THEOREM | orbit representatives / Choice |
| BT-013 | Absorption + radial extension yields `B^3 ~ B^3 ⊔ B^3` | STANDARD_THEOREM | Banach–Tarski |
| BT-014 | Banach–Tarski is a closed reduction in this repository | CLOSED_REDUCTION | BT-001..BT-013 |
| BT-015 | TIR dynamics forces antipodal completion `T -> T ∪ (-T)` | OPEN / NOT REQUIRED | semantic/dynamical binding |
| BT-016 | Every TIR spatial transport `W^X_ij` equals the BT minimal geodesic lift | OPEN / NOT REQUIRED | semantic/dynamical binding |
| BT-017 | BT geometry closes the Riemann-hypothesis XF-8C Loewner gate | OPEN / SEPARATE PROJECT | requires explicit Xi-translation/operator bridge |
