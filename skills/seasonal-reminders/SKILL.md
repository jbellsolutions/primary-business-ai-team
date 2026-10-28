---
name: seasonal-reminders
description: Build and keep the grain-storage seasonal calendar from the material Chris gives it, and turn the entries that are due into reminder posts. Use when the calendar is missing or out of date, and when the weekly drafts routine finds an entry due.
---

# Seasonal reminders

Serves #40 ("it's coming into a time of year that they need to do a certain task around their grain storage, send them a reminder") and #37.

## Inputs
- `seasonal-calendar.md`: the calendar, a Project file. Its master copy is `AI Team/projects/_content/seasonal-calendar.md`, which Adrielle saves and re-uploads when it changes.
- The material Chris gives it: pages on the business website, workshop slides, past posts, or his spoken walk-through (dictated, then pasted by Adrielle). Pages on the project website (names in `owner.md`) are the project's material, not Chris's own, so the funder acknowledgement check applies to anything taken from them.
- `owner.md`: the regions, crops and storage types his projects cover.
- `post-log.md`: which reminders already went out this season.

## Steps
1. **No calendar yet?** Don't write one from general knowledge. Timing differs by region, crop and storage type, and a wrong date in a reminder costs Chris's trust. Ask Adrielle for Chris's material, or for a spoken walk-through of the year.
2. **Extract rows.** One row per job farmers do, with these columns:
   - ID, and What farmers need to do.
   - When: months, or a trigger such as "before the grain goes in".
   - Applies to: region, crop, storage type.
   - Remind in: when the reminder should go out.
   - Source: the page, slide or Chris's words, with the date.
   - Status: `to check` or `confirmed`.
3. **Every new row starts as `to check`.** A row becomes `confirmed` only when Chris says so about that row, in his words.
   - Ask about gaps one question at a time, for example: "When does <job> matter in <region>, and does it change by crop?"
   - Record his answer as the row's source.
4. **Give the calendar to Adrielle** as one table to save over the master and re-upload to this Project. Add the date of the last change.
5. **Find what is due.** A confirmed row is due when its "Remind in" window opens before the next run of the weekly drafts routine and `post-log.md` shows no reminder for it this season. If `Remind in` is empty, propose the start of the "When" window and mark it `to check`.
6. **Draft each due reminder** with farmer-post, using the row as the source.
   - Say what to do, by when and why, in Chris's words.
   - If the row's source is the project website, add the funder line as farmer-post step 8 says.
   - One row, one idea, one post.
   - Never more drafts than the routine's cap.
7. **Due but not confirmed:** don't draft. Put it on the list of questions for Chris: "Row <ID> falls due before the next run and isn't confirmed. Is the timing right for <region>?"
8. **Review the calendar once a year,** at the quiet time Chris names. Ask him to read it and say which rows are wrong, missing or retired. Retire a row with a date; never delete it.

## Output
- The calendar table (new or changed rows highlighted) for Adrielle to save.
- The due reminders as farmer-post drafts, each tagged with its row ID.
- A list of questions for Chris, one per line.

## Done when
Every drafted reminder comes from a `confirmed` row with a source, and Adrielle has the latest calendar to save.

## Never
- Invent a date, month, product, rate, dose or practice, or copy one region's timing to another.
- Treat a `to check` row as true.
- Remind about anything fumigation- or chemical-related except in Chris's words, checked against the label.
- Delete a row, or send a reminder by email or text.
