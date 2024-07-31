//header file

#ifndef BEACON_H
#define BEACON_H

#define TIME_BEACON 16000
#define TIMER_WAKEUP 1000
#define TIMER_WAIT 2000
#define MAX_SLAVE 10 
#define TIMER_SCANNER 30000

//predefined structure

typedef nx_struct radio_count_msg {
  nx_uint16_t counter;
} radio_count_msg_t;

//predefined structure ends

// Structure of the Beacon Message
typedef struct beaconMsg 
{
  nx_uint8_t sndId;  // Id of Message Sender
  nx_uint16_t nextBeaconTime;  // local Clock of sender
  nx_uint8_t beaconVector[MAX_SLAVE]; //beacon vector of wireless network
  
  nx_uint16_t temp;
  nx_uint16_t hum;
 
  nx_uint16_t stato; // Automatic(0) , Manual ( 1 o 2 )  User Command 
	
  nx_uint16_t light_TSR;  // total solar radiation
  nx_uint16_t light_PAR; // photosynthetically active radiation
  nx_uint16_t detach; // Rivelatore
  
  nx_uint8_t myfather;

} beaconMsg;	   // 29-byte payload

typedef beaconMsg * beaconMsgPtr;

typedef struct data_t 
{
  nx_uint8_t slave;  // Id of Message Sender
  nx_uint8_t posInBeacon;
} data_t;	   

//typedef beaconMsg * beaconMsgPtr;

enum { 
AM_BEACONMSG=38,
AM_BEACONMSGUART=39
};   // please change if needed

enum utente{
DOWN=1,
UP=2

};

#endif
