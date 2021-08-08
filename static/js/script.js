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
