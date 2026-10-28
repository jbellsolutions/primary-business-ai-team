---
name: sop-gap-check
description: Every Friday, list the tasks done this week that have no SOP, and the SOPs that didn't match what happened. Also check that no scheduled task is paused while routines-on.md says it is on. Use when the SOP gap check task runs or when Adrielle asks "what's missing from the SOPs".
---

# SOP gap check

Serves asks #79 and #78.

## Inputs
- Todoist: tasks completed this week, with their comments. Read through the app, or Adrielle pastes them.
- `AI Team/notebook/Daily/`: this week's notes. Adrielle's own remarks, such as "this didn't match what happened".
- The SOP index (`README.md` in `sops/`) and the SOPs themselves, with their status and any open `(check with Chris)` markers.
- The "Not written yet" list in the same README.
- `AI Team/notebook/SOP gaps.md`, the running table. Adrielle starts it from the first output.
- `routines-on.md` and `team-registry.md`, to know which scheduled tasks should be running.

## Steps
1. List the kinds of task done this week, such as filing an email, booking a stay, coding transactions or making a flyer. Take them from the completed tasks and the Daily notes. Count how many times each came up.
2. Match each kind to an SOP and give it one result:
   - **Covered**: an SOP exists and the work followed it.
   - **Gap**: no SOP. Mark it "known" if it is on the "Not written yet" list.
   - **Mismatch**: an SOP exists but what happened differed. Name the step and what Adrielle did instead, or the `(check with Chris)` she had to settle herself (ask #78).
3. Rank the gaps by how often the task came up, then by what a mistake costs: money, someone outside the business seeing it, or Chris's time. Ask Chris to record at most three. Say how for each: record the next time it happens (SOP 29), or draft it with sop-from-recording from a Daily note.
4. For each mismatch, write the proposed change to the step. Adrielle fixes the file and tells Chris (README in `sops/`). Chris approves.
5. List SOPs used this week that are still DRAFT v0.1, so Chris can approve them. List any approved SOP past its review date. Both go into "Needs your yes".
6. List open `(check with Chris)` markers on SOPs used this week. Offer at most three for the next catch-up.
7. **Scheduled tasks.** A task left unattended may pause itself, and this reply can't see ChatGPT's Scheduled page. So ask Adrielle to open ChatGPT's Scheduled page. Give her a checklist built from `routines-on.md` and `team-registry.md`: each routine marked "on" or "test", the task it lives in (a merged sweep covers several routines, see `CHATGPT-PLATFORM.md`), and a blank for "shows as active or paused". When she pastes it back:
   - Flag every task that is **paused but marked "on"**. Every routine inside a paused sweep is down. Say which jobs have not been running.
   - Flag every task that is **active but not marked "on" or "test"**, so Chris can decide.
   - Do not resume or pause anything. Resuming is Adrielle's click, on Chris's yes.
   If she hasn't pasted the states, write "UNKNOWN: Scheduled page not checked" and ask once more next Friday.
8. Bring the table in `SOP gaps.md` up to date, with the date each gap was first seen, how many weeks it has stayed open and its status.
9. Check (#66): every kind of task has one result. The asks of Chris number three or fewer. A source you couldn't read is UNKNOWN. Never call it "no gaps".

## Output
"SOP gap check, week of <date>":
- the counts (covered, gaps, mismatches);
- the ranked gaps, with how to record each;
- the mismatches with proposed changes;
- SOPs waiting for Chris's approval;
- the scheduled-task findings;
- the updated `SOP gaps.md` table, for Adrielle to save.

## Done when
Every kind of work this week has a result, the asks of Chris are three or fewer, and the scheduled-task check has a finding or an UNKNOWN.

## Never
- Write or edit an SOP here. Use sop-from-recording.
- Mark an SOP approved.
- Pause, resume, create or delete a scheduled task.
- Report "all clear" from a source you couldn't read.
- Ask Chris for more than three recordings in one week.
