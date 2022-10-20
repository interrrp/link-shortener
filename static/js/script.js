const shortenForm = document.getElementById("shorten-form");
const info = document.getElementById("info");

shortenForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const data = {
    url: document.getElementById("shorten-form__url").value,
  };

  fetch("/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((res) => res.json())
    .then((data) => {
      if (data.error) {
        info.innerText = data.error;
      } else {
        const url = `${window.location.origin}/${data.id}`;

        info.innerHTML = `<a href="${url}" target="_blank">${url}</a>`;
      }
    });
});
