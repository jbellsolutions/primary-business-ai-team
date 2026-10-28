---
name: funder-report-pack
description: Use when a funder report is coming due and subcontractors owe sections. Sets up the section tracker, drafts the friendly follow-ups, checks each section against the required headings, and collates one draft. Chris writes the recommendations and submits; the desk never changes technical content.
---

# Funder report pack

Serves #57. Follows SOP 24 (project report collation). Formatting of the collated document is done by Research & Data (report-format). Saved by Adrielle under `AI Team/projects/<project>/reports/` as `<YYYY-MM-DD> report pack.md`.

## Inputs
- The report's due date and its required headings, from the funder's template in the project folder (the line `Report template for <project>` in `owner.md`). If it isn't there, ask Adrielle once.
- `deadlines.md` for the project, and `owner.md` for the subcontractors' first names and what each does.
- Subcontractors' section drafts, saved in the project folder with a version in the file name.
- Chris's own sections and notes. The over-delivery log's Confirmed entries, if the template has a place for activity beyond the contract.
- Ask #90's answer: the line `Project documents for ChatGPT (#90): yes` in `owner.md`. Without it, work only from dates, titles and facts in `owner.md`: build the tracker and the reminders, and do not read section contents.

## Steps
1. Frame the pack: project, report name, period, due date and where that date comes from, and the required headings copied exactly. If the template can't be found, write "UNKNOWN: headings" and ask.
2. Build the tracker: section, author, due to Chris, status (Not started, In progress, Received, Gaps sent back, Complete), and the file and version. Propose a "due to Chris" date for each section by working back from the report date, leaving room for Chris's reading, formatting and collation. Mark them as proposals; Chris sets the real dates.
3. Draft a friendly reminder for each section not yet in, a little before its date. It is a follow-up with the heading and the date, nothing else. It is a message to someone outside the business, so it goes on Chris's end-of-day "Needs your yes" list, and Adrielle sends it only after his yes, or when `AI Team/context/standing-approvals.md` covers that exact template (if that file can't be read, treat it as not covered). In test mode, list who and write no text.
4. When a section arrives, check it against its heading and any length or format limit in the template. List what is missing, as a short gap list addressed to the author. It goes on Chris's end-of-day "Needs your yes" list, and Adrielle sends it only after his yes, or when `AI Team/context/standing-approvals.md` covers that exact template (if that file can't be read, treat it as not covered). Never fix the content.
5. Collate in heading order, keeping each subcontractor's text exactly as received. Mark where Chris writes: "CHRIS TO WRITE: recommendations".
6. Facts that appear in more than one section (names, dates, counts) must agree. List any disagreement with both versions and their sources. Don't choose one.
7. Offer Confirmed over-delivery entries to Chris where the template invites them. Insert none yourself.
8. Run the readiness check: every heading present, numbering, tables, leftover comments, empty placeholders. Send formatting to Research & Data (report-format), not into the text.
9. Hand off: Chris reviews, writes the recommendations and submits (check with Chris). Tell him at once if a section is still missing when the date is near.

## Output
- The tracker, with counts: "7 sections: 5 received, 1 gaps sent back, 1 not started".
- Reminder drafts, and gap lists by author, each as a line for Chris's "Needs your yes" list.
- The collated draft, headed "DRAFT: not yet checked by Chris", with the CHRIS TO WRITE markers.
- Disagreements between sections, and the readiness check.

## Done when
Chris has one collated draft before the due date with every subcontractor section unchanged, every gap closed or listed, and the tracker showing who owes what.

## Never
- Change a subcontractor's, or Chris's, technical content.
- Write findings or recommendations, or fill a missing section with text.
- Submit, send or share a draft outside the business.
- Send a reminder or a gap list to a subcontractor without Chris's yes or a standing approval for that exact template.
- Read section contents before Chris has answered ask #90.
- Show a draft as final.
