function rememberChoice(myRadio) {
  sessionStorage.setItem("RadioButton",myRadio.id);
}

var data = sessionStorage.getItem('RadioButton');

if(data!=null){
  document.getElementById(data).checked = true;
}
