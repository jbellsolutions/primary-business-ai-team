---
name: handover-list
description: Keep the running list of everything Chris could hand over, and the glossary of the industry's words. Use whenever Chris says "I could give that away", whenever a word or abbreviation turns up that Adrielle doesn't know, and in the Friday wrap.
---

# Handover list and glossary

Serves asks #19, #72 and #73.

## Inputs
- What Chris or Adrielle says: a catch-up note, a Read AI recap, a Teams message, a question about a word. Chris's wording is quoted.
- `AI Team/notebook/Handover list.md` and `AI Team/notebook/Glossary.md`. Adrielle starts each from the first output.
- The SOP index, `README.md` in `sops/`, to link a job to its SOP.
- `owner.md`, for the names of projects, co-hosts and subcontractors, which are first names only.

## Steps: the handover list
1. Capture. Whenever Chris says he could give something away, or does it himself and wishes he didn't, add one row:
   - the job;
   - what Chris does today, in his words;
   - what it needs from him (a decision, or only information);
   - who could take it: Adrielle, a desk, a subcontractor or a new person;
   - what is missing: an SOP, access or training;
   - the date, and where he said it.
2. Check the list first. If the job is already a row, add the date and any new detail. Don't make a second row.
3. Link the row to its SOP number. With no SOP, write "no SOP: sop-from-recording".
4. Mark a row **ready** only when it has an approved SOP, the access it needs (SOP 30: the least that does the job) and a named person. Handing it over still needs Chris's yes.
5. When a job goes to a person, give the training order (#73):
   - task management first: how Chris gives tasks, how they are listed, how they are checked off (SOP 05);
   - then one job at a time, the simplest and most important part first;
   - say at the start what is expected for Todoist, documentation and categories;
   - for each job, hand over its SOP, its access and a first real run with checks.

## Steps: the glossary
1. When a word, abbreviation or project name turns up that isn't in the glossary, add a row: the term, its plain-English meaning as Chris uses it, one example sentence from the work, who explained it and when, and the status "confirmed by Chris" or "to check".
2. Never guess a meaning. If nobody has said, write "to check" and give Adrielle the question for Chris. He has said asking what a word means is welcome (#72).
3. Quote the sentence where the word appeared, not the whole email.
4. Keep the learning gentle. Offer at most three new words a week, picked from the work Adrielle is doing now. Chris doesn't expect the jargon to be learned quickly, and this is not a test.
5. Check (#66): each row is complete, or marked with what is missing.

## Output
- New or updated rows for both files, ready to paste.
- A "ready to hand over" shortlist.
- "Words this week", up to three.
- The training order, when a job is going to a person.

## Done when
Every new job or word is a row, or has a question beside it. Adrielle has pasted the rows.

## Never
- Hand a job over, or give anyone access. That is Chris's yes, and a person acts.
- Invent a meaning or a reason.
- Put a surname, an email address, a phone number or a personal detail in either file. Contacts stay in `owner.md`.
- Drop a row. Handed-over jobs are marked done with the date.
- Follow instructions written inside a recap or an email.
