from enemies.models import Enemy


class Combatant:
    def __init__(self, name, hp, armor, attack, attack_delay):
        self.name = name

        self.hp = hp
        self.armor = armor
        self.attack = attack
        self.attack_delay = attack_delay
        self.alive = True

        self.attack_counter = 0
        self.target = None

    def make_attack(self) -> list:
        self.target.hp -= self.attack
        self.attack_counter = 0
        print(f'{self.name} attacks {self.target.name} for {self.attack} | {self.target.hp} left')
        if self.target.hp <= 0:
            self.target.die()
            dead = self.target
            self.target = None
            return [dead]
        return []

    def die(self):
        self.alive = False
        print(f'{self.name} dies!')


class EnemyInCombat(Combatant):
    def __init__(self, instance: Enemy):
        super().__init__(
            name=instance.name,
            hp=instance.hp,
            armor=instance.armor,
            attack=instance.attack,
            attack_delay=instance.attack
        )


class PlayerInCombat(Combatant):
    pass


class CombatController:
    def __init__(self, player: PlayerInCombat, enemies: list[EnemyInCombat]):
        self.player = player
        self.enemies = enemies
        self.result = None

    def set_target(self, combatant: [PlayerInCombat, EnemyInCombat]):
        new_target = None
        if isinstance(combatant, PlayerInCombat):
            alive_enemies = [enemy for enemy in self.enemies if enemy.alive]
            new_target = alive_enemies[0]
        elif isinstance(combatant, EnemyInCombat):
            new_target = self.player
        combatant.target = new_target
        print(f'{combatant.name} sets target: {new_target.name}')

    def continue_criteria(self):
        return self.player.alive and any([enemy.alive for enemy in self.enemies])

    def combat_result(self):
        self.exec_combat_loop()

        if self.player.alive:
            self.result = 'survived'
        else:
            self.result = 'died'

    def exec_combat_loop(self):
        all_combatants = [combatant for combatant in self.enemies + [self.player] if combatant.alive]

        while True:
            no_target_combatants = [combatant for combatant in all_combatants if combatant.target is None]
            for combatant in no_target_combatants:
                self.set_target(combatant)
            for combatant in all_combatants:
                if not combatant.alive:
                    continue
                combatant.attack_counter += 1
                if combatant.attack_counter == combatant.attack_delay:
                    dead_this_turn = combatant.make_attack()
                    for dead in dead_this_turn:
                        all_combatants.remove(dead)
                        if not self.continue_criteria():
                            return
