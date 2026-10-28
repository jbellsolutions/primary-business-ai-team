NAME: Xero coding prep
OWNER: Office Admin
ACCOUNT: operator
WHEN: Every Thursday at 9:23 AM (Melbourne time, Australia/Melbourne)
MILESTONE: M2
STATUS: Created paused. Turned on only after Chris says yes.
---
Switch check: if you can read the project file routines-on.md and "Xero coding prep" isn't listed there as "on" or "test", reply only "Xero coding prep · SKIPPED_OFF" and stop. If this task can't read project files at all, its own paused or active state in ChatGPT is the switch, so carry on.
Test mode: if it's listed as "test", start your reply with "TEST" and write everything for Adrielle and Chris only. Draft nothing addressed to anyone else.
Isolation guard: use only this Project's files and this account's own connected apps. If you can't find owner.md, reply only "Xero coding prep · NO_CLIENT_SOURCE · owner.md missing" and stop. Never use anyone else's login or files.
Lean run: read only what this job needs. If nothing changed since the last run, reply only "Xero coding prep · NO_CHANGE · <why>" and stop.
Run log: start your reply with one status line, "<date> <time> · Xero coding prep · EXECUTED · <one-line result>" (or FAILED with the reason). Adrielle copies it into AI Team/log/runs-<YYYY-MM>.md. A source you couldn't read is UNKNOWN, never zero.

Job: prepare this week's Xero coding list, following the skill xero-coding-prep and SOP 20. You prepare; Adrielle codes in Xero. Nothing is sent. The Unknowns note for Chris is written for Adrielle to send on Teams today, ready for the next catch-up.

Read: owner.md (the project list, the calendar categories, and whether Chris has OK'd bank lines for ChatGPT); the Xero export of unreconciled lines, and the chart of accounts and coding notes, in the Project files or the chat; Chris's calendar for the days since the last run; the admin inbox for receipts and invoices since the last run; and the last "Xero coding prep" line and the open Unknowns in AI Team/log/runs-<YYYY-MM>.md and the Daily notes.

If owner.md doesn't have the line "Bank lines for ChatGPT: yes" with Chris's name and a date, reply only "Xero coding prep · NO_CLIENT_SOURCE · Chris's OK for bank lines not in owner.md" and stop.

If there is no export for this week, don't stop. Make the calendar map and the receipts list, mark the Xero lines "UNKNOWN: no export this week", and end with one request to Adrielle: "Please paste this week's unreconciled lines, account numbers removed." If that is the second run in a row with no export, say so in the status line.

Produce, in this order: the coding table; the Unknowns list for Chris, written to him and ready to send; the calendar map and the receipts with no matching line; proposed coding-note additions; and the counts check (lines in, lines coded, lines unknown). The status line reads like "... · Xero coding prep · EXECUTED · 22 lines, 19 coded, 3 unknown".

Stop when the lists are written. If there are no new lines, no new receipts and no open Unknowns since the last run, reply NO_CHANGE. If you can't read what the last run produced, treat it as changed and don't reply NO_CHANGE. Never code, reconcile, pay or send anything, and never write a bank account number.
