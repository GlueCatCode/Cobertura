function setSpace(space) {
    refreshSpace(space);    
}

function refreshSpace(space) {
    $('#loader-' + space.script).show();
    $.get('render/' + space.script, function(data){
        $('#loader-' + space.script).hide();
        $('#space-' + space.script).html(data);
        setTimeout(function(){ refreshSpace(space) }, space.refresh * 1000);
        refreshTagsCobertura();
    });
}

function setTimeLeft(comp){
    let timeleft = $(comp).attr('time');
    $(comp).html(timeleft + 's');
    var downloadTimer = setInterval(function(){
        if(timeleft <= 1){
            clearInterval(downloadTimer);
        }
        timeleft -= 1;
        $(comp).html(timeleft + 's');
    }, 1000);
}

function refreshTagsCobertura(){
    $('.timeLeft').each(function(i, comp){ 
        if($(comp).attr('init') != 1){
            $(comp).attr('init', 1);
            setTimeLeft(comp);
        }
    });
}

function modalInfo(info){
    $('#coberturaModalInfo .modal-body').html(info);
    $('#coberturaModalInfo').modal('show');
}

$(function(){
    Chart.register(ChartDataLabels);
});