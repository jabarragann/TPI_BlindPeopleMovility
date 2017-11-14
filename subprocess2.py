import subprocess

cat = subprocess.Popen(['./deviceInformation.sh'],
                        stdout=subprocess.PIPE,
			stderr=subprocess.PIPE
                        )

grep = subprocess.Popen(['grep', 'Connected'],
                        stdin=cat.stdout,
                        stdout=subprocess.PIPE,
                        )

end_of_pipe = grep.stdout

print('Device Status:')

for line in end_of_pipe:
    info1=str(line).strip()
    info1=info1[4:-3]
    print(info1)

