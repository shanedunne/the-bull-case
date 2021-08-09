// Tiny MCE Editor - Post Article
tinymce.init({
  selector: '#article_body',
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
