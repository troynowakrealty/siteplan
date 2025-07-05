import subprocess
import sys

def run(params):
    cmd = params.get("command")
    if not cmd:
        return "Missing command"
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout.strip() or result.stderr.strip()
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    command = " ".join(sys.argv[1:]) or "echo test"
    output = run({"command": command})
    print(output)
