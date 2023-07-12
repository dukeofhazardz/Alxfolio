var para = document.getElementsByClassName("long-text")[0];
var text = para.innerHTML;
para.innerHTML = "";
var words = text.split(" ");
for (i = 0; i < 30; i++) {
    para.innerHTML += words[i] + " ";
}
para.innerHTML += "...";