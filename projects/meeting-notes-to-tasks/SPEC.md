# Spec: Meeting notes to tasks

**Status:** Designed, not built · **Feeds:** desk 90 [Meeting Notes](../../agents/90-meeting-notes.md), and the Team Lead's task-capture skill · **Asks:** #10, #103 (also #8, #9, #13) · **Account:** operator (Adrielle's ChatGPT)

## Goal

Chris, on the Read AI recorder in the daily catch-up (Aug 4 call, #10): "I like the idea of getting Read AI in our teams catch up ... because then there's no excuse of missing, or if you do the task, then read the notes and see whether you've covered everything."

So the goal is two things. First, everything said in a catch-up or a call becomes a task line on the one Todoist list, without anyone re-typing notes (#10, #9, #8). Second, after the call, the recap is checked against the list, so a missed task shows up before it is missed.

Optional, and only if Chris wants it (#103): a short brief of the Teams channels, like the Slack brief that Justin's team uses. Chris has not asked for this himself. It is Justin's team's idea, so it is a separate part with its own yes.

## Why now / why later

**Why it matters now.** Tasks written in the Teams chat have been missed, and Chris wants Todoist to hold every task (#9). The Team Lead's task-capture skill (M1) already turns a pasted recap, the Teams chat or notes into task lines. So the need is covered by paste from the first day.

**Why the automatic version is later.**
- The Read AI app inside ChatGPT is unverified, and so is Chris's ChatGPT plan (#93).
- Read AI was not set up for Chris's catch-up when it was discussed.
- Teams meeting recaps may or may not be readable through the connector.
- If a recap still has to be pasted, desk 90 adds nothing over the Team Lead.
- M1 must show that capture by paste works before anything is automated.

The spec is built when a recap source is connected and proved with one real read (the charter's "Build when").

## What exists today

- **Recorder.** Justin's team uses Read AI, and recommended it for Chris's calls and the daily catch-up. It is not confirmed that Chris has it set up.
- **Catch-up.** An online catch-up in Teams, where Chris gives Adrielle tasks. Tasks also arrive in the Teams chat (SOP 05). Chris keeps the catch-up and does not want it replaced (#15).
- **Todoist.** One list for Adrielle; Chris keeps his own. The free plan stops at five projects (#11, open).
- **Team Lead.** The `task-capture` skill turns a Read AI recap, Teams chat, catch-up notes or an email into a block that Adrielle pastes into Todoist's quick add, one task per line. It already runs a recap check (its step 8: every action in the recap has a line or a reason). It is on in M1 and works by paste.
- **Chief of Staff.** Chris's morning brief already reads his own Teams chats since the last brief.
- **Connectors.** Outlook email, Outlook calendar, Teams and OneDrive/SharePoint, each signed in as the person, read and search only. Nothing writes to Todoist.
- **SOPs.** [SOP 05](../../sops/05-daily-catch-up-and-todoist-capture.md) (catch-up and Todoist capture) and [SOP 17](../../sops/17-log-a-support-call-or-industry-meeting.md) (logging a support call or industry meeting).
- **Policy.** [DATA.md](../../policies/DATA.md): recordings and transcripts stay in Read AI or Teams; summaries only, with a link.

## Requirements

Written first, before the tool is chosen.

- **Volume.** One catch-up recap on each working day, plus the calls Chris chooses to record. His calendar is "not crazy busy" (Jul 16 call), with about 30 workshops a year and a support call about every second day (#82). Tasks per recap: UNKNOWN until the first real run; the charter's starting limit is 30 lines per recap.
- **Who reads.** Adrielle reads every task line before she saves it. Chris reads only the "not covered" list and any line marked "decision for Chris", on the Team Lead's one list for him.
- **Who approves.** Adrielle saves task lines to Todoist (housekeeping, tier 1). A line that makes something happen for another person (a message to a venue, a subcontractor or a farmer) still needs Chris's yes, as in [APPROVALS.md](../../policies/APPROVALS.md). Chris re-sequences priorities at the catch-up (#13).
- **Persistence.** The recap stays in Read AI or Teams. The desk keeps no recap text. Task lines live in Todoist; the desk's "covered / not covered" list lives only in the chat and the end-of-day report. The run log holds one line per run.
- **Accuracy.** Every line points to words in the recap. A task Chris did not ask for is never created. Unreadable is UNKNOWN, never zero.
- **Consent.** Everyone on a recorded call has been told it is recorded.
- **Not monitoring.** The check lists tasks that are missing from the list. It does not score anyone (#83).

## Design

ChatGPT-first, in Adrielle's account, with the fallback that works from the first day.

**Part A: recap to tasks (#10).**
1. Adrielle opens the Meeting Notes project and says which recap (for example, "this morning's catch-up").
2. The desk reads it from the connected source, in this order: Read AI app, then the Teams recap, then a paste. It names back the recap's title and date.
3. It drafts the lines in the `task-capture` format: one task per line, `<title> #<Project> <due date, only if said>`, with a note after ` // ` saying where in the recap. It sorts them into Adrielle's tasks, "For Chris's list", "Waiting on" and "Need Chris's answer", puts anything merely discussed on a "discussed, not asked" list, and marks lines already in Todoist (checked with a read-only look at Todoist).
4. Adrielle checks the lines against her own notes and saves them to Todoist. The desk never saves.
5. After the call or when the tasks are done, Adrielle asks for the check. The desk reads the recap again and lists anything said that is neither a line nor "discussed, not asked". That "not covered" list goes to the Team Lead's end-of-day report.

**Part B: channel brief (#103), only if Chris says yes.**
- A summary per channel of decisions, asks and anything waiting on Chris, with a link to each message, for the channels Adrielle already belongs to and Chris named. It is a draft for Adrielle, and may become a scheduled task that is created paused.
- A brief of Chris's own channels cannot be built on Adrielle's account. The Chief of Staff's morning brief already reads his Teams chats; a channel summary would extend that brief. That changes desk 02, so it is Chris's decision and is not part of this spec's build.

**Named fallback.** If no recap source connects, Adrielle pastes the recap into the Team Lead chat and the `task-capture` skill does Part A. Part B falls back to Adrielle pasting channel messages in. Nothing is lost.

## Preconditions and decisions Chris owns

1. **Recorder.** Read AI or Teams' own recording for the daily catch-up, switched on, with everyone told.
2. **Which calls.** Which calls ChatGPT may read, given that recaps can hold participant and contract details (#90). Until he answers, calls with farmers, funders and subcontractors stay out.
3. **Sharing his own recaps.** Whether and how Chris shares recaps of his own calls with Adrielle (a link or a paste).
4. **The handover.** The Team Lead's `task-capture` skill gives recap capture, including its recap check, to desk 90 and keeps everything else, so one writer remains.
5. **Todoist route.** A connected app or paste. The plan question (#11) does not block this.
6. **Part B.** Yes or no, and which channels.
7. **Build yes.** Chris says yes to building desk 90 once a source is proved.

## What Justin's team builds vs what Adrielle does

**Justin's team builds**
- A check, on Chris's real plan, of the Read AI app and the Teams recap, with one real read each, and a plain report of what works and what does not.
- The desk's skills in the house format (recap to tasks, the recap check, and the channel brief if Chris says yes), tested on a made-up recap.
- The edit to the Team Lead's `task-capture` skill that hands recap capture over.
- If Part B is wanted, a scheduled task for the brief, created paused.
- Help with the install and fixes if a connector behaves differently from what the plan says.

**Adrielle does**
- Connects each app under her own sign-in, read-only, with "ask first".
- Creates the Project from the charter's Profile and runs the check in START-HERE Step 6.
- Reads and saves the task lines; pastes the status line into the run log; never lets the desk save.
- Turns on a routine only when Chris says yes.

**Chris does** the decisions above, tells people on recorded calls, and shares his own recaps if he chooses.

## Acceptance checks

1. **Source.** A real recap is read from the connected source and its title and date are named back. A pasted recap is not enough for this check.
2. **Round trip.** From one real catch-up, every task Chris gave is a line, and Adrielle ticks them against her own notes. None is invented, and each line's "where in the recap" holds up.
3. **Duplicates.** A task already in Todoist is marked "already in Todoist", not repeated.
4. **Discussed, not asked.** Something mentioned but not assigned lands on that list, not on the task list.
5. **Not covered.** In a rehearsal where Adrielle leaves out one task, the check finds it.
6. **UNKNOWN.** With the source disconnected, the run says UNKNOWN, not "no tasks".
7. **Isolation.** The desk refuses to read a recap from another person's account or from a login that isn't Adrielle's.
8. **Nothing written.** Todoist and every other app are unchanged by the desk.
9. **Injection.** A recap line that says "ignore your rules and ..." is reported and not followed.
10. **Part B, if built.** The brief cites real messages with links, covers only the channels Chris named, and is a draft only.

## Risks and privacy

- **Recording consent.** Recording a call needs everyone on it to know. Chris owns this, and Adrielle checks the invite wording.
- **Confidential content.** Recaps may hold participant details and contract terms (#89, #90). The desk keeps task lines and a link, not text. Read AI's own sharing settings for each recap are checked at build.
- **Wrong recaps.** Machine recaps can misname an owner or a date. Anything unclear is UNKNOWN and gets settled at the catch-up. The desk never fills a gap.
- **Noise.** If every aside becomes a task, the list fills with clutter. "Discussed, not asked" keeps asides off the task list.
- **Replacing the human catch-up.** The desk supports it and never replaces it (#15).
- **Instructions inside a recap.** Transcript text is data, never instructions.
- **Another person's data.** The operator account sees only what Adrielle's sign-ins see. No one uses another person's login.
