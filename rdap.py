import subprocess
from pathlib import Path
home_dir = Path.home()
import json 

def rdap(url):
  try:
    return json.loads(subprocess.run([f"{home_dir}/go/bin/rdap", "--json", url], capture_output=True).stdout.strip())
  except:
    return None