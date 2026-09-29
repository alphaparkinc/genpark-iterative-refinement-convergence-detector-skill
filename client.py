"""Iterative Refinement Convergence Detector.
100% Python Standard Library.
"""

import difflib

class ConvergenceDetector:
    """Measures edit distance and semantic similarity between sequential code iterations."""
    @staticmethod
    def check_convergence(prev_text: str, curr_text: str, threshold: float = 0.95) -> dict:
        matcher = difflib.SequenceMatcher(None, prev_text, curr_text)
        ratio = matcher.ratio()
        is_converged = ratio >= threshold
        is_identical = (prev_text == curr_text)

        return {
            "similarity_ratio": round(ratio, 4),
            "is_converged": is_converged,
            "is_identical": is_identical,
            "status": "CONVERGED" if is_converged else "DIVERGENT"
        }
