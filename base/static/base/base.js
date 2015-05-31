$(document).ready(function() {
    $(document).on("click",".logout-button",function(){
         var form = $(this).closest("form");
         console.log(form);
         form.submit();
       });
    $(document).on("click",".login-button",function(){
         var form = $(this).closest("form");
         console.log(form);
         form.submit();
       });
});