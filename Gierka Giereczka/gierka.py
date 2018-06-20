from plan_ix import Window
from random import randint




class Food:
    def __init__(self,app):
        self.x = randint(0,400)
        self.y = randint(0,400)
        self.image = app.vars.canvas.create_polygon(self.x,self.y,
                                       self.x-10,self.y+10,
                                       self.x+10,self.y+10,fill="green")
        
class Agent:
    def __init__(self,app,x,y):
        self.app =app
        self.x = x
        self.y = y
        self.speed = 20
        app.vars.agents.append(self)

    def go(self,app,x,y):
        checkFoodCollision()
        speed = 20
        deltaX = x*self.speed
        deltaY = y*self.speed

        self.x += deltaX
        
        app.vars.canvas.move(app.vars.agents[app.vars.agents.index(self)].image,deltaX,deltaY)
        
    def goLeft(self,app,name,row,col,event):
        self.go(app,-1,0)
    
    def goRight(self,app,name,row,col,event):
        self.go(app,1,0)
    
    def goUp(self,app,name,row,col,event):
        self.go(app,0,-1)
    
    def goDown(self,app,name,row,col,event):
        self.go(app,0,1)


class Player(Agent):
    def __init__(self,app,x,y):
        Agent.__init__(self,app,x,y)
        self.x = x
        self.y = y
        self.image = app.vars.canvas.create_oval(10,10,50,50,fill="red")
        app.event('<Left>',self.goLeft)
        app.event('<Right>',self.goRight)
        app.event('<Down>',self.goDown)
        app.event('<Up>',self.goUp)


class Enemy(Agent):
    def __init__(self,app,x,y):
        Agent.__init__(self,app,x,y)
        self.x = x
        self.y = y
        self.image = app.vars.canvas.create_rectangle(10,10,50,50,fill="black")
    def randomMovement(self):
        deltaX = randint(-10,10)
        deltaY = randint(-10,10)

        self.x += deltaX
        self.y += deltaY

        self.app.vars.canvas.move(self.image,deltaX,deltaY)

    def randomMovementsTimer(self,app,name,row,col,event):
        self.randomMovement()
        app.timer(100,self.randomMovementsTimer)
        
        
        
def addFood(app):
    food = Food(app)
    app.vars.food.append(food)


def addFoodTimer(app,name,row,col,event):
    addFood(app)
    app.timer(randint(2000,8000),addFoodTimer)


def checkForCollision(obj1,obj2,minimal_distance):
    print(obj1.x-obj2.x)
    if(abs(obj1.x-obj2.x)<minimal_distance and abs(obj1.y-obj2.y)<minimal_distance):
        return True
    return False

def checkFoodCollision():
    for i in range(len(window.vars.food)):
        if(checkForCollision(player,window.vars.food[i],20)):
            window.vars.canvas.delete(window.vars.food[i].image)
    
window = Window("game")
window.vars.canvas = window.add("Ca",width = 400,height = 400,row=1,col=1)
window.vars.border = window.vars.canvas.create_rectangle(1,1,400,400)
window.vars.agents = []
window.vars.food = []

player = Player(window,50,50)
enemy = Enemy(window,100,100)

window.timer(100,enemy.randomMovementsTimer)

window.timer(100,addFoodTimer)


window.start()
