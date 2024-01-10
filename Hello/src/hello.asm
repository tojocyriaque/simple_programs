section .data
  hello dd 'Hello world',10,0
  hlen equ $-hello

section .text
  global _start

  _start:
    MOV EAX,4       ;SYS_WRITE
    MOV EBX,1       ;STDOUT
    MOV ECX,hello
    MOV EDX,hlen
    INT 0x80

  _exit:
    MOV EAX,1
    INT 0x80
  
