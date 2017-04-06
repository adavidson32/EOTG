const int pA0 = A0;  // Analog input pin that the potentiometer is attached to
const int pA1 = A1; // Analog output pin that the LED is attached to

int A0_samples = 0;        // value read from the pot
int A1_samples = 0;
float A0_voltage = 0;
float A1_voltage = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  A0_samples = analogRead(pA0);
  A1_samples = analogRead(pA1);
  A0_voltage = ((A0_samples) * 5) / 1024;
  A1_voltage = ((A1_samples) * 5) / 1024;
  Serial.print("A0:  Voltage= ");
  Serial.print(A0_voltage);
  Serial.print("\t Samples= ");
  Serial.println(A0_samples);
  Serial.print("A1:  Voltage= ");
  Serial.print(A1_voltage);
  Serial.print("\t Samples= ");
  Serial.println(A1_samples);
  
  delay(1);
}
