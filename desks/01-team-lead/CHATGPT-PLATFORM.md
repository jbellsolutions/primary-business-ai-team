# How this team uses ChatGPT, and what to check

The team is built from ordinary ChatGPT features. This page says which ones it relies on, how sure we are of each, and what to do if one isn't on your plan. Everything here gets checked again at install: see the **Check** at the end of each step in [START-HERE](START-HERE.md).

## Why ChatGPT

- Chris already uses ChatGPT, and Adrielle uses it every day.
- The business runs on Microsoft 365, and ChatGPT connects to Outlook, Teams and OneDrive/SharePoint, with each person signing in to their own account. Nobody shares a login or a computer.
- Chris asked for the assistant to "learn how to use ChatGPT and do the plugins" and set up automation. This package is that, written down so it lasts.

## The building blocks

| Feature | How the team uses it | How sure | If it's not on your plan |
|---|---|---|---|
| **Projects** (instructions + files + chats) | One project per desk. The desk's instructions are its charter's Profile | Long-standing feature | Use one chat per desk, with the instructions pasted at the top |
| **Apps / connectors:** Outlook email, Outlook calendar, Teams, SharePoint/OneDrive | Read and search Chris's and the admin inbox's mail, calendars and Teams chats, each through the person's own sign-in | Documented as read-only by university IT guides (2026). OpenAI's help pages say some actions need a Microsoft Entra administrator to grant Graph permissions, and that a workspace admin can limit apps to read actions. Chris is the Microsoft 365 admin | Paste or forward the email, invite or message into the chat |
| Connectors don't send | Every outward message is a draft that a person sends | Third-party guide; it's also the design | n/a |
| **Skills** (saved, reusable instructions) | Each `skills/<name>/SKILL.md` becomes a skill | Third-party guides and OpenAI's changelog; Record & Replay (show it once, then reuse) was on macOS first | Keep the `skill-*.md` files in the project. The instructions say "follow skill-<name>" |
| **Scheduled tasks** | Each `routines/*.prompt` becomes a scheduled task, created paused | Third-party guide citing OpenAI docs: web tasks can use apps and skills; desktop tasks need the computer awake and the app open | A saved prompt, "Run <name>", that Adrielle runs at that time |
| **Todoist** app | Desks propose tasks; Adrielle adds them | **Not confirmed** | Desks give one task per line; paste into Todoist's quick add |
| **Read AI** app | Meeting recaps become tasks (later desk 90) | **Not confirmed** | Paste the Read AI recap into the Team Lead chat |
| **Project files** | Each desk's files. The compact downloads (15 files at most, plus `owner.md` and `routines-on.md`) fit every paid plan | Third-party guides citing OpenAI (checked 2026-10-28): Plus about 20 to 25 files per project, Business and Pro 40, and 10 files per upload. OpenAI's own pages disagree on the Plus number | The full `desks/` folders (up to 36 files) need Business or Pro |
| **Memory** | Desks remember corrections | Plan-dependent | Corrections go into `owner.md` or the SOP, then get re-uploaded |
| **Shared projects** | Not relied on. Chris and Adrielle each have their own desks | Plan-dependent | n/a |

## Limits we design around (ChatGPT's, not ours)

- **It reads; people act.** No desk sends an email, books, pays, posts or saves into a business system. Adrielle or Chris does the last click, every time. This is how Chris wants it: "to free up time for me, not to add time for me" means getting it right before it reaches him, not acting without him.
- **No real-time triggers.** A scheduled task runs at its time; it doesn't wake on a new email. The start-of-day and end-of-day tasks cover the day. A later milestone can add an instant trigger if ChatGPT offers one.
- **Create every task on the web, not as a desktop task.** Tasks made at chatgpt.com run in the cloud, so they run even when a computer is off. A desktop task needs the computer awake and the app open. Adrielle's tasks are timed inside her working day so she's there to act on them. Her hours sit in `owner.md`, and Step 8 moves any WHEN that falls outside them.
- **A cap on active scheduled tasks, set by plan.** OpenAI's help page (checked 2026-10-27) gives:

  | Plan | Active scheduled tasks |
  |---|---|
  | Go | 3 |
  | Plus | 5 |
  | Business and Edu | 10 (one FAQ line on the same page says 15) |
  | Pro and Enterprise | 15 |

  At the cap, ChatGPT won't create a new task or resume a paused one. Other rules on the same page:
  - A task can't run more than once an hour.
  - A task left unattended may pause itself, so the Friday SOP gap check also reads the Scheduled page for anything paused that should be on.

  Chris's account needs 2 tasks. Adrielle's needs:

  | Milestone | Tasks on Adrielle's account |
  |---|---|
  | M1 | 3 |
  | M2 | 8 |
  | M3 | 10 |
  | M4 | 12 |

  This is ChatGPT's limit, not the design: **the jobs stay and the tasks merge.** A merge only ever joins routines of **the same desk**, so the merged task lives in that desk's own project and has that desk's skills, SOPs and files. Its instruction says: "Follow each of these routine instructions in turn, on the days given. Each one keeps its own switch check and gives its own status line."
  - **Business (10):** two merges at M4.
    - **Growth weekly** (06, Mondays at 9:53 AM): the Deadlines check every Monday, plus the Funding and tender radar on the first Monday of the month.
    - **Office weekly** (07, Tuesdays at 9:41 AM): the Bills and vehicle check and Xero coding prep.

    That leaves 10.
  - **Plus (5):** from M2.
    - **Ops end of day** (01): also runs the SOP gap check on Fridays.
    - **Workshops & Travel daily** (03, weekdays at 2:43 PM): the Travel-day pack and Post-workshop follow-up, plus the Workshop pipeline on Mondays.
    - **Office weekly** (07), as above.
    - **Content weekly** (04, Mondays at 11:07 AM): Farmer post drafts, plus the Website check on the first Monday of the month.
    - **Growth weekly** (06), as above.

    That is 4 tasks at M2 and 5 at M3. At M4 it would be 6, so Ops end of day becomes a saved prompt, "Run Ops end of day", which Adrielle runs herself at the end of her day.

  The Team Lead writes the merged tasks into `team-registry.md` and keeps each routine's own name in `routines-on.md`. A job is never dropped to fit the cap.
- **Files don't update themselves.** When `owner.md`, `routines-on.md` or an SOP changes in `AI Team/`, Adrielle replaces the copy in each desk's project files. The Team Lead reminds her which ones.

## Plans

Check the current plan page at openai.com. Each person needs their own account on a plan with Projects, apps and scheduled tasks. ChatGPT Business, with a seat each, keeps both accounts in one workspace with admin controls. **Chris decides; the desks never buy or upgrade anything.**
