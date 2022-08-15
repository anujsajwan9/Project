function readURL(input) 
{
    console.log("Yes")
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function (e) 
    {
      $("#imgview").attr("src", e.target.result);
    };
    reader.readAsDataURL(input.files);
  }
}
