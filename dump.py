from pykeepass import PyKeePass

kp = PyKeePass('Database.kdbx', password='mercedes1')
for entry in kp.entries:
    print(f"{entry.title} = {entry.username}:{entry.password}")
