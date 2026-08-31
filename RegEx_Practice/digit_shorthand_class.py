#Practice reading a mixed pattern left to right and prove that re.search() stops at the first complete match.
import re

text= "aa Qx7 bb Rt4 cc"
pattern=r"[A-Z][a-z]\d"

# \d matches the digits means 0-9 any numbers.

print(f"Matched Output: {re.search(pattern,text).group()} and Span: {re.search(pattern,text).span()}")