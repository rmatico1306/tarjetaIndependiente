function myFunction() {
    // Declare variables 
    var input, filter, table, tr, td, i, j, visible;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("userList");
    tr = table.getElementsByTagName("tr");
  
    // Loop through all table rows, and hide those who don't match the search query
    //inicio en 1 para no perder los titulos de la tabla 
    for (i =1 ; i < tr.length; i++) {
      visible = false;
      /* Obtenemos todas las celdas de la fila, no sólo la primera */
      td = tr[i].getElementsByTagName("td");
      for (j = 0; j < td.length; j++) {
        if (td[j] && td[j].innerHTML.toUpperCase().indexOf(filter) > -1) {
          visible = true;
        }
      }
      if (visible === true) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
}

document.getElementById('buttonDelete').onclick = function(){
  var x = confirm("Eliminar Tarjeta 2?");
  if (x)
    return true;
  else
    return false;
}