const API_BASE = "http://127.0.0.1:8000";  // FastAPI backend

async function handleResponse(res) {
  if (!res.ok) {
    const text = await res.text();  // backend ka error text
    throw new Error(`API Error ${res.status}: ${text}`);
  }
  return res.json();
}

export async function apiGet(path) {
  const res = await fetch(`${API_BASE}${path}`);
  return handleResponse(res);
}

export async function apiPost(path, data) {
  const res = await fetch(`${API_BASE}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return handleResponse(res);
}

export async function apiPatch(path, data) {
  const res = await fetch(`${API_BASE}${path}`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return handleResponse(res);
}
