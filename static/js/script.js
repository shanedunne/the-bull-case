// Tiny MCE Editor - Post Article
tinymce.init({
  selector: '#article_body',
  toolbar: 'undo redo',
  content_css: 'static/css/textarea.css',
  menubar: 'file edit view',
  relative_urls : true,
  document_base_url : 'http://www.example.com/path1/'

});

// Tiny MCE Editor - Edit Article

// Catches article body from DB and places in editor for editing
var body = document.getElementById("edit_article_body").getAttribute("value");
var stringBody = body.toString(); 
document.getElementById("edit_article_body").innerHTML = stringBody;

tinymce.init({
  selector: '#edit_article_body',
  toolbar: 'undo redo',
  content_css: 'static/css/textarea.css',
  menubar: 'file edit view',
  relative_urls : true,
  document_base_url : 'http://www.example.com/path1/'

});

// Tiny MCE Editor - Post Comment
tinymce.init({
  selector: '#comment-body',
  toolbar: '',
  content_css: 'static/css/textarea.css',
  menubar: ''
});

