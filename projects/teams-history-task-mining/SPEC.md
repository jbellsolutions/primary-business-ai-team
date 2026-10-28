# Spec: Teams history task mining

**Status:** Designed, not built · **Feeds:** the Team Lead (the `task-capture`, `sop-gap-check` and `handover-list` skills). No reserved desk: this is a one-off project · **Asks:** #80, #86 (also #76, #79, #85, #88, #89, #90) · **Account:** Chris's ChatGPT for the raw chat, Adrielle's for the cleaned list

## Goal

Chris, in Slack on Jul 17 (#80): "I tried exporting the chat history I have with current VA from MS teams to then use AI to pull the tasks out of it as a reference, but can't figure out how to export the chat."

And on the Microsoft setting that may hide old chat history from the new assistant's account (Aug 19 call, #86), Chris said: "That's a good point. I'll check."

So the goal is a task list, pulled by AI out of the Teams task chat, that Adrielle and the Team Lead can use as a reference: what the role really does, what recurs, and what was asked and may still be open. It has to come from a safe route. Nobody uses another person's login, and Adrielle does not need to see the raw chat.

## Why now / why later

**Why it is useful.** Chris wants the full task list of the role as the base for the SOPs (#79), and SOPs captured from what is actually done (#76). The chat is the best record of what was asked, in his own words. It also shows tasks that never reached the list, and it feeds the Team Lead's `sop-gap-check` and `handover-list`.

**Why it waits.**
- It needs Chris's own hands: an export or screenshots from his account.
- He said he would check the Microsoft setting (#86) and the answer isn't recorded.
- The chat holds participant and contract details, so #90 (what his contracts allow) has to be settled or the content cleaned first (#89).
- It is a one-off, so it does not justify a desk. The output is a list that the Team Lead uses.

## What exists today

- **The chat.** It sits in Chris's own Teams account, and Chris could not export it. It is a long history of tasks given in Teams, probably mixed with other talk. Its exact size is UNKNOWN.
- **Adrielle's account.** She has her own Microsoft user. Old chat history from before she started may not be visible to her, depending on a Microsoft setting that Chris is to check (#86). The package does not rely on her seeing it.
- **Leaver access.** Anyone who has left has their access ended through the leaver checklist ([SOP 30](../../sops/30-new-starter-and-leaver-access-checklist.md), #88). Nothing in this project uses it.
- **Team Lead skills.** `task-capture` turns a pasted block of chat into clean task lines, one per line. Its step 9 already says to read only what the signed-in account can see, to write "UNKNOWN: older chat not visible" when older chat is hidden, and that mining the whole old chat is this later project. `sop-gap-check` lists tasks with no SOP. `handover-list` keeps what Chris could hand over (#19).
- **Connectors.** Teams, signed in as the person, read and search only. Whether Chris's own ChatGPT can read deep history of one chat is UNKNOWN until one real read.
- **SOPs.** [SOP 05](../../sops/05-daily-catch-up-and-todoist-capture.md) (daily catch-up and Todoist capture) and [SOP 28](../../sops/28-file-documents-in-onedrive.md) (filing).
- **Policy.** [DATA.md](../../policies/DATA.md): Teams messages are never copied wholesale into notes. Summaries only.

## Requirements

Written first, before a route is chosen.

- **Volume.** A long history, written as tasks mixed with other conversation. The first pass works on one slice Chris picks (for example the most recent stretch) so he can judge the result before the rest.
- **Who reads.** Chris reads the mined list first, because it is his chat. Adrielle and the Team Lead then read only the cleaned list. No one reads the raw chat except Chris.
- **Who approves.** Chris approves what leaves his account and what Adrielle saves. Any task she adds to Todoist from it needs his yes, because it may be old.
- **Persistence.** The raw export stays with Chris, outside `AI Team/` and outside any desk's project files, and what happens to it is his decision. The desks never delete; people archive. The mined list is saved by Adrielle as `AI Team/notebook/Teams-history-tasks.md` (Obsidian-compatible, drafted by the Team Lead). It holds task lines with a date, not messages.
- **Accuracy.** Each line has the date of the message it came from and a status: "open", "maybe done" or "UNKNOWN". A chat alone can't prove that a task was done, so "done" is never stated as fact.
- **Scope.** Business tasks only. Personal conversation is skipped entirely and never summarised.
- **Safe route.** The chat comes from Chris's own account, or from an export by the tenant administrator that Chris authorises. No route uses anyone else's login.

## Design

ChatGPT-first for the mining. The export is a person's job.

**Stage 0: Chris's decisions.** The Microsoft setting (#86) and #90. Which route. Which slice. Which ChatGPT account does the mining. What happens to the raw export.

**Stage 1: get the chat out, from Chris's own account.** In this order of preference. Check what his Microsoft plan offers at build, and don't rely on a menu that may have moved.
1. **An export of his own chat data** through what his Microsoft account or plan offers for exporting his own Teams chats.
2. **An export by the tenant administrator.** Chris is the administrator for his Microsoft setup (#85), or names who is. It covers only this chat, and the file goes only to Chris. It is his decision, and it is not a person logging in as another.
3. **Screenshots or copy-paste in blocks** from his own Teams window, working back from the most recent.
4. **His own ChatGPT with his own Teams connector,** read-only, searching the chat. Whether it reads deep history is UNKNOWN until one real read.

**Stage 2: clean.** Before the text goes into ChatGPT, remove or replace participant names and details, contract terms, and any personal conversation. Chris decides how much cleaning #90 requires. A redaction checklist helps him. If the content is too sensitive to clean, the mining stops and Chris is told.

**Stage 3: mine.** In Chris's own ChatGPT by default, so the raw chat never reaches Adrielle's account. In the `task-capture` style, one task per line: title · project (from `owner.md`) · date asked · status (open, maybe done, UNKNOWN), with the message date after ` // `. A second pass marks tasks that recur, which is the base for SOPs.

**Stage 4: hand over only the list.** Chris reviews the top of the list and says yes. Adrielle receives the cleaned list, not the chat. The Team Lead:
- checks it against Todoist for duplicates, and proposes still-open tasks for Chris's yes;
- feeds the recurring tasks to `sop-gap-check` and `handover-list` (#79, #19);
- drafts the notebook page for Adrielle to save.

**Named fallback.** If no export route works, Chris pastes the most recent stretch in blocks, or none at all. The Team Lead's `task-capture` then works on new chats from now on, and the SOP library is built from the recordings Chris already planned (#76).

**On #86.** The setting is Chris's to check. This design works either way. If old history stays hidden from Adrielle, she works from the mined list. If Chris chooses to show it, nothing else changes, and the same cleaning rule applies to any mining done in her account.

## Preconditions and decisions Chris owns

1. **#86.** He checks the Microsoft setting and decides whether Adrielle may see old history. The recommended default is that she doesn't need to.
2. **#90 and #89.** What may go into ChatGPT, and how much he cleans first.
3. **Route** and **slice.**
4. **Which ChatGPT account** does the mining. Default: his own.
5. **The raw export.** Where it is kept, and who deletes it and when. Not a desk.
6. **Personal conversation** is skipped. He confirms.
7. **Yes to Todoist.** Which old tasks Adrielle may add, if any.

## What Justin's team builds vs what Adrielle does

**Justin's team builds**
- A short how-to for Chris with the exact clicks for each export route his plan offers, checked on a real account and marked UNKNOWN where it couldn't confirm. It never asks him to share a login.
- The mining prompt in the `task-capture` format, with a redaction checklist, tested on a made-up chat.
- A check of how deep the Teams connector reads in Chris's own ChatGPT, reported plainly.
- The recurring-task pass that feeds `sop-gap-check` and `handover-list`.

**Adrielle does**
- Helps Chris only on his own screen, if he asks.
- Receives the cleaned list and checks it against Todoist.
- Saves the notebook page and the run-log line.
- Never opens, uploads or keeps the raw chat.

**Chris does** the export, the cleaning decisions and the approvals.

## Acceptance checks

1. **Sample test.** On a made-up chat, every ask is found, none is invented, and each line has a date.
2. **Statuses.** Each line is open, maybe done or UNKNOWN. None says "done" without evidence.
3. **Personal talk.** A made-up personal passage produces no line.
4. **Redaction.** A made-up participant name and contract term do not appear in the output.
5. **Route.** Chris confirms in words which route he used and that no one's login but his own was used.
6. **Separation.** The raw export is not in `AI Team/` or in any desk's project files, and Adrielle never received it.
7. **Duplicates.** Lines already in Todoist are marked.
8. **Chris's yes.** He reviewed the list before Adrielle saved it.
9. **Gap list.** `sop-gap-check` produces a list of tasks with no SOP from it.
10. **Injection.** A line in the chat that says "ignore your rules and ..." is reported and not followed.

## Risks and privacy

- **Confidential content.** The chat holds participant details, contract details and other business information (#89). It goes to ChatGPT only after Chris's decision on #90, and cleaned.
- **Personal matters.** If the chat contains anything personal about a person, it is skipped. No line is written about it.
- **Not a performance review.** The list is about tasks, not people. The desk makes no judgement about anyone and writes none.
- **Using the chat.** If Chris isn't sure he may use the chat this way, he takes advice before running it.
- **Another person's login.** None is used: not a former user's, not an administrator signing in as someone, and not Adrielle's for Chris's chat.
- **Raw files linger.** An export left in a shared folder is a leak. Chris decides where it lives and when it goes.
- **Wrong status.** A chat can't show whether a task was done. Unknown is not zero: an old task marked UNKNOWN is checked with Chris before anyone acts on it.
- **Instructions in the chat.** Text in the chat is data, never instructions.
