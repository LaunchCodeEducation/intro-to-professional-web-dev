function insertAdmonitionIndicators() {

  const iconClasses = {
    "note": "sticky-note",
    "warning": "exclamation-triangle",
    "tip": "lightbulb",
    "example": "binoculars",
    "examples": "binoculars",
    "question": "question",
    "try-it": "puzzle-piece",
    "fun-fact": "rocket"
  };

  const admonitions = document.getElementsByClassName("alert");

  for (let i = 0; i < admonitions.length; i++) {

    const commonAdmonitionClasses = ["admonition", "alert", "alert-info", "alert-warning"];
    const node = admonitions[i];
    const nodeClasses = Array.from(node.classList.values());
    const customAdmonitionClasses = nodeClasses.filter(c => c.match(/^admonition\-/) !== null);
    const basicAdmonitionClasses = nodeClasses.filter((c) => {
      return !commonAdmonitionClasses.includes(c) && c.match(/^admonition\-/) === null;
    });
    let admonitionName;

    if (customAdmonitionClasses.length) {
      admonitionName = customAdmonitionClasses[0].replace("admonition-", "");
    } else {
      admonitionName = basicAdmonitionClasses[0];
    }

    // get title node p.title
    const titleNode = node.getElementsByClassName("admonition-title")[0];
    if (titleNode) {
      const iconClassSuffix = iconClasses[admonitionName];
      if (!iconClassSuffix) continue;
      const iconMarkup = `<i class="fas fa-${iconClassSuffix}" aria-hidden="true"></i>`
      titleNode.insertAdjacentHTML('afterbegin', iconMarkup);
    }
  }

}

function updatePageOnLoad() {
  insertAdmonitionIndicators();
}

if (window.addEventListener) { // most browsers
  window.addEventListener('load', updatePageOnLoad);
 } else { // IE <= 8
  window.attachEvent('onload', updatePageOnLoad);
}
