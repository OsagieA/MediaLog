# MediaLog

A media tracker for books, movies, shows, games, anime, and manga.
CIS 3296 Software Design, Fall 2026.

This repository is a proof of concept showing the project's stack working
together: a React frontend calls a FastAPI backend, which queries the
AniList GraphQL API and returns anime titles to display.

## Build environment

| Component | Version |
|---|---|
| Operating system | [Windows 11] |
| Python | [3.13.14] |
| Node.js | [v24.21.0] |
| pnpm | [12.9.1] |

Python is interpreted, so the backend has no compile step. The frontend
is compiled from JSX to JavaScript by Vite.

## Running it

Open two terminals, run venv in both then start the server using pnpm run dev for the front end, and uvicorn for the back. you may then visit your locally hosted medialog

### Backend

To compile all you need to do is press decode and bug, there isn't much in here currently and all thats going on is importing FastAPI 
Make sure your running Node.js ABOVE 21.11.0, other than that it wont work
must use httpx and vite!