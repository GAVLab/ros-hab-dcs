/*
* Arduino Wireless Communication Tutorial
*     Example 1 - Transmitter Code
*                
* by Dejan Nedelkovski, www.HowToMechatronics.com
* 
* Library: TMRh20/RF24, https://github.com/tmrh20/RF24/
*/

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

const int buttonPin = 4;     // the number of the pushbutton pin
const int ledPin =  3;      // the number of the LED pin

int buttonState = 0;         // variable for reading the pushbutton status

RF24 radio(7, 8); // CE, CSN

const byte addresses[][6] = {"00001", "00002"};

void setup() {
  radio.begin();
  radio.openWritingPipe(addresses[1]); // 00002
  radio.openReadingPipe(1, addresses[0]); // 00001
  radio.setPALevel(RF24_PA_MIN);
  radio.stopListening();

  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
}

void loop() {

  // ---- Transmission ----  
  radio.stopListening();
  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) {
    // turn LED on:
    digitalWrite(ledPin, HIGH);
    const char text[] = "2468";
    radio.write(&text, sizeof(text));
    
  } else {
    // turn LED off:
    digitalWrite(ledPin, LOW);
    const char text[] = "0000";
    radio.write(&text, sizeof(text));
  }
  delay(10);
  
  // ---- Receive ----  
  radio.startListening();
  if (radio.available()) {
      char text[32] = "";
      radio.read(&text, sizeof(text));
      Serial.println(text);
  }
  delay(10);
}
