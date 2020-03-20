(function(){
  var jquery_version = '3.3.1';

  var site_url = 'http://127.0.0.1:8000'
  // var site_url = 'https://3f6ad53c.ngrok.io/';
  var static_url = site_url + 'static/';
  var min_width = 100;
  var min_height = 100;

    function bookmarklet(msg) {
        // Загрузка CSS-стилей.
        var css = jQuery('<link>');
        css.attr({
            rel: 'stylesheet',
            type: 'text/css',
            href: static_url + 'css/bookmarklet.css?r=' +
            Math.floor(Math.random()*99999999999999999999)
            });
        jQuery('head').append(css);
        // Загрузка HTML.
        box_html = '<div id="bookmarklet"><a href="#"id="close">&times;</a><h1>Select an image to bookmark:</h1><divclass="images"></div></div>';
        jQuery('body').append(box_html);
        // Добавление скрытия букмарклета при нажатии на крестик.
        jQuery('#bookmarklet #close').click(function(){
            jQuery('#bookmarklet').remove();
        });
    }

  // Check if jQuery is loaded
  if(typeof window.jQuery != 'undefined') {
    bookmarklet();
  } else {
    // Check for conflicts
    var conflict = typeof window.$ != 'undefined';
    // Create the script and point to Google API
    var script = document.createElement('script');
    script.src = '//ajax.googleapis.com/ajax/libs/jquery/' +
      jquery_version + '/jquery.min.js';
    // Add the script to the 'head' for processing
    document.head.appendChild(script);
    // Create a way to wait until script loading
    var attempts = 15;
    (function(){
      // Check again if jQuery is undefined
      if(typeof window.jQuery == 'undefined') {
        if(--attempts > 0) {
          // Calls himself in a few milliseconds
          window.setTimeout(arguments.callee, 250)
        } else {
          // Too much attempts to load, send error
          alert('An error ocurred while loading jQuery')
        }
      } else {
          bookmarklet();
      }
    })();
  }
})()