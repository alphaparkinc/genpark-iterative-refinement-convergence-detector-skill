from client import ConvergenceDetector

v1 = "def solve(): return 42"
v2 = "def solve(): return 42
"
res = ConvergenceDetector.check_convergence(v1, v2)
print("Convergence check:", res)
