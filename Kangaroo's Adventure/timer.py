# http://programarcadegames.com/python_examples/f.php?file=timer.py

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

# Set the height and width of the screen
size = [200, 40]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Timer")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

font = pygame.font.Font(None, 25)

frame_count = 0
frame_rate = 60
start_time = 180

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(WHITE)

    # --- Timer going up ---
    # Calculate total seconds
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0

    # Divide by 60 to get total minutes
    minutes = total_seconds // 60

    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60

    # Use python string formatting to format in leading zeros
    output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)

    # Blit to the screen
    if total_seconds < 11 :
        text = font.render(output_string, True, (255, 0, 0))
    else:
        text = font.render(output_string, True, BLACK)

    screen.blit(text, [40, 15])


    frame_count += 1

    # Limit frames per second
    clock.tick(frame_rate)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
