
#define POTENTIOMETER A0

void setup() {
  
  pinMode(POTENTIOMETER, INPUT);

  Serial.begin(9600);

}

void loop() {
  
  Serial.println(analogRead(POTENTIOMETER));
  delay(1000);

}
