import pygame

pygame.init()
print("Joystics: ", pygame.joystick.get_count())
my_joystick = pygame.joystick.Joystick(0)
my_joystick.init()
clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
        if event.type == pygame.JOYAXISMOTION:
            if my_joystick.get_axis(0) < -0.5 and my_joystick.get_axis(1) == 0:
                print("gauche")
            elif my_joystick.get_axis(0) > 0.5 and my_joystick.get_axis(1) == 0:
                print("droite")
            elif my_joystick.get_axis(0) == 0 and my_joystick.get_axis(1) > 0.5:
                print("bas")
            elif my_joystick.get_axis(0) == 0 and my_joystick.get_axis(1) < -0.5:
                print("haut")
        clock.tick(40)

pygame.quit ()