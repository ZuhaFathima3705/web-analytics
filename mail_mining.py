import imaplib
import email
from email.header import decode_header
from collections import Counter
USERNAME = "230071601254@crescent.education"
PASSWORD = "hdtr aqek mcsi avfu"
imap_server = "imap.gmail.com"
mail = imaplib.IMAP4_SSL(imap_server)
mail.login(USERNAME, PASSWORD)
status, messages = mail.select('"[Gmail]/Sent Mail"')
if status == "OK":
    status, data = mail.search(None, "ALL")
    email_ids = data[0].split()
    print("Total Sent Emails:", len(email_ids))
    senders = []
    subjects = []
    for i in email_ids[-20:]:
        res, msg_data = mail.fetch(i, "(RFC822)")
        for response in msg_data:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                subject, enc = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(enc or "utf-8")
                to_, enc = decode_header(msg.get("To"))[0]
                if isinstance(to_, bytes):
                    to_ = to_.decode(enc or "utf-8")
                senders.append(to_)
                subjects.append(subject)
                print("To:", to_)
                print("Subject:", subject)
                print("-" * 50)
    print("\n🔹 MOST CONTACTED PEOPLE:")
    count = Counter(senders)
    for person, freq in count.most_common(5):
        print(person, "->", freq, "emails")
    print("\n🔹 COMMON TOPICS (WORDS IN SUBJECT):")
    words = " ".join(subjects).lower().split()
    common_words = Counter(words)
    for word, freq in common_words.most_common(10):
        print(word, "->", freq)
else:
    print("Failed to open Sent Mail")
mail.logout()
