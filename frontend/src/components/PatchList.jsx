import React from "react";

export default function PatchList({ patches, onDeploy }) {
  return (
    <table border="1" cellPadding="6" style={{ width:"100%", marginTop:12 }}>
      <thead>
        <tr><th>ID</th><th>Product</th><th>Version</th><th>CVE</th><th>Scheduled</th><th>Deployed</th><th>Action</th></tr>
      </thead>
      <tbody>
        {patches.map(p => (
          <tr key={p.id}>
            <td>{p.id}</td><td>{p.product}</td><td>{p.version}</td><td>{p.cve || "-"}</td>
            <td>{p.scheduled_at ? new Date(p.scheduled_at).toLocaleString() : "-"}</td>
            <td>{p.deployed ? "✅" : "🕒"}</td>
            <td>{!p.deployed && <button onClick={() => onDeploy(p.id)}>Mark Deployed</button>}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
