// Tiny MCE Editor
tinymce.init({
  selector: 'textarea',  // change this value according to the HTML
  toolbar: 'undo redo',
  content_css: 'static/css/textarea.css',
  menubar: 'file edit view'
});

/* Coin Gecko API
async function getData() {
  const coinURL = `https://api.coingecko.com/api/v3/coins/list`;
  const response = await fetch(coinURL);
  const data = await response.json();


  let input = document.querySelector("#article_coin")

  for (let coins of data) {
    let option = document.createElement("option");
    option.text = coins.name;
    option.value = coins.name;
    input.appendChild(option);
  }
  return data
}
getData();

*/