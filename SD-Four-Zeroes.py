###############################
# Four-Zeroes.py 1.0          #
# By Chris Stoddard, Aug 2023 #
# Based on the Shadowdark RPG #
# by Arcane Library           #
# This code is licensed under #
# the Creative Commons        #
# Attribution-NonCommercial   #
# 4.0 License.                #
###############################

###############################
# Import needed libraries
import random

###############################
# Define functions
# 3d6 for rolling ability scores
def roll_3d6():
    dice_rolls = [random.randint(1, 6) for _ in range(3)]
    return sum(sorted(dice_rolls, reverse=True)[:3])

###############################
# Print Legal Statement.
print ("-------------------------------------------------------")
print ("Legal Statement:")
print ("This Shadowdark Character Generator is an independent")
print ("product published under the Shadowdark RPG Third-Party")
print ("License and is not affiliated with The Arcane Library,")
print ("LLC. Shadowdark RPG © 2023 The Arcane Library, LLC.")
print ("-------------------------------------------------------")

Character_Number = input ("How many Zero level charcters would you like? ")
File_name = input ("Name the file to save your characters to? ")
print ("Generating " + Character_Number + " Zero level characters.")
print ('....')

with open(File_name + '.txt', 'w') as f:

    Counting_Characters = range(int(Character_Number))

    for counting in Counting_Characters:
        
        ###############################
        # Generate ability scores
        ability_scores = [roll_3d6() for _ in range(6)]

        # Sort out what number go where
        Strength = (ability_scores[0])
        Dexterity = (ability_scores[1])
        Constitution = (ability_scores[2])
        Intellegence = (ability_scores[3])
        Wisdom = (ability_scores[4])
        Charisma = (ability_scores[5])

        # Determines Modifiers
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

            # Assign Modifiers
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

        # Randomly chooses Ancestry
        Random_Ancestry = ['Dwarf','Elf', 'Goblin', 'Half-Orc', 'Halfling', 'Human' ]
        Ancestry = random.choice(Random_Ancestry)

        if Ancestry == "Dwarf":
            Language = "Common and Dwarvish"
            AncestryFeature = "Stout. +2 HP at 1st level, each level there after, roll hit points with advantage."

        if Ancestry == "Elf":
            Language = "Common, Elvish, and Sylvan"
            AncestryFeature = "Farsight. Choose; +1 bonus to ranged weapon attacks or +1 bonus to spellcasting checks."

        if Ancestry == "Goblin":
            Language = "Common and Goblin"
            AncestryFeature = "Keen Senses. Character cannot be surprised."

        if Ancestry == "Half-Orc":
            Language = "Common and Orcish"
            AncestryFeature = "Mighty. +1 bonus to hit and damage with melee weapons."

        if Ancestry == "Halfling":
            Language = "Common"
            AncestryFeature = "Stealthy. You become invisible for 3 rounds, use this ability once per day"

        if Ancestry == "Human":
            Language = "Common and one additional common language."
            AncestryFeature = "Ambitious. Roll one additional on the talent table at 1st level."

        # Randomly chooses background
        Random_Backgrounds = ['Urchin','Wanted', 'Cult Initiate', 'Thieves Guild', 'Banished', 'Orphaned', 'Wizards Apprentice', 'Jeweler', 'Herbalist', 'Barbarian', 'Mercenary', 'Sailor', 'Alcolyte', 'Soldier', 'Ranger', 'Scout', 'Minstrel', 'Scholar', 'Nobel', 'Chirurgeon' ]
        Background = random.choice(Random_Backgrounds)

        # Randomly choose Alignment
        Random_Alignment = ['Chaotic', 'Lawful', 'Neutral']
        Alignment = random.choice(Random_Alignment)
        
        ###############################
        # Modify hit Points by Constitution
        HITPOINTS = 0
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
        # Generate random equipment for Zero level character
        Equipment_List = (" ")
        Random_Equipment = ['Torch,', 'Dagger,', 'Pole,', 'Shortbow and 5 arrows,', '60 Feet of rope,', 'flask of oil,', 'Crowbar,', 'Iron spikes x10,', 'Flint and steel,', 'Grappling hook,', 'Club,', 'Bag of caltrops,']
        Equipment_Count = random.randint(1, 4)
        counter = range(Equipment_Count)
        for count in counter:
            Equipment_Item = random.choice(Random_Equipment)
            Equipment_List = (Equipment_List + " " + Equipment_Item)    

        ###############################
        #
        f.write ('\n')
        f.write ("Shadowdark Character Sheet 1.0" + '\n')
        f.write ("------------------------------" + '\n')
        f.write ("Character Name: _____________ " + '\n')
        f.write ("Ancestry " + Ancestry + '\n')
        f.write ("Background: " + Background + '\n')
        f.write ("Alignment: " + Alignment + '\n')
        f.write ("Deity: _______________________" + '\n')
        f.write ("Character Class: Zero level" + '\n')
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
        f.write ("     Weapons: All weapons until 1st level." + '\n')
        f.write ("     Armor: All armor and shields until 1st level." + '\n')
        f.write ("     Beginner's luck, you can wield any and all equipment until 1st level." + '\n' + '\n')
        f.write ("------------------------------" + '\n')
        f.write ("EQUIPMENT:" + '\n' + '\n')
        f.write (Equipment_List + '\n'+ '\n'+ '\n' + '\n')
        f.write ("==============================" + '\n')

exit ()
