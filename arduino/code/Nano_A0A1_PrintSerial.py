// c++ program to read Arduino A0+A1 voltage, send via serial
// Important: Serial uses 115200 speed to communicate.
// Use A0 and A1 or change numbers in program

int A0_samples = 0;        // value read from the pot
int A1_samples = 0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  A0_samples = analogRead(0);
  A1_samples = analogRead(1);
  Serial.print("A0: "); Serial.print(A0_samples); Serial.print(" \t A1: "); Serial.println(A1_samples);
  float A0_voltage = ((A0_samples / 1024.00) * 5.00);
  float A1_voltage = ((A1_samples / 1024.00) * 5.00);
  Serial.print("A0: "); Serial.print(A0_voltage); Serial.print("V \t A1:"); Serial.print(A1_voltage); Serial.println("V");
  Serial.println(""); Serial.println(""); Serial.println(""); Serial.println(""); Serial.println(""); 
  delay(500);
}
