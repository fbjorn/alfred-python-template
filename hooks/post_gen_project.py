import os
import subprocess
from distutils.spawn import find_executable


def run(cmd):
    res = subprocess.Popen(
        cmd,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
        cwd=".",
        env={"PWD": os.path.abspath("."), "HOME": os.path.expanduser("~")},
    )
    stdout, stderr = res.communicate()
    if res.returncode != 0:
        if stdout:
            print(stdout.decode("utf8"))
        if stderr:
            print(stderr.decode("utf8"))
    return res.returncode == 0


print("=" * 10)
if run(["make"]):
    print("Project bootstrapped")

if (
    find_executable("pre-commit")
    and os.path.exists(".git")
    and run(["pre-commit", "install"])
):
    print("Hooks are installed")
else:
    print("You can optionally install pre-commit and its hooks")

print("\nNow open Alfred on Workflows tab")
print("=" * 10)
