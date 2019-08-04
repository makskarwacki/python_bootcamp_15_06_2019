import sys

if len(sys.argv) == 1:
    in_name = "dane/emails.txt"
    out_name = "dane/cleand_emails.txt"
else:
    in_name = sys.argv[1]
    out_name = sys.argv[2]

emails = set()
with open(in_name) as f:
    for line in f:
        line = line.lower().strip()
        if line.count("@") == 1:
            emails.add(line)

with open(out_name, 'w') as f:
    text = "\n".join(sorted(emails))
    f.write(text)
