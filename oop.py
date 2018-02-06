from dog import Dog
from dragon import Dragon


dog = Dog('Fiddo')
dragon = Dragon("Trogdor")

dragon.fly().walk().displayHealth()
dog.walk().pet().displayHealth()
print dragon
