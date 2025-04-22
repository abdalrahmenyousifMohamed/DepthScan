"""
Example usage of the DeepResearcher to produce a report.

See deep_output.txt for the console output from running this script, and deep_output.pdf for the final report
"""

import asyncio
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from deep_researcher import DeepResearcher

manager = DeepResearcher(
    max_iterations=1,
    max_time_minutes=5,
    verbose=True,
    tracing=True
)

query = "Generate a strategy intelligence report for the electric vehicle market and its key players " 
report = asyncio.run(
    manager.run(
        query
    )
)

print("\n=== Final Report ===")
print(report)
with open("final_report_electric_vehicle_deep.md", "w") as f:
    f.write("# Final Report\n\n")
    f.write(str(report))