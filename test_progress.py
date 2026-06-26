from hqai.core.progress import ProgressManager
import time

with ProgressManager() as progress:
    task = progress.add_task("Testing Progress...", total=100)

    for _ in range(100):
        time.sleep(0.03)
        progress.update(task, advance=1)

print("✅ Progress test completed")
