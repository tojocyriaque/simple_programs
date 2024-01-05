#include <stdio.h>
#include <stdint.h>

int main(){
  int s=56;
  while(s>=0){putc(0x48656c6c6f>>s,stdout);s=s-8;}
  return 0;
}
