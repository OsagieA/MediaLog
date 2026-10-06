import { useState } from "react";

export default function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  async function handleSearch(event) {
    event.preventDefault();
    const response = await fetch(
      `http://localhost:8000/search?q=${encodeURIComponent(query)}`
    );
    const data = await response.json();
    setResults(data);
  }

  return (
    <div>
      <h1>MediaLog</h1>
      <form onSubmit={handleSearch}>
        <input
          value={query}
          onChange={(event) => setQuery(event.target.value)}
          placeholder="Search anime"
        />
        <button type="submit">Search</button>
      </form>
      <ul>
        {results.map((show) => (
          <li key={show.id}>{show.title}</li>
        ))}
      </ul>
    </div>
  );
}