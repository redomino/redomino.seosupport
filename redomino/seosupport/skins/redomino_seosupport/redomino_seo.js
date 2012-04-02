/* With this javascript you prevent description longer than 156 chars.
 * Description are considered mandatory.
 *
 * The title must have the following format:
 * DOCUMENT TITLE &mdash; PORTAL TITLE
 *
 * Document titles max size: 63 - len(' &mdash; PORTAL TITLE')
 *
 * */

(function ($){

  $(document).ready(function(){
    var title_text = $('title').text();
    var index_title = title_text.lastIndexOf('—'); 
    var portal_title_len = title_text.substr(index_title-1).length;
    
    $("div#archetypes-fieldname-title input").load(function () {
          var max = 63 - portal_title_len;
          this.setAttribute("maxlength", max);
        }).load();


    var check_title = function(event_type) {
      $("div#archetypes-fieldname-description textarea")[event_type](function () {
          var max = 156;
          var node = this;
          if(node.value.length > max) {
              node.value = node.value.substring(0, max);
              }
          });
    }


    $(document).ready(function () {(function(event_type) {check_title(event_type)})('keyup')});

    $(document).ready(function () {(function(event_type) {check_title(event_type)})('click')});

//    $('form').submit(function() {
//        var description = $('#description');
//        var description_len = description.val().length;
//        if (description_len > 0) {return true;}
//        $('#archetypes-fieldname-description').addClass('error');
//        return false;
//        
//    })
});

})(jQuery);

