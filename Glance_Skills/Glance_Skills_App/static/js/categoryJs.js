function fun1() {
  $.ajax({
    url: "/category",
    dataType: "json",
    success: function (data) {
      document.getElementById("drop").innerHTML = "";
      for (i = 0; i < 2; i++) {
        var ele = document.createElement("li");
        var ele2 = document.createElement("a");
        console.log(data[i].name);
        ele2.classList.add("dropdown-item");
        ele2.href = "/categoryPage/" + data[i].id + " ";
        ele.appendChild(ele2);
        ele2.textContent = data[i].name;
        $("#drop").append(ele);
      }
    },
  });
}

function showPassword() {
  var x = document.getElementById("password")
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
} 



