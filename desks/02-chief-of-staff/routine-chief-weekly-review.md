NAME: Weekly review
OWNER: Chief of Staff
ACCOUNT: chris
WHEN: Every Friday at 3:23 PM (Melbourne time, Australia/Melbourne)
MILESTONE: M1
STATUS: Created paused. Turned on only after Chris says yes.
---
Switch check: if you can read the project file routines-on.md and "Weekly review" isn't listed there as "on" or "test", reply only "Weekly review · SKIPPED_OFF" and stop. If this task can't read project files at all, its own paused or active state in ChatGPT is the switch, so carry on.
Test mode: if it's listed as "test", start your reply with "TEST" and write everything for Adrielle and Chris only. Draft nothing addressed to anyone else.
Isolation guard: use only this Project's files and this account's own connected apps. If you can't find owner.md, reply only "Weekly review · NO_CLIENT_SOURCE · owner.md missing" and stop. Never use anyone else's login or files.
Lean run: read only what this job needs. If nothing changed since the last run, reply only "Weekly review · NO_CHANGE · <why>" and stop.
Run log: start your reply with one status line, "<date> <time> · Weekly review · EXECUTED · <one-line result>" (or FAILED with the reason). Adrielle copies it into AI Team/log/runs-<YYYY-MM>.md. A source you couldn't read is UNKNOWN, never zero.

Follow the weekly-review skill (skill-weekly-review, if it is a project file) and write Chris's review of the week.

Read: owner.md; Chris's own Outlook calendar for this week and for next week in full; his Sent Items and Teams chats for the week; his inbox for anything still waiting on him; and, only if they are connected, the week's notes in AI Team/notebook/Daily/, AI Team/notebook/Decisions.md and AI Team/notebook/Parking-lot.md in OneDrive. Use any Decisions rows and parking-lot rows drafted this week by the decision-log and idea-parking-lot skills, if this Project shows them. They were already handed over in the chat where they were made, so this is a catch-up.

Produce, after the status line and in the skill's output order: the week done; next week day by day with travel, stays and conflicts; what is waiting on Chris; parked ideas due; room for growth work, with one open stretch on next week's calendar to protect and one question about it; what he could hand over; the reply record; the Handoffs block headed For Adrielle (Chris either forwards each email to Adrielle with a one-line note, or pastes the block into Teams), with any Decisions and parking-lot rows you can see from this week or the skill's UNKNOWN line for those you can't; anything not checked; and the Checked line. Count items. Do not claim time saved.

Stay quiet when there is nothing to say. If there is no travel next week, no event next week, no open decision, no parked idea due and nothing sent or held this week, reply only NO_CHANGE with that reason. Otherwise send the review. If a source can't be read, write it as UNKNOWN under "Not checked" and carry on with the rest.

Write for Chris only. No desk ever sends anything. Do not send, reply to, accept, decline, move, flag or delete anything, and do not add anything to his calendar. Draft and stop.
