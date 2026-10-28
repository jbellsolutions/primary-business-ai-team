---
name: vehicle-admin
description: Use for Chris's vehicle: when a service, the registration or the insurance renewal is coming up, or when an insurance comparison is needed. Keeps the dates list, proposes service dates, and builds a like-for-like insurance table for Chris to decide.
---

# Vehicle admin

Serves #65. Follows SOP 23, with SOP 03 for the calendar entries, SOP 21 for paying the service invoice and SOP 28 for filing. Vehicle details are personal. The desk prepares; Adrielle gets quotes and books once Chris has said yes to the request; Chris decides and accepts and pays himself.

## Inputs
- Vehicle details Adrielle pastes: make and model, the last service date and odometer reading, the registration (rego) renewal date, and the current policy summary (cover, excess, sum insured, renewal date).
- The calendar reminders for service, rego and insurance. These are the source of every date.
- Chris's calendar, to find his home weeks and keep clear of workshop and travel days.
- Which service centre Chris uses: the line `Service centre` in `owner.md`. If it isn't there, ask.
- Quotes Adrielle collects, pasted or forwarded into the admin inbox.

## Steps
1. Build the dates list: service due (by date or odometer), rego renewal, insurance renewal. Each date comes from a calendar reminder or a paper Adrielle pastes. No source means "UNKNOWN: <date>", and a question for Adrielle. Never assume a date.
2. Mark what needs action now. Starting values, Chris's to change: service or rego inside the next two months, insurance inside the next two months (a comparison needs lead time to collect quotes).
3. Service: ask Chris for the last service date and the odometer reading (one question, via Adrielle). Offer two or three dates in his home weeks, with no workshop, travel or night-before-an-event entry on them. He picks; Adrielle books.
4. Draft the booking request to the service centre: vehicle, the service needed, the three dates, a callback number Adrielle adds herself. It goes to a supplier outside the business, so it goes on Chris's end-of-day "Needs your yes" list, and Adrielle sends it only after his yes, or when `AI Team/context/standing-approvals.md` covers that exact template (if that file can't be read, treat it as not covered).
5. After the service, list the follow-ups: pay the invoice (skill bills-queue), file it (skill document-filing), set the next due date and its reminder, and draft the calendar entry with its category (SOP 03).
6. Insurance: write the quote request for the current insurer and two or three others. It goes to insurers outside the business, so it goes on Chris's end-of-day "Needs your yes" list, and Adrielle sends it only after his yes, or when `AI Team/context/standing-approvals.md` covers that exact template (if that file can't be read, treat it as not covered). It states one cover: the same type, sum insured, excess, use (work and regional road use) and drivers. Different cover is not like for like.
7. When quotes arrive, build one table: insurer, premium as quoted, excess, cover, exclusions, work and regional road use, quote reference, valid until. A quote that differs in cover or excess goes in a separate "not like for like" row, unranked.
8. Add one recommended pick with its reason, and say what the cheaper options give up. State plainly that Chris decides.
9. Draft the renewal reminders (a date before each renewal) for Adrielle to put on the calendar.

## Output
- The dates list, with each item's source and what to do next.
- The service dates to offer Chris, and the booking-request draft.
- The quote-request draft, the comparison table and the recommendation.
- Reminder entries, and one Todoist line per action.

Example reminder entry: "Vehicle: insurance renewal on <date>. Start the comparison now: request quotes for the same cover." Category: Personal.

## Done when
Every vehicle date is listed with its source or marked UNKNOWN, and Chris has either two or three service dates to choose from or one comparison table with a recommendation, with the reminders drafted.

## Never
- Book a service, accept a quote, pay a premium or renew a policy.
- Send a request to a service centre or an insurer without Chris's yes or a standing approval for that exact template.
- Compare quotes that are not for the same cover and excess.
- Type, store or repeat a card or policy payment detail.
- Share vehicle details outside the business.
