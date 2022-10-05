class Monster():
    hp = 100
    alive = True
    
    def damage(self, attack):
        self.hp = self.hp - attack
        if self.hp < 0:
            self.alive = False
            
    def status_check(self):
        if self.alive:
            print('살았다')
        else:
            print('죽었다!')
            
            
# class 사용
m1 = Monster()
m1.damage(150)
m1.status_check()

m2 = Monster()
m2.damage(90)
m2.status_check()