from Hexa import *

Display = Engine.Display.Create("Never Gonna Give You Up...", (1000, 575))

PlayerX, PlayerY = 100, 250
CoinX, CoinY = 500, 250
Player = Entity.Circle(Display, (43, 153, 255), (PlayerX, PlayerY), 25)
Coin = Entity.Circle(Display, (255, 211, 89), (CoinX, CoinY), 10)
GameOver = GUI.Text(Display, "Game over", (255, 255, 255), (400, 240), 0)

FPS = GUI.Text(Display, "0", (255, 255, 255), (10, 10), 22)
while True:
    DeltaTime = Engine.Time.DeltaTime()
    Engine.Display.Canvas(Display)
    Engine.Display.Events()
    FPS.update(Engine.Time.GetFPS(120), (255, 255, 255), (10, 10), 22)
    FPS.draw()

    CoinHitbox = Coin.draw()
    PlayerHitbox = Player.draw()
    if Engine.Input.GetKey("up"): PlayerY -= 1000 * DeltaTime
    if Engine.Input.GetKey("down"): PlayerY += 1000 * DeltaTime
    if Engine.Input.GetKey("right"): PlayerX += 1000 * DeltaTime
    if Engine.Input.GetKey("left"): PlayerX -= 1000 * DeltaTime
    Player.update((43, 153, 255), (PlayerX, PlayerY), 25)

    GameOver.draw()
    if Physics.IsColliding(PlayerHitbox, CoinHitbox):
        Coin.kill()
        GameOver.update("Game over", (255, 255, 255), (400, 240), 40)

    Engine.Display.Update()
