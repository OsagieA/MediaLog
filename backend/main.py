import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

ANILIST_URL = "https://graphql.anilist.co"

QUERY =  """
query ($search: String) {
  Page(perPage: 5) {
    media(search: $search, type: ANIME) {
      id
      title {
        romaji
        english
      }
    }
  }
}
"""

@app.get("/")
def home():
    return {"message": "backend is now running"}

@app.get("search")
def search (q: str):
    response = httpx.post(
        ANILIST_URL,
        json={"query": QUERY, "variables": {"search": q}},
    )
    data = response.json()

    results = []
    for show in data["data"]["Page"]["media"]:
        results.append({
            "id": show["id"],
            "title": show["title"]["english"] or show["title"]["romaji"],
        })

    return results