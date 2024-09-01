
def canPlaceFlowers(flowerbed, n):
    ans = ''
    zeros = flowerbed.count(0)
    z_remainder = zeros % 2
    z_floor = zeros // 2
    if z_remainder == 1:
        if n <= z_floor:
            ans = 'true'
        else:
            ans = 'false'
    else:
        ans = 'false'
    return ans

print(canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))