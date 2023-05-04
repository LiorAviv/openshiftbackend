const express = require("express");
const cors = require("cors");
const app = express();
const PORT = 8000;
app.use(cors());
app.get("/getlocations", (req, res) => {
  console.log("lolo")
  res.status(200);
  res.send([
    { id: 1, lat: 36.4117, lon: 35.0818 },
    { id: 2, lat: 37.2799, lon: 37.1297 },
    { id: 3, lat: 38.2799, lon: 37.1297 },
  ]);
});
app.listen(PORT, (error) => {
  if (!error)
    console.log(
      "Server is Successfully Running, and App is listening on port " + PORT
    );
  else console.log("Error occurred, server can't start", error);
});
