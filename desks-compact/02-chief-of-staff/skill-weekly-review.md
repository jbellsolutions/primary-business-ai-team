---
name: weekly-review
description: Chris's Friday review: the week that was, next week's calendar and travel, decisions waiting on him, parked ideas that fall due, and where there is room for higher-level work and the next contract. Use for the Weekly review scheduled task, or when Chris asks "how did the week go" or "what's next week".
---

# Weekly review

Serves #56 (time freed for higher-level work and the next contract) and #14 (a work log he can see: what got through, what is on his plate). Feeds #19 (what he could hand over) and #91 (the reply record).

## Inputs
- Chris's Outlook calendar: this week as it happened, and next week in full, including travel that starts at the weekend.
- Sent Items and Teams for the week, to see what Chris actually answered and what he handed on.
- Inbox items still waiting on him.
- If OneDrive is connected: the week's notes in `AI Team/notebook/Daily/` (what Adrielle closed, and its "Waiting on Chris" section), `AI Team/notebook/Decisions.md` and `AI Team/notebook/Parking-lot.md`. If not, write "OneDrive: not connected" and work from this Project's files and what Chris pastes.
- `owner.md`: projects and their report dates.
- Decisions rows and parking-lot rows drafted this week, if this Project shows them. They were already handed over in the chat where they were made; this review is only a catch-up.
- Skills used here: email-triage, reply-draft, idea-parking-lot, decision-log.

## Steps
1. **The week done.** List what happened, each with its source: events held, important replies Chris sent, decisions logged, jobs Adrielle closed (only if her Daily notes are readable). Facts only. If a source is unreadable, say UNKNOWN. Never write "nothing" for a source you couldn't read.
2. **Next week.** Day by day: time, title, place, project category. Travel legs, with the stay for each night and whether a confirmation was found ("confirmation found" or "not found in your calendar or travel folder"). Conflicts as in morning-brief, with drive times from a named map source or "not checked". Report dates for each project from `owner.md`, and anything the other side is waiting on.
3. **Waiting on you.** Open decisions, oldest first, five at most: who is waiting, since when, what is needed. Take them from the inbox, from the "Waiting on Chris" section of her Daily notes, and from decision-log questions Chris hasn't answered.
4. **Parked ideas due.** Rows in the parking lot whose "Remind on" falls next week. Don't ask about them here; the question comes when each one falls due (idea-parking-lot, step 6).
5. **Room for growth work (#56).** Under "Off your plate", list what actually left his desk this week: the Handoffs lines you gave him, drafts he used, jobs Adrielle closed. Use counts and item names, and write UNKNOWN for any you can't see. Don't claim time saved. Then find the longest open stretch next week that is not a travel day, give its day and clock times, and ask one question: "Protect <day, time> for <proposals / the next contract / a workshop presentation>?" You can't add it to his calendar. If the funding and tender radar exists (Projects & Growth, a later milestone), point to it; if not, don't name any opportunity.
6. **Could hand over (#19).** Up to three jobs Chris did himself this week that Adrielle could take, from Sent Items and the calendar (scheduling replies, forwarding documents, entering details). One line each, as suggestions for the Team Lead's handover list. Don't suggest handing over the funder, new work, money, contracts or complaints unless he asks.
7. **Reply record (#91).** From Sent Items: of the drafts you wrote, how many he sent as written, lightly edited, rewritten, or didn't use. UNKNOWN if you can't read it. If one exact kind of reply has gone out unchanged at least five times, name it and ask the standing-yes question from reply-draft. Only once.
8. **Handoffs.** One block headed For Adrielle, for Chris to paste into Teams: any Decisions rows and parking-lot rows you can see from this week, with any `routines-on.md` or `standing-approvals.md` lines, so a row missed earlier gets a second chance; the hand-over candidates for him to keep or cross out; and, if you can see the week's Morning brief status lines, those, for the run log. For anything you can't see, write "Rows drafted in other chats this week: UNKNOWN, not visible to this task. Paste any not yet sent." and "Run lines UNKNOWN: not visible to this task".
9. **Check pass.** Dates and times match the calendar; no item appears twice; each count adds up; everything unreadable is named.

## Output
```
Weekly review · week ending <date>

DONE THIS WEEK
- <item> · <source>

NEXT WEEK
<Day> · <time> · <title> · <place> · <category>
Travel: <legs and stays, with confirmation status>
Conflicts: <none found in Outlook | each one>
Report dates: <project · date, from owner.md>

WAITING ON YOU
1. <who> · "<subject>" · since <date> · needs <decision>

PARKED IDEAS DUE
- <idea> · remind on <date>

ROOM FOR GROWTH WORK
Off your plate: <items and counts, or UNKNOWN>
Open next week: <day, clock times>. Protect it for <suggestion>?

COULD HAND OVER
- <job> · <why Adrielle could take it>

REPLY RECORD
<sent as written / lightly edited / rewritten / not used, or UNKNOWN>

HANDOFFS · FOR ADRIELLE (copy into Teams, once a week)
1. <row or instruction>

NOT CHECKED
- <source> UNKNOWN: <why>

Checked: <what you cross-checked>
```
A heading with nothing under it says "none". Keep it to what Chris can read through in one sitting.

## Done when
Chris has one message he can read through, every item cites a real calendar entry, email or note, and nothing unread is reported as empty. The Handoffs block can be pasted as it stands.

## Never
- Add to his calendar, send, flag or move anything.
- Claim time saved. Count items; don't estimate.
- Name a contract, funder or opportunity you haven't seen in his mail, calendar or `owner.md`.
- Raise a decision or idea more than once in the same review.
- Send a review with nothing in it. If there is no travel, no open decision, no parked idea and nothing from the week, reply NO_CHANGE.
