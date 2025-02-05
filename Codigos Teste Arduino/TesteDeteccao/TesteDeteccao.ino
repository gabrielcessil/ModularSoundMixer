 void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
}
int num_max = 9;
int num = 0;

void loop() {
  // put your main code here, to run repeatedly:
  
  for(int i =0; i <= num; i++){
    Serial.print("F ");
    Serial.print(i);
    Serial.print(" 0.5\n");
  }
  Serial.print("stop\n"); 
  
  num = (num+1)%(num_max+1);


}
