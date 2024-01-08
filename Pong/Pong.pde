Ball B;
Spot S;
float fRate = 100;
int score = 0;

void handleCollision(){
  if(B.pos.y == S.pos.y-S.h && (S.pos.x<=B.pos.x && B.pos.x<=S.pos.x+S.w)){
    B.vel.y = -B.vel.y;
    score = score + 1;
    fRate = fRate + 5;
  }
}

void setup(){
  size(600,400);
  B = new Ball(new PVector(10,10));
  S = new Spot(new PVector(10,height-40));
}

void keyPressed(){
  switch(keyCode){
    case 37:
      if(S.pos.x>0)S.moveLeft();
      break;
      
    case 39:
      if(S.pos.x<width-S.w)S.moveRight();
      break;
  }
}

void draw(){

  if(B.pos.y>S.pos.y){
    noLoop();
  }
  
  frameRate(fRate);
  background(5,40,5);
  
  textFont(createFont("Consolas",20));
  fill(255);
  text("Score: "+score, 5,25);
  
  handleCollision();
  B.show();
  B.move();
  S.show();
  
}
