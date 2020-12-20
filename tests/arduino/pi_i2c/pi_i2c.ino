//  I2C Pinouts
//  SDA -> A4
//  SCL -> A5


//Import the library required
#include <Wire.h>
#include "queue.h";

Queue<char> queue(100);

//Slave Address for the Communication
#define SLAVE_ADDRESS 0x04

int count = 65;
char c = '0';

//Code Initialization
void setup() {
  // initialize i2c as slave
  Serial.begin(9600);
  Wire.begin(SLAVE_ADDRESS);
  // define callbacks for i2c communication

  Wire.onRequest(sendData);
}

void send_string(String str){
  queue.push(2); // send start command
  for (int i = 0; i<str.length(); i++){
    queue.push(str[i]);
  }
  queue.push(3); // send end command
}

void loop() {  
  send_string("Hello World");
  delay(500);
} // end loop


// callback for sending data
void sendData() {
  Wire.write(queue.pop());
}

//End of the program
