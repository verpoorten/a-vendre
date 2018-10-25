
function createCookie(name,value,days) {
    if (days) {
        var date = new Date();
        date.setTime(date.getTime()+(days*24*60*60*1000));
        var expires = "; expires="+date.toGMTString();
    }
    else var expires = "";
    document.cookie = name+"="+value+expires+"; path=/";
}

function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}

function readCookieStartWith(name) {
    console.log('readCookieStartWith');
    var nameEQ = name ;
    var ca = document.cookie.split(';');
    var cpt=0;
    var ids = [-1];
    cpt=1;
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        var pos=c.indexOf(nameEQ);
        if (pos >= 0){
            var posegal=c.indexOf('=');
            var id = c.substring(pos+6,posegal);
            if(ids.includes(id)){
            }else {
                ids[cpt] = id;
                cpt =cpt +1;
            }


        }


    }
    ids[cpt] = -1;

    document.getElementById('ids').innerHTML=ids;

    return cpt-1 + " favoris";

}
function eraseCookie(name) {
    createCookie(name,"",-1);
}