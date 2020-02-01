import pickle
from os import path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
lcd_columns = 16
lcd_rows = 2
i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

class Sheets_Logging:
   # The ID and range of a sample spreadsheet.
   SPREADSHEET_ID = '1py6rmh3pJJA0L8c6P6z71Zw7AopN_p_Gf_UyZnEBa0U'
   RANGE_NAME = 'Sheet1'
   # If modifying these scopes, delete the file token.pickle.
   SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive.file',
             'https://www.googleapis.com/auth/drive']

   def __init__(self):
       self.service = None
       self.credentials = self.auth()

   def auth(self):
       """Shows basic usage of the Sheets API.
       Prints values from a sample spreadsheet.
       """
       creds = None
       # The file token.pickle stores the user's access and refresh tokens, and is
       # created automatically when the authorization flow completes for the first
       # time.
       if path.exists('token.pickle'):
           with open('token.pickle', 'rb') as token:
               creds = pickle.load(token)
       # If there are no (valid) credentials available, let the user log in.
       if not creds or not creds.valid:
           if creds and creds.expired and creds.refresh_token:
               creds.refresh(Request())
           else:
               flow = InstalledAppFlow.from_client_secrets_file(
                   'credentials.json', self.SCOPES)
               creds = flow.run_local_server(port=0)
           # Save the credentials for the next run
           with open('token.pickle', 'wb') as token:
               pickle.dump(creds, token)
       self.service = build('sheets', 'v4', credentials=creds)

   def read_data(self):
       # Call the Sheets API
       service = self.service
       sheet = service.spreadsheets()
       result = sheet.values().get(spreadsheetId=self.SPREADSHEET_ID,
                                   range=self.RANGE_NAME).execute()
       values = result.get('values', [])
       if not values:
           print('No data found.')
           return None
       else:
           return values

   def write_data(self, data):
       service = self.service
       values = [data]
       body = {
           'values': values
       }
       range_name = 'Sheet1'
       result = service.spreadsheets().values().append(
           spreadsheetId=self.SPREADSHEET_ID, range=range_name,
           valueInputOption='USER_ENTERED', body=body).execute()

from random import randrange
from datetime import datetime
import os
import time


def gen_data(id):
    lcd.color = [0, 0, 100]
    dateout = datetime.now()
    name = check_id(id)
    lcd.clear()
    print(name + "\n has checked out.")
    lcd.message = name + "\nhas checked out."
    time.sleep(2)
    lcd.clear()
    lcd.message = " Hit 'ENTER' to \n   sign back in.  "
    signin = input("Hit 'Enter' to sign back in")
    datein = datetime.now()
    lcd.clear()
    print(name + "has checked in.")
    lcd.message = name + "\n has checked in."
    return [name, id, str(dateout).split('.')[0], str(datein).split('.')[0]]

def id_input():
    lcd.color = [0, 100, 0]
    id = input()
    lcd.message = "   Student ID:\n" + id
    return id

def check_id(id):
    while(True):
        if id == 123456:
            return "R. Kramlich"
        if id == 177692:
            return "E. Boerstler"
        if id == 174950:
            return "T. Cronin"
        if id == 177748:
            return "A. Gazinschi"
        if id == 200560:
            return "A. Jakubowski"
        if id == 192890:
            return "K. Jensen"
        if id == 212627:
            return "J. Lawson"
        if id == 210901:
            return "S. Lee"
        if id == 174632:
            return "L. Marland"
        if id == 180471:
            return "G. McBride"
        if id == 191037:
            return "M. McLeod"
        if id == 177474:
            return "T. Moore"
        if id == 209132:
            return "G. Nelson"
        if id == 208915:
            return "Q. Nguyen"
        if id == 178001:
            return "J. O'Brien"
        if id == 187712:
            return "C. Oceguera"
        if id == 190161:
            return "N. Oldham"
        if id == 209865:
            return "N. Pinto"
        if id == 211041:
            return "A. Reyes"
        if id == 178370:
            return "E. Routon"
        if id == 182536:
            return "S. Samnani"
        if id == 201901:
            return "Y. Tamura"
        if id == 208632:
            return "T. Wade"
        if id == 212211:
            return "V. Weaver"
        if id == 185670:
            return "T. Wheaton"
        if id == 179179:
            return "J. Zondervan"
        if id == 175288:
            return "K. Austensen"
        if id == 191890:
            return "K. Boyce"
        if id == 189150:
            return "M. Call"
        if id == 190645:
            return "J. Chang"
        if id == 174703:
            return "W. Dannelly"
        if id == 167611:
            return "J. Deng"
        if id == 204267:
            return "B. Feldman"
        if id == 174779:
            return "C. Giorgi"
        if id == 198980:
            return "M. Jimenez Escobar"
        if id == 167508:
            return "K. Lin"
        if id == 174962:
            return "S. Lutz"
        if id == 194023:
            return "J. Maldonado"
        if id == 185909:
            return "C. Maxwell"
        if id == 204097:
            return "E. Prindle"
        if id == 207574:
            return "H. Ricketts"
        if id == 182953:
            return "H. Seay"
        if id == 208186:
            return "S. Sharma"
        if id == 175164:
            return "M. Stephens"
        if id == 174777:
            return "J. Uszynski"
        if id == 178318:
            return "H. Watts"
        if id == 175074:
            return "W. Wheeler"
        if id == 191355:
            return "A. Williams"
        if id == 190725:
            return "Z. Wiseman"
        if id == 201368:
            return "S. Wright"
        if id == 175601:
            return "J. Zhang"
        if id == 171157:
            return "T. Bennett"
        if id == 193168:
            return "E. Crowe"
        if id == 185593:
            return "T. Hong"
        if id == 203638:
            return "S. Katabattula"
        if id == 168853:
            return "D. Kusharsky"
        if id == 171204:
            return "Q. Lambert"
        if id == 171379:
            return "P. Millians"
        if id == 207926:
            return "S. Noh"
        if id == 202454:
            return "O. Sanusi"
        if id == 172968:
            return "M. Schwensen"
        if id == 206772:
            return "R. Sheppard"
        if id == 184629:
            return "W. Thuon"
        if id == 193991:
            return "L. Xu"
        if id == 167737:
            return "S. Yavari"
        if id == 174460:
            return "A. Ajibade"
        if id == 185683:
            return "L. Bourque"
        if id == 189778:
            return "S. Cho"
        if id == 167691:
            return "L. Fennell"
        if id == 202094:
            return "C. Gangler"
        if id == 172239:
            return "A. Graffeo"
        if id == 172140:
            return "B. Hays"
        if id == 207330:
            return "I. McKeirnan"
        if id == 203874:
            return "V. Miranda"
        if id == 168229:
            return "G. Moore"
        if id == 171216:
            return "H. Moore"
        if id == 171699:
            return "N. Nadarajan"
        if id == 193603:
            return "E. O'Brien"
        if id == 195018:
            return "M. Premkumar"
        if id == 170018:
            return "S. Smith"
        if id == 203434:
            return "A. Spencer"
        if id == 196653:
            return "E. Tonnesen"
        if id == 200154:
            return "J. Zhang"
        if id == 208861:
            return "A. Arahill"
        if id == 177858:
            return "D. Batcha"
        if id == 211249:
            return "M. Bryant"
        if id == 211528:
            return "K. Chen"
        if id == 181608:
            return "J. Enck"
        if id == 177806:
            return "G. Eves"
        if id == 212137:
            return "M. Gamalathge"
        if id == 176709:
            return "M. Gentilella"
        if id == 177652:
            return "J. Gevertz"
        if id == 178559:
            return "A. Giffen"
        if id == 190083:
            return "C. Hawkins"
        if id == 201536:
            return "M. Hwang"
        if id == 191671:
            return "M. Kirkland"
        if id == 196676:
            return "A. LaVigna"
        if id == 189762:
            return "O. Leonard"
        if id == 177752:
            return "G. Martin"
        if id == 207162:
            return "T. Miller-Constanzo"
        if id == 203931:
            return "N. Mustian"
        if id == 182268:
            return "B. Ok"
        if id == 178053:
            return "C. Ortega Montiel"
        if id == 177448:
            return "G. Proffitt"
        if id == 194547:
            return "G. Snow"
        if id == 190121:
            return "E. Sposaro"
        if id == 211865:
            return "J. Valle Rosa"
        if id == 177733:
            return "J. Ward"
        return str(id)

while (True):
    if __name__ == '__main__':
        lcd.blink = True
        lcd.color = [0, 100, 0]
        lcd.message = "   Student ID:\n"
        id = id_input()
        while len(id) != 6:
            lcd.clear()
            lcd.color = [100, 0, 0]
            lcd.message = "    Invalid\n   Student ID!"
            time.sleep(2)
            lcd.clear()
            id = id_input()
        while (True):
            try:
                id = int(id)
                break
            except:
                lcd.clear()
                lcd.color = [100, 0, 0]
                lcd.message = "    Invalid\n   Student ID!"
                time.sleep(2)
                lcd.clear()
                id = id_input()
        data = gen_data(id)
        doc = Sheets_Logging()
        doc.write_data(data=data)
        time.sleep(5)
        lcd.clear()
        os.system('cls')
