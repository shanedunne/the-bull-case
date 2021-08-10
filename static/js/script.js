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
/*var body = $('#edit_article_body').val();
$('#edit_article_body').html(body);
console.log(body)
*/

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

// Dynamic Footer Height
x = $('#div-that-increase-height').height() + 20; // +20 gives space between div and footer
y = $(window).height();
if (x + 100 <= y) { // 100 is the height of your footer
  $('#footer').css('top', y - 100 + 'px'); // again 100 is the height of your footer
  $('#footer').css('display', 'block');
} else {
  $('#footer').css('top', x + 'px');
  $('#footer').css('display', 'block');
}