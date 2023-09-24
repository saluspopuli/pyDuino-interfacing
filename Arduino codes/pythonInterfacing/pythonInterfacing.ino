
#define POTENTIOMETER1 A0
#define POTENTIOMETER2 A1

void setup() {
  
  pinMode(POTENTIOMETER1, INPUT);
  pinMode(POTENTIOMETER2, INPUT);

  Serial.begin(9600);

}

void loop() {
  
  Serial.print(analogRead(POTENTIOMETER1));
  Serial.print("-");
  Serial.print(analogRead(POTENTIOMETER2));
  Serial.println();
  delay(10);

}
