/*
* Arduino Wireless Communication Tutorial
*       Example 1 - Receiver Code
*                
* by Dejan Nedelkovski, www.HowToMechatronics.com
* 
* Library: TMRh20/RF24, https://github.com/tmrh20/RF24/
*/
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
RF24 radio(7, 8); // CE, CSN
const byte addresses[][6] = {"00001", "00002"};

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openWritingPipe(addresses[0]); // 00001
  radio.openReadingPipe(1, addresses[1]); // 00002
  radio.setPALevel(RF24_PA_MIN);
  radio.startListening();
  pinMode(10, OUTPUT);
}
void loop() {
  // ---- receive ----
  radio.startListening();
  if (radio.available()) {
    char text[32] = "";
    radio.read(&text, sizeof(text));
    if (text[0] == '2' && text[1] == '4' && text[2] == '6' && text[3] == '8'){
      digitalWrite(10, HIGH);
    }
    else{
      digitalWrite(10, LOW); 
    }
    Serial.println(text);
    
  }

  // ----- Transmitter ----
  delay(10);
  radio.stopListening();
  const char text[] = "Hello World";
  radio.write(&text, sizeof(text));
  
  delay(10);
}
