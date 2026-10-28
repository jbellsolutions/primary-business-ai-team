---
name: automation-backlog
description: Spot what is worth automating, rank it by leverage, volume and risk, draft a try-out for the best one, and write up the hard cases for Justin's team. Use when Adrielle or Chris says "could this be automated", at the Friday wrap, or when a task keeps repeating.
---

# Automation backlog

Serves asks #81 and #82. It respects #28 (travel choices stay human) and #12 (Todoist stays).

## Inputs
- Todoist and the Daily notes, for what repeats and how often. Count it; don't guess.
- The SOPs, because a task with written steps is a candidate, and one without is not ready.
- `handover-list`, `sop-gap-check` and the run log, for repeated work and for what the routines already do.
- `owner.md`, and what the apps can do, from the install checks (START-HERE Step 5) and `CHATGPT-PLATFORM.md`.
- `AI Team/notebook/Automation backlog.md`, the running table. Adrielle starts it from the first output.
- Chris's volume, in his words: low, about three transactions a day, and a support call every second day (ask #82).

## Steps
1. Start from the need and not from a tool. Write what the job must do, and only then check whether a tool can do it. If a tool can't, call that the tool's limit, not the business's. Say who could solve it.
2. Spot candidates. Look for work that repeats, follows the same steps, uses information already in an app, and has its steps in an SOP. Give each one line: the job, how often it came up (counted from the record), and where its steps are written.
3. Score each on three things, High, Medium or Low:
   - **Leverage**: does it free Chris's time or Adrielle's, and whose?
   - **Volume**: how often it happens. At Chris's volume, many jobs are Low, and a Low is a good reason to skip. His own test: "is it worth automating that?... if it's easy to, well, why not?"
   - **Risk**: what if it is wrong. Count money, anything an outsider sees, participant data and Chris's name.
4. Give each a verdict:
   - **Skip**: Low volume and low leverage, or the decision is Chris's. Booking and choosing travel, paying (NAB Connect), and replying as Chris all stay with people.
   - **Try**: leverage and volume at least Medium, risk Low or Medium, and ChatGPT can do it with a skill, a saved prompt, an app or a scheduled task.
   - **Hard**: it needs something ChatGPT can't do alone, such as a server, a link between two apps, or a login it must not have.
5. Try one at a time. Draft the skill or saved prompt, then a test plan: the real item to run it on, what a good result looks like, and how Adrielle checks it. She runs it in test mode. Switching anything on, connecting an app or buying anything is tier 3, which needs Chris's yes (`APPROVALS.md`).
6. Hard cases: write a short request to Justin's team through the route settled at install (ask #98 is open). Say what is done by hand now, how often, what is wanted, what was tried and where the tool stopped. Chris's own wording: "we want to automate this, have you got any suggestions, tools, tips to start that?" Adrielle sends it.
7. Record each result in the table with its date. Mark one "done (evidence)" only after a real run succeeded. Send a new ask Chris voices to ask-ledger.
8. Check (#66): every Skip has a reason, every Try has a test plan, every Hard has a request. Time saved is claimed only from counts in the record. Never estimate it.

## Output
- A ranked table: job, how often, leverage, volume, risk, verdict, reason.
- The top Try item with its test plan.
- Any request for Justin's team, as a draft.
- The updated `Automation backlog.md`, for Adrielle to save.

## Done when
Chris can read the ranked list on one screen: the biggest leverage points, what is skipped and why, and one candidate with a test plan.

## Never
- Build, connect, switch on or pay for anything without Chris's yes.
- Automate a decision that is Chris's.
- Present a tool's limit as how the business has to work.
- Claim savings without counts.
- Send the request to Justin's team yourself.
