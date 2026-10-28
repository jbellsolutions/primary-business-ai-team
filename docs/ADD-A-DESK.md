# Adding a desk or a skill yourselves

The team is built so Adrielle can extend it, with Chris approving. This is how.

## A new skill (a job you do more than twice)

1. Do the job once with the Team Lead, talking it through as you go. Or record a training session with Chris, and paste in the transcript or recap.
2. Ask the Team Lead: **"Turn this into a skill. Use the skill format in `skill-ask-ledger.md`."** It writes the frontmatter, the inputs, the steps, the output, "done when" and "never".
3. Read it. Is it short, and true to how you actually do it? Fix anything that isn't.
4. Chris approves it. Then save it as a ChatGPT skill, or add it to the desk's project files, and record it in the ask ledger.
5. If the plan offers **Record & Replay**, Adrielle can show ChatGPT the steps on screen once, and it saves them as a skill. Check the result the same way.

## A new scheduled task

1. Copy any file in `routines/` and change the header (NAME, OWNER, ACCOUNT, WHEN, MILESTONE) and the job below the `---` line. Keep the five fixed lines at the top: the switch check, test mode, isolation guard, lean run and run log.
2. Use odd minutes, Melbourne time, and one job per task.
3. Create it paused. Test it once with `<NAME>: test` in `routines-on.md`, then turn it on only on Chris's yes.

## A new desk

Use a new desk only when a job needs different instructions or different apps. Otherwise, add a skill to an existing desk.

1. Copy `agents/03-workshops-and-travel.md` as a model. Fill in every section, especially the **Operating contract**. The row "Only writer of" must not overlap any other desk: one writer per record.
2. Add it to `PROJECT_CHARTER.md` §4 and §7, and to `manifest.json`.
3. Run `python3 scripts/build_desks.py`, then follow START-HERE Step 6 for that desk.

## The reserved desks

`agents/90-*` to `agents/93-*` are written down but not built. Each one says what has to be true before it's worth building, for example a Read AI or Teams recap source, or a social account set up properly. When that's true, ask Justin's team, or follow the steps above.
