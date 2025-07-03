import React, { useState } from "react";

function App() {
  const [audio, setAudio] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => setAudio(e.target.files[0]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!audio) return;
    setLoading(true);
    const formData = new FormData();
    formData.append("audio", audio);

    const res = await fetch("http://localhost:8000/api/upload-audio", {
      method: "POST",
      body: formData,
    });
    const data = await res.json();
    setResult(data);
    setLoading(false);
  };

  return (
    <div style={{ maxWidth: 600, margin: "2rem auto", fontFamily: "sans-serif" }}>
      <h2>Carbon Footprint Tracker (Voice)</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" accept="audio/*" onChange={handleFileChange} />
        <button type="submit" disabled={loading}>
          {loading ? "Processing..." : "Upload & Analyze"}
        </button>
      </form>
      {result && (
        <div style={{ marginTop: "2rem" }}>
          <h4>Transcription:</h4>
          <p>{result.transcription}</p>
          <h4>Activities & Emissions:</h4>
          <ul>
            {result.emissions.map((item, idx) => (
              <li key={idx}>
                {item.activity}: <b>{item.emission} kg CO₂e</b>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
