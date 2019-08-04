from faker import Faker

fake = Faker("pl_PL")

def create_emails(n=1000):
    mails = []
    for i in range(n):
        mails.append(fake.email())
    return mails

def write_to_file(mails, fname="fake_mails.txt"):
    with open(fname, 'w') as f:
        text = "\n".join(mails)
        f.write(text)

mails = create_emails()
write_to_file(mails)