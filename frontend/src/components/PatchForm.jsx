import React, { useState } from "react";
import { apiPost } from "../services/api";

export default function PatchForm({ onCreated }) {
  const [product, setProduct] = useState("ubuntu");
  const [version, setVersion] = useState("22.04.5");
  const [cve, setCve] = useState("");
  const [scheduledAt, setScheduledAt] = useState("");

  async function submit(e) {
    e.preventDefault();
    const p = await apiPost("/patches/", {
      product, version, cve: cve || null,
      scheduled_at: scheduledAt ? new Date(scheduledAt).toISOString() : null
    });
    setCve(""); setScheduledAt("");
    onCreated?.(p);
  }
  return (
    <form onSubmit={submit} style={{ display:"flex", gap:8, marginTop:12 }}>
      <input value={product} onChange={e=>setProduct(e.target.value)} placeholder="product"/>
      <input value={version} onChange={e=>setVersion(e.target.value)} placeholder="version"/>
      <input value={cve} onChange={e=>setCve(e.target.value)} placeholder="CVE (optional)"/>
      <input type="datetime-local" value={scheduledAt} onChange={e=>setScheduledAt(e.target.value)}/>
      <button>Schedule Patch</button>
    </form>
  );
}
