$('#modificarProveedorr').click(function(){
        
    rut = $("#dato").val();
    if (rut == ""){
      alert("INGRESE UN RUT")
    }
    else
    $('#modificarProveedorr').attr('href', '/modificarProveedor/'+ rut);
    
});
$('#eliminarProveedor').click(function(){
    
    rut = $("#dato").val();
    if (rut == ""){
      alert("INGRESE UN RUT")
    }
    else
    $('#eliminarProveedor').attr('href', '/elimiProveedor/'+ rut);
    alert("Proveedor eliminado Correctamente")
    
});

