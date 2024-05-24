import { marked } from "https://cdn.jsdelivr.net/npm/marked/lib/marked.esm.js";

document.querySelectorAll('.md').forEach((element) => {
  let currentContent = element.innerHTML;
  element.innerHTML = marked.parse(currentContent);
});

if (window.location.pathname == '/create/description') {
  let backgrounds;

  function fetchJSONData() {
    fetch("/backgrounds.json")
      .then((res) => {
        if (!res.ok) {
          throw new Error
            (`HTTP error! Status: ${res.status}`);
        }
        return res.json();
      })
      .then((data) =>
        backgrounds = data)
      .catch((error) =>
        console.error("Unable to fetch data:", error));
  }

  var background = document.querySelector("#background");

  fetchJSONData();

  background.addEventListener("change", function () {
    console.log(background.selectedIndex);
    if (background.selectedIndex == 0) {
      document.querySelector('#background_desc').innerHTML = "";
      document.querySelector('#skills').innerHTML = "";
    }

    else {
      document.querySelector('#background_desc').innerHTML = marked.parse(backgrounds['results'][background.selectedIndex - 1]['desc']);
      document.querySelector('#skills').innerHTML = backgrounds['results'][background.selectedIndex - 1]['skill_proficiencies']
    }
  });
}
