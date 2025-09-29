section .data
	msg1:     db 'SIMPLE CALCULATOR',10  
	msg1Len:  equ $-msg1             
  prodt:     db 'Product (4x2) = ',
  prodtLen   equ $-prodt
  newline   db 10
  sum:      db 'SUM(4+2) = '
  sumLen:   equ $-sum
  prodf:     db 'RESULT = ',10
  prodfLen:  equ $-prodf
  result db 0
  
  
section .text
	global _start

_start:

	mov eax,4          
	mov ebx,1            
	mov ecx,msg1        
	mov edx,msg1Len    
	                     
	int 0x80              
	mov eax, 4          
	mov ebx, 1           
	mov ecx, sum
	mov edx, sumLen 
	int 0x80
	
  mov al, 4 
  add al, 2
  
  add al, '0'
  
  mov [result], al
	mov eax, 4          
	mov ebx, 1           
	mov ecx, result
	mov edx, 1 
	int 0x80              

	mov eax, 4          
	mov ebx, 1           
	mov ecx, newline
	mov edx, 1 
	int 0x80

	mov eax, 4          
	mov ebx, 1           
	mov ecx, prodt
	mov edx, prodtLen 
	int 0x80
	
	mov al, 4
	mov bl, 2
	
	mul bl
	
	add al, '0'
	mov [result], al
	
	mov eax, 4          
	mov ebx, 1           
	mov ecx, result
	mov edx, 1
	int 0x80
	
	
	mov eax,1            
	mov ebx,0            
	int 0x80;