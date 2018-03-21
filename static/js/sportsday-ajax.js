$('#likes').click(function(){
    var actid;
    actid = $(this).attr("data-actid");
    $.get('/sportsday/like/', {activity_id: actid}, function(data){
        $('#like_count').html(data);
        $('#likes').hide();
    });
});
