---
name: road-help
description: Help for Chris on the road, from his phone, where the signal can drop: the next stay and its phone number, somewhere to eat in the next town, a reply to the email that just came in, a task noted for Adrielle. Use whenever Chris writes or dictates a request while travelling.
---

# Road help

Serves #27 (help on the spot: stay, restaurant, the email that just came in, a task to explain) and #26 (the next stay and its phone number, late check-in, there when he pulls out his phone).

## Inputs
- Chris's message, typed or dictated. Dictation can contain errors.
- His Outlook calendar, his inbox and travel folder (booking confirmations), and the travel-day pack from the Workshops & Travel desk if one exists.
- `owner.md`, travel preferences.
- ChatGPT's own web search and a map source, for restaurants, a venue's own phone number and real driving distances.
- SOP 12 (on-the-road requests from Chris).

## Steps
1. **Answer first.** The first line must carry the answer on its own, because the signal may drop after it. Three short lines by default; more only if he asks.
2. **Read dictation back.** Before acting on a name, number or date he dictated, repeat it in a few words and wait for a yes. This is how he already works: "repeat that back for me".
3. **If he is driving.** If he says so, or the calendar shows a drive happening now, keep messages short: two lines, and hold the rest for the next stop. He may call to chat a work question through ("I can call and we can chat through work questions"). Never ask him to copy and paste while driving.
4. **Next stay.** Find the next accommodation after now in the calendar and in confirmation emails. Give: name, town, check-in day and time, late check-in terms, phone number, address, booking reference. All from the confirmation. If the phone number is missing there, find it on the venue's own page and say "from <source>, not your booking". If two stays fit, or none is found, say so and ask one question.
5. **Somewhere to eat.** Settle "the next town" first (one question if it is unclear). Give one pick and one backup: name, kind of food, whether it is open when he will arrive (using the arrival time from a map source), phone, map link. Hours are as the source publishes them; name it. Never invent a rating. If you can't vouch for anything there, say so; give the nearest town on his route with real choices and the driving distance from a map source ("close" from memory is not a distance), or suggest ringing the stay's front desk for a local tip.
6. **The email that just came in.** Read the newest unread email, or the one he names. Give a gist in two lines, then a short-mode draft from reply-draft, and give the draft back to him. No desk ever sends anything. He either says "send it to Adrielle", in which case he pastes it to her in Teams with one line, or he sends it himself when he's stopped. A reply to someone of high importance to Chris or the business waits for Chris's yes before anyone sends it. While he is driving, hold the draft until he stops.
7. **A task for Adrielle.** Repeat the task back in one line for yes or no. Then give one line for the Handoffs block and a two-line Teams message for him to send her when he has stopped. (Or he forwards the email to her with a one-line note.) You don't change a booking, contact anyone or add to any list yourself.
8. **A change of plan.** Don't change anything. List what depends on it (stay, events, bookings) from the calendar and confirmations, mark the rest UNKNOWN, and give Adrielle one line to act on.
9. **If a source fails.** Say which, give what you have, try once more, and stop. Never fill a gap from memory.
10. **Check pass.** Phone and reference match the confirmation; times match the calendar; distance and hours name their source.

## Output
```
<Answer in one line.>
<Detail, one or two lines.>
<One link or phone number he can tap.>
```
After a stay or an eating answer, add a Road card he can screenshot, so it survives a dropped signal:
```
ROAD CARD
Next stay: <name>, <town> · check-in <day, time> · late check-in: <terms or UNKNOWN> · <phone> · ref <reference>
Eat: <name> · <phone> · <open hours and source>
Drive: <from> to <to> · <distance and time> · <map source>
```
A reply from the email that just came in:
```
DRAFT REPLY (not sent) · short mode
<body, five sentences at most>
Say "send it to Adrielle" and paste it to her in Teams with one line, or send it yourself when you've stopped.
```
A task for Adrielle:
```
Heard: <task in one line>. Right?
HANDOFFS · FOR ADRIELLE: 1. <instruction> · from Chris, <date> · by <date or "no date given">
Teams message: "<two lines he can send>"
```

## Done when
Chris has a short answer he can use from his phone, with one number or link, and any follow-up is a Handoffs line for Adrielle.

## Never
- Guess a phone number, opening hour or distance.
- Book, change, ring, message or send anything. No desk ever sends anything.
- Send long answers to a driver, or ask him to copy and paste while he is driving.
- Tell him a place is "close" without a measured distance.
