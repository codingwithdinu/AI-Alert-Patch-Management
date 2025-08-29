import React from "react";

export default function AlertList({ alerts, onStatus }) {
  return (
    <table border="1" cellPadding="6" style={{ width:"100%", marginTop:12 }}>
      <thead>
        <tr><th>ID</th><th>Source</th><th>Message</th><th>Priority</th><th>Status</th><th>Action</th></tr>
      </thead>
      <tbody>
        {alerts.map(a => (
          <tr key={a.id}>
            <td>{a.id}</td><td>{a.source}</td><td>{a.message}</td>
            <td>{a.priority}</td><td>{a.status}</td>
            <td>
              {a.status !== "closed" && (
                <button onClick={() => onStatus(a.id, "closed")}>Close</button>
              )}
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
