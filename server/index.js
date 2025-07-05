const express = require('express');
const fs = require('fs');
const app = express();
const PORT = 3000;

app.use(express.json());
app.use(require('cors')());

app.post('/webhook', (req, res) => {
  const { title, url, timestamp } = req.body;

  console.log(`${title}\n    ↳ ${url} @ ${timestamp}`);

  const logLine = JSON.stringify({ title, url, timestamp }) + "\n";
  fs.appendFileSync("notifications.log", logLine, "utf8");

  res.status(200).json({ status: "received" });
});

app.listen(PORT, () => {
  console.log(`Webhook server running at http://localhost:${PORT}/webhook`);
});
