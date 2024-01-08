
class Ball{ 

  float r = 15;
  PVector pos,
          vel = new PVector(1,1);
          
  public Ball(PVector p){
    pos = new PVector(p.x, p.y);
  }
  
  void move(){
    pos.add(vel);
    if(pos.x<r){
      pos.x = r;
      vel.x = -vel.x;
    }
    if(pos.x>width-r){
      pos.x = width-r;
      vel.x = -vel.x;
    }
    
    if(pos.y<r){
      pos.y = r;
      vel.y = -vel.y;
    }
    if(pos.y>height-r){
      pos.y = height-r;
      vel.y = -vel.y;
    }
    
  }
  
  void show(){
    fill(#ff9805);
    ellipse(pos.x,pos.y,r*2,r*2);
  }
  
}
