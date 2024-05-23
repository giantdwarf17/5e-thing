import { marked } from "https://cdn.jsdelivr.net/npm/marked/lib/marked.esm.js";

// Get all elements with the class name 'md'
var md = document.getElementsByClassName('md');

// Iterate over each element and modify its innerHTML
for (var i = 0; i < md.length; i++) {
  var currentContent = md[i].innerHTML;
  md[i].innerHTML = marked.parse(currentContent);
}
