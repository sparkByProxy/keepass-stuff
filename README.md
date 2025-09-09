## Cracking Keepass
get keepass master hash
`keepass2john CrackThis.kdb | grep -o "$keepass$.*" >  CrackThis.hash`

crack it with hashcat
`hashcat -m 13400 hash.txt /usr/share/wordlists/rockyou.txt`


## Dumping all passwords
`pyhton3 dump.py`
or as oneliner
```bash
python3 -c "from pykeepass import PyKeePass; print(PyKeePass('Database.kdbx', password='masterpassword').entries)"
```
