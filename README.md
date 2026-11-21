# micro-instruction-engineering

Small toolkit for systematic prompt engineering — template construction,
optimization passes, and evaluation scoring for LLM prompts.

## What exists

```
src/
  optimization/  PromptOptimizer — iterative prompt improvement
                 (CoT decomposition, few-shot selection, instruction
                 clarification, format specification, constraints)
  evaluation/    PromptEvaluator — metric-based scoring + feedback
  templates/     PromptTemplate & MicroInstructionEngine —
                 structured templates, chain-of-thought / few-shot
                 prompt builders
examples/        runnable usage demo
```

```sh
pip install -r requirements.txt
python examples/basic_usage.py
```

## Status

Early-stage implementation — the core scaffolding and evaluation
metrics exist; measured gains on real tasks are not yet published.
`IMPLEMENTATION_ROADMAP.md` and other generated scaffolding docs were
removed as stale scaffolding.
