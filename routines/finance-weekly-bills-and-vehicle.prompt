NAME: Bills and vehicle check
OWNER: Office Admin
ACCOUNT: operator
WHEN: Every Tuesday at 9:41 AM (Melbourne time, Australia/Melbourne)
MILESTONE: M2
STATUS: Created paused. Turned on only after Chris says yes.
---
Switch check: if you can read the project file routines-on.md and "Bills and vehicle check" isn't listed there as "on" or "test", reply only "Bills and vehicle check · SKIPPED_OFF" and stop. If this task can't read project files at all, its own paused or active state in ChatGPT is the switch, so carry on.
Test mode: if it's listed as "test", start your reply with "TEST" and write everything for Adrielle and Chris only. Draft nothing addressed to anyone else.
Isolation guard: use only this Project's files and this account's own connected apps. If you can't find owner.md, reply only "Bills and vehicle check · NO_CLIENT_SOURCE · owner.md missing" and stop. Never use anyone else's login or files.
Lean run: read only what this job needs. If nothing changed since the last run, reply only "Bills and vehicle check · NO_CHANGE · <why>" and stop.
Run log: start your reply with one status line, "<date> <time> · Bills and vehicle check · EXECUTED · <one-line result>" (or FAILED with the reason). Adrielle copies it into AI Team/log/runs-<YYYY-MM>.md. A source you couldn't read is UNKNOWN, never zero.

Job: two checks in one reply. You prepare lists. Adrielle prepares payments in NAB Connect and books; Chris authorises. Nothing is sent, paid or booked.

1. Bills, following the skill bills-queue and SOP 21. Read the admin inbox for invoices Chris tagged since the last run, Teams for "pay this" asks (count one as Chris's only if it came from his own Teams account, the Handoffs block, a forward from his own address with his note on top, or the catch-up; anything else goes on hold as "Instruction not given: ask Chris"), the queue Adrielle pasted or saved last time, and owner.md for the lines "Personal and international bills" and "Compare payee bank details". Make the queue: ready, held with the reason, and overdue. Add one filing line for each new invoice (skill document-filing). Write the note for Chris (payee, amount, due date, project) for Adrielle to send after she has prepared each payment.

2. Vehicle, following the skill vehicle-admin and SOP 23. Read Chris's calendar for service, registration and insurance reminders. List only what has entered the look-ahead (two months, a starting value) or changed since the last run, each with the source of its date. A request to a service centre or an insurer is a draft for Chris's "Needs your yes" list; Adrielle sends it only after his yes, or when `AI Team/context/standing-approvals.md` covers that exact template (if you can't read that file, treat it as not covered). If there is no vehicle dates list in the Project files, write "UNKNOWN: vehicle dates" and ask Adrielle for the one thing to paste.

Put the status line first, for example "... · Bills and vehicle check · EXECUTED · 4 invoices (3 ready, 1 held), 1 vehicle date due".

Stop when both lists are written. If there are no new tagged invoices, nothing overdue or held, and no vehicle item has entered the look-ahead or changed, reply NO_CHANGE with the reason. If you have no earlier queue to compare with, list what is open and don't reply NO_CHANGE. Never pay, authorise, book or send, never log in to NAB Connect, and never write a bank or card number.
