from collections import deque


bullet_price = int(input())
gun_barrel_size = int(input())
bullets = deque(input().split())
locks = deque(input().split())
intelligence_value = int(input())

safe_open = False
gun_barrel = gun_barrel_size
bullets_used = 0
while locks and bullets:
    bullets_used += 1
    current_bullet = int(bullets.pop())
    current_lock = int(locks[0])
    if current_bullet <= current_lock:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")
    gun_barrel -= 1
    if gun_barrel == 0 and bullets:
        gun_barrel = gun_barrel_size
        print("Reloading!")
    if not locks:
        safe_open = True

money_earned = intelligence_value - bullets_used * bullet_price
if safe_open:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")

