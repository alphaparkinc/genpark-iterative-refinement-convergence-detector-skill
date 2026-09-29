# genpark-iterative-refinement-convergence-detector-skill

Sequence matcher and convergence detector monitoring edit distance between sequential agent refinement iterations.

## Architecture

```mermaid
flowchart LR
    Prev[Revision N-1] --> Matcher[difflib.SequenceMatcher]
    Curr[Revision N] --> Matcher
    Matcher --> Ratio[Similarity Ratio]
    Ratio --> Condition{Ratio >= Threshold?}
    Condition -->|Yes| Halt[Halt Refinement Loop]
    Condition -->|No| Continue[Continue Iteration]
```

## Features
- **Oscillation Detection**: Prevents infinite ping-pong edits.
- **Pure Python**: 100% Standard Library.
