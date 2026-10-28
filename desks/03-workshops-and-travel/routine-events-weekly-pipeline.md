NAME: Workshop pipeline
OWNER: Workshops & Travel
ACCOUNT: operator
WHEN: Every Monday at 9:13 AM (Melbourne time, Australia/Melbourne)
MILESTONE: M2
STATUS: Created paused. Turned on only after Chris says yes.
---
Switch check: if you can read the project file routines-on.md and "Workshop pipeline" isn't listed there as "on" or "test", reply only "Workshop pipeline · SKIPPED_OFF" and stop. If this task can't read project files at all, its own paused or active state in ChatGPT is the switch, so carry on.
Test mode: if it's listed as "test", start your reply with "TEST" and write everything for Adrielle and Chris only. Draft nothing addressed to anyone else.
Isolation guard: use only this Project's files and this account's own connected apps. If you can't find owner.md, reply only "Workshop pipeline · NO_CLIENT_SOURCE · owner.md missing" and stop. Never use anyone else's login or files.
Lean run: read only what this job needs. If nothing changed since the last run, reply only "Workshop pipeline · NO_CHANGE · <why>" and stop.
Run log: start your reply with one status line, "<date> <time> · Workshop pipeline · EXECUTED · <one-line result>" (or FAILED with the reason). Adrielle copies it into AI Team/log/runs-<YYYY-MM>.md. A source you couldn't read is UNKNOWN, never zero.

The job: show Adrielle where every workshop stands and draft whatever is missing. Follow skill-workshop-pack.md for the stages, and SOPs 13 to 16.

Read, in this order:
1. owner.md: Projects, the tag Chris uses on workshop emails, and the "Funder step" line if it is there.
2. Chris's calendar from today forward: every workshop entry, with tentative ones marked.
3. The admin inbox: threads carrying Chris's workshop tag that have no Todoist task yet.
4. Todoist, the workshop tasks and their comments, if it is connected. If not, write "Todoist: UNKNOWN, paste the workshop tasks" and carry on from the calendar and folders.
5. The folders in AI Team/workshops/: file names only.

Produce, in this chat, for Adrielle only:
- One table, soonest workshop first, up to ten rows: date · town · stage (1 to 12 from the pack) · waiting on · next action · UNKNOWN items.
- In the next-action column, flag: a flyer waiting for Chris; a website event not live when the workshop is dated this week; travel not confirmed for a workshop Chris must travel to; a deck not yet checked when the venue only uses PowerPoint (skill-slides-check.md); a date or venue that differs between the thread, the calendar and the task; the funder step still UNKNOWN (ask #30).
- For each tagged workshop with no task, draft the opening of its pack (facts table, task name and stage list, flyer brief). Do this for up to three per run and list the rest as "pack needed".
- A last section, "For the end-of-day list": one line for each thing waiting on Chris (a flyer to approve, a stay to pick, an answer on the funder step). Adrielle carries these to the Team Lead's end-of-day report. Do not message Chris.

For the lean-run test, "nothing changed" means: no new tagged thread, no stage waiting on anyone, no difference between sources, and no UNKNOWN that Adrielle could settle. If you can't read the calendar, that is UNKNOWN, not "no change": say so in the status line.

Draft, then stop. Never wait for an approval, and never send, book, post or change anything.
