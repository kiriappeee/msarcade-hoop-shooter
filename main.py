@namespace
class SpriteKind:
    hoop = SpriteKind.create()
    hoopstand = SpriteKind.create()
    scoredBall = SpriteKind.create()

def on_on_destroyed(sprite):
    evaluateEndGame()
sprites.on_destroyed(SpriteKind.scoredBall, on_on_destroyed)

def on_a_pressed():
    global ballSprite, scored
    if len(sprites.all_of_kind(SpriteKind.projectile)) == 0 and len(sprites.all_of_kind(SpriteKind.scoredBall)) == 0:
        ballSprite = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . 4 4 4 4 . . . . . . 
                            . . . . 4 4 4 5 5 4 4 4 . . . . 
                            . . . 3 3 3 3 4 4 4 4 4 4 . . . 
                            . . 4 3 3 3 3 2 2 2 1 1 4 4 . . 
                            . . 3 3 3 3 3 2 2 2 1 1 5 4 . . 
                            . 4 3 3 3 3 2 2 2 2 2 5 5 4 4 . 
                            . 4 3 3 3 2 2 2 4 4 4 4 5 4 4 . 
                            . 4 4 3 3 2 2 4 4 4 4 4 4 4 4 . 
                            . 4 2 3 3 2 2 4 4 4 4 4 4 4 4 . 
                            . . 4 2 3 3 2 4 4 4 4 4 2 4 . . 
                            . . 4 2 2 3 2 2 4 4 4 2 4 4 . . 
                            . . . 4 2 2 2 2 2 2 2 2 4 . . . 
                            . . . . 4 4 2 2 2 2 4 4 . . . . 
                            . . . . . . 4 4 4 4 . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            playerSprite,
            0,
            0)
        ballSprite.set_velocity(80, -200)
        ballSprite.ay = 500
        ballSprite.z = 1
        scored = False
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_countdown_end():
    if not (scored):
        game.over(False)
info.on_countdown_end(on_countdown_end)

def createHoop():
    global hoopStandSprite, hoopSprite
    if scored:
        for value in sprites.all_of_kind(SpriteKind.hoop):
            value.destroy()
        for value2 in sprites.all_of_kind(SpriteKind.hoopstand):
            value2.destroy()
        hoopStandSprite = sprites.create(img("""
                ................................
                            ................................
                            ................................
                            ................................
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ..ff.ffffffffffffff.fffff.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            ........................f.......
                            .......................fff......
                            .....................fffffff....
                            ....................fffffffff...
                            ...................fffffffffff..
                            ..................fffffffffffff.
            """),
            SpriteKind.hoopstand)
        hoopSprite = sprites.create(img("""
                2 . . . 8 . . . 8 . . . 8 . . 2 
                            2 . . . 8 . . . 8 . . . 8 . . 2 
                            2 . . . 8 . . . 8 . . . 8 . . 2 
                            2 . . . 8 . . . 8 . . . 8 . . 2 
                            2 . . . 8 . . . 8 . . . 8 . . 2 
                            2 1 1 1 8 1 1 1 1 1 1 1 8 1 1 2 
                            2 . . . 8 . . . 8 . . . 8 . . 2 
                            2 . . . 8 . . . 8 . . . 8 . . 2 
                            2 . . . 8 . . . 8 . . . 8 . . 2 
                            2 1 1 1 1 1 1 1 8 1 1 1 1 1 1 2 
                            2 . . . 8 . . . 8 . . . 8 . . 2 
                            2 . . . 8 . . . 8 . . . 8 . . 2 
                            2 . . . 8 . . . 8 . . . 8 . . 2 
                            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
            """),
            SpriteKind.hoop)
        hoopStandSprite.z = 3
        hoopSprite.z = 4
        hoopStandSprite.set_position(randint(70, 150), randint(95, 50))
        hoopSprite.set_position(hoopStandSprite.x - 4, hoopStandSprite.y - 10)
        if info.score() <= 3:
            info.start_countdown(10)
        elif info.score() <= 10:
            info.start_countdown(5)
        elif info.score() <= 20:
            info.start_countdown(3)
        else:
            info.start_countdown(2)

def on_on_overlap(sprite, otherSprite):
    global scored
    print("X position of ball: " + ("" + str(sprite.x)))
    print("Right position of ball: " + ("" + str(sprite.right)))
    print("Left position of ball: " + ("" + str(sprite.left)))
    print("Left position of hoop: " + ("" + str(otherSprite.left)))
    print("Right position of hoop: " + ("" + str(otherSprite.right)))
    print("Y position of ball: " + ("" + str(sprite.y)))
    print("Y position of hoop: " + ("" + str(otherSprite.y)))
    if sprite.x < otherSprite.right - 4 and sprite.x > otherSprite.left / 4 and sprite.y < otherSprite.top - 0:
        info.change_score_by(1)
        sprite.set_position(otherSprite.x, sprite.y)
        sprite.set_velocity(0, -100)
        scored = True
        info.stop_countdown()
    sprite.set_kind(SpriteKind.scoredBall)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.hoop, on_on_overlap)

def evaluateEndGame():
    global chances, scored
    createHoop()
    if not (scored):
        chances += -1
        chancesTextSprite.set_text("Chances: " + ("" + str(chances)))
    if chances == 0:
        game.over(False)
    scored = False

def on_on_destroyed2(sprite):
    evaluateEndGame()
sprites.on_destroyed(SpriteKind.projectile, on_on_destroyed2)

hoopSprite: Sprite = None
hoopStandSprite: Sprite = None
ballSprite: Sprite = None
chancesTextSprite: TextSprite = None
chances = 0
scored = False
playerSprite: Sprite = None
scene.set_background_color(13)
playerSprite = sprites.create(img("""
        . . . . f f f f . . . . 
            . . f f e e e e f f . . 
            . f e e e e e e e f f . 
            f f e f e e e e e e f f 
            f f f e e e e e e e e f 
            f f f e e e e e e f e f 
            f f f f e e e e f f f f 
            f f f f f f f f f f f f 
            f f f f f f f f f f f f 
            . f f f f f f f f f f . 
            . e f f f f f f f f e . 
            e 4 f b b b b b b f 4 e 
            4 d f d d d d d d c d 4 
            4 4 f 6 6 6 6 6 6 f 4 4 
            . . . f f f f f f . . . 
            . . . f f . . f f . . .
    """),
    SpriteKind.player)
controller.move_sprite(playerSprite)
scored = True
playerSprite.z = 2
playerSprite.set_stay_in_screen(True)
# let textSprite = textsprite.create("")
chances = 3
chancesTextSprite = textsprite.create("Chances: " + ("" + str(chances)), 13, 10)
chancesTextSprite.set_position(35, 110)
createHoop()
scored = False