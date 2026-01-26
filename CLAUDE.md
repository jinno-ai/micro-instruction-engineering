# Claude Code Instructions

## Project Overview
Micro-instruction-engineering focuses on prompt engineering optimization and evaluation techniques.

## Repository Structure
```
src/
├── evaluation/          # Prompt evaluation metrics and tools
├── optimization/        # Prompt optimization algorithms
└── templates/          # Prompt template management

examples/               # Usage examples
```

## Key Commands
- Install dependencies: `pip install -r requirements.txt`
- Run examples: `python examples/basic_usage.py`

## Development Guidelines
1. Follow Python best practices (PEP 8)
2. Add type hints for new functions
3. Write tests for new functionality
4. Update documentation for API changes

## Concept Sync System
This project uses the Concept Sync System v0.3 for maintaining conceptual consistency:
- Source: `instructions/advanced/12_concept_sync_system`
- Concept storage: `.concept/` directory
- Auto-decisions for resolving ambiguities
- Aggressive bloat control with GC policies

## Testing
Run tests with: `python -m pytest tests/`

## Notes
- This is a research-focused project
- Emphasis on reproducible prompt engineering techniques
- Documentation is as important as implementation