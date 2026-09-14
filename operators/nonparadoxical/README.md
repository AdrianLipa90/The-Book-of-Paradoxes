# Nonparadoxical operators

Status: `SUPPORTING_OPERATOR_LIBRARY`

This directory contains typed operators used to analyse, reduce, or connect
paradoxical structures without classifying the operators themselves as paradoxes.

A candidate belongs here only when all of the following are explicit:

1. domain and codomain;
2. branch predicates or control parameters;
3. preserved semantic/type distinctions;
4. exact versus numerical versus conditional claims;
5. a proof firewall stating what the operator does **not** establish.

A `NONPARADOXICAL_OPERATOR` must not require a contradictory state assignment,
a whole-part equivalence, or an untyped identification in order to be defined.
It may still be used inside the analysis of a paradox.

## Current entries

- `information_energy_bifurcation/` — an information-controlled Poincare
  pitchfork model with a closed mathematical kernel, a Q28 numerical witness,
  and an explicitly open information-to-physical-energy binding.
- `dynamic_identity_invariant/` — a transport-compatible operator invariant with
  an exact tetrahedral kernel, exact graph commutator theorem under stated
  hypotheses, exact tetrahedral half-turn holonomy, and a conditional periodic
  n-simplex extension. No personal or physical identity binding is claimed.
