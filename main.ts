input.onButtonPressed(Button.A, function () {
    if (Tools == 1) {
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Ode), music.PlaybackMode.UntilDone)
    }
    if (Tools == 2) {
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Entertainer), music.PlaybackMode.UntilDone)
    }
    if (Tools == 5) {
        tally += -1
    }
    if (Tools == 4) {
        bird.change(LedSpriteProperty.Y, 1)
    }
    if (Tools == 0) {
        cycle_count += -1
        if (cycle_count == 1) {
            basic.showLeds(`
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                `)
        }
        if (cycle_count == 2) {
            basic.showLeds(`
                . . # # #
                . . # . #
                # # # . .
                # . # . .
                # # # . .
                `)
        }
        if (cycle_count == 3) {
            basic.showLeds(`
                . # # . .
                # . # . .
                . . # . .
                . . # . .
                # # # # #
                `)
        }
        if (cycle_count == 4) {
            basic.showLeds(`
                # # # # .
                # . . # .
                # . # # .
                # . . # .
                # # # # .
                `)
        }
        if (cycle_count == 5) {
            basic.showLeds(`
                . # # # .
                . # # # .
                . . # . .
                # . # . #
                # # # # #
                `)
        }
        if (cycle_count == 6) {
            basic.showLeds(`
                . . # . #
                . . # . #
                # . . . #
                . . # . #
                . . # . .
                `)
        }
    }
})
input.onButtonPressed(Button.AB, function () {
    if (Tools == 2) {
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Nyan), music.PlaybackMode.UntilDone)
    }
    if (cycle_count == 2) {
        Tools = 1
        basic.clearScreen()
    }
    if (cycle_count == 3) {
        Tools = 5
        basic.clearScreen()
    }
    if (cycle_count == 4) {
        Tools = 2
        cycle_count = 0
    }
    if (cycle_count == 5) {
        basic.clearScreen()
        Tools = 3
    }
    if (cycle_count == 6) {
        basic.clearScreen()
        Tools = 4
    }
    if (Tools == 7) {
        radio.sendNumber(2)
    }
    if (Tools == 4) {
        bird = game.createSprite(0, 2)
        bird.set(LedSpriteProperty.Blink, 200)
        obstacles = []
        index = 0
    }
    if ((0 as any) == (2 as any)) {
        Tools = 7
    }
})
input.onButtonPressed(Button.B, function () {
    if (Tools == 1) {
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Blues), music.PlaybackMode.UntilDone)
    }
    if (Tools == 2) {
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Ode), music.PlaybackMode.UntilDone)
    }
    if (Tools == 5) {
        tally += 1
    }
    if (Tools == 4) {
        bird.change(LedSpriteProperty.Y, -1)
    }
    if (Tools == 0) {
        cycle_count += 1
        if (cycle_count == 1) {
            basic.showLeds(`
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                `)
        }
        if (cycle_count == 2) {
            basic.showLeds(`
                . . # # #
                . . # . #
                # # # . .
                # . # . .
                # # # . .
                `)
        }
        if (cycle_count == 3) {
            basic.showLeds(`
                . # # . .
                # . # . .
                . . # . .
                . . # . .
                # # # # #
                `)
        }
        if (cycle_count == 4) {
            basic.showLeds(`
                # # # # .
                # . . # .
                # . # # .
                # . . # .
                # # # # .
                `)
        }
        if (cycle_count == 5) {
            basic.showLeds(`
                . # # # .
                . # # # .
                . . # . .
                # . # . #
                # # # # #
                `)
        }
        if (cycle_count == 6) {
            basic.showLeds(`
                . . # . #
                . . # . #
                # . . . #
                . . # . #
                . . # . .
                `)
        }
    }
})
let empty_obstacle = 0
let ticks = 0
let reading = 0
let index = 0
let obstacles: game.LedSprite[] = []
let bird: game.LedSprite = null
let tally = 0
let Tools = 0
let cycle_count = 0
game.setScore(0)
let flappy = 1
cycle_count = 1
Tools = 0
music.setVolume(100)
basic.forever(function () {
    if (cycle_count >= 8) {
        cycle_count = 1
    }
    if (cycle_count <= 1) {
        cycle_count = 7
    }
    if (Tools == 5) {
        basic.showString("" + (tally))
    }
    if (cycle_count == 2) {
        basic.showLeds(`
            . . # # #
            . . # . #
            # # # . .
            # . # . .
            # # # . .
            `)
    }
    if (Tools == 3) {
        pins.analogWritePin(AnalogPin.P1, 1023)
        reading = pins.analogReadPin(AnalogPin.P0)
        pins.analogWritePin(AnalogPin.P1, 0)
        led.plotBarGraph(
        reading,
        1023
        )
        if (input.buttonIsPressed(Button.A)) {
            basic.showNumber(reading)
        }
    }
})
basic.forever(function () {
    for (let obstacle of obstacles) {
        if (obstacle.get(LedSpriteProperty.X) == bird.get(LedSpriteProperty.X)) {
            game.addScore(1)
        }
    }
    if (Tools == 4) {
        while (obstacles.length > 0 && obstacles[0].get(LedSpriteProperty.X) == 0) {
            obstacles.removeAt(0).delete()
        }
        for (let obstacle2 of obstacles) {
            obstacle2.change(LedSpriteProperty.X, -1)
        }
        if (ticks % 3 == 0) {
            empty_obstacle = randint(0, 4)
            for (let index2 = 0; index2 <= 4; index2++) {
                if (index2 != empty_obstacle) {
                    obstacles.push(game.createSprite(4, index2))
                }
            }
        }
        for (let obstacle3 of obstacles) {
            if (obstacle3.get(LedSpriteProperty.X) == bird.get(LedSpriteProperty.X) && obstacle3.get(LedSpriteProperty.Y) == bird.get(LedSpriteProperty.Y)) {
                game.gameOver()
            }
        }
        ticks += 2
        basic.pause(500)
    }
})
