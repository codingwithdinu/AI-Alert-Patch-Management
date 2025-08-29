import React, { useEffect, useState } from "react";
import { apiGet, apiPatch, apiPost } from "./services/api";
import AlertForm from "./components/AlertForm";
import AlertList from "./components/AlertList";
import PatchForm from "./components/PatchForm";
import PatchList from "./components/PatchList";

export default function App() {
  const [alerts, setAlerts] = useState([]);
  const [patches, setPatches] = useState([]);

  async function refresh() {
    setAlerts(await apiGet("/alerts/"));
    setPatches(await apiGet("/patches/"));
  }

useEffect(() => {
  fetch("http://127.0.0.1:8000/patches")
    .then(res => res.json())
    .then(data => setPatches(data));
}, []);


  async function changeAlertStatus(id, status) {
    await apiPatch(`/alerts/${id}`, { status });
    refresh();
  }
  async function markDeployed(id) {
    await apiPost(`/patches/${id}/deployed`, {});
    refresh();
  }

  return (
    <div style={{ padding: 16 }}>
      <h2>AI Alert & Patch Dashboard</h2>

      <h3>Create Alert</h3>
      <AlertForm onCreated={refresh} />
      <AlertList alerts={alerts} onStatus={changeAlertStatus} />

      <h3>Schedule Patch</h3>
      <PatchForm onCreated={refresh} />
      <PatchList patches={patches} onDeploy={markDeployed} />
    </div>
  );
}
