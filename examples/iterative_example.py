"""
Example usage of the IterativeResearcher to produce a report.

See iterative_output.txt for the console output from running this script, and iterative_output.pdf for the final report
"""

import asyncio
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from deep_researcher import IterativeResearcher

manager = IterativeResearcher(
    max_iterations=2,
    max_time_minutes=3,
    verbose=True,
    tracing=True
)

query = "Generate a strategy intelligence report for the electric vehicle market and its key players " 
output_length = "10 pages"
output_instructions = ""

report = asyncio.run(
    manager.run(
        query, 
        output_length=output_length, 
        output_instructions=output_instructions
    )
)

print("\n=== Final Report ===")
print(report)
with open("test_final_report_electric_vehicle_os.md", "w") as f:
    f.write("# Final Report\n\n")
    f.write(str(report))