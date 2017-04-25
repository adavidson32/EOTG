#include <NeoPixelBus.h>

const uint16_t PixelCount = 24; // this example assumes 4 pixels, making it smaller will cause a failure
const uint8_t PixelPin = 11;  // make sure to set this to the correct pin, ignored for Esp8266

#define colorSaturation 128

NeoPixelBus<NeoRgbwFeature, Neo800KbpsMethod> strip(PixelCount, PixelPin);

RgbColor red(colorSaturation, 0, 0);
RgbColor green(0, colorSaturation, 0);
RgbColor blue(0, 0, colorSaturation);
RgbColor white(colorSaturation);
RgbColor black(0);

void setup()
{
    Serial.begin(115200);
    while (!Serial); // wait for serial attach
    Serial.println(); Serial.println("Initializing..."); Serial.flush();
    strip.Begin(); strip.Show();
    Serial.println();  Serial.println("Running...");
}

void loop()
{
  
}
