
#include <Wire.h>
  int BH1750_address = 0x23; // i2c Addresse
  byte buff[2];
  int IN1=5;
  int IN2=6;
  int IN3=10;
  int IN4=9;
  int ENA=3;
  int ENB=11;
  int light;
  int place=1;
  int endpoint=2;
  int startpoint=0;
  int i;

  void setup(){
    pinMode (IN1 , OUTPUT);
    pinMode (IN2 , OUTPUT);
    pinMode (IN3 , OUTPUT);
    delay(200);
    Serial.begin(9600);
  }


//=============================================================

  void loop(){
    float valf=0;
    //place=1;
    if(BH1750_Read(BH1750_address)==2){
      valf=((buff[0]<<8)|buff[1])/1.2;
      light=valf;

      if(light>900){ // day
            if(place > startpoint ){  //closed
                  /////clockwise
                  analogWrite (ENA,80);
                  digitalWrite (IN1,HIGH);
                  digitalWrite (IN2,LOW);
                  delay (1000);
                  digitalWrite (IN1,LOW);
                  digitalWrite (IN2,LOW); 
                  delay (4000);//هر نیم ساعت بیاد ببینه نور در چه حدیه و جهت باید کدوم وری باشه
                  //و قبلش چک کنه ببینه موقعیت موتور و به تبع اون پرئه کجا قرار داره اگه قابلیت چرخش داره خب بچرخه اگه نه هیچ کاری نکنه و نیم ساعت دیگه صبر کنه.
                  place--;
             }
             else  delay (4000);
       }
 
       else{   ///night
           if(place < endpoint ){ //opened
                  //analogWrite (ENA,80);
                  digitalWrite (IN1,LOW);
                  digitalWrite (IN2,HIGH);
                  delay (1000);
                  digitalWrite (IN1,LOW);
                  digitalWrite (IN2,LOW);
                  delay (4000);
                  place++;
            }
            else  delay (4000);
      }
    }
  }


//==================================================================
  byte BH1750_Read(int address)
  {
    byte i=0;
    Wire.beginTransmission(address);
    Wire.requestFrom(address, 2);
    while(Wire.available()){
      buff[i] = Wire.read();
      i++;
    }
    Wire.endTransmission();  
    return i;
  }


