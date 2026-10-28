---
name: expense-record
description: Use when Chris has paid for something that is claimed back, a trip has ended, or the week's reporting-sheet entries are due. Builds the claim-sheet rows from receipts, finds the missing ones, and fills the reporting-sheet rows from the sheet's own columns.
---

# Expense record

Serves #60 and #63. Follows SOP 22, with SOP 28 for the receipt filing and SOP 20 for matching to Xero. The desk builds rows; Adrielle checks the totals, Chris approves the sheet, and Adrielle submits.

## Inputs
- Receipts from the admin inbox, Teams, and photos Adrielle pastes or describes. Read them only if `owner.md` has the line `Receipts for ChatGPT: yes`; without it, say "NO_CLIENT_SOURCE: Chris's OK for receipts" and ask Adrielle to get his yes.
- The claim sheet: Adrielle pastes its header row and any existing rows. Without a header row the columns are UNKNOWN; the plain SOP 22 columns are date, what, who was paid, amount, project, receipt filed.
- The reporting sheet: its header row, pasted on the run, and any entry rule Adrielle gives.
- The week's Xero export (the same paste as Xero coding prep) to match against.
- The trip folder, Chris's calendar categories, and what each project allows to be claimed (`owner.md`, or Chris's answer).

## Steps
1. Read the header rows exactly as pasted and keep their column names and order. Never add or rename a column. A header you haven't been given is "UNKNOWN: columns"; ask Adrielle to paste it.
2. For each receipt, pull out: date, who was paid, what it was, the amount as printed, the tax shown (if any), the project, and the receipt's file name.
3. Find the project from the calendar category and the trip, as in Xero coding prep. If two fit, mark Unknown and ask.
4. Check what each project allows to be claimed. If `owner.md` doesn't say, mark the row "Needs Chris".
5. List the missing receipts: a bank line or a booking with no receipt behind it. No receipt, no claim, so ask early, one question per item.
6. Match each row to a Xero line (same date, payee and amount). Mark matched or not yet seen.
7. Keep personal and business apart. A row of doubtful type is "Needs Chris".
8. Total each project by re-adding. Show the sum and the count, and say they were added twice. Tax treatment follows Xero; write a note for Chris, never a decision.
9. Reporting-sheet rows: use only the columns in the pasted header. Put each fact where the header says it goes. Leave a cell empty and flagged if the source doesn't give it; never fill it from a guess.
10. After the sheet is submitted, add a tracking line: date submitted, who it went to, when to look for the payment. Adrielle fills in the facts.

## Output
- Claim rows ready to paste, in the sheet's column order.
- Missing receipts, with the one question for each.
- Per-project totals with counts, and the "Needs Chris" items.
- Reporting-sheet rows, with empty cells flagged.
- The tracking line, and the filing suggestions for each receipt.

Example missing-receipt question, for Chris: "The <date> payment to <payee> for <amount> has no receipt. Did you keep one, or shall we ask <payee> to reissue it?" A request to the payee is a message outside the business: it goes on Chris's end-of-day "Needs your yes" list, and Adrielle sends it only after his yes, or when `AI Team/context/standing-approvals.md` covers that exact template (if that file can't be read, treat it as not covered).

## Done when
Each receipt is a row or a named gap, each row is matched or marked not yet seen, totals were added twice, and Chris has the sheet and the short "Needs Chris" list.

## Never
- Submit a claim, or write a claim as approved.
- Invent a receipt, a date, an amount or a column.
- Change a figure to make the totals agree.
- Mix personal and business spending.
