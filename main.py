def on_received_number(receivedNumber):
    if receivedNumber == 1:
        music._play_default_background(music.built_in_playable_melody(Melodies.ENTERTAINER),
            music.PlaybackMode.IN_BACKGROUND)
    if receivedNumber == 2:
        music._play_default_background(music.built_in_playable_melody(Melodies.ODE),
            music.PlaybackMode.IN_BACKGROUND)
    if receivedNumber == 3:
        music._play_default_background(music.built_in_playable_melody(Melodies.NYAN),
            music.PlaybackMode.IN_BACKGROUND)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global tally, cycle_count
    if Tools == 1:
        music._play_default_background(music.built_in_playable_melody(Melodies.ODE),
            music.PlaybackMode.UNTIL_DONE)
    if Tools == 2:
        music._play_default_background(music.built_in_playable_melody(Melodies.ENTERTAINER),
            music.PlaybackMode.UNTIL_DONE)
    if Tools == 5:
        tally += -1
    if Tools == 4:
        bird.change(LedSpriteProperty.Y, 1)
    if Tools == 7:
        radio.send_number(1)
    if Tools == 0:
        cycle_count += -1
        if cycle_count == 1:
            basic.show_leds("""
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                """)
        if cycle_count == 2:
            basic.show_leds("""
                . . # # #
                . . # . #
                # # # . .
                # . # . .
                # # # . .
                """)
        if cycle_count == 3:
            basic.show_leds("""
                . # # . .
                # . # . .
                . . # . .
                . . # . .
                # # # # #
                """)
        if cycle_count == 4:
            basic.show_leds("""
                # # # # .
                # . . # .
                # . # # .
                # . . # .
                # # # # .
                """)
        if cycle_count == 5:
            basic.show_leds("""
                . # # # .
                . # # # .
                . . # . .
                # . # . #
                # # # # #
                """)
        if cycle_count == 6:
            basic.show_leds("""
                . . # . #
                . . # . #
                # . . . #
                . . # . #
                . . # . .
                """)
        if cycle_count == 7:
            basic.show_leds("""
                # # # # .
                . . . . #
                # # . . #
                . . # . #
                # . # . #
                """)
    if Tools == 6:
        if Radio_cycle == 2:
            basic.show_leds("""
                # # # # .
                # . . # .
                # . # # .
                # . . # .
                # # # # .
                """)
        if Radio_cycle == 3:
            basic.show_leds("""
                . # # # .
                # . . . #
                # # # # #
                # . # . #
                . # # # .
                """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Tools, cycle_count, Radio_cycle, bird, obstacles, index
    if Tools == 2:
        music._play_default_background(music.built_in_playable_melody(Melodies.NYAN),
            music.PlaybackMode.UNTIL_DONE)
    if cycle_count == 2:
        Tools = 1
        basic.clear_screen()
    if cycle_count == 3:
        Tools = 5
        basic.clear_screen()
    if cycle_count == 4:
        Tools = 2
        cycle_count = 0
    if cycle_count == 5:
        basic.clear_screen()
        Tools = 3
    if cycle_count == 6:
        basic.clear_screen()
        Tools = 4
    if cycle_count == 7:
        basic.clear_screen()
        Tools = 6
        Radio_cycle = 1
    if Tools == 7:
        radio.send_number(2)
    if Tools == 4:
        bird = game.create_sprite(0, 2)
        bird.set(LedSpriteProperty.BLINK, 200)
        obstacles = []
        index = 0
    if Radio_cycle == 2:
        Tools = 7
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global tally, cycle_count
    if Tools == 1:
        music._play_default_background(music.built_in_playable_melody(Melodies.BLUES),
            music.PlaybackMode.UNTIL_DONE)
    if Tools == 2:
        music._play_default_background(music.built_in_playable_melody(Melodies.ODE),
            music.PlaybackMode.UNTIL_DONE)
    if Tools == 5:
        tally += 1
    if Tools == 3:
        timeanddate.set24_hour_time(0, 0, 0)
    if Tools == 4:
        bird.change(LedSpriteProperty.Y, -1)
    if Tools == 7:
        radio.send_number(3)
    if Tools == 0:
        cycle_count += 1
        if cycle_count == 1:
            basic.show_leds("""
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                """)
        if cycle_count == 2:
            basic.show_leds("""
                . . # # #
                . . # . #
                # # # . .
                # . # . .
                # # # . .
                """)
        if cycle_count == 3:
            basic.show_leds("""
                . # # . .
                # . # . .
                . . # . .
                . . # . .
                # # # # #
                """)
        if cycle_count == 4:
            basic.show_leds("""
                # # # # .
                # . . # .
                # . # # .
                # . . # .
                # # # # .
                """)
        if cycle_count == 5:
            basic.show_leds("""
                . # # # .
                . # # # .
                . . # . .
                # . # . #
                # # # # #
                """)
        if cycle_count == 6:
            basic.show_leds("""
                . . # . #
                . . # . #
                # . . . #
                . . # . #
                . . # . .
                """)
        if cycle_count == 7:
            basic.show_leds("""
                # # # # .
                . . . . #
                # # . . #
                . . # . #
                # . # . #
                """)
    if Tools == 6:
        if Radio_cycle == 2:
            basic.show_leds("""
                # # # # .
                # . . # .
                # . # # .
                # . . # .
                # # # # .
                """)
        if Radio_cycle == 3:
            basic.show_leds("""
                . # # # .
                # . . . #
                # # # # #
                # . # . #
                . # # # .
                """)
input.on_button_pressed(Button.B, on_button_pressed_b)

empty_obstacle = 0
ticks = 0
reading = 0
index = 0
obstacles: List[game.LedSprite] = []
bird: game.LedSprite = None
tally = 0
Radio_cycle = 0
Tools = 0
cycle_count = 0
game.set_score(0)
flappy = 1
cycle_count = 0
Tools = 0
Radio_cycle = 1
music.set_volume(100)

def on_forever():
    global cycle_count, reading
    if cycle_count >= 7:
        cycle_count = 0
    if Tools == 5:
        basic.show_string("" + str((tally)))
    if cycle_count == 2:
        basic.show_leds("""
            . . # # #
            . . # . #
            # # # . .
            # . # . .
            # # # . .
            """)
    if Tools == 3:
        pins.analog_write_pin(AnalogPin.P1, 1023)
        reading = pins.analog_read_pin(AnalogPin.P0)
        pins.analog_write_pin(AnalogPin.P1, 0)
        led.plot_bar_graph(reading, 1023)
        if input.button_is_pressed(Button.A):
            basic.show_number(reading)
    if Radio_cycle == 1:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
basic.forever(on_forever)

def on_forever2():
    global empty_obstacle, ticks
    for obstacle in obstacles:
        if obstacle.get(LedSpriteProperty.X) == bird.get(LedSpriteProperty.X):
            game.add_score(1)
    if Tools == 4:
        while len(obstacles) > 0 and obstacles[0].get(LedSpriteProperty.X) == 0:
            obstacles.remove_at(0).delete()
        for obstacle2 in obstacles:
            obstacle2.change(LedSpriteProperty.X, -1)
        if ticks % 3 == 0:
            empty_obstacle = randint(0, 4)
            for index2 in range(5):
                if index2 != empty_obstacle:
                    obstacles.append(game.create_sprite(4, index2))
        for obstacle3 in obstacles:
            if obstacle3.get(LedSpriteProperty.X) == bird.get(LedSpriteProperty.X) and obstacle3.get(LedSpriteProperty.Y) == bird.get(LedSpriteProperty.Y):
                game.game_over()
        ticks += 2
        basic.pause(500)
basic.forever(on_forever2)
