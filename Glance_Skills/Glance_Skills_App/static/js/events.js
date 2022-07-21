
function appendbox()
{
    var v = document.getElementById("reply");

    console.log(v.value);
    var d = document.getElementById('comment-div');
   d.innerHTML += "<textarea type='textarea' id='replybox"+1 +"'><br >";
}