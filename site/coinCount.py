__author__ = 'student'

coins = {
    1:6,
    5:4,
    10:2,
    25:1
}

 def pow(coins):
     cents = 0
     for x, y in coins.viewitems():
             cents += x * y
     return cents

 pow(coins)


pow(coins)

