namespace SpriteKind {
    export const hoop = SpriteKind.create()
    export const hoopstand = SpriteKind.create()
    export const scoredBall = SpriteKind.create()
}

sprites.onDestroyed(SpriteKind.scoredBall, function on_on_destroyed(sprite: Sprite) {
    
    createHoop()
    if (!scored) {
        chances += -1
    }
    
    if (chances == 0) {
        game.over(false)
    }
    
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    if (sprites.allOfKind(SpriteKind.Projectile).length == 0 && sprites.allOfKind(SpriteKind.scoredBall).length == 0) {
        ballSprite = sprites.createProjectileFromSprite(img`
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
            `, playerSprite, 0, 0)
        ballSprite.setVelocity(80, -200)
        ballSprite.ay = 500
        ballSprite.z = 1
        scored = false
    }
    
})
function createHoop() {
    
    if (scored) {
        for (let value of sprites.allOfKind(SpriteKind.hoop)) {
            value.destroy()
        }
        for (let value2 of sprites.allOfKind(SpriteKind.hoopstand)) {
            value2.destroy()
        }
        hoopStandSprite = sprites.create(img`
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
            `, SpriteKind.hoopstand)
        hoopSprite = sprites.create(img`
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
            `, SpriteKind.hoop)
        hoopStandSprite.z = 3
        hoopSprite.z = 4
        hoopStandSprite.setPosition(randint(70, 150), randint(95, 50))
        hoopSprite.setPosition(hoopStandSprite.x - 4, hoopStandSprite.y - 10)
    }
    
}

sprites.onOverlap(SpriteKind.Projectile, SpriteKind.hoop, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    
    console.log(sprite.x)
    console.log(otherSprite.x)
    console.log(sprite.y)
    console.log(otherSprite.y)
    if ((sprite.x < otherSprite.x + 3 || sprite.x > otherSprite.x - 13) && sprite.y < otherSprite.y - 11) {
        info.changeScoreBy(1)
        sprite.setPosition(otherSprite.x, sprite.y)
        sprite.setVelocity(0, -100)
        scored = true
    }
    
    sprite.setKind(SpriteKind.scoredBall)
})
sprites.onDestroyed(SpriteKind.Projectile, function on_on_destroyed2(sprite: Sprite) {
    
    createHoop()
    if (!scored) {
        chances += -1
    }
    
    if (chances == 0) {
        game.over(false)
    }
    
})
let hoopSprite : Sprite = null
let hoopStandSprite : Sprite = null
let ballSprite : Sprite = null
let chances = 0
let scored = false
let playerSprite : Sprite = null
scene.setBackgroundColor(13)
playerSprite = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(playerSprite)
scored = true
playerSprite.z = 2
playerSprite.setStayInScreen(true)
chances = 3
createHoop()
