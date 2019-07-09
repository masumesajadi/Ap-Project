int IN1=5;
int IN2=6;
int IN3=10;
int IN4=9;
int ENA=3;
int ENB=11;


void setup() {
  pinMode (IN1 , OUTPUT);
  pinMode (IN2 , OUTPUT);
  pinMode (IN3 , OUTPUT);
  //pinMode (IN4 , OUTPUT);
  //pinMode (ENA , OUTPUT);
  //pinMode (ENB , OUTPUT);
}

void loop() {
 
  /////clockwise for 4 sec
 
  digitalWrite (IN1,HIGH);
  digitalWrite (IN2,LOW);
    delay(4000);  
 
   



   ////pad clockwise for 2 sec
analogWrite (ENA,100);
   digitalWrite (IN2,HIGH);
  digitalWrite (IN1,LOW);
  delay(2000);  
 
 // digitalWrite (IN3,LOW);
 // digitalWrite (IN4,HIGH);
 // analogWrite (ENB,200);
}
