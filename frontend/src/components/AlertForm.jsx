import React, { useState } from "react";
import { apiPost } from "../services/api";

export default function AlertForm({ onCreated }) {
  const [source, setSource] = useState("monitor");
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  async function submit(e) {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const a = await apiPost("/alerts/", { source, message });
      setMessage("");
      onCreated?.(a); // callback to parent list
    } catch (err) {
      setError(err.message || "Failed to create alert");
    } finally {
      setLoading(false);
    }
  }

  return (
    <form onSubmit={submit} style={{ display: "flex", gap: 8 }}>
      <input
        value={source}
        onChange={(e) => setSource(e.target.value)}
        placeholder="source"
      />
      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="alert message"
      />
      <button disabled={loading}>
        {loading ? "Adding..." : "Add Alert"}
      </button>

      {error && <span style={{ color: "red" }}>{error}</span>}
    </form>
  );
}
