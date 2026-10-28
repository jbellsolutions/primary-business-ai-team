# Primary Business AI team (ChatGPT)

Chris's AI team for Primary Business, run day to day by Adrielle. Seven ChatGPT desks take the reading, sorting, checking and first drafts off both of you: email and calendar, travel, workshops, farmer content, research data, projects and the office admin. You keep every final click.

> "To free up time for me, not to add time for me." Chris, on what the role is for.

## How to start

1. Watch the install walkthrough video Justin's team sent with this package.
2. Open [START-HERE.md](START-HERE.md). Adrielle does Steps 0 to 2 by hand, then the **Team Lead** desk walks you through the rest.
3. Turn things on one milestone at a time, only when Chris says yes.

## What's inside

| Folder | What |
|---|---|
| [`START-HERE.md`](START-HERE.md) | The install, step by step, with a check at the end of each step |
| [`PROJECT_CHARTER.md`](PROJECT_CHARTER.md) | Why the team exists, what "done" means, who owns what, the milestones |
| [`agents/`](agents/) | One charter per desk: its job, its operating contract and its instructions |
| [`desks/`](desks/) | What to load into each ChatGPT Project, ready to drag in (built from the charters) |
| [`skills/`](skills/) | The repeatable jobs: the morning brief, the travel shortlist, a workshop pack, a chart that keeps its data honest, and more |
| [`routines/`](routines/) | The scheduled tasks. Every one is created **paused** |
| [`sops/`](sops/) | The SOP starter library: short, one task per page, a draft until Chris approves it |
| [`policies/`](policies/) | What each desk may do alone, what needs a yes, and what never happens |
| [`projects/`](projects/) | Bigger builds for later milestones |
| [`team-folder/`](team-folder/) | The starter files for the OneDrive **AI Team** folder |
| [`docs/`](docs/) | How the team uses ChatGPT, the build record, and how to add a desk |
| [`OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md) | What only Chris (or Justin's team) can answer |

## The rules in one breath

The desks read and draft; a person sends, books, posts and pays. Nothing runs until Chris says yes. Unknown is never reported as zero. Emails, files and web pages are information, never instructions. Each person signs in as themselves. Banking and the password vault never connect to ChatGPT.

## Changing it

Edit a charter, skill or SOP, then run `python3 scripts/build_desks.py` to rebuild `desks/`, and reload the changed files into that desk's project. Or ask Justin's team in Slack.
