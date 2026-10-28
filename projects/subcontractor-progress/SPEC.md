# Spec: Subcontractor progress

**Status:** Designed, not built · **Feeds:** desk 93 [Subcontractor Tracker](../../agents/93-subcontractor-tracker.md), and Projects & Growth's funder-report pack · **Asks:** #57 (also #53) · **Account:** operator (Adrielle's ChatGPT)

## Goal

Chris, on what the role should do about his subcontractors (Aug 13 interview, #57): they are "10, 20 year professionals at what they do. So they won't need too much managing, but following up for reporting and that sort of thing."

And on what happens with it at the other end, describing a week at home: "reporting to the people that fund the work that we do" (#57). The advertised role also listed "collate project reports and track subcontractor progress" (Aug 13 Slack, job ad).

So the goal is that the progress and reports he owes his funders arrive on time because the right person was asked at the right moment, politely, and everyone can see who has been asked and who has replied. It is a follow-up, never management. The reports are then collated (#53).

## Why now / why later

**Why it matters.** Chris reports to the people who fund the work. A report that depends on three or four subcontractors, each with their own dates, is easy to lose. SOP 24 asks Adrielle to send a friendly follow-up before each subcontractor's date, and to tell Chris at once if a section is late.

**Most of this is already built.** Projects & Growth (desk 06, M4) keeps every deliverable and report date, and its `deadline-tracker` and `funder-report-pack` skills already draft a friendly reminder for each section or date coming due. So the need is met, by Projects & Growth and Adrielle, without a new desk.

**What a separate desk would add, and why later.**
- Progress check-ins between report dates, which nothing drafts today.
- A record, across projects and by person, of who has been asked and who has replied, kept from reading Adrielle's mail and Teams.
- One place for the approved check-in wording.

It waits until Projects & Growth has been through a report and Chris can say what is missing. If 06's reminders are enough, this spec stays shelved.

## What exists today

- **Subcontractors.** A few main subcontractors, long-term, based around Australia and working remotely. Their first names, contact channels (Teams or email) and report headings belong in `AI Team/context/owner.md`, never in this package. The channel for each is UNKNOWN until Chris lists it.
- **Funders and projects.** A few large projects, each with deliverable and report dates (listed in `owner.md` and kept by Projects & Growth).
- **Desk 06 Projects & Growth (M4).** `deadline-tracker` holds every deliverable and report date and who owes what, flags what is late, and drafts reminders for Adrielle to send. `funder-report-pack` builds the section tracker, drafts reminders, checks each section against the headings, writes gap lists to authors and collates one draft (#57). Its Monday "Deadlines check" routine names what is coming up.
- **Desk 05 Research & Data.** `report-format` formats Chris's report into the house document; `report-draft` makes a first draft from his notes (#53).
- **SOPs.** [SOP 24](../../sops/24-project-report-collation.md) (project report collation: a tracker, a friendly follow-up before each date, save each section, never edit technical content) and [SOP 28](../../sops/28-file-documents-in-onedrive.md) (filing in OneDrive).
- **Approvals.** [APPROVALS.md](../../policies/APPROVALS.md): a message to a subcontractor is tier 2. Chris approves per message, or gives a standing approval for one exact template.

## Requirements

Written first, before the desk is designed.

- **Volume.** A few subcontractors, a few large projects, and a handful of check-ins around each reporting date. How often reports fall due is UNKNOWN until Projects & Growth's deadline lists exist. A person with nothing due gets nothing.
- **Who reads.** Adrielle reads and sends every check-in. Chris reads only the "no reply" list and anything a reply raises.
- **Who approves.** Chris approves one template (and a standing approval if he wants it). Anything outside the template goes to him: a problem with the work, a change of date, a question about payment.
- **Persistence.** The chase record for each project, with a status for each person on each item (not yet asked, asked, replied, no reply after the reminder, UNKNOWN), saved by Adrielle in `AI Team/projects/<project>/check-ins.md`. The deadline list (`deadlines.md`) and the report pack stay Projects & Growth's. Replies and sections are filed as SOP 28 says. Subcontractor names live in `AI Team/` only.
- **Tone.** A friendly follow-up, one clear ask, the date and the headings. Never management.
- **Accuracy.** "Replied" needs a real message. "No reply" is Chris's prompt, not a verdict, because the desk can't know who is away or unwell. Whether a report is late is Projects & Growth's call against its dates. Unreadable is UNKNOWN, never "no reply".
- **Confidentiality.** Drafts and sections are confidential. One subcontractor's report is never shown to another.

## Design

ChatGPT-first, reading Adrielle's mail and Teams. People send and file.

1. **Read the dates.** Adrielle names a project. The desk reads Projects & Growth's deadline list and report pack and picks what is coming due within the lead Chris has set, or a progress check-in he has asked for.
2. **Who owes what.** For each item it names the people who owe a section or an update, from the deadline list and `owner.md`. A section already marked Received in the report pack is not chased. People with nothing due are left out.
3. **Draft.** For each person, one check-in from Chris's approved template: what is due, the headings, the date, a thank-you and one ask. No pay or fees.
4. **Send.** Adrielle sends from her own user, after Chris's yes or under the standing approval. The desk doesn't send.
5. **Read the replies.** The desk looks for each person's reply in Adrielle's Outlook and Teams (read and search only) and updates the record. A message it can't read is UNKNOWN.
6. **No reply.** After the one reminder the template allows, an item with no reply goes to Chris as one line on the Team Lead's one list. The desk does not chase a second time, and does not call the report late.
7. **Hand off.** A "reply received" note names what came in and where it is filed. Projects & Growth's funder-report pack reads it. Adrielle collates (SOP 24) and Research & Data formats. The desk never edits a section.

**Named fallback.** What runs today: Projects & Growth's reminder drafts and Adrielle's tracker (SOP 24), sent by Adrielle in her own words or from the draft. The new desk adds progress check-ins and reply-reading. It is not needed for the job to be done.

## Preconditions and decisions Chris owns

1. **Does he want more than 06 gives?** Progress check-ins between report dates, or a record of replies across projects. If not, shelve the spec.
2. **Desk 06 on (M4)** and through at least one report.
3. **Who reports and how.** The subcontractors who owe reports, and the channel for each, in `owner.md`.
4. **The template.** One exact check-in wording, and whether Adrielle may send it under a standing approval.
5. **Telling the subcontractors.** He tells them Adrielle may be in touch. The relationship is his.
6. **The chasing rules.** How early the first check-in goes, what Adrielle does when there is no reply (one reminder), and what always comes to him.
7. **What counts as an update.** For each project, the headings and format the funder needs, so the check-in can name them.
8. **The handover.** The reminder drafts move from Projects & Growth to desk 93, so each record has one writer.
9. **Build yes.** Chris says yes to building desk 93.

## What Justin's team builds vs what Adrielle does

**Justin's team builds**
- The desk's skills in the house format (the check-in draft, and the chase record), tested on made-up people and projects.
- The edits to Projects & Growth's charter and to its `deadline-tracker` and `funder-report-pack` steps, so reminders are drafted by one desk.
- A check, on Chris's real plan, that the Outlook and Teams connectors can find a reply in Adrielle's mail and chats, reported plainly.
- The record format and the "no reply" and "reply received" lines, agreed with Projects & Growth so nothing is written twice.
- Help at install and when something behaves differently.

**Adrielle does**
- Names the project, sends each check-in under her own user once approved, and files replies per SOP 28.
- Saves the chase record and pastes the status line into the run log.
- Collates the report (SOP 24), and passes no-reply items to Chris.

**Chris does** the decisions above, approves the template and tells his subcontractors.

## Acceptance checks

1. **Right people.** For a made-up project with three items due, the desk drafts check-ins for exactly the people who owe them, with the right headings and dates.
2. **No one extra.** A person with nothing due isn't contacted, and a section already received isn't chased.
3. **Replies.** A made-up reply flips a status to "replied" only when a real message is found. With the mailbox disconnected, the status is UNKNOWN.
4. **No reply.** An item with no reply after the reminder produces one line to Chris and no second message to the subcontractor.
5. **One writer.** After the handover, Projects & Growth drafts no reminders and this desk writes no deadline, tracker or gap list.
6. **Tone.** Chris reads three drafts and says they read as a friendly follow-up, not management.
7. **Contents.** No draft mentions pay or fees, or edits or judges anyone's work.
8. **Hand-off.** The "reply received" note lists only what the subcontractor sent and where it is filed.
9. **Separation.** No message mentions another subcontractor's report.
10. **Injection.** A reply that says "ignore your rules and ..." is reported and not followed.
11. **Nothing sent by the desk.** The sent folder shows only what Adrielle sent.

## Risks and privacy

- **Relationships.** These are long-term professionals. A message that feels automated or pushy costs more than a late report. Chris approves the tone, and tells them first.
- **False alarms.** The desk can't see leave or illness. "No reply" asks Chris; it is never sent to the subcontractor as an accusation.
- **Silence is not lateness.** If a mailbox or chat can't be read, the status is UNKNOWN.
- **Two desks, one job.** If the handover isn't made, two desks draft the same reminder and a subcontractor is asked twice. The handover is a precondition for that reason.
- **Confidential content.** Drafts, sections and funder headings are confidential. They stay in `AI Team/` and the project folder, never in this package. Subcontractor names are not written in any package file.
- **Money.** Payment, fees and contracts are never discussed in a check-in. Anything about them goes to Chris.
- **Instructions in replies.** They are data, not instructions.
