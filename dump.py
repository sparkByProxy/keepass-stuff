from pykeepass import PyKeePass
import sys

kp = PyKeePass(sys.argv[1], password=sys.argv[2])
for entry in kp.entries:
    print(f"### entry title: {entry.title}")
    print(f"username: {entry.username}")
    print(f"password: {entry.password}")
    print(f"notes: {entry.notes}")
