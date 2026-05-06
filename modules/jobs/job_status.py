import json
from pathlib import Path

BASE_DIR = Path.home() / "Nobara_FF_UI"
DATA_FILE = BASE_DIR / "data.json"
JOBS_FILE = BASE_DIR / "modules" / "jobs" / "jobs.json"

try:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    with open(JOBS_FILE, "r", encoding="utf-8") as f:
        jobs = json.load(f)

    job_code = data.get("job", "WAR")
    job = jobs.get(job_code, jobs["WAR"])

    print(f"{job_code} {job['name']}")

except Exception:
    print("WAR Warrior")