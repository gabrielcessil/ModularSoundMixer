 void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
}
int VolMax = 1;
float vol = 0.0;

char letra = 'A';
char letraMax = 'Z';
void loop() {
  // put your main code here, to run repeatedly:
  vol += 0.01;
  letra += 1;
  if(vol >= VolMax){
      vol = 0;    
      letra = 'A';
  }
  if(letra == letraMax){
    letra = 'A';
  }
  
  Serial.print(letra);
  Serial.print(" 0 ");
  Serial.print(vol);
  Serial.print("\n");
  Serial.print("stop");
  Serial.print("\n");
 
}
