// Tiny MCE Editor - Post Article
tinymce.init({
  selector: '#article_body',
  toolbar: 'undo redo',
  content_css: 'static/css/textarea.css',
  menubar: 'file edit view'
});

// Tiny MCE Editor - Post Comment
tinymce.init({
  selector: '#comment-body',
  toolbar: '',
  content_css: 'static/css/textarea.css',
  menubar: ''
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