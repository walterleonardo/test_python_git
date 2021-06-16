import subprocess

from subprocess import check_output

commit_messages = check_output(
        ['pwd'], stderr=subprocess.STDOUT
    )


print(commit_messages)