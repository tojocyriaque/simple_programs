class Spot{
  float h = 10,
        w = 120;
  PVector pos,
          vel = new PVector(30,0);
  
  public Spot(PVector p){
    pos = new PVector(p.x,p.y);
  }
  
  void moveLeft(){
    vel.x = -20;
    pos.add(vel);
  }
  
  void moveRight(){
    vel.x = 20;
    pos.add(vel);
  }
  
  void show(){
    stroke(250,50,0);
    strokeWeight(h);
    line(pos.x,pos.y,pos.x+w,pos.y);
    noStroke();
  }
  
}
