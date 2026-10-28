NAME: Morning brief
OWNER: Chief of Staff
ACCOUNT: chris
WHEN: Every weekday at 6:07 AM (Melbourne time, Australia/Melbourne)
MILESTONE: M1
STATUS: Created paused. Turned on only after Chris says yes.
---
Switch check: if you can read the project file routines-on.md and "Morning brief" isn't listed there as "on" or "test", reply only "Morning brief · SKIPPED_OFF" and stop. If this task can't read project files at all, its own paused or active state in ChatGPT is the switch, so carry on.
Test mode: if it's listed as "test", start your reply with "TEST" and write everything for Adrielle and Chris only. Draft nothing addressed to anyone else.
Isolation guard: use only this Project's files and this account's own connected apps. If you can't find owner.md, reply only "Morning brief · NO_CLIENT_SOURCE · owner.md missing" and stop. Never use anyone else's login or files.
Lean run: read only what this job needs. If nothing changed since the last run, reply only "Morning brief · NO_CHANGE · <why>" and stop.
Run log: start your reply with one status line, "<date> <time> · Morning brief · EXECUTED · <one-line result>" (or FAILED with the reason). Adrielle copies it into AI Team/log/runs-<YYYY-MM>.md. A source you couldn't read is UNKNOWN, never zero.

Follow the morning-brief skill (skill-morning-brief, if it is a project file) and write Chris's brief for today.

Read: owner.md; Chris's own Outlook calendar for today and the next three working days; his inbox since the last brief (since Friday afternoon on a Monday), his Sent Items and his travel folder; his Teams chats since the last brief; and, only if they are connected, Todoist, and the newest note in AI Team/notebook/Daily/ and AI Team/notebook/Parking-lot.md in OneDrive. Pick the emails that need him with the email-triage skill. Use web search and a map source only for a drive time or a phone number the skill asks for, and name the source.

Produce, after the status line and in the skill's output order: today's calendar with conflicts; the Road card on a travel day; at most five emails that need Chris, each with why and a suggested action; what is due; the gaps in the next three working days; the Handoffs block headed For Adrielle (Chris either forwards each email to Adrielle with a one-line note, or pastes the block into Teams); anything not checked; and the Checked line. Under the divider, add drafts (reply-draft skill) for at most two of those emails, only where every fact for the reply is already in hand. Keep everything above the divider to one phone screen. Check the brief against the calendar and the inbox before you finish.

This is the one message that always goes out. A new day is always a change, so the lean-run NO_CHANGE rule does not apply to this routine: never reply NO_CHANGE. On a quiet day, send the short brief: say nothing is on the calendar and nothing needs Chris, and still give the Checked line. If a source can't be read, write it as UNKNOWN under "Not checked" and carry on with the rest. Chris is up at about 5:45 and reads this first.

Write for Chris only. No desk ever sends anything. Do not send, reply to, accept, decline, move, flag or delete anything. The drafts under the divider are for his own mailbox, for him to edit and send himself; a reply he would rather Adrielle sent goes in the Handoffs block, and a reply to someone of high importance to Chris or the business waits for Chris's yes before anyone sends it. In test mode, skip the drafts and write "Drafts skipped in test mode" instead, because they are addressed to other people. Draft and stop.
