#!/bin/bash

cuadra(){
	cua=$(($in*$in))
	echo "El cuadrado de" $in "es:" $cua
}

facto(){
	fac=1
	while [ "$in" != "1" ];
	do
		fac=$(($fac*$in))
		in=$(($in-1))
	done
	echo "El factorial de" $in "es:" $fac
}

while :
do
	read -p "Introduzca un número: " in
	clear
	echo "Operaciones"
	echo "1. Elevar al cuadrado"
	echo "2. Factorial"
	echo "3. Salir"
	read -p "Seleccione una opción: " op
	case $op in 
	1) clear
	cuadra;;
	2) clear
	facto;;
	3) clear
	echo "Tenga un buen día"
	exit;;
	*) echo "Opción no válida";
	echo "Enter para continuar...";
	read foo;;
	esac
done
