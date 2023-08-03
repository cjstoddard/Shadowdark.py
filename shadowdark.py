###############################
# Shadowsdark.py 1.0          #
# By Chris Stoddard, Aug 2023 #
# Based on the Shadowdark RPG #
# by Arcane Library           #
###############################

###############################
import random

###############################
# Print Legal Statement.
print ("-------------------------------------------------------")
print ("Legal Statement:")
print ("This Shadowdark Character Generator is an independent")
print ("product published under the Shadowdark RPG Third-Party")
print ("License and is not affiliated with The Arcane Library,")
print ("LLC. Shadowdark RPG © 2023 The Arcane Library, LLC.")
print ("-------------------------------------------------------")

###############################
# 4d6 take the best 3 for rolling ability scores
def roll_4d6():
    dice_rolls = [random.randint(1, 6) for _ in range(4)]
    return sum(sorted(dice_rolls, reverse=True)[:3])

# 3d6 for rolling ability scores
def roll_3d6():
    dice_rolls = [random.randint(1, 6) for _ in range(3)]
    return sum(sorted(dice_rolls, reverse=True)[:3])

###############################
# Roll ability scores
print ('\n')
print ("Choose which method of attribute generation you want to use:")
print (" 1 Roll 3d6 for attributes")
print (" 2 Roll 4d6 take the best 3 for attributes")

RollChoice = input ("? ")
if RollChoice == "2":
    ability_scores = [roll_4d6() for _ in range(6)]    
if RollChoice == "1":
    ability_scores = [roll_3d6() for _ in range(6)]

###############################
# Assign Ability Scores and determines Modifiers
Strength = (ability_scores[0])
Dexterity = (ability_scores[1])
Constitution = (ability_scores[2])
Intellegence = (ability_scores[3])
Wisdom = (ability_scores[4])
Charisma = (ability_scores[5])

counter = range(6)
for count in counter:
    temp = ability_scores[count]
    if temp == 3:
        temp_mod = "-4"
    if temp == 4 or temp == 5:
        temp_mod = "-3"
    if temp == 6 or temp == 7:
        temp_mod = "-2"
    if temp == 8 or temp == 9:
        temp_mod = "-1"
    if temp == 10 or temp == 11:
        temp_mod = "0"
    if temp == 12 or temp == 13:
        temp_mod = "+1"
    if temp == 14 or temp == 15:
        temp_mod = "+2"
    if temp == 16 or temp == 17:
        temp_mod = "+3"
    if temp == 18:
        temp_mod = "+4"

    if count == 0:
        Strength_mod = temp_mod
    if count == 1:
        Dexterity_mod = temp_mod
    if count == 2:
        Constitution_mod = temp_mod
    if count == 3:
        Intellegence_mod = temp_mod
    if count == 4:
        Wisdom_mod = temp_mod
    if count == 5:
        Charisma_mod = temp_mod

###############################
# Print Ability scores to screen
print ('\n')
print ("STR: " + str(Strength) + " / " + Strength_mod)
print ("DEX: " + str(Dexterity) + " / " + Dexterity_mod)
print ("CON: " + str(Constitution) + " / " + Constitution_mod)
print ("INT: " + str(Intellegence) + " / " + Intellegence_mod)
print ("WIS: " + str(Wisdom) + " / " + Wisdom_mod)
print ("CHR: " + str(Charisma) + " / " + Charisma_mod)

YN = input ("Do you want to keep this character, Y or N? ")
if YN == "N" or YN == "n":
    exit()

###############################
# Player chooses ancestry
print ('\n')
print ("Choose an Ancestry for your character:")
print (" 1 Dwarf")
print (" 2 Elf")
print (" 3 Goblin")
print (" 4 Half-Orc")
print (" 5 Halfling")
print (" 6 Human")
Choose_Ancestry = input ("Choose Your Ancestry? ")

if Choose_Ancestry == "1":
    Ancestry = "Dwarf"
    Language = "Common and Dwarvish"
    AncestryFeature = "Stout. +2 HP at 1st level, each level there after, roll hit points with advantage."

if Choose_Ancestry == "2":
    Ancestry = "Elf"
    Language = "Common, Elvish, and Sylvan"
    AncestryFeature = "Farsight. Choose; +1 bonus to ranged weapon attacks or +1 bonus to spellcasting checks."

if Choose_Ancestry == "3":
    Ancestry = "Goblin"
    Language = "Common and Goblin"
    AncestryFeature = "Keen Senses. Character cannot be surprised."

if Choose_Ancestry == "4":
    Ancestry = "Half-Orc"
    Language = "Common and Orcish"
    AncestryFeature = "Mighty. +1 bonus to hit and damage with melee weapons."

if Choose_Ancestry == "5":
    Ancestry = "Halfling"
    Language = "Common"
    AncestryFeature = "Stealthy. You become invisible for 3 rounds, use this ability once per day"

if Choose_Ancestry == "6":
    Ancestry = "Human"
    Language = "Common and one additional common language."
    AncestryFeature = "Ambitious. Roll one additional on the talent table at 1st level."

###############################
# Player chooses class
print ('\n')
print ("Choose a Class for your character:")
print (" 1 Fighter")
print (" 2 Priest")
print (" 3 Thief")
print (" 4 Wizard")
print (" 5 Zero Level")
Choose_Class = input ("Choose your Class? ")

if Choose_Class == "1":
    Class = "Fighter"
    HITPOINTS = dice_rolls = random.randint(1, 8)
    Weapon = "Weapons: All weapons"
    Armor = "Armor: All armor and shields"
    ClassFeature1 = "Hauler. You gain additional gear slots equal to you Constitution modifier, if positive."
    ClassFeature2 = "Weapon Mastery. With one type of weapon, you gain +1 to attack and damage with that weapon type. Also, add half your level to attack and damage rolls (round down)."
    ClassFeature3 = "Grit. Choose Strength or Dexterity. You have advantage on checks based on that attribute."
    ClassFeature4 = " "
    talent_roll = [random.randint(1, 6) for _ in range(2)]
    talent_roll_sum = sum(talent_roll)
    if talent_roll_sum == 2:
        ClassTalent = "Gain Weapon Mastery with another weapon type"
    if talent_roll_sum == 3 or talent_roll_sum == 4 or talent_roll_sum == 5 or talent_roll_sum == 6:
        ClassTalent = "+1 bonus to melee and ranged attacks"
    if talent_roll_sum == 7 or talent_roll_sum == 8 or talent_roll_sum == 9:
        ClassTalent = "+2 bonus to Strength, Dexterity, or Constitution attribute"
    if talent_roll_sum == 10 or talent_roll_sum == 11:
        ClassTalent = "Choose one type of armor. You get +1 your AC when wearing that armor"
    if talent_roll_sum == 12:
        ClassTalent = "Choose a talent or +2 points to distribute to attributes"

if Choose_Class == "2":
    Class = "Priest"
    HITPOINTS = random.randint(1, 6)
    Weapon = "Weapons: Club, crossbow, dagger, mace, longsword, staff, warhammer"
    Armor = "Armor: All armor and shields"
    Language = Language +  " and you know either Celestial, Diabolic, or Primordial."
    ClassFeature1 = "Turn Undead. You know the turn undead spell, this does not count toward your number of known spells."
    ClassFeature2 = "Spellcasting. You can cast priest spells you have prepared."
    ClassFeature3 = " "
    ClassFeature4 = " "
    talent_roll = [random.randint(1, 6) for _ in range(2)]
    talent_roll_sum = sum(talent_roll)
    if talent_roll_sum == 2:
        ClassTalent = "Gain advantage with one spell you know, when roll to cast."
    if talent_roll_sum == 3 or talent_roll_sum == 4 or talent_roll_sum == 5 or talent_roll_sum == 6:
        ClassTalent = "+1 bonus to melee or ranged attacks"
    if talent_roll_sum == 7 or talent_roll_sum == 8 or talent_roll_sum == 9:
        ClassTalent = "+1 bonus to priest spellcasting checks"
    if talent_roll_sum == 10 or talent_roll_sum == 11:
        ClassTalent = "+2 to Strength or Wisdom attribute"
    if talent_roll_sum == 12:
        ClassTalent = "Choose a talent or +2 points to distribute to attributes"

if Choose_Class == "3":
    Class = "Thief"
    HITPOINTS = random.randint(1, 4)
    Weapon = "Weapons: Club, crossbow, dagger, shortbow, shortsword"
    Armor = "Armor: Leather armor, mithral chainmail"
    ClassFeature1 = "Backstab. On successful attack roll, If the target is unaware of your attack, you deal an extra die of damage and an additional die of damage equal to half your level (round down)."
    ClassFeature2 = "Thievery. You are trained thieving skills and have can carry the necessary tools at no equipment slot cost."
    ClassFeature3 = "You are adept in the skills associated with thievery, you have advantage on any associated checks"
    ClassFeature4 = " "
    talent_roll = [random.randint(1, 6) for _ in range(2)]
    talent_roll_sum = sum(talent_roll)
    if talent_roll_sum == 2:
        ClassTalent = "You have advantage on initiative rolls (reroll if duplicate)"
    if talent_roll_sum == 3 or talent_roll_sum == 4 or talent_roll_sum == 5 or talent_roll_sum == 6:
        ClassTalent = "Your Backstab deals +1 die of damage"
    if talent_roll_sum == 7 or talent_roll_sum == 8 or talent_roll_sum == 9:
        ClassTalent = "+2 bonus to Strength, Dexterity, or Charisma attribute"
    if talent_roll_sum == 10 or talent_roll_sum == 11:
        ClassTalent = "+1 bonus to melee and ranged attacks"
    if talent_roll_sum == 12:
        ClassTalent = "Choose a talent or +2 points to distribute to atributes"

if Choose_Class == "4":
    Class = "Wizard"
    HITPOINTS = random.randint(1, 4)
    Weapon = "Weapons: Dagger, staff"
    Armor = "Armor: None"
    Language = Language + " and you know two additional common languages and two rare languages"
    ClassFeature1 = "Learning Spells. You can learn new wizard spells from a scroll by studying it for a day and succeeding on a DC 15 INT check."
    ClassFeature2 = "Spellcasting. You can cast wizard spells you have prepared."
    ClassFeature3 = " "
    ClassFeature4 = " "
    talent_roll = [random.randint(1, 6) for _ in range(2)]
    talent_roll_sum = sum(talent_roll)
    if talent_roll_sum == 2:
        ClassTalent = "Make a single random magic item of a type you choose"
    if talent_roll_sum == 3 or talent_roll_sum == 4 or talent_roll_sum == 5 or talent_roll_sum == 6:
        ClassTalent = "+2 to Intelligence attribute or +1 bonus to wizard spellcasting checks"
    if talent_roll_sum == 7 or talent_roll_sum == 8 or talent_roll_sum == 9:
        ClassTalent = "Gain advantage on casting a single spell you know"
    if talent_roll_sum == 10 or talent_roll_sum == 11:
        ClassTalent = "Learn one additional wizard spell of any tier you know"
    if talent_roll_sum == 12:
        ClassTalent = "Choose a talent or +2 points to distribute to attribute"

if Choose_Class == "5":
    Class = "Zero Level"
    HITPOINTS = 0
    Weapon = "Weapons: All weapons until 1st level"
    Armor = "Armor: All armor and shields until 1st level"
    ClassFeature1 = "Beginner's luck, you can wield any and all equipment until 1st level."
    ClassFeature2 = " "
    ClassFeature3 = " "
    ClassFeature4 = " "
    ClassTalent = " "

###############################
# Randomly chooses background
Random_Backgrounds = ['Urchin','Wanted', 'Cult Initiate', 'Thieves Guild', 'Banished', 'Orphaned', 'Wizards Apprentice', 'Jeweler', 'Herbalist', 'Barbarian', 'Mercenary', 'Sailor', 'Alcolyte', 'Soldier', 'Ranger', 'Scout', 'Minstrel', 'Scholar', 'Nobel', 'Chirurgeon' ]
Background = random.choice(Random_Backgrounds)

###############################
# Modify hit Points by Constitution
if Constitution_mod == "-1":
    HITPOINTS = HITPOINTS - 1
if Constitution_mod == "-2":
    HITPOINTS = HITPOINTS - 2
if Constitution_mod == "-3":
    HITPOINTS = HITPOINTS - 3
if Constitution_mod == "-4":
    HITPOINTS = HITPOINTS - 4
if Constitution_mod == "+1":
    HITPOINTS = HITPOINTS + 1
if Constitution_mod == "+2":
    HITPOINTS = HITPOINTS + 2
if Constitution_mod == "+3":
    HITPOINTS = HITPOINTS + 3
if Constitution_mod == "+4":
    HITPOINTS = HITPOINTS + 4
if HITPOINTS < 1:
    HITPOINTS = 1

###############################
# Prints out the finished character to the screen
print ('\n')
Character_name = input ("What is your characters name? ")
print ('\n')
print ("Shadowdark Character Sheet 1.0")
print ("------------------------------")
print ("Character Name: " + Character_name)
print ("Ancestry " + Ancestry)
print ("Background: " + Background)
print ("Character Class: " + Class)
print ("XP:    _____")
print ("Level: _____")
print ("------------------------------")
print ("STR: " + str(Strength) + " / " + Strength_mod)
print ("DEX: " + str(Dexterity) + " / " + Dexterity_mod)
print ("CON: " + str(Constitution) + " / " + Constitution_mod)
print ("INT: " + str(Intellegence) + " / " + Intellegence_mod)
print ("WIS: " + str(Wisdom) + " / " + Wisdom_mod)
print ("CHR: " + str(Charisma) + " / " + Charisma_mod)
print ('\n')
print ("Hit Points: " + str(HITPOINTS))
print ('\n')
print ("------------------------------")
print ("Ancestry Feature: " + AncestryFeature)
print ("Languages: " + Language)
print ("Class Features:")
print ("     " +  Weapon)
print ("     " +  Armor)
print ("     " +  ClassFeature1)
print ("     " +  ClassFeature2)
print ("     " +  ClassFeature3)
print ("     " +  ClassFeature4)
print ("Class Talent: " + ClassTalent)
print ("------------------------------")
print ("EQUIPMENT:")

###############################
# Write character to a text file using the character name
YN = input ("Do you want to save this character to a text file, Y or N? ")
if YN == "N" or YN == "n":
    exit()

with open(Character_name + '.txt', 'w') as f:
    f.write ('\n')
    f.write ("Shadowdark Character Sheet 1.0" + '\n')
    f.write ("------------------------------" + '\n')
    f.write ("Character Name: " + Character_name + '\n')
    f.write ("Ancestry " + Ancestry + '\n')
    f.write ("Background: " + Background + '\n')
    f.write ("Character Class: " + Class + '\n')
    f.write ("XP:    _____" + '\n')
    f.write ("Level: _____" + '\n')
    f.write ("------------------------------" + '\n')
    f.write ('\n')
    f.write ("STR: " + str(Strength) + " / " + Strength_mod + '\n')
    f.write ("DEX: " + str(Dexterity) + " / " + Dexterity_mod + '\n')
    f.write ("CON: " + str(Constitution) + " / " + Constitution_mod + '\n')
    f.write ("INT: " + str(Intellegence) + " / " + Intellegence_mod + '\n')
    f.write ("WIS: " + str(Wisdom) + " / " + Wisdom_mod + '\n')
    f.write ("CHR: " + str(Charisma) + " / " + Charisma_mod + '\n')
    f.write ('\n')
    f.write ("Hit Points: " + str(HITPOINTS) + '\n')
    f.write ('\n')
    f.write ("------------------------------" + '\n')
    f.write ("Ancestry Feature: " + AncestryFeature + '\n')
    f.write ("Languages: " + Language + '\n')
    f.write ("Class Features:" + '\n')
    f.write ("     " +  Weapon + '\n')
    f.write ("     " +  Armor + '\n')
    f.write ("     " +  ClassFeature1 + '\n')
    f.write ("     " +  ClassFeature2 + '\n')
    f.write ("     " +  ClassFeature3 + '\n')
    f.write ("     " +  ClassFeature4 + '\n')
    f.write ("Class Talent: " + ClassTalent + '\n')
    f.write ("------------------------------" + '\n')
    f.write ("EQUIPMENT:" + '\n')

exit()
