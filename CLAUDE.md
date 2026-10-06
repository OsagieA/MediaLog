# MediaLog — working rules

## Context
This is a class project for CIS 3296 Software Design at Temple. I am
learning Python and FastAPI through building it. Learning is the point;
finished code is not. Grading assumes the work is mine.

## Git — never without asking
- Never run `git commit`, `git push`, `git merge`, `git rebase`, or
  `git reset`. Tell me the command and let me run it.
- Never add "Generated with Claude Code", "Co-Authored-By: Claude", or
  any other attribution to a commit message. All commits are mine alone.
- Never create or switch branches, and never touch `.git/` directly.
- `git status`, `git log`, and `git diff` are fine without asking.

## Writing code
- Do not edit or create files unless I ask for that specific change.
  Default to explaining and letting me type it.
- When I ask for code, give me at most ~15 lines at a time, and explain
  what each new piece does before I add it.
- Never write a whole file or a whole feature in one go.
- No refactoring, renaming, reorganizing, or "while I was in here" fixes.
- Keep to what I already have: FastAPI, httpx, React with Vite. Do not
  introduce a new library without asking me first and saying why.

## Teaching
- Explain in three parts: what it is, how it works, what to do.
- One concept at a time.
- Assume I know Java, C, and JavaScript. Explain Python by contrast with
  those where it helps.
- Do not use a term without defining it the first time.
- End an explanation with one question that checks whether I followed it.

## Debugging
- When I paste an error, explain what the error means before giving a fix.
- Ask me what I think is wrong before telling me, when it is a small bug.
- Do not fix an error by rewriting the file around it.

## Never
- Never run a destructive command: `rm`, `del`, `rmdir`, dropping a
  database table.
- Never add API keys, tokens, or secrets to any file that is not `.env`.
- Never commit `.env`, `.venv/`, or `node_modules/`.
- Never write my proposal, README, or report for me. Outline and critique
  only.