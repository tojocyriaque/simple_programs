#include <stdio.h>
#include <unistd.h>
#include <time.h>

void show(char* time_){
  char numbers[11][6][6] = {
    {" ### ","#   #","#   #","#   #"," ### "},
    {"  #  "," ##  ","  #  ","  #  "," ### ",},
    {"#####","    #","#####","#    ","#####"},
    {"#####","    #","#####","    #","#####"},
    {"#   #","#   #","#####","    #","    #"},
    {"#####","#    ","#####","    #","#####"},
    {"#####","#    ","#####","#   #","#####"},
    {"#####","    #","   # ","  #  ","  #  "},
    {"#####","#   #","#####","#   #","#####"},
    {"#####","#   #","#####","    #","#####"},

    {"     ","  #  ","     ","  #  ","     "}//representation of ":"
  };

  for(int i=0; i<5; i++){
    for(int j=0; time_[j]; j++){
      if(time_[j]!=':'){
        printf("%s ",numbers[time_[j]-48][i]);
      }
      else{
        printf("%s ",numbers[10][i]);
      }
    }
    printf("\n");
  }

}

void timer(char* time_){
  int sec=0,min=0,hour=0;
  time_t t;
  struct tm* now;

  while(1){
    time(&t);
    now = localtime(&t);

    hour = now->tm_hour;
    min = now->tm_min;
    sec = now->tm_sec;

    printf("\x1b[H");
    sprintf(time_, "%.2d:%.2d:%.2d",hour,min,sec);
    show(time_);
    sleep(1);
  }
}

int main(){
  char time_[9];
  timer(time_);
  return 0;
}


