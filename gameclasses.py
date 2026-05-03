class Character:
    def __init__(self, name, max_hp, health, attack, defense, speed, current_location, gold, ug, rp, rum, srk, krakenmap):
        # Initialize instance variables
        self.name = name
        self.health = health
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.current_location = current_location
        self.gold = gold
        self.ug = ug
        self.rp = rp
        self.rum = rum
        self.srk = srk
        self.krakenmap = krakenmap

    def take_damage(self, damage):
        """Reduce health by damage amount, ensuring it doesn't go below zero."""
        if damage < 0:
            raise ValueError("Error: Damage must be a non-negative number.")

        self.health -= damage
        if self.health < 0:
            self.health = 0

    def __str__(self):
        """String representation for debugging."""
        return (f"{self.name} | HP: {self.health} | ATK: {self.attack} | "
                f"DEF: {self.defense} | SPD: {self.speed} | "
                f"Location: {self.current_location} | Gold: {self.gold}")
    
    
    def enemystats(self):
        print(f"{self.name} | HP: {self.health}")