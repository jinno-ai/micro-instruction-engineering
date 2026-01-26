# AI Agents Documentation

## Overview
This document describes the AI agents used in the micro-instruction-engineering project.

## Concept Sync Agent

### Purpose
Maintains the "Source of Truth" for project concepts in `.concept/` directory, detecting ambiguities and conflicts between specifications, design, and implementation.

### Responsibilities
- Extract claims from project artifacts (spec, design, code, tests, DB, ops)
- Maintain ontology, invariants, mappings, and ambiguities
- Detect conceptual conflicts and make AUTO decisions to resolve high-severity ambiguities
- Control bloat through aggressive GC and budget management
- Ensure concept synchronization across the project

### Execution
Run on demand or after significant changes to:
- Requirements or specifications
- Design documents  
- Implementation code
- Test suites
- Database schemas

### Output
- `.concept/ontology.yml` - Canonical terms dictionary
- `.concept/invariants.yml` - Project invariants
- `.concept/ambiguities.yml` - Ambiguities with AUTO decisions
- `.concept/conflicts.yml` - Contradictions between claims
- `.concept/decisions.md` - Active AUTO decisions (cache)

## Version
- Based on Concept Sync System v0.3
- Path: `instructions/advanced/12_concept_sync_system/12_concept_sync_system.md`