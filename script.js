function generate() {
  const keywords = document.getElementById("keywords").value;
  const platform = document.getElementById("platform").value;
  const tone = document.getElementById("tone").value;

  fetch("/generate", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({keywords, platform, tone})
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById("caption").textContent = data.caption;
    document.getElementById("hashtags").textContent = data.hashtags;
  });
}