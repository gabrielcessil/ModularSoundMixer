 void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
}

float j = 0.0;
float vol = 0.0;
void loop() {
  j += 0.01;
  if(cos(j) < 0){
    j = 0.0;
  }
  vol = cos(j);
  Serial.print("F 0 ");
  Serial.print(vol);
  Serial.print("\n");
  Serial.print("stop");
  Serial.print("\n");
  
}
