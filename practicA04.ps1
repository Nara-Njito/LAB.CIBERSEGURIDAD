function Opss{
    do 
    {   
         cls
         Write-Host "¿Qué quiere realizar?"
         Write-Host "1. Crear un archivo"
         Write-Host "2. Eliminar un archivo"
         write-Host "3. Salir"
         $op = Read-Host "Escoja una opción: " 
         cls
         switch ($op) 
         { 
               
               '1' { 
                        $nom = Read-Host "Nombre del archivo. (ej: Prueba.txt)"
                        ni $nom
                    } 
               '2' {  
                        $nam = Read-Host "Nombre del archivo que desea eliminar. (ej: Prueba.txt)"
                        rm $nam
                    } 
               '3' {
                        Write-Host "Saliendo..."
               }
               default{
                        Write-Host "Opción no valida"
               }
         } 
         pause
         cls
    } 
    until ($op -eq '3')
}
Opss