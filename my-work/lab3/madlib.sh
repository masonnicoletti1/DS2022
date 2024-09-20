#!/bin/bash

# Introduction
clear
echo "Let's build a mad-lib!"

# Collect values from user input
read -p "1. Enter a name: " NAME
read -p "2. Enter an animal: " ANIMAL1
read -p "3. Enter another anminal: " ANIMAL2
read -p "4. Enter a food: " FOOD1
read -p "5. Enter another food: " FOOD2
read -p "6. Enter a past-tense verb: " VERB
read -p "7. Enter a color: " COLOR
read -p "8. Enter an adjective: " ADJECTIVE

echo ""
echo "------------------------------------------------------------"
echo ""

#Tell story
echo "Deep in the jungle, there lived a $COLOR $ANIMAL1 named $NAME."

sleep 4

echo ""
echo "$NAME was hungry, so $NAME $VERB across the jungle looking for its favorite
food: $FOOD1."

sleep 6

echo ""
echo "Just as $NAME came across a fresh pile of $FOOD1, 
a $ADJECTIVE $ANIMAL2 arrived and tried to claim the $FOOD1 for itself!"

sleep 6

echo ""
echo "Luckily, $NAME smelled $FOOD2 nearby. $NAME and the $ADJECTIVE $ANIMAL2
stopped their fighting and enjoyed the $FOOD1 and $FOOD2 together!"

sleep 6

echo ""
echo "The end."

echo ""
echo "------------------------------------------------------------"

