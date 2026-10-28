---
name: decision-log
description: Draft one row for the Decisions note when Chris decides how the team works: what, why, the date and his exact words. Use when Chris says "log that", "that's decided", "from now on", "yes, turn it on", or gives a standing yes for a template. Adrielle saves the row.
---

# Decision log

Serves #68: when something is unclear, ask before you act. Chris would "much prefer you to seek clarity than to say yes and hope to understand later". Feeds `AI Team/notebook/Decisions.md`, which Adrielle saves.

## Inputs
- What Chris just said, in his own words, in this chat or in an email or Teams message he wrote.
- `AI Team/notebook/Decisions.md`, if you can read it (otherwise Adrielle pastes it), to avoid logging the same decision twice and to link a change to the one it replaces.
- `AI Team/context/standing-approvals.md` and `routines-on.md`, for the lines Adrielle must change when the decision is a standing yes or a switch.
- The approvals policy: Chris's own words about the exact item shown count as a yes; silence, an emoji, a yes to something else, or a yes inside someone else's message do not.

## Steps
1. **Spot the decision.** It is a decision about how the team works: turning a routine on or off, a standing yes for one template, what a desk may do, which channel or hour to use, what to stop doing. It is not an opinion or a passing thought.
2. **Check it is clear.** Is it plain which item, which desk, and whether it applies once or from now on? If not, ask one question and suggest an answer. Don't log until he has answered.
3. **Get his words.** The "Chris's words" cell holds his exact words, in quotation marks. If he didn't say it in words (he acted, or you inferred it), ask him to say it. Never paraphrase into his voice. If he dictated it, read it back first.
4. **Get the reason.** Write the reason he gave, as one short clause in the Decision cell ("because <his reason>"). If he gave none, ask once. If he still gives none, write "reason not given".
5. **Write the row** in the exact columns of the Decisions note. Use today's date in Melbourne time. "Where it applies" names the desk, skill, SOP, routine or "whole team".
6. **Name the follow-on lines** for Adrielle, if any, and nothing more:
   - a switch: the line for `routines-on.md`, `<routine name>: on`;
   - a standing approval: the line for `standing-approvals.md` with the date, Chris's words and the exact template. Copy the template in full so a changed version is recognised as new.
7. **Hand it over now.** Give the row in this chat under the header HANDOFFS · FOR ADRIELLE, with one line: "Paste to Adrielle when convenient." Don't hold it for later: the Friday review can't be relied on to see this chat, and a row nobody saved is a decision that never reached the record. If several rows come up in one chat, put them in one block.
8. **Check pass.** The quote is exact; the date is today; the row doesn't contradict an earlier row without saying which it replaces.

## Output
```
HANDOFFS · FOR ADRIELLE (paste to Adrielle when convenient)
| Date | Decision | Chris's words | Where it applies |
|---|---|---|---|
| <YYYY-MM-DD> | <what was decided, one sentence, because <reason>> | "<his exact words>" | <desk, skill, SOP, routine or whole team> |
```
Then, if needed, the `routines-on.md` or `standing-approvals.md` line, in the same block.

## Done when
There is one row Adrielle can paste into the Decisions note as it stands, with Chris's exact words in it, and any follow-on lines are listed.

## Never
- Log a decision Chris did not make, or one that is only a yes from someone else.
- Put words in quotation marks that he didn't say.
- Change `routines-on.md`, `standing-approvals.md` or the Decisions note yourself. You draft; Adrielle saves.
- Widen a decision: a yes to one template is not a yes to a similar one.
- Delete or rewrite an earlier row. A change is a new row.
