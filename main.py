@namespace
class SpriteKind:
    hoop = SpriteKind.create()
    hoopstand = SpriteKind.create()
    scoredBall = SpriteKind.create()

def on_on_destroyed(sprite):
    global chances
    createHoop()
    if not (scored):
        chances += -1
    if chances == 0:
        game.over(False)
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

def on_on_overlap(sprite, otherSprite):
    global scored
    print("X position of ball: " + ("" + str(sprite.x)))
    print("X position of hoop: " + ("" + str(otherSprite.x)))
    print("Y position of ball: " + ("" + str(sprite.y)))
    print("Y position of hoop: " + ("" + str(otherSprite.y)))
    if (sprite.x < otherSprite.x + 3 or sprite.x > otherSprite.x - 13) and sprite.y < otherSprite.y - 7:
        info.change_score_by(1)
        sprite.set_position(otherSprite.x, sprite.y)
        sprite.set_velocity(0, -100)
        scored = True
    sprite.set_kind(SpriteKind.scoredBall)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.hoop, on_on_overlap)

def on_on_destroyed2(sprite):
    global chances
    createHoop()
    if not (scored):
        chances += -1
    if chances == 0:
        game.over(False)
sprites.on_destroyed(SpriteKind.projectile, on_on_destroyed2)

hoopSprite: Sprite = None
hoopStandSprite: Sprite = None
ballSprite: Sprite = None
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
chances = 3
createHoop()