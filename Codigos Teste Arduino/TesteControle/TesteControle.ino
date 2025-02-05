 void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
}

float i = 0.0;
float j = 0.0;
float vol = 0.0;
void loop() {
  // put your main code here, to run repeatedly:
  i += 0.01;
  if(sin(i) < 0){
    i = 0.0;
  }
  vol = sin(i);
  
  Serial.print("F 0 ");
  Serial.print(vol);
  Serial.print("\n");

  j += 0.01;
  if(cos(j) < 0){
    j = 0.0;
  }
  vol = cos(j);
  Serial.print("F 1 ");
  Serial.print(vol);
  Serial.print("\n");
  Serial.print("stop");
  Serial.print("\n");
  
  
  
}
