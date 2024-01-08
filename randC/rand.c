#include <stdio.h>
#include <stdlib.h>

typedef unsigned long long vlong;

vlong getfrand(){
  vlong val;
  FILE* rfile = fopen("rand","r");
  fscanf(rfile, "%llu", &val);
  fclose(rfile);
  return val;
}

vlong genrand(vlong* s){
  vlong rand = *s,
        a = 1789622347,
        c = 654654767544,
        m = 4294967296;

  rand = (a*rand + c)%m;
  FILE* rfile = fopen("rand","w");
  fprintf(rfile,"%llu",rand);
  fclose(rfile);
  *s = rand;
  return rand;
}


int main(){
  vlong s = getfrand();
  for(int i=0; i<10; i++) printf("%llu\n",genrand(&s));
  return 0;
}
