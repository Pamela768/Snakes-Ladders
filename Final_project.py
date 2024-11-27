from tkinter import *
import tkinter.ttk as ttk
from random import randint
from PIL import Image, ImageTk
from time import sleep
from tkinter import messagebox
import pygame




class MyApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Snakes & Ladders")
        self.iconbitmap(r"C:\Users\Pamela\Documents\GTB\Project\S and L\snake-pic.ico") #Logo used
        pygame.init() # Initializes pygame for sound
        pygame.mixer.init() # initalizes music
        self.play_music()
        
       
    
        
        
        # Create frames for different screens
        self.frame1 = Frame(self) #Frame for first page (menu)
        self.frame2 = Frame(self) #frame for second page (game)
    

        self.position = 0  # Player 1's position
        self.position2 = 0 # Player 2's (Computer) position
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 51: 67, 72: 91, 80: 99} #Position for ladders
        self.snakes = {17: 7, 54: 34, 62: 18, 64: 60, 87: 36, 93: 73, 95: 75, 98: 79} # Position for snekes

        
        self.back = ttk.Button(self.frame2, text= "Back Button", command=self.Error) #Back button 
        self.back.pack(anchor= NW) #Packs it at the top right
        ttk.Button(self.frame1, text="Play Alone", command=lambda:(self.show_frame2(), self.button_pressed("alone"), self.player2_label.pack_forget())).pack(pady=10)  # Play Alone button
        ttk.Button(self.frame1, text="Play Against Computer", command= lambda:(self.show_frame2(), self.button_pressed("computer"), self.player2_label.pack(), self.show_player2())).pack(pady=10) # Player with Computer button 
        
        self.player1_label= ttk.Label(self.frame2, text="Your position is 0" ) # Displays Initial position of player 1
       
        self.player2_label = ttk.Label(self.frame2, text = "Opponent position is 0") #Displays intial position of player 2
        
        self.player1_label.pack(pady=5)
        self.player2_label.pack(pady=5)
        self.dice = ttk.Button(self.frame2, text ="Dice", command = None ) # Initalizes dice button
        
        self.music_on = ImageTk.PhotoImage(Image.open(r"C:\Users\Pamela\Documents\GTB\Project\S and L\volume_small.jpg")) # Button to turn game on
        self.music_off = ImageTk.PhotoImage(Image.open(r"C:\Users\Pamela\Documents\GTB\Project\S and L\volume_off (1).jpg")) # Button to turn game off
        
       
        self.button = Button(self, image=self.music_on, command=self.change_image) #Creates button for executing the command for changing vlume
        self.button.pack(anchor=SE)
    
        self.dice.pack(padx= 10)
        self.frame1.pack()
        
        

        # Loads the board image
        image_path = r"C:\Users\Pamela\Documents\GTB\Project\S and L\board.jpg"
        try:
            self.pic = ImageTk.PhotoImage(Image.open(image_path))  # Store as an instance variable
            self.canvas = Canvas(self.frame2, width=self.pic.width(), height=self.pic.height()) #Sets the canvas height & width to be the same has the picture
            self.canvas.create_image(0, 0, image=self.pic, anchor=NW) #Draws the image on the canvas
            self.player1 = self.canvas.create_oval(0, 470, 25, 495, fill="blue") #Creates blue circle has the player 1's icon 
            
            
           
            self.canvas.pack() #Displays image
            print("Image loaded successfully!")
        except Exception as e: 
            '''Executes Error whem unsuccessful'''
            print(f"Error loading image: {e}")
        
        
      
        
        

        # Board coordinates
        self.board_mapping = {
         # Row 1 (Left to Right, 1-10)
0: (0, 460),1: (0, 470), 2: (50, 470), 3: (100, 470), 4: (150, 470), 5: (200, 470),
6: (250, 470), 7: (300, 470), 8: (350, 470), 9: (400, 470), 10: (450, 470),

# Row 2 (Right to Left, 11-20)
11: (450, 420), 12: (400, 420), 13: (350, 420), 14: (300, 420), 15: (250, 420),
16: (200, 420), 17: (150, 420), 18: (100, 420), 19: (50, 420), 20: (0, 420),

# Row 3 (Left to Right, 21-30)
21: (0, 370), 22: (50, 370), 23: (100, 370), 24: (150, 370), 25: (200, 370),
26: (250, 370), 27: (300, 370), 28: (350, 370), 29: (400, 370), 30: (450, 370),

# Row 4 (Right to Left, 31-40)
31: (450, 320), 32: (400, 320), 33: (350, 320), 34: (300, 320), 35: (250, 320),
36: (200, 320), 37: (150, 320), 38: (100, 320), 39: (50, 320), 40: (0, 320),

# Row 5 (Left to Right, 41-50)
41: (0, 270), 42: (50, 270), 43: (100, 270), 44: (150, 270), 45: (200, 270),
46: (250, 270), 47: (300, 270), 48: (350, 270), 49: (400, 270), 50: (450, 270),

# Row 6 (Right to Left, 51-60)
51: (450, 220), 52: (400, 220), 53: (350, 220), 54: (300, 220), 55: (250, 220),
56: (200, 220), 57: (150, 220), 58: (100, 220), 59: (50, 220), 60: (0, 220),

# Row 7 (Left to Right, 61-70)
61: (0, 170), 62: (50, 170), 63: (100, 170), 64: (150, 170), 65: (200, 170),
66: (250, 170), 67: (300, 170), 68: (350, 170), 69: (400, 170), 70: (450, 170),

# Row 8 (Right to Left, 71-80)
71: (450, 120), 72: (400, 120), 73: (350, 120), 74: (300, 120), 75: (250, 120),
76: (200, 120), 77: (150, 120), 78: (100, 120), 79: (50, 120), 80: (0, 120),

# Row 9 (Left to Right, 81-90)
81: (0, 70), 82: (50, 70), 83: (100, 70), 84: (150, 70), 85: (200, 70),
86: (250, 70), 87: (300, 70), 88: (350, 70), 89: (400, 70), 90: (450, 70),

# Row 10 (Right to Left, 91-100)
91: (450, 20), 92: (400, 20), 93: (350, 20), 94: (300, 20), 95: (250, 20),
96: (200, 20), 97: (150, 20), 98: (100, 20), 99: (50, 20), 100: (0, 20),


 }
        

    def show_frame1(self):
        """Display the main menu."""
        self.frame1.pack()
        self.frame2.pack_forget()
    

    def show_frame2(self):
        """Switch to the individual game screen."""
        self.frame1.pack_forget()
        self.frame2.pack()
        

            


    def alone(self): # Function to execute game logic for one player
        dice = randint(1, 6) #Generates a random no between 1 and 6
        target_position1 = self.position + dice # Calculate the target position after dice roll


        #if target position exceeds 100
        if target_position1 > 100:
            target_position1 = self.position
            self.player1_label.config(text=f"You have overshot. Stay at {self.position}")
            
        # If the player lands exactly on 100, they win
        elif target_position1 == 100:
            self.animate_player_movement(self.position2, target_position1, "player1")    
            self.player1_label.config(text=f"You rolled a {dice}. You won!")
            return

        else:
            # Animate the skipping movement
            self.animate_player_movement(self.position, target_position1, "player1")
            

        # Update position after reaching target
            self.position = target_position1
        
        # Check if the player lands on ladder 
            if target_position1 in self.ladders:
                ladder_end = self.ladders[target_position1] # Get the endpoint of the ladder
                self.slide_up_or_down(target_position1, ladder_end, 'player1')  # Animates the movement for sliding up
                self.position = ladder_end  # Update the position
                self.player1_label.config(text=f" You climbed up to {ladder_end}") #Updates the label
                
            #Checks if the player lands on a snake
            elif target_position1 in self.snakes:
                snake_end = self.snakes[target_position1]  # Get the endpoint of the ladder
                self.slide_up_or_down(target_position1, snake_end, 'player1')  # Get the endpoint of the snake
                self.position = snake_end #Updates the position
                self.player1_label.config(text=f" You slid down to {snake_end}") #Updates the label
            
              # If no ladder or snake, update the label with the current position
            else: 
                self.player1_label.config(text=f"You rolled a {dice}. You're now at {self.position}")
      
        

    def animate_player_movement(self, start, end,player):
        """
    Animate the player's movement from the start position to the end position.
    Args:
        start (int): The starting position.
        end (int): The target position.
        player (str): The player to animate ('player1' or 'player2').
    """
        
        for pos in range(start + 1, end + 1):  # Iterate through the positions
            x, y = self.board_mapping[pos] # Get the (x, y) coordinates for the current position
            if player == "player1": 
                self.canvas.coords(self.player1, x, y, x + 30, y + 30) #Update player1 position
            elif player == "player2":
                self.canvas.coords(self.player2, x, y, x + 30, y + 30)#Update player2 postion
            self.update() # Refresh the canvas to reflect change
            sleep(0.2)  # Pauses for animation speed
            
    def slide_up_or_down(self, start, end, player):
        """
    Animate sliding up a ladder or down a snake.
    Args:
        start (int): The starting position of the player.
        end (int): The ending position of the player.
        player (str): The player to animate ('player1' or 'player2').
    """
        if start < end:  # Animate climbing up the ladder
            for pos in range(start, end + 1):
                x, y = self.board_mapping[pos]
                if player == "player1":
                    self.canvas.coords(self.player1, x, y, x + 30, y + 30)
                elif player == "player2":
                    self.canvas.coords(self.player2, x, y, x + 30, y + 30)
                self.update()
                sleep(0.2)  # Animation speed
                
        elif start > end:  # Animate Sliding down the snake
            for pos in range(start, end - 1, -1):
                x, y = self.board_mapping[pos]
                if player == "player1":
                    self.canvas.coords(self.player1, x, y, x + 30, y + 30)
                elif player == "player2":
                    self.canvas.coords(self.player2, x, y, x + 30, y + 30)
                self.update()
                sleep(0.2)  # Animation speed
        





    def computer(self):
        """Execute the computer's turn."""
        # Move player 1 (human)
        dice = randint(1, 6) #Generates number between 1 and 6
        target_position1 = self.position + dice # Calculate the target position after dice roll
        
        #Checks if the player exceeds 100
        if target_position1 > 100:
            target_position1 = self.position
            self.player1_label.config(text=f"You overshot! Stay at {self.position}")
        
        # Checks if the players position is at 100, if True they win
        elif target_position1 == 100:
            self.player1_label.config(text="You won!")
            self.animate_player_movement(self.position2, target_position1, "player1") #animates players movement
            return  # Stop the game here
        
        else:
            self.animate_player_movement(self.position, target_position1, "player1") # Animate the skipping movement
            self.position = target_position1 #Updates players position

            #Checks if target position is in ladders
            if target_position1 in self.ladders:
                ladder_end = self.ladders[target_position1] # Get the endpoint of the ladder
                self.slide_up_or_down(target_position1, ladder_end, 'player1')  #Animates sliding up
                self.position = ladder_end  # Update the position
                self.player1_label.config(text=f"You climbed up to {ladder_end}") #Updates label
            

            
            elif target_position1 in self.snakes:
                snake_end = self.snakes[target_position1]  # Gets endpoint of the snake
                self.slide_up_or_down(target_position1, snake_end, 'player1')  # Animates Sliding down the snake
                self.position = snake_end # Updates the position
                self.player1_label.config(text=f"You slid down to {snake_end}") #Updates the label
        
        
       
            else:
                self.player1_label.config(text=f"You rolled a {dice}. You're now at {self.position}") #Updates the position



        # Move player 2 (computer)
        dice_2 = randint(1, 6) #Gives random number between 1 and 6 for the computer's dice
        target_position2 = self.position2 + dice_2 #Calculates computer's position
        
        #Checks if the position exceeded 100
        if target_position2 > 100:
            self.player2_label.config(text=f"Computer overshot! Staying at {self.position2}")
            target_position2 = self.position2
        
        #Checks if the Computer landed on 100, if True it wins
        elif target_position2 == 100:
            self.player2_label.config(text="Computer won!")
            self.animate_player_movement(self.position2, target_position2, "player2")
            return
        
        else:
            self.animate_player_movement(self.position2, target_position2, "player2")#Animates computer's movement
            self.position2 = target_position2

            #Checks if the computer landed on a ladder
            if target_position2 in self.ladders:
                ladder_end = self.ladders[target_position2]  # Gets endpoint of ladder
                self.slide_up_or_down(target_position2, ladder_end, 'player2')  # Animates climbing up the ladder
                self.position = ladder_end #Updates the position
                self.player2_label.config(text=f"Computer climbed to {ladder_end}") #Updates label
            
            #Checks if computer landed on a snake
            elif target_position2 in self.snakes:
                snake_end = self.snakes[target_position2]  # Gets end point of the snale
                self.slide_up_or_down(target_position2, snake_end, 'player2')  # Animates sliding down the snake
                self.position = snake_end #Updates the position
                self.player2_label.config(text=f" Computer slid to {snake_end}") #Updates the label
            
       
            else:
                self.player2_label.config(text=f"Computer rolled a {dice_2}. Now at {self.position2}")
       

    
    def show_player2(self):
        """Display the opponent's piece on the board."""
        # Check if the player2 piece has not been created yet
        if not hasattr(self, 'player2'):
            # Create the opponent's piece as a red circle on the canvas
            self.player2 = self.canvas.create_oval(15, 475, 45, 505, fill="red")
            # Display the player2 label with some padding
            self.player2_label.pack(pady=10)


    def button_pressed(self, mode):
        """Handle button press based on mode selection."""
        self.game = True  # Mark the game as active
        if mode == "alone":
            # Set the dice button to trigger the single-player mode
            self.dice.config(command=self.alone)
        elif mode == "computer":
            # Set the dice button to trigger the computer opponent mode
            self.dice.config(command=self.computer)


    def Error(self):
        """Handle the back button functionality, prompting the user and resetting the game."""
        # Check if the game is active
        if self.game:
            # Prompt the user with a confirmation dialog
            response = messagebox.askquestion(
                "Exit", "Are you sure you want to go back? \nYour progress will be lost"
            )
            if response == "yes":
                # Navigate back to the main frame
                self.show_frame1()
                # Reset player positions
                self.position = 0
                self.position2 = 0
                self.game = False  # Reset game status
                # Update UI labels to reflect reset positions
                self.player1_label.config(text="Your position is 0")
                self.player2_label.config(text="Opponent position is 0")
                # Move player pieces back to the starting positions
                x, y = self.board_mapping[self.position]
                self.canvas.coords(self.player1, x, y, x + 30, y + 30)
                if hasattr(self, 'player2'):  # Check if player2 exists before resetting
                    self.canvas.coords(self.player2, x + 35, y + 35, x + 65, y + 65)


    def play_music(self):
        """Play background music in a loop."""
        global music  # Declare music as a global variable
        music = r"C:\Users\Pamela\Documents\GTB\Project\S and L\music.mp3"
        pygame.mixer.music.load(music)  # Load the music file
        pygame.mixer.music.play(loops=-1)  # Play the music in an infinite loop


    def change_image(self):
        """Change the button image and toggle music playback."""
        # Check the current button image
        if self.button.cget("image") == str(self.music_on): 
            # If the button indicates music is on, pause the music
            pygame.mixer.music.pause()
            self.button.config(image=self.music_off)  # Change the button to music-off image
        else:
            # If the button indicates music is off, play the music
            self.play_music()
            self.button.config(image=self.music_on)  # Change the button to music-on image

            
  
        
    
# Run the app
app = MyApp()
app.mainloop()

