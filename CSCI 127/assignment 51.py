#Jessica De Mota Munoz
#jessica.demotamunoz86@myhunter.cuny.edu
#November 21 2019 

ADDI $s0, $zero, 0 
ADDI $s1, $zero, 2
ADDI $s2, $zero, 20 
AGAIN: ADDI $s0, $s0, $s1
BEQ $s0, $s2, DONE
J AGAIN
DONE:  
